# Golden Session — one full session traced through the rules (added 2026-10-25, user request)

This is the repo's test. A rulebook run by a language model has no unit tests; what it can
have is one worked session whose every number is derived from a named rule, so that a rule
change can be checked by re-tracing it. The user is **Sam Example**, fictional, whose files
are in `examples/sample-user/` in their *before* state. Nothing here is a real person.

**How to use it.** When a revision touches any rule this trace exercises, re-run the trace in
your head (or in a session with `examples/sample-user/` copied to `users/sam/`) and update
the affected numbers here in the same commit. The assertions in §8 are the pass/fail list.
If a rule change makes an assertion wrong, either the trace or the rule is wrong; decide
which before committing.

---

## 1. Opener

> Home workout today, 60 minutes.

Extracted: **location** Home · **time limit** 60 min · **special requests** none ·
date 2026-10-25 (Saturday).

## 2. Files read (and not read)

Per `operating-protocol.md` §1 and the read map in `sbs-progression-rules.md`:

| File | Read? | Why |
|---|---|---|
| operating-protocol, output-format, reporting-protocol | yes | the floor |
| sbs-progression-rules §1, §2, §3, §6 *Hypertrophy Block* only, §8, §10, §11, §12, §13a, §13 | yes | every-session set; current block is Hypertrophy |
| sbs-progression-rules §4, §4a, §5, §7, §9, §6 transitions / deload / rotation | no | Strength-only, no ceiling, no plateau query, 3 days since last session, not a boundary |
| bodyweight-ladders (General Rules, Ladder 2, Tracking) | yes | a ladder is in state |
| mcgill-pullups | yes, no action | FB-A carries v_pull and a pull-up is in state; Hypertrophy block, and the user is at ladder step 5 (no strict bodyweight pull-up yet), so neither cluster nor primer applies |
| splits | no | rotation already in state; no day-type conflict in the opener |
| bone-loading | no | state says "Not started" |
| conditioning-hiit | no | not requested; the "HIIT due" line comes from state |
| aerobic-base | no | not requested; its weekly line belongs to the Snapshot, which is not due |
| quick-sessions, kettlebell, suspension-trainer, modality-rotation, reminders, exercise-library | no | off-trigger (60 min; no KB or straps; not a deload; no reminders; no new exercise to choose) |
| users/sam/* (all four) | yes | always |

## 3. Gates (`operating-protocol.md` §2)

| Gate | Result |
|---|---|
| New user | no (`lastSessionDate` 2026-10-22) |
| Quick session | no (60 min, no trigger word) |
| Straps-only / KB-only location | no |
| Missed time | 3 days: no decay |
| Readiness | no flag word in the opener: `readiness.md` not read, no adjustment |
| Injury flags | right shoulder: prehab block prescribed verbatim; Barbell OHP and Dips excluded (neither is on FB-A anyway) |
| Unknown exercise | none |
| Loads | DB pairs by 5 lb; nothing at the 50 lb ceiling |
| Time limit | computed in §4; one cut |
| Bone module | not started: section omitted, file not read |
| Day type due | FB-A (`training-state.md` Split & Rotation) |
| HIIT | due since 2026-10-20, none performed: one-line note; full-body split, so a standalone on a non-lifting day (`splits.md` §3) |
| Weekly Snapshot | last 2026-10-20, 5 days: not due |

## 4. Deriving the prescription

Block parameters (`sbs-progression-rules.md` §6 Hypertrophy, Week 2): RIR 2; compounds 6–10,
isolation 8–12 (§3); rest 150 s compounds, 90 s isolation (§12); main lifts get one
maintenance set, 4 @ 82.5% e1RM, performed after the warmup ramp and before the working sets
(`bone-loading.md` §2 order, which applies whether or not the module is active).

| Exercise | Rule applied | Result |
|---|---|---|
| **DB Bench Press** (main) | §3 Step 4 after 2026-10-22's 10/9/9: same weight, aim ≥ 1 more total rep | 40 lb × 3 × 6–10, target 10/10/10 (29+ total) |
| maintenance set | 82.5% × e1RM 56 = 46.2 → nearest pair | 45 lb × 4 |
| warmup ramp (§10) | 40%, 60%, 80% of 40 = 16, 24, 32 → nearest pairs | 15 × 5, 25 × 5, 30 × 3, rest 45 s |
| **Chest-Supported DB Row** (main) | §3 Step 2 fired on 2026-10-22 (30 × 10/10/10): next increment, reps reset to the window low | 35 lb × 3 × 6–10, target 6 each |
| maintenance set | 82.5% × e1RM 42 = 34.65 → 35 | 35 lb × 4 (lands on the working weight; the rule still runs it) |
| warmup ramp | 14, 21, 28 → 15, 20, 30 | 15 × 5, 20 × 5, 30 × 3 |
| **Bulgarian Split Squat** | §3 Step 4 after 8/8/7: same weight, aim +1. Secondary compound: no maintenance set. §10 ramps the first compounds of the session; the two main lifts took it | 25 lb × 3 × 6–10/leg, target 8/8/8 |
| **Pull-up ladder** | `bodyweight-ladders.md` Ladder 2, step 5, advance standard 3 × 8 | 3 × 8, light band |
| **DB Hammer Curl** | §3 Step 4 after 12/12/11 | 20 lb × 3 × 8–12, target 12/12/12 |
| **Prehab** | `injury-protocols.md`, fixed block, 2 rounds | Band Pull-apart 15 · Band External Rotation 12/side |

**Duration** (`output-format.md`, 3 s per rep, unilateral both sides, window top, 60 s setup
per exercise, 15% margin):

| Item | Work | Rest | Setup | Seconds |
|---|---|---|---|---|
| Prehab: 4 item-rounds × 60 s + 4 × 30 s transitions | 240 | 120 | — | 360 |
| Bench ramp: 13 reps × 3 s; 2 × 45 s | 39 | 90 | 60 | 189 |
| Row ramp | 39 | 90 | 60 | 189 |
| Bench: (4 + 30 reps) × 3 s; 3 × 150 s | 102 | 450 | 60 | 612 |
| Row: (4 + 30) × 3; 3 × 150 | 102 | 450 | 60 | 612 |
| Bulgarian: 3 × 10 × 2 legs × 3 s; 2 × 150 | 180 | 300 | 60 | 540 |
| Pull-up: 24 × 3; 2 × 150 | 72 | 300 | 60 | 432 |
| Hammer Curl: 36 × 3; 2 × 90 | 108 | 180 | 60 | 348 |
| **Full sheet** | | | | **3,282 s = 54.7 min × 1.15 = 62.9 min** |

62.9 > 60, so cut from the end of the accessory order (`operating-protocol.md` §2): drop the
Hammer Curl. 2,934 s = 48.9 min × 1.15 = **56.2 min**. Fits. Prehab, ramp and the first two
working exercises were never candidates.

## 5. Output

### Block 1 — Coaching view

```
## Saturday — Home (FB-A)
Block: Hypertrophy | Week 2 of 4

### Prehab (right shoulder, always-active)
- Band Pull-apart: 2 x 15
- Band External Rotation: 2 x 12/side
  (2 rounds: one set of each, then repeat)

### Warmup Ramp
- DB Bench Press: 15 lb x 5, 25 lb x 5, 30 lb x 3 (rest 45s)
- Chest-Supported DB Row: 15 lb x 5, 20 lb x 5, 30 lb x 3 (rest 45s)

### Working Sets
1. **DB Bench Press** — maintenance 1 x 4 @ 45 lb, then 3 x 6-10 @ 40 lb DBs | Rest: 150s
   > Progression note: Step 4, same load; last was 10/9/9, aim for 29+ total. Maintenance = 82.5% of e1RM 56 → 45.
   > Last session: 2026-10-22, 40 x 10, 9, 9

2. **Chest-Supported DB Row** — maintenance 1 x 4 @ 35 lb, then 3 x 6-10 @ 35 lb DBs | Rest: 150s
   > Progression note: advanced from 30 after 10/10/10; reps reset to 6. Maintenance rounds to the working weight; it still runs.
   > Last session: 2026-10-22, 30 x 10, 10, 10

3. **Bulgarian Split Squat** — 3 x 6-10/leg @ 25 lb DBs | Rest: 150s
   > Progression note: Step 4, same load; last 8/8/7, aim for 8/8/8.
   > Last session: 2026-10-20, 25 x 8, 8, 7/leg

4. **Pull-up (ladder step 5, light band)** — 3 x 8 | Rest: 150s
   > Progression note: advance standard. 3 x 8 clean → step 6 (full pull-up) next, starting 3 x 5.
   > Last session: 2026-10-20, 7, 7, 6

### Session Notes
- Estimated duration: ~56 min (full sheet computed at 63 min; DB Hammer Curl cut to fit 60)
- Today's focus: Hypertrophy Week 2; the row's first session at 35 lb
- Effort target: RIR 2 (good-hard)
- HIIT due — 5 days since the week opened, none performed. Tomorrow is 24 h clear on both sides of a lifting day: standalone slot, Format A, stairs.
```

### Block 2 — Checklist view

```
2026-10-25 — Home (FB-A) — Hypertrophy Wk 2/4

PREHAB
ROUND 1
Band Pull-apart — 15

Band External Rotation — 12/side

ROUND 2
Band Pull-apart — 15

Band External Rotation — 12/side

WARMUP
DB Bench Press — 15 lb — 5
DB Bench Press — 25 lb — 5
DB Bench Press — 30 lb — 3

Chest-Supported DB Row — 15 lb — 5
Chest-Supported DB Row — 20 lb — 5
Chest-Supported DB Row — 30 lb — 3

WORKING
DB Bench Press — R2m30s
DB Bench Press — Maintenance — 45 lb — 4
DB Bench Press — Set 1 — 40 lb — 10
DB Bench Press — Set 2 — 40 lb — 10
DB Bench Press — Set 3 — 40 lb — 10

Chest-Supported DB Row — R2m30s
Chest-Supported DB Row — Maintenance — 35 lb — 4
Chest-Supported DB Row — Set 1 — 35 lb — 6
Chest-Supported DB Row — Set 2 — 35 lb — 6
Chest-Supported DB Row — Set 3 — 35 lb — 6

Bulgarian Split Squat — R2m30s
Bulgarian Split Squat — Set 1 — 25 lb — 8/leg
Bulgarian Split Squat — Set 2 — 25 lb — 8/leg
Bulgarian Split Squat — Set 3 — 25 lb — 8/leg

Pull-up (step 5, light band) — R2m30s
Pull-up (step 5, light band) — Set 1 — 8
Pull-up (step 5, light band) — Set 2 — 8
Pull-up (step 5, light band) — Set 3 — 8
```
Annotate what changed and paste it back.

## 6. The report, parsed

The user pastes back the checklist with these changes (everything else untouched):

```
DB Bench Press — Maintenance — 45 lb — 4
right shoulder pinched a little on rep 3, eased off, working sets fine
...
DB Bench Press — Set 3 — 40 lb — 9
...
Chest-Supported DB Row — Set 1 — 35 lb — 8
Chest-Supported DB Row — Set 2 — 35 lb — 7
Chest-Supported DB Row — Set 3 — 35 lb — 6 hard
```

`reporting-protocol.md`:

| Line | Reading |
|---|---|
| Free-text line under the bench maintenance line | attaches to the line above (the maintenance set). "pinched" is a pain report → **Pain Response Protocol for DB Bench Press** |
| Bench Set 3: 9 | actual reps; Sets 1–2 unchanged = 10 at RIR 2 |
| Row 8 / 7 / 6, "hard" on Set 3 | actual reps; Set 3 at RIR 1; the exercise's effort for stall tracking is its hardest set |
| Bulgarian, pull-up unchanged | 8/8/8 and 8/8/8 at the prescribed RIR |
| Hammer Curl | not on the sheet: not performed, not a miss |

## 7. Decision tree and state edits

| Exercise | §3 steps | Bookkeeping | Result in state |
|---|---|---|---|
| **DB Bench Press** | Step 1 no (no set under 6, no fail) · Step 2 no (not all at 10) · Step 4: same weight, aim +1 | stallCounter stays 0 (effort not hard). e1RM: Set 1 = 40 × (1 + 12/30) = **56**, equals stored; maintenance set 45 × (1 + 6/30) = 54, lower. Stored stays 56 | **Overridden by the Pain Response Protocol**: state `TEST` (`return-to-training.md` §1). Next session on the lift = the §2 test: one increment down, **35 lb × 3 × 6** (window floor), RIR ≥ 3, 3-s eccentric, extra ramp set 15 × 8, **no maintenance set**. PRP opened 2026-10-25. The pending Step 4 result (40, aim +1) is recorded and resumes at `CLOSED`; a sensation on the test = `EXCLUDED` (protocol step 5). Neighbour (§5): Seated DB OHP holds its load on the next FB-B even if it hits 10/10/10 |
| **Chest-Supported DB Row** | Step 1 no (6 is the floor, not below it) · Step 2 no · Step 4: same weight, aim +1 | effort hard and weight did not increase → **stallCounter 0 → 1**. e1RM: Set 1 = 35 × (1 + 10/30) = **46.7**; Set 3 = 35 × (1 + 7/30) = 43.2; maintenance = 42. Session best 46.7 > stored 42 → **stored 46.7** | next: 35 × 3 × 6–10, target 8/8/7+. Next maintenance set: 82.5% × 46.7 = 38.5 → **40 lb × 4** |
| **Bulgarian Split Squat** | Step 4 | stallCounter 0 | next: 25 × 3 × 6–10/leg, aim 9/8/8 |
| **Pull-up ladder** | advance standard met (3 × 8 clean at step 5) | stallCounter 0; `lastSessionDate` 2026-10-25 | **currentStep 6** (full pull-up), start 3 × 5 |
| **DB Hammer Curl** | not performed | nothing changes | next: unchanged (20 × 3 × 8–12) |

Rotation: next due **FB-B**. `lastSessionDate` **2026-10-25**. HIIT due: still yes.
§8 reactive-deload triggers: none. §13 same-day overshoot: not applicable (reported after).

**State diff** (`users/sam/training-state.md`):

```
- **Next due**: FB-A · HIIT due: yes, since 2026-10-20
+ **Next due**: FB-B · HIIT due: yes, since 2026-10-20 (standalone slot possible 2026-10-26)
- **Last session date**: 2026-10-22
+ **Last session date**: 2026-10-25

DB Bench Press
+ PRP: shoulder (right) · opened 2026-10-25 on maintenance set 45 × 4 · state TEST
+      pre-flag: 40 × 3 × 6–10, pending Step 4 (aim +1) · test: 35 × 3 × 6, 3-s ecc, RIR ≥ 3, no maintenance set
+      log: 10-25 opened · —
  history: … · 2026-10-25 45 × 4 (maint, pinch) · 40 × 10/10/9
- next: 40 × 3 × 6–10, aim ≥ 1 more total rep (§3 Step 4)
+ next: TEST per return-to-training.md §2 (above); pending Step 4 resumes at CLOSED

Seated DB Overhead Press
+ hold: shoulder PRP open — no Step 2 advance or §13a fast-track on the next FB-B (return-to-training.md §5)

Chest-Supported DB Row
- stallCounter 0 · e1RM 42
+ stallCounter 1 · e1RM 46.7 (2026-10-25, 35 × 8 @ RIR 2)
  history: … · 2026-10-25 35 × 8/7/6 (hard)
+ next: 35 × 3 × 6–10, aim ≥ 1 more; maintenance 40 × 4

Bulgarian Split Squat
  history: … · 2026-10-25 25 × 8/8/8
  next: 25 × 3 × 6–10/leg, aim ≥ 1 more

Pull-up ladder
- currentStep: 5 (band-assisted, light band) · lastSessionDate: 2026-10-20
+ currentStep: 6 (full pull-up) · lastSessionDate: 2026-10-25
  history: … · 2026-10-25 step 5 × 8/8/8 → advance
+ next: 3 × 5 at step 6
```

**Log entry** appended to `users/sam/workout-log.md`:

```
## 2026-10-25 — Home (FB-A) — Hypertrophy Wk 2/4

### Working Sets
- DB Bench Press: 45 × 4 (maintenance) · 40 × 10, 10, 9 (good-hard)
  > Right shoulder pinched on the maintenance set (rep 3), eased, working sets fine.
  > Pain Response Protocol opened (state TEST); next session is a test at 35 lb × 3 × 6, 3-s eccentric, no maintenance set.
- Chest-Supported DB Row: 35 × 4 (maintenance) · 35 × 8, 7, 6 (hard on set 3)
- Bulgarian Split Squat: 25 × 8, 8, 8/leg (good-hard)
- Pull-up ladder step 5 (light band): 8, 8, 8 → step 6 (full pull-up) next, 3 × 5
  > DB Hammer Curl cut for time (60-min limit); not a miss.
  > HIIT due; standalone slot possible 2026-10-26.
```

Then: `git add -A && git commit -m "2026-10-25" && git push`. The reply to the user states,
in a few lines, what changed and why: bench held and under a test next time because of the
pinch, row e1RM up, pull-up moved to full pull-ups.

**Session-end review** (`operating-protocol.md` §6): no improvisation was needed; every
number above names its rule. Nothing proposed.

## 8. Assertions (the pass list)

A re-trace after a rule change must still produce all of these, or the change explains why
not and updates this file:

1. The files in §2 marked "no" are not read; bone-loading and McGill in particular.
2. Bench maintenance set = 45 lb × 4 (82.5% × 56 = 46.2 → nearest pair).
3. Row maintenance set = 35 lb × 4 even though it equals the working weight.
4. Bench ramp = 15 × 5, 25 × 5, 30 × 3; row ramp = 15 × 5, 20 × 5, 30 × 3; 45 s rest.
5. Row working target after an advance = 6 (window low), not 8 or 10.
6. Full sheet = 62.9 min; Hammer Curl is the one cut; result 56.2 min; prehab, ramp and the first two working exercises untouched.
7. Checklist: one line per set, prehab as ROUND 1 / ROUND 2, rest once per exercise as `R2m30s`, blank line between exercises, no BONE section.
8. The free-text line attaches to the maintenance set above it and opens a Pain Response Protocol on DB Bench Press; it does not touch any other exercise's progression.
9. Bench next = `TEST`: 35 lb × 3 × 6, RIR ≥ 3, 3-s eccentric, no maintenance set; stored e1RM 56 unchanged; the OHP holds its load on the next FB-B.
10. Row: 6 reps is not a Step 1 failure; stallCounter becomes 1; e1RM becomes 46.7; next maintenance set 40 × 4.
11. Pull-up ladder advances to step 6 at 3 × 5.
12. Hammer Curl: no state change, no miss, one log note.
13. Rotation advances to FB-B; HIIT stays due with a one-line note; the log entry is written only after the report, never from the prescription.
