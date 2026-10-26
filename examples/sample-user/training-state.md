# Training State

<!-- SAMPLE USER "Sam Example" — fictional. Part of examples/; never a real person.
     This is the state BEFORE the session traced in examples/golden-session.md.
     The AFTER state is shown there as a diff. -->

Current progression state for all tracked exercises. Updated after every workout.

---

## Profile

- **Name**: Sam Example
- **Age**: 40 (HRmax for HIIT: 208 − 0.7 × 40 = 180)
- **Goals** (ranked): 1. general fitness, 2. first strict pull-up, 3. keep the shoulder quiet
- **Locations**: Home (only)
- **Injury flags**: see injury-protocols.md (right shoulder, always-active)
- **Units**: lb
- **Experience**: 1 year, inconsistent before this program

---

## Current Block

- **Block type**: Hypertrophy, **Week 2 of 4** (RIR target 2). Goal rotation: General
  Fitness → H, S, H, S. This is block 1.
- **Deload**: scheduled after Week 4. Deferred: no.
- **Implement tier** (main-lift slots): 1 (DB). Rotation counter: 0.
- **Last Weekly Snapshot**: 2026-10-20
- **Readiness flags (last 4 sessions)**: — · — · — · —

---

## Split & Rotation

- **Current split**: Full body (3 days/week; set at intake 2026-10-06) — `system/splits.md` §1
- **Rotation order**: FB-A → FB-B · HIIT: once per calendar week, standalone on a non-lifting day (`system/splits.md` §3)
- **Next due**: FB-A · HIIT due: yes, since 2026-10-20 (none performed this week)
- **Last session date**: 2026-10-22

### Prehab blocks by day type

(fixed lists, built from injury-protocols.md at intake; identical on FB-A and FB-B per
`system/splits.md` §4)

- **FB-A / FB-B**: 2 rounds — Band Pull-apart 15 · Band External Rotation 12/side

---

## Conditioning — HIIT

Rules: `system/conditioning-hiit.md`. Safety screen (§8): asked 2026-10-06, clear.
Modality: stairs (one flight) or outdoor hill. Format cycle position: A (none performed yet).

---

## Aerobic Base

Rules: `system/aerobic-base.md`. Level: Floor (90 min/week; set 2026-10-25). Ceiling: MAF
140 bpm (180 − 40, no adjustment). Preferred modality: incline walk (outdoor hill).
Rolling 7 days: 0 / 90 min · last: —. Weeks at or over target (consecutive): 0.

---

## Bone Loading Module (OPTIONAL)

Rules: `system/bone-loading.md`. Not started (offered at intake, declined for now).

---

## Power Module (OPTIONAL)

Rules: `system/power-and-plyometrics.md`. Not started (offered at intake, declined for now).

---

## Balance Module (OPTIONAL)

Rules: `system/balance.md`. Not started (offered at intake, declined for now).

---

## Benchmarks

Rules: `system/benchmarks.md`. Not started (offered at intake, declined for now; the HIIT
benchmark runs on its own clock).

---

## Kettlebell

None owned. Not started.

---

## Suspension Trainer

None owned. Not started.

---

## Quick Sessions

Rules: `system/quick-sessions.md` §5. Families enabled: stairs, core. Last served: —.
Vigorous snacks, last 7 days: 0.

---

## Variety

Rules: `system/modality-rotation.md` §3. Families in use (block 1): FB-A DB, BW · FB-B DB,
BAND. Floor check: ok (2 per day type, 3 in program). Last variety swap: —.
Modality-forward block: none.

---

## Reminders

Rules: `system/reminders.md`. None agreed (declined at intake). Next 4-week review: —.

---

## Per-Exercise State

### Main-lift slots (Tier 1, DB)

- **DB Bench Press** (h_push, FB-A and FB-B) — main lift
  - working: 40 lb DBs · window 6–10 · 3 sets · failCount 0 · successCount 1 · stallCounter 0
  - e1RM: 56 (2026-10-20, 40 × 10 @ RIR 2)
  - maintenance set (Hypertrophy): 4 @ 82.5% e1RM
  - history: 2026-10-13 35 × 10/10/10 → advance · 2026-10-20 40 × 10/10/9 · 2026-10-22 40 × 10/9/9
  - next: 40 × 3 × 6–10, aim ≥ 1 more total rep (§3 Step 4)

- **Chest-Supported DB Row** (h_pull, FB-A and FB-B) — main lift
  - working: 35 lb DBs (advanced 2026-10-22) · window 6–10 · 3 sets · failCount 0 · successCount 2 · stallCounter 0
  - e1RM: 42 (2026-10-22, 30 × 10 @ RIR 2)
  - history: 2026-10-13 30 × 9/9/8 · 2026-10-20 30 × 10/10/9 · 2026-10-22 30 × 10/10/10 → advance
  - next: 35 × 3 × 6–10, reps reset to window low (§3 Step 2)

- **Seated DB Overhead Press** (v_push, FB-B) — main lift, shoulder-flag exception (stays DB)
  - working: 25 lb DBs · window 6–10 · 3 sets · failCount 0 · successCount 0 · stallCounter 0
  - e1RM: 35 (2026-10-22, 25 × 10 @ RIR 2)
  - history: 2026-10-15 25 × 9/8/7 · 2026-10-22 25 × 10/9/8
  - next: 25 × 3 × 6–10, aim ≥ 1 more total rep

### Secondary compounds

- **Bulgarian Split Squat** (squat, FB-A) — DB · entered block 1 · keep used: n
  - working: 25 lb DBs · window 6–10/leg · 3 sets · failCount 0 · stallCounter 0
  - history: 2026-10-13 20 × 10/10/10 → advance · 2026-10-20 25 × 8/8/7
  - next: 25 × 3 × 6–10/leg, aim ≥ 1 more total rep

- **DB Romanian Deadlift** (hinge, FB-B) — DB · entered block 1 · keep used: n
  - working: 45 lb DBs · window 6–10 · 3 sets · failCount 0 · stallCounter 0
  - history: 2026-10-15 40 × 10/10/10 → advance · 2026-10-22 45 × 8/8/8
  - next: 45 × 3 × 6–10, aim ≥ 1 more total rep

### Ladders

- **Pull-up ladder** (v_pull, FB-A) — `system/bodyweight-ladders.md` Ladder 2 — BW
  - currentStep: 5 (band-assisted, light band) · stallCounter: 0 · lastSessionDate: 2026-10-20
  - history: 2026-10-13 step 5 × 6/6/5 · 2026-10-20 step 5 × 7/7/6
  - next: 3 × 8 at step 5 (advance standard); on 3 × 8 clean → step 6, start 3 × 5

### Accessories

- **DB Hammer Curl** (arms, FB-A) — DB · entered block 1 · keep used: n
  - working: 20 lb · window 8–12 · 3 sets · failCount 0 · stallCounter 0
  - history: 2026-10-13 20 × 12/11/10 · 2026-10-20 20 × 12/12/11
  - next: 20 × 3 × 8–12, aim ≥ 1 more total rep

- **Band Face Pull** (h_pull accessory, FB-B) — BAND · entered block 1 · keep used: n
  - working: medium band · window 8–12 · 3 sets
  - history: 2026-10-15 medium × 12/12/12 (easy) → held (§3 Step 3) · 2026-10-22 medium × 12/12/12 (good) → heavy band next
  - next: heavy × 3 × 8–12
