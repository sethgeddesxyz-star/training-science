# Reporting and Logging

**Never log a session that has not happened.** A prescription is not a result. Until
the user reports, either leave the log untouched or write the entry under a
"Prescribed" heading marked `RESULTS PENDING` — never under "Working Sets." Never
invent reps or effort.

**Effort is reported by exception.** Never ask for per-exercise ratings. Silence means
clean completion at the session's prescribed RIR. The user flags "easy" when a load
should jump, a failure when one happens, and pain when it occurs.

---

## Parsing a returned checklist

| User's change to the line | Interpretation |
|---|---|
| Unchanged | Completed as prescribed, at the session's prescribed RIR |
| Rep number changed | Actual rep count for that set |
| Weight changed | Actual load used |
| Free text appended | Note on that set — effort, pain, form, substitution |
| Deleted, or marked `x` / `skip` | Set not performed |
| Line added | Extra set or exercise; add to the log |

**Rep-out lines** (Strength-block main lifts, `sbs-progression-rules.md` §4a): the number
written is the reps done at the line's cap (RIR 1, or RIR 2 where overridden); unchanged = exactly the target (`4+` unchanged = 4). An
appended pain, joint or stop-rule note means the set is not scored.

**HIIT lines**: parsed per `system/conditioning-hiit.md` §9 — a changed number is actual
output (watts, pace, speed); an appended HR is peak HR for that rep. A skipped HIIT session
leaves HIIT due.

**AEROBIC lines** (`system/aerobic-base.md` §4): unchanged = done at the prescribed minutes
under the ceiling; a changed number = actual minutes; appended HR or pace = data; "over" =
over ceiling, still counts. A natural-language report of easy cardio ("walked 40 min") logs
the same way with its date; under 20 min it goes to the quick-session log instead. Never
touches the HIIT ledger or any lift.

**BONE lines** (optional module): unchanged = performed as prescribed; deleted or `x` =
not performed, which is **not a miss** and affects nothing else. Log every performed bout
to the Bone Loading Module's bout log in `training-state.md` and recompute the tally.
Next-morning Achilles, shin or foot soreness reported later still counts against that bout
(`system/bone-loading.md` §3).

**Quick-session lines** (`system/quick-sessions.md` §6): unchanged = done; a number on a
circuit or EMOM line = rounds or minutes completed; `x` = skipped, which is **not a miss**.
Log to the Quick Sessions log in `training-state.md`, advance that session's own small
ladder only, and never touch the main lifts' state unless the entry is the 20-minute full
body on tracked lifts (its own rule says when).

**Kettlebell and strap lines**: parsed like any set line. A changed bell or mark is the
actual load; "form broke", "ugly rep", "lost the bell" ends the set at the rep given and
holds the step (`kettlebell.md` §4, `suspension-trainer.md` §2). Timed standards (S&S
5:00 swings, 10:00 get-ups) report the time achieved.

**Reminder replies** ("did my bone drops", "core done", "HIIT today"): the module that owns
the reminder's `kind` logs it (`system/reminders.md` §7). Never log a ping as done without a
reply.

Free text outranks the defaults. "Easy" or "too light" triggers the §13a undershoot
fast-track. **Any mention of pain triggers the Pain Response Protocol
(`users/<name>/injury-protocols.md`) and overrides all progression for that
exercise.** A note on an exercise's first set applies to that exercise unless a later
set contradicts it.

**A free-text line of its own, not appended to a set line (added 2026-09-12, approved),**
attaches to the set line **immediately above it**. If that line's numbers contradict the
note, the line is self-contradictory: ask, and record only what is unambiguous in the
meantime. Never resolve the contradiction by choosing a rep count. Worked example — the
2026-09-12 reverse lunge returned three unchanged 7/leg lines with `Stopped at 4, knee
flag` sitting between the Set 2 and Set 3 lines. This rule attaches the note to Set 2,
which the user then confirmed (Set 1 7/leg, Set 2 4/leg, Set 3 skipped).

Do not ask the user to confirm untouched lines — untouched *is* the report. Ask only
when a line is genuinely ambiguous or self-contradictory. If a report contradicts
something earlier in the conversation, say so plainly and ask which is correct rather
than picking one.

---

## Natural-language reports

Same treatment: parse into (exercise, sets, reps, weight, effort), apply the decision
tree, edit `training-state.md` and `workout-log.md` in place, push, and state briefly
what changed and why.
