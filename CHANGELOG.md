# Changelog

Personal repos pin this repo as a submodule. Each tag below is a version a personal repo can
pin by name (`git -C system checkout v1.1`), and each entry says what changed for the
trainer's behaviour. Dates are the day the rule landed. Inside the rule files, every added
or clarified rule also carries its own `(added YYYY-MM-DD)` note.

## v1.1 — 2026-10-25

Closing the gaps found in the 2026-10-25 overview. Nine commits on `rules/gap-closing`.

- **`splits.md`** (new). Full body (`FB-A` / `FB-B`), upper/lower and push/pull/legs defined
  as day types with rotations; HIIT placement per split (a rotation slot only in PPL;
  once-per-cycle or once-per-week standalone otherwise); the table mapping every
  per-day-type rule (prehab, deload coverage, turnover cap, modality floor, McGill, Bone
  Doubles, carries, reminders, Snapshot) onto each split; wrong-day-type openers.
- **Read map** at the top of `sbs-progression-rules.md`: which sections load every session
  and which by trigger. `bone-loading.md` is read only while the module is active;
  `mcgill-pullups.md` only on a v_pull day with a pull-up in state. Typical per-session
  read drops from about 1,580 lines to about 620.
- **`examples/`** (new). A fictional sample user and `golden-session.md`: one session traced
  rule by rule with 13 assertions. `operating-protocol.md` §6 now requires revisions that
  touch a traced rule to re-trace it in the same commit.
- **`readiness.md`** (new). Same-day adjustments for a sleep, fatigue, soreness or illness
  flag the user volunteers (never asked): loads −5% and no rep-outs; longer ramp for
  soreness; neck check for illness. A 4th reactive-deload trigger (§8) on 3 flags in 4
  sessions. State is never edited by a flag.
- **`aerobic-base.md`** (new). Easy aerobic work as a weekly minutes target (Floor 90 /
  Build 150 / Hold 60), sessions from 20 min under the MAF ceiling, loose placement, a
  three-line prescription and an `AEROBIC` checklist line, its own ledger separate from
  HIIT, a Snapshot line and an `aerobic` reminder kind.
- **`return-to-training.md`** (new). Pain Response Protocol states (OPEN → TEST → RAMP →
  CLOSED; EXCLUDED → RE-ENTRY), the test session spelled out, one increment per session
  back, frozen counters, substitution and re-entry at 0.80, neighbouring-lift holds, the
  state block format. Defines "open" and "cleared" for the nine files that used them.
- **`warmup-and-mobility.md`** (new). The general warm-up (2 min raise + one round of
  joint prep by day type; 180 s in the estimate; never cut), no static stretching over 30 s
  before lifting, flexibility only as a declared goal, range-of-motion limits by variant
  regression and re-test. `output-format.md` gains a `GENERAL` section.
- Small fixes found on the way: the duration formula now has a default tempo (3 s/rep);
  the state template has a "last Weekly Snapshot" line and a readiness flag line;
  `aerobic-heart-rate.md` points at the base file.

## v1.0 — 2026-10-25 (pre-gap baseline)

The repo as it stood before the gap work: SBS progression engine, exercise library,
bodyweight ladders, HIIT, bone loading, McGill pull-ups, kettlebell, suspension trainer,
quick sessions, modality rotation, reminders, templates. Tagged at commit `a703c40` (§4a
APRE rep-out, the last change before the overview).
