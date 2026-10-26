# training-science — plan

Public shared rulebook for Dug Trainer. Personal repos mount it as a submodule at
`system/`. Nothing personal is committed here. No deploy: commit and push to main.

## Goal (2026-10-25)

Close the gaps found in the 2026-10-25 overview, most important first. Each gap lands as
one commit in the house style (dated header, numbered sections, rules then evidence,
no personal data). Nutrition and bodyweight tracking are explicitly out of scope: a new
tracking vector, not a rule gap.

## Ranked gap list

| # | Gap | Why this rank | Status |
|---|-----|---------------|--------|
| 1 | Splits beyond push/pull/legs: HIIT placement, prehab, McGill, Bone Doubles, carries, modality floor and deload coverage are all written against PUSH → LEGS → PULL → HIIT; full body and upper/lower are named but undefined | Wrong or improvised prescriptions for any user under 5 days/week | done (`splits.md`) |
| 2 | Per-session read is heavy (often 1,500+ lines per workout; bone-loading and McGill read every session) | Clause-dropping risk on every other rule | done (read map) |
| 3 | No worked example / golden session: a filled sample user and one session traced through the decision tree | The only test an LLM-run rulebook can have; catches drift in 1 and 2 | done (`examples/`) |
| 4 | No session-start readiness check (sleep, soreness, stress feed nothing until a deload trigger fires after the fact) | Daily load accuracy | done (`readiness.md`) |
| 5 | Easy aerobic work has no slot: heart-rate card only, no day type, target or log | Feature gap; the card exists, the program does not | done (`aerobic-base.md`) |
| 6 | Return-to-training after a pain flag: protocol stops and substitutes, then "test lighter"; no ramp back, no rule for clearing a flag | Safety, but rare | done (`return-to-training.md`) |
| 7 | No mobility / joint-prep layer; warmup ramp is a load ramp only | Feature gap | done (`warmup-and-mobility.md`) |
| 8 | No tags or changelog; personal repos pin a bare hash | Housekeeping | done (`CHANGELOG.md`, tags) |
| — | Nutrition / bodyweight tracking | Skipped by decision 2026-10-25 | skipped |

## Exercise-type brainstorm (2026-10-26)

Twelve candidate exercise types were ranked against what the repo already covers. The two
picked first close the "aging athlete" hole the bone module only half covers; the rest are
listed so they are not re-derived.

| # | Module | Why | Status |
|---|--------|-----|--------|
| 1 | Power and plyometrics (jumps, throws, intent cue) | Power is lost faster than strength and predicts function; jumping existed only inside the bone module | done (`power-and-plyometrics.md`) |
| 2 | Balance and fall prevention (static, stepping, reactive) | Strongest fall-prevention evidence of any exercise type; zero coverage | done (`balance.md`) |
| 3 | Isometrics as a tool (wall squat, handgrip for blood pressure; long holds for tendon pain) | Best BP effect of any mode in the 2023 BJSM meta-analysis; mentioned only as warm-up filler | open |
| 4 | Fitness benchmarks (grip, 30-s sit-to-stand, dead hang, push-up count, walk/run VO2 estimate) | A whole-person scorecard every 8–12 weeks; KB, HIIT, power and balance each have one, nothing joins them | open |
| 5 | Band repertoire | Named as a modality family but, unlike KB and TRX, has no file | open |
| 6 | Prehab hotspot library (calves, tibialis, ankle, neck, rotator cuff, Nordics) | Referenced in 17 files, exercises scattered; calves and feet nearly absent | open |
| 7 | Rucking / loaded walking | Bridges aerobic minutes, bone loading and carries | open |
| 8 | Jump rope snack | Quick session plus impact | open |
| 9–11 | Sandbag / odd objects · skill and play days · neck, forearm, calf as declared goals | nice to have | parked |
| — | Daily steps | A tracking vector, same reason as nutrition | skipped |

## Working rules for this repo

- Every new rule file: `# Title — one line (added YYYY-MM-DD, user request)`, numbered
  sections, rules before evidence, references last with DOIs.
- Touch `operating-protocol.md` only to add the file-table row and the read trigger.
- Never a user's name, load, log or injury in any file here.

## Open items

- [x] Merged `rules/gap-closing` into `main` (fast-forward) and pushed, 2026-10-25. `v1.1`
      sits on main's head.
- [ ] Real personal repos (DugTrainerClaude and any other) pull the new rules with
      `git submodule update --remote system` and fill the new state lines (Next due,
      Last Weekly Snapshot, Readiness flags, Aerobic Base) at their next session.
- [ ] The Hypertrophy maintenance set rounds to the working weight at the window top with
      5-lb steps; decide whether that is fine or the rule wants a floor (e.g. skip the set
      when it rounds to ≤ working weight).
