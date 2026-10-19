#!/usr/bin/env python3
"""Dug Trainer reminders: push the reminders a user agreed to, on their schedule.

Reads  users/<name>/reminders.json  (schema in system/reminders.md) and sends
each reminder that is due through ntfy (https://ntfy.sh), a free phone push
service that needs no account. Run it every 10-15 minutes from cron, or by hand.

    */15 * * * *  /usr/bin/python3 /path/to/your-repo/system/scripts/remind.py --user <name>

Design rules (see system/reminders.md):
  - Only reminders the user agreed to, only on the days and times they agreed.
  - One push per reminder per day. Re-running never double-sends (state file).
  - Quiet hours hold a push until they end; a daily cap stops pile-ups.
  - The ntfy topic is a secret-ish string: it is never read from the repo, only
    from the DUG_NTFY_TOPIC environment variable or ~/.config/dug-trainer/ntfy-topic.
  - No third-party packages. Python 3.9+ (zoneinfo). On Windows: pip install tzdata.

Useful flags:
  --list            show the schedule and exit
  --test <id>       send one reminder now, ignoring its schedule
  --dry-run         decide, print, send nothing, record nothing
  --sink stdout     print instead of pushing (pipe into any other notifier)
  --ics <file>      write the schedule as a calendar file (phone alarms, no server needed)
  --now <ISO time>  pretend it is this time (testing)
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import date, datetime, time, timedelta
from zoneinfo import ZoneInfo

DAY_NAMES = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
DEFAULT_SERVER = "https://ntfy.sh"
DEFAULT_WINDOW_MIN = 20          # a reminder fires if its time fell inside the last N minutes
DEFAULT_DAILY_CAP = 4
STATE_DIR = pathlib.Path.home() / ".local" / "state" / "dug-trainer"
TOPIC_FILE = pathlib.Path.home() / ".config" / "dug-trainer" / "ntfy-topic"


# ----------------------------------------------------------------------------- config


def find_repo(start: pathlib.Path) -> pathlib.Path:
    """The personal repo is the directory that contains users/. Walk up from this script."""
    for p in [start] + list(start.parents):
        if (p / "users").is_dir():
            return p
    return start


def load_config(path: pathlib.Path) -> dict:
    cfg = json.loads(path.read_text(encoding="utf-8"))
    cfg.setdefault("timezone", "UTC")
    cfg.setdefault("quiet_hours", {"start": "21:00", "end": "07:00"})
    cfg.setdefault("daily_cap", DEFAULT_DAILY_CAP)
    cfg.setdefault("reminders", [])
    return cfg


def parse_hhmm(s: str) -> time:
    h, m = s.split(":")
    return time(int(h), int(m))


def reminder_times(r: dict) -> list[time]:
    times = r.get("times") or ([r["time"]] if r.get("time") else [])
    return [parse_hhmm(t) for t in times]


def reminder_days(r: dict) -> set[int]:
    days = r.get("days") or DAY_NAMES
    if days == "daily" or days == ["daily"]:
        days = DAY_NAMES
    if days == "weekdays":
        days = DAY_NAMES[:5]
    if days == "weekends":
        days = DAY_NAMES[5:]
    out = set()
    for d in days:
        d = d.lower()[:3]
        if d not in DAY_NAMES:
            raise ValueError(f"bad day name {d!r} in reminder {r.get('id')}")
        out.add(DAY_NAMES.index(d))
    return out


def in_date_range(r: dict, today: date) -> bool:
    start = r.get("from")
    until = r.get("until")
    if start and today < date.fromisoformat(start):
        return False
    if until and today > date.fromisoformat(until):
        return False
    return True


def in_quiet_hours(now_t: time, qh: dict) -> bool:
    start, end = parse_hhmm(qh["start"]), parse_hhmm(qh["end"])
    if start <= end:                      # e.g. 13:00-15:00
        return start <= now_t < end
    return now_t >= start or now_t < end  # wraps midnight, e.g. 21:00-07:00


# ------------------------------------------------------------------------------ state


def state_path(user: str) -> pathlib.Path:
    return STATE_DIR / f"{user}-reminders.json"


def load_state(user: str) -> dict:
    p = state_path(user)
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return {"fired": {}}


def save_state(user: str, st: dict, today: date) -> None:
    cutoff = (today - timedelta(days=8)).isoformat()
    st["fired"] = {k: v for k, v in st["fired"].items() if k.rsplit(":", 1)[-1] >= cutoff}
    p = state_path(user)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(st, indent=2, sort_keys=True), encoding="utf-8")


def fired_today(st: dict, today: date) -> int:
    suffix = f":{today.isoformat()}"
    return sum(1 for k in st["fired"] if k.endswith(suffix))


# ---------------------------------------------------------------------------- sending


def resolve_topic(explicit: str | None) -> str | None:
    if explicit:
        return explicit
    env = os.environ.get("DUG_NTFY_TOPIC")
    if env:
        return env.strip()
    if TOPIC_FILE.exists():
        return TOPIC_FILE.read_text(encoding="utf-8").strip() or None
    return None


def send_ntfy(server: str, topic: str, title: str, message: str, tags: str, priority: str) -> bool:
    req = urllib.request.Request(
        f"{server.rstrip('/')}/{topic}",
        data=message.encode("utf-8"),
        method="POST",
        headers={
            "Title": title.encode("utf-8").decode("latin-1", "replace"),
            "Tags": tags or "muscle",
            "Priority": priority or "default",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return 200 <= resp.status < 300
    except urllib.error.URLError as e:
        print(f"ntfy error: {e}", file=sys.stderr)
        return False


def deliver(r: dict, args, topic: str | None) -> bool:
    title = r.get("title") or r["id"]
    message = r.get("message", "").rstrip()
    reply = r.get("reply")
    if reply:
        message = f"{message}\n\nReply to the trainer: \"{reply}\"".strip()
    if args.sink == "stdout" or args.dry_run:
        print(f"--- {title}\n{message}\n")
        return not args.dry_run
    if not topic:
        print("No ntfy topic. Set DUG_NTFY_TOPIC or write it to "
              f"{TOPIC_FILE} (see system/reminders.md).", file=sys.stderr)
        return False
    return send_ntfy(args.server, topic, title, message, r.get("tags", ""), r.get("priority", ""))


# -------------------------------------------------------------------------------- ics


def write_ics(cfg: dict, out: pathlib.Path) -> None:
    """Recurring all-schedule calendar with a 0-minute alarm per reminder. Import on the phone."""
    tz = cfg["timezone"]
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Dug Trainer//reminders//EN"]
    today = date.today()
    for r in cfg["reminders"]:
        if not r.get("enabled", True):
            continue
        byday = ",".join(DAY_NAMES[i].upper()[:2] for i in sorted(reminder_days(r)))
        for t in reminder_times(r):
            start = datetime.combine(today, t)
            uid = f"{r['id']}-{t.strftime('%H%M')}@dug-trainer"
            desc = (r.get("message", "") + (f"\\nReply: {r['reply']}" if r.get("reply") else "")) \
                .replace("\n", "\\n")
            rrule = f"RRULE:FREQ=WEEKLY;BYDAY={byday}"
            if r.get("until"):
                rrule += ";UNTIL=" + date.fromisoformat(r["until"]).strftime("%Y%m%dT235959")
            lines += [
                "BEGIN:VEVENT", f"UID:{uid}",
                f"DTSTART;TZID={tz}:{start.strftime('%Y%m%dT%H%M%S')}",
                f"DTEND;TZID={tz}:{(start + timedelta(minutes=10)).strftime('%Y%m%dT%H%M%S')}",
                rrule, f"SUMMARY:{r.get('title') or r['id']}", f"DESCRIPTION:{desc}",
                "BEGIN:VALARM", "ACTION:DISPLAY", "TRIGGER:PT0M",
                f"DESCRIPTION:{r.get('title') or r['id']}", "END:VALARM", "END:VEVENT",
            ]
    lines.append("END:VCALENDAR")
    out.write_text("\r\n".join(lines) + "\r\n", encoding="utf-8")
    print(f"wrote {out}")


# ------------------------------------------------------------------------------- main


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--user", required=True, help="users/<name>")
    ap.add_argument("--repo", help="personal repo path (default: found from this script's location)")
    ap.add_argument("--sink", choices=["ntfy", "stdout"], default="ntfy")
    ap.add_argument("--server", default=os.environ.get("DUG_NTFY_SERVER", DEFAULT_SERVER))
    ap.add_argument("--topic", help="ntfy topic (prefer DUG_NTFY_TOPIC or the config file)")
    ap.add_argument("--window", type=int, default=DEFAULT_WINDOW_MIN, help="minutes of lateness tolerated")
    ap.add_argument("--now", help="ISO datetime to pretend it is (testing)")
    ap.add_argument("--no-pull", action="store_true", help="skip the best-effort git pull")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--test", metavar="ID", help="send this reminder now")
    ap.add_argument("--ics", metavar="FILE", help="write the schedule as an .ics calendar and exit")
    args = ap.parse_args()

    repo = pathlib.Path(args.repo).resolve() if args.repo else find_repo(pathlib.Path(__file__).resolve().parent)
    cfg_path = repo / "users" / args.user / "reminders.json"
    if not cfg_path.exists():
        print(f"no reminders file at {cfg_path}", file=sys.stderr)
        return 2

    if not args.no_pull and not args.list and not args.ics:
        # Pick up schedule or message changes the trainer pushed from another session.
        # Best effort: offline or dirty = fall back to the file on disk.
        subprocess.run(["git", "-C", str(repo), "pull", "--ff-only", "-q"],
                       capture_output=True, timeout=60)

    cfg = load_config(cfg_path)
    tz = ZoneInfo(cfg["timezone"])
    now = datetime.fromisoformat(args.now).replace(tzinfo=tz) if args.now else datetime.now(tz)
    today = now.date()
    topic = resolve_topic(args.topic)

    if args.ics:
        write_ics(cfg, pathlib.Path(args.ics))
        return 0

    if args.list:
        print(f"{args.user}: {len(cfg['reminders'])} reminders, tz {cfg['timezone']}, "
              f"quiet {cfg['quiet_hours']['start']}-{cfg['quiet_hours']['end']}, cap {cfg['daily_cap']}/day")
        for r in cfg["reminders"]:
            flag = "on " if r.get("enabled", True) else "off"
            days = ",".join(DAY_NAMES[i] for i in sorted(reminder_days(r)))
            times = ",".join(t.strftime("%H:%M") for t in reminder_times(r))
            rng = f" until {r['until']}" if r.get("until") else ""
            print(f"  [{flag}] {r['id']:<18} {days:<27} {times}{rng}  agreed {r.get('agreed', '?')}")
        return 0

    by_id = {r["id"]: r for r in cfg["reminders"]}
    if args.test:
        if args.test not in by_id:
            print(f"no reminder with id {args.test!r}; ids: {', '.join(by_id)}", file=sys.stderr)
            return 2
        ok = deliver(by_id[args.test], args, topic)
        print(f"test {args.test}: sent={ok}")
        return 0 if ok or args.dry_run else 1

    st = load_state(args.user)
    window = timedelta(minutes=args.window)
    quiet = in_quiet_hours(now.time(), cfg["quiet_hours"])
    quiet_end = parse_hhmm(cfg["quiet_hours"]["end"])
    sent = 0

    for r in cfg["reminders"]:
        if not r.get("enabled", True) or not in_date_range(r, today):
            continue
        if now.weekday() not in reminder_days(r):
            continue
        for t in reminder_times(r):
            key = f"{r['id']}:{t.strftime('%H%M')}:{today.isoformat()}"
            if key in st["fired"]:
                continue
            due_at = datetime.combine(today, t, tzinfo=tz)
            # A time inside quiet hours is held until quiet hours end that morning.
            if in_quiet_hours(t, cfg["quiet_hours"]) and t < quiet_end:
                due_at = datetime.combine(today, quiet_end, tzinfo=tz)
            if not (due_at <= now < due_at + window):
                continue
            if quiet and not in_quiet_hours(t, cfg["quiet_hours"]):
                continue
            if fired_today(st, today) >= int(cfg["daily_cap"]):
                print(f"{now:%Y-%m-%d %H:%M} cap reached, skipped {r['id']}")
                continue
            ok = deliver(r, args, topic)
            print(f"{now:%Y-%m-%d %H:%M} {r['id']} sent={ok}")
            if ok and not args.dry_run:
                st["fired"][key] = now.isoformat(timespec="minutes")
                sent += 1

    if not args.dry_run:
        save_state(args.user, st, today)
    return 0


if __name__ == "__main__":
    sys.exit(main())
