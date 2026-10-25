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
| 1 | Splits beyond push/pull/legs: HIIT placement, prehab, McGill, Bone Doubles, carries, modality floor and deload coverage are all written against PUSH → LEGS → PULL → HIIT; full body and upper/lower are named but undefined | Wrong or improvised prescriptions for any user under 5 days/week | in progress |
| 2 | Per-session read is heavy (often 1,500+ lines per workout; bone-loading and McGill read every session) | Clause-dropping risk on every other rule | pending |
| 3 | No worked example / golden session: a filled sample user and one session traced through the decision tree | The only test an LLM-run rulebook can have; catches drift in 1 and 2 | pending |
| 4 | No session-start readiness check (sleep, soreness, stress feed nothing until a deload trigger fires after the fact) | Daily load accuracy | pending |
| 5 | Easy aerobic work has no slot: heart-rate card only, no day type, target or log | Feature gap; the card exists, the program does not | pending |
| 6 | Return-to-training after a pain flag: protocol stops and substitutes, then "test lighter"; no ramp back, no rule for clearing a flag | Safety, but rare | pending |
| 7 | No mobility / joint-prep layer; warmup ramp is a load ramp only | Feature gap | pending |
| 8 | No tags or changelog; personal repos pin a bare hash | Housekeeping | pending |
| — | Nutrition / bodyweight tracking | Skipped by decision 2026-10-25 | skipped |

## Working rules for this repo

- Every new rule file: `# Title — one line (added YYYY-MM-DD, user request)`, numbered
  sections, rules before evidence, references last with DOIs.
- Touch `operating-protocol.md` only to add the file-table row and the read trigger.
- Never a user's name, load, log or injury in any file here.

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
- Observed, not changed: the Hypertrophy maintenance set (82.5% e1RM) rounds to the
  working weight whenever a lift sits at the top of its rep window with 5-lb steps
  (e1RM = 1.4 × w, 82.5% of that = 1.155 w). It still runs; worth a look later.