- [ ] Add a `training-science` row to `~/.claude/references/projects.md`.
- [ ] Next module from the brainstorm table, if wanted: isometrics (#3) or fitness
      benchmarks (#4); the benchmark one would also absorb the power and balance benchmarks.

## Session notes

### 2026-10-25
- Cloned to `~/projects/training-science` on sethlap; branch `rules/gap-closing`.
- Overview and gap list produced; nutrition skipped by Seth.
- Gap 1 done: `splits.md` plus pointers in operating-protocol, conditioning-hiit, the
  state template and README.
- Gap 2 done: read map at the top of `sbs-progression-rules.md`; bone-loading and McGill
  now load on condition (module active / pull-up in state), not every session. Typical
  pull-day read in a Hypertrophy block, lines: before ≈ 1,580 (engine 1,100 + bone 328 +
  McGill 153); after ≈ 620 (engine floor 400 + ≈ 220 of the progression rules), plus 153
  only with a pull-up in state and 328 only with the bone module active.
- Gap 3 done: `examples/sample-user/` (fictional "Sam Example", full-body split,
  Hypertrophy Wk 2, shoulder flag, pull-up ladder) and `examples/golden-session.md` with
  13 assertions. Two small rule holes it exposed were fixed in passing: the duration
  formula had no default tempo (now 3 s/rep, output-format.md) and the state template had
  no "last Weekly Snapshot" line.
- Gap 4 done: `readiness.md` (flags by exception from the opener, same-day only, −5% /
  no rep-outs for sleep or fatigue, longer ramp for soreness, neck check for illness),
  a 4th reactive-deload trigger in §8, a rolling flag line in the state template, a §2
  gate, and a golden-session gate row.
- Gap 5 done: `aerobic-base.md` (Floor 90 / Build 150 / Hold 60 min per week, sessions
  count from 20 min, MAF ceiling, loose placement, three-line prescription, AEROBIC
  checklist line, state section, Snapshot line, `aerobic` reminder kind); HIIT §2 and §6
  now hand easy work to that ledger.
- Gap 6 done: `return-to-training.md` (states OPEN → TEST → RAMP → CLOSED and
  EXCLUDED → RE-ENTRY, the test session spelled out, one increment per session back,
  frozen counters, substitution and re-entry at 0.80, neighbouring-lift holds, state
  block format). Golden session bench PRP re-traced to match.
- Gap 7 done: `warmup-and-mobility.md` (2-min raise + one-round joint prep by day type,
  fixed 180 s in the estimate, never cut; no static stretching over 30 s before lifting;
  flexibility only as a declared goal at 60 s × 2–3/week; range limits handled by variant
  regression and re-test). Output format gains a GENERAL section; golden session
  re-traced: full sheet 66.4 min, Hammer Curl cut, 59.7 min.
- Gap 8 done: `CHANGELOG.md`; tags `v1.0` (a703c40, pre-gap) and `v1.1` (this branch's
  head); README shows how to pin a tag.
- Observed, not changed: the Hypertrophy maintenance set (82.5% e1RM) rounds to the
  working weight whenever a lift sits at the top of its rep window with 5-lb steps
  (e1RM = 1.4 × w, 82.5% of that = 1.155 w). It still runs; worth a look later.

### 2026-10-26
- Brainstorm of further exercise types (table above); Seth picked power first, balance next.
- `power-and-plyometrics.md` (optional): primer between prehab and the ramp (fixed 180 s,
  cut after Bone Doubles and before accessories), intent cue in Strength blocks, jump ladder
  (6 rungs, 12" drop jump the top) and throw ladder (5 rungs, or the bone upper ladder
  without a ball), standalone bouts 48 h apart on the cardio cap, weekly tally, broad-jump
  benchmark, `power` reminder kind. Any readiness flag drops the day's power work. Shares
  one jump bout and one knee gate with the bone module.
- `balance.md` (optional): static ladder S1–S8 and dynamic ladder D1–D8, the static rung
  appended to the leg-day general warm-up (+60 s, never cut), 7-min standalone sessions,
  minutes target Floor 30 / Build 90 / Fall-prevention 180 counting bouts from 2 min and
  classes, one-leg-stance + four-stage + TUG benchmark, Snapshot check for one unilateral
  lower-body lift a week, `balance` reminder kind, re-offer triggers (bone module, 60, a
  fall, a closed lower-limb protocol).
- Golden session re-traced: both modules "Not started" for Sam, so no number changes;
  the not-read table, the gate table and assertions 1, 6 and 7 now name them.
- `CHANGELOG.md` v1.2; tag `v1.2` on main.
