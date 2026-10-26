# Reminders — scheduled phone pings the user agreed to (added 2026-10-18, user request)

Anything in this program that benefits from a regular rhythm can become a phone reminder:
bone drops, a core snack, a kettlebell practice, "HIIT is due", "deload week, two day types
left". Reminders are **opt-in, agreed one by one, and reviewed**. The trainer proposes; the
user decides; the schedule is written down; the phone does the remembering. The trainer never
adds, removes or reschedules a reminder on its own, and a reminder the user keeps ignoring is
dropped, not repeated louder.

Per-user reminders live in `users/<name>/reminders.json` (template in `templates/user/`).
The sender is `system/scripts/remind.py`. Neither holds anything secret; the push address
(the ntfy topic) lives outside the repo (§5).

---

## 1. Principles

1. **Agreed, not imposed.** A reminder exists only after the user said yes to its content,
   days and time. "Mutually agreed" means the trainer proposes a concrete schedule from what
   it knows (training days, stated availability, the module's own cadence) and the user
   confirms or edits it. The agreement date is recorded on the entry.
2. **One thing per ping, and it is actionable.** The message is the prescription itself
   (moves and doses), not "remember to exercise". It ends with the reply phrase that logs it.
3. **Few.** Start with at most three reminders. Daily cap 4 (configurable), quiet hours
   21:00–07:00 by default, never two pings for the same thing in a day.
4. **State-driven messages track the state.** When a rung advances, HIIT is done, or a
   deload closes, the trainer edits the reminder's `message`, `enabled` or `until` **in the
   same commit as the state change**. This mirrors the bone-ping rule in `bone-loading.md` §5:
   a reminder that lags the state prescribes the wrong thing.
5. **Measured.** Every 4 weeks (at the block boundary, during the deload) the trainer lists
   each reminder with its hit rate: pings sent vs. "did my …" replies or matching log entries.
   Any reminder under one hit in three gets a keep / change / drop question. Any reminder at
   zero hits over 4 weeks is proposed for dropping, once. A class of ping the user never acts
   on is noise, and noise trains the user to ignore the useful ones.
6. **Easy to pause.** "Pause reminders for a week" → every entry gets `until` or `enabled:
   false` with a note; the trainer re-offers them once when the week is over. Travel, illness
   and a Pain Response Protocol are the usual reasons.
7. **Never a nag.** A skipped ping is not a miss anywhere in the program. The trainer does not
   mention unanswered pings in session, except in the 4-week review.

---

## 2. What can be reminded (the catalogue)

| `kind` | Says | Default cadence | Rules file | Message source |
|---|---|---|---|---|
| `bone` | Today's impact and upper-limb rungs, doses, cues | daily, mid-morning | `bone-loading.md` §5 | state-driven (rung table) |
| `quick:core` | A core snack (McGill Big 3 or the 10-min circuit) | 2×/week, afternoon | `quick-sessions.md` | family fixed, instance rotates |
| `quick:kb` | A kettlebell snack (swing EMOM, S&S-lite, carry medley) | 2–3×/week, non-leg days | `kettlebell.md`, `quick-sessions.md` | instance rotates |
| `quick:trx` | A 10-min strap circuit | 1–2×/week | `suspension-trainer.md` | instance rotates |
| `quick:cardio` | Stair snack or 7-minute workout | weekdays | `quick-sessions.md` | instance rotates |
| `quick:mobility` | The user's fixed prehab block as a 5-min snack, or the mobility snack | daily, evening | `quick-sessions.md`, `injury-protocols.md` | fixed |
| `walk` | 5-min walk break | 1–3 fixed times on desk days | `quick-sessions.md` | fixed |
| `aerobic` | "Aerobic this week: [done]/[target] min, [n] days left" | on stated rest days, morning | `aerobic-base.md` §4 | state-driven (rolling 7-day tally) |
| `balance` | An anchored stance bout: "Kettle / teeth: [position] (S[rung]), [hold] each side" | daily, at the user's named anchor | `balance.md` §6 | state-driven (rung table) |
| `power` | Today's jump and throw rungs with doses; "48 h since the last lower bout?" | 1–2×/week, non-leg days, morning | `power-and-plyometrics.md` §6 | state-driven (rung table) |
| `gtg` | Grease-the-groove set (pull-up / push-up, ≤ 50% max) | 2–4 fixed times/day on non-pull days | `bodyweight-ladders.md` gap bridge 1 | state-driven (current step) |
| `state:train` | "Next up: [day type]. HIIT due? Deload?" on the user's stated training days | per training day, morning | `operating-protocol.md` §2 | state-driven |
| `state:hiit-due` | HIIT has been next for N days; next format | daily once HIIT is ≥ 7 days overdue, `until` it is done | `conditioning-hiit.md` §2 | state-driven |
| `state:deload` | Deload open; day types still to cover; calendar floor date | daily during the window | `sbs-progression-rules.md` §6 | state-driven, `until` = floor date |
| `state:rotation` | Accessories due to rotate at this boundary, with proposals | once, first deload day | `sbs-progression-rules.md` §6, `modality-rotation.md` | state-driven |
| `state:benchmark` | HIIT or kettlebell benchmark due | every 8 weeks | `conditioning-hiit.md` §7, `kettlebell.md` §5 | state-driven |
| `snapshot` | "Ask for your weekly snapshot" | weekly, Sunday evening | `operating-protocol.md` §5 | fixed |

Anything outside training (water, sleep, supplements) is out of scope for this file.

**Quick-session reminders carry the family, not the instance.** The ping names the family
and today's pick; the trainer chooses the instance when writing the message, rotating per
`quick-sessions.md` §4 so the same snack is not served more than twice running.

---

## 3. The agreement protocol

**When the trainer offers reminders** (and only then):
- At intake, after goals, equipment and injuries: "Do you want phone reminders for any of
  this? The usual first three are …" with a concrete proposal.
- When the user asks ("remind me to …", "can I get a ping for …").
- When a module's own rhythm is slipping: a bone tally below minimum 3 weeks running, HIIT
  overdue by 14 days, a quick-session family enabled but unused for 3 weeks. Offer **once**
  per trigger, in one line, in the Session Notes.
- At the 4-week review (§1 principle 5).

**How the proposal looks** (coaching view or chat, never buried in prose):

```
Proposed reminders (say "yes", or edit any line):
| id          | days         | time  | says                                   | reply            |
| bone-drops  | daily        | 10:00 | Heel drops 2x15 · Pogo hops 2x15       | did my bone drops |
| core-snack  | Tue, Thu     | 15:00 | McGill Big 3, 5-3-1, 10 s holds        | did my core snack |
| hiit-due    | daily (auto) | 08:00 | only while HIIT is ≥ 7 days overdue     | HIIT today        |
```

Defaults the trainer uses to pick times, unless the user says otherwise: morning pings
08:00–10:00, afternoon snacks 14:00–16:00, evening mobility 19:00–20:00, nothing inside quiet
hours, nothing within 2 h before a stated training time, no lower-body snack the day before
a legs session (quick-sessions §2). Days come from the user's stated training days and desk
days; the trainer asks for those once if it does not have them.

**On "yes"** the trainer writes the entries into `users/<name>/reminders.json` with
`"agreed": "<today>"`, commits them with the session, and tells the user which delivery
route (§4) is in place or still needs the one-time setup (§5).

**Edits.** The user can change any field by saying so ("move core to 4pm", "drop the walk
pings", "pause everything until the 28th"). The trainer applies it and the commit message
names the change. The trainer may change `message`, `enabled` and `until` without asking
**only** to track state (principle 4), and says so in the Session Notes in one line.

**What the trainer never does:** add a reminder because it seems useful, raise frequency,
move a time earlier than agreed, or re-enable a dropped reminder without a new yes.

---

## 4. Delivery routes (pick one; the file is the same for all)

| Route | Needs | Best for |
|---|---|---|
| **A. ntfy + cron** (`remind.py`) | A computer that is on at the scheduled times (a home server, a Raspberry Pi, a desktop that never sleeps) and the free ntfy app on the phone | Everything, including state-driven reminders, because the script re-reads the repo each run |
| **B. Calendar file** (`remind.py --ics`) | Nothing but the phone | Fixed-schedule reminders (bone, snacks, walks). State-driven ones go stale between re-exports; re-export at each block boundary |
| **C. Claude Code scheduled routine** | A Claude plan with scheduled routines and outbound network from the routine | A routine that opens the personal repo at the agreed times and pushes to ntfy; useful when no always-on computer exists. Confirm the routine can reach ntfy before relying on it |
| **D. Any other notifier** | `remind.py --sink stdout` piped into it | Home-automation systems, Slack, email |

Route A is the reference implementation. The others are fallbacks; a user without any
always-on machine takes B.

---

## 5. One-time setup for route A (10 minutes, no accounts)

1. **Phone:** install the **ntfy** app (Android: Play Store or F-Droid; iPhone: App Store).
   Tap **+**, subscribe to a topic with a long random name, e.g.
   `trainer-7f3a9c2e1b5d4a8f`. Anyone who knows the topic name can push to it, so treat it
   like a password: never commit it, never paste it in a public place.
2. **Computer that stays on:** put the topic name in one file, nowhere else:
   ```bash
   mkdir -p ~/.config/dug-trainer && echo trainer-7f3a9c2e1b5d4a8f > ~/.config/dug-trainer/ntfy-topic
   ```
   (or set the environment variable `DUG_NTFY_TOPIC`). Windows: also `pip install tzdata`.
3. **Test once:**
   ```bash
   python3 /path/to/your-repo/system/scripts/remind.py --user <name> --list
   python3 /path/to/your-repo/system/scripts/remind.py --user <name> --test <id>
   ```
   The phone should buzz within a few seconds.
4. **Schedule the checker every 15 minutes** (`crontab -e`, one line):
   ```
   */15 * * * * /usr/bin/python3 /path/to/your-repo/system/scripts/remind.py --user <name> >> ~/dug-remind.log 2>&1
   ```
   The script pulls the repo first (best effort), fires what came due in the last 20
   minutes, holds anything inside quiet hours until they end, and records what it sent in
   `~/.local/state/dug-trainer/<name>-reminders.json` so a re-run never double-sends.
5. **Route B instead:** `remind.py --user <name> --ics reminders.ics`, send the file to the
   phone, open it, and the phone's calendar imports every reminder as a repeating event with
   an alarm.

A user whose personal repo already runs its own reminder script (for example an older
bone-ping job) keeps it until they choose to move the entry into `reminders.json`; the two
must not both be enabled for the same `kind` on the same day.

---

## 6. `reminders.json` schema

```json
{
  "version": 1,
  "timezone": "America/Los_Angeles",
  "quiet_hours": {"start": "21:00", "end": "07:00"},
  "daily_cap": 4,
  "reminders": [
    {
      "id": "bone-drops",              // unique, stable; used in replies and the state file
      "kind": "bone",                  // catalogue key (§2)
      "enabled": true,
      "days": "daily",                 // or "weekdays", "weekends", or ["mon","wed","fri"]
      "time": "10:00",                 // or "times": ["11:00","15:00"] for several a day
      "from": "2026-10-20",            // optional: first day it may fire
      "until": "2026-10-26",           // optional: last day it may fire (deload, pauses)
      "title": "Bone drops",
      "message": "- Heel drops: 2 x 15\n- Pogo hops (Rung 2): 2 x 15",
      "reply": "did my bone drops",    // appended to the ping; the phrase that logs it
      "tags": "bone",                  // ntfy icon tag, optional
      "priority": "default",           // ntfy priority, optional
      "agreed": "2026-10-13"           // date the user said yes to this schedule
    }
  ]
}
```

Times are local to `timezone`. A time inside quiet hours is delivered when quiet hours end.
`id` never changes once agreed; to change what a reminder is, edit its fields, do not
re-create it, or the review loses its history.

---

## 7. Logging the replies

A reply that matches a reminder's `reply` phrase, or any natural-language equivalent ("did
the hops", "core done"), is logged by the module that owns the `kind`: bone bouts to the
bone bout log, quick sessions to the Quick Sessions log, GtG sets to the ladder's daily
total, a training-day reply to nothing (it just starts the session). The reminders file
itself keeps no log. Hit rate for the 4-week review is computed from the module logs
against the days the reminder was enabled.

---

## 8. Why this design (brief)

- Prompts work when they are specific, timely and tied to an action the person already
  intends; generic "be active" prompts fade within weeks. Implementation-intention style
  cues ("when X, do Y") roughly double follow-through on health behaviours in meta-analysis
  (Gollwitzer & Sheeran 2006). The ping is therefore the prescription plus the cue, not a
  slogan.
- The trial evidence on push prompts is mixed and modest. Well-timed prompts raise
  short-term engagement with a health app (Bidargaddi 2018, micro-randomised trial), and in
  one small trial more frequent prompts led to more actions without raising overall use or
  driving people away (Morrison 2017, n = 77, exploratory). What no trial supports is that
  volume alone helps; relevance and timing carry the effect. Hence messages that track the
  state, a daily cap, and a review loop that drops what is not acted on rather than
  repeating it.
- Variety of content helps adherence, which is why quick-session pings rotate the instance
  (see `modality-rotation.md` for the adherence evidence on variety).

**References**
1. Gollwitzer PM, Sheeran P. 2006. Implementation intentions and goal achievement: a meta-analysis of effects and processes. *Adv Exp Soc Psychol* 38:69–119. doi:10.1016/S0065-2601(06)38002-1
2. Bidargaddi N et al. 2018. To prompt or not to prompt? A microrandomized trial of time-varying push notifications to increase proximal engagement with a mobile health app. *JMIR Mhealth Uhealth* 6(11):e10123. doi:10.2196/10123
3. Morrison LG et al. 2017. The effect of timing and frequency of push notifications on usage of a smartphone-based stress management intervention: an exploratory trial. *PLoS One* 12(1):e0169162. doi:10.1371/journal.pone.0169162
