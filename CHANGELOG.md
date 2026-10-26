# Changelog

Personal repos pin this repo as a submodule. Each tag below is a version a personal repo can
pin by name (`git -C system checkout v1.1`), and each entry says what changed for the
trainer's behaviour. Dates are the day the rule landed. Inside the rule files, every added
or clarified rule also carries its own `(added YYYY-MM-DD)` note.

## v1.4 — 2026-10-26

- **`isometrics.md`** (new, optional). Held contractions as a tool, in two halves that
  activate separately. The **blood-pressure protocol**: wall squat (knee angle from 135°
  down to 95° in 10° steps) or handgrip (30% of maximal grip, hands alternating), 4 × 2 min,
  three times a week, breathed through, standalone and outside every time budget, with
  optional user-logged readings reported as a 4-week trend and a single 180/120 stop line.
  Offered only when blood pressure comes up. The **tendon holds**: only for a pain the user
  names as tendon pain, a site table (patellar, Achilles, plantar, elbow, hamstring, hip,
  cuff, adductor), 5 × 45 s standalone bouts and a 3 × 45 s primer (fixed 255 s, never
  cut) before the affected lift's ramp while its protocol is `TEST` or `RAMP`, a ≤ 3/10
  during-pain rule and a next-morning rule. Holds never open, advance or close a protocol.
  Weekly tally, nudge line, `isometric` reminder kind.
- Pointers in `operating-protocol.md` (row, §2 gate, Snapshot), `output-format.md` (primer
  section, estimate, ISOMETRIC block), `reporting-protocol.md`, `reminders.md` §2,
  `readiness.md` §2 (`ILL` drops it), `return-to-training.md` §1, `benchmarks.md` (grip row),
  `conditioning-hiit.md` §8 (the safety screen covers the first BP session), the state
  templates, the sample user and the golden session (not read; assertions 1, 6 and 7).

## v1.3 — 2026-10-26

- **`benchmarks.md`** (new, opt-in at intake). One scorecard every 8 weeks, taken in the
  first deload week at or after the due date: a core set needing only a wall, a chair, a
  tape and a timer (one-leg stance, 30-s chair stand, push-up max at the ladder step, grip
  or dead hang, sit and rise, one aerobic test chosen at intake, broad jump when cleared,
  main-lift e1RMs read from state), with the HIIT, kettlebell, power and balance benchmarks
  folded in while their module is active so no module runs its own clock. Fixed test order,
  a separate aerobic day, trend first, a cited norm band printed once, a flag rule that only
  asks. While "Not started", each module's benchmark runs under its own file as before.
- Pointers in `conditioning-hiit.md` §7, `kettlebell.md` §5, `power-and-plyometrics.md` §7,
  `balance.md` §7, `operating-protocol.md` (row, §2 gate, Snapshot), `output-format.md`
  (BENCHMARK block), `reporting-protocol.md`, `reminders.md` (`state:benchmark` row), the
  state templates, the sample user and the golden session (not read; assertion 1).

## v1.2 — 2026-10-26

Two optional modules from the 2026-10-26 brainstorm, one commit each, both "Not started"
until a user opts in and not read before then.

- **`power-and-plyometrics.md`** (new, optional). A 3-set power primer between prehab and
  the warmup ramp (fixed 180 s; cut after Bone Doubles, before any accessory), the
  explosive-intent cue on Strength-block main lifts, a six-rung jump ladder and a
  five-rung throw ladder, standalone 15-min bouts (48 h apart, on the cardio cap), a
  weekly tally with a nudge line, a broad-jump benchmark every 8 weeks, and a `power`
  reminder kind. Any readiness flag drops the day's power work. A jump bout feeds the bone
  tally too when both modules are active, and the two share one knee gate.
- **`balance.md`** (new, optional). An eight-rung static ladder and an eight-rung dynamic
  ladder (heel-to-toe through reactive stepping), the current static rung appended to the
  leg-day general warm-up (fixed +60 s, never cut), standalone 7-min sessions, a weekly
  minutes target (Floor 30 / Build 90 / Fall-prevention 180) counting bouts from 2 min and
  classes such as tai chi, a one-leg-stance and four-stage benchmark every 8 weeks, a
  Snapshot check that the week carries one unilateral lower-body lift, and a `balance`
  reminder kind. Re-offered once when the bone module activates, at 60, on a reported fall,
  or when a lower-limb protocol closes.
- Pointers added in `operating-protocol.md` (rows, §2 gates, Snapshot), `output-format.md`
  (POWER section, balance line, estimate), `splits.md` §4, `warmup-and-mobility.md` §2,
  `reminders.md` §2, `reporting-protocol.md`, `readiness.md` §2, `bone-loading.md` §5, the
  state templates, the sample user and the golden session (both modules not read; assertions
  1, 6 and 7 name them).

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
