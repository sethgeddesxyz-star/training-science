# SBS Progression Rules — Complete Reference

This document contains every progression rule the trainer uses. Apply these deterministically — no improvisation.

## Read map (added 2026-10-25)

This file is 700+ lines and most of it is conditional. Reading all of it every session is
where clauses get dropped. Read by situation:

| Read | Sections |
|---|---|
| **Every session** | §1 effort → RIR · §2 e1RM · §3 double progression · §8 reactive deload triggers · §10 warmup ramp · §11 volume · §12 rest · §13a undershoot · §13 overshoot · and, from §6, **only the subsection for the current block type** (Hypertrophy, Strength, Endurance or Deload Week) |
| **Strength block, any week** | §4 AMRAP training-max adjustment · §4a APRE rep-out |
| **First loading session of a new block** | the §6 transition that applies (Hypertrophy → Strength, Strength → Hypertrophy) · post-deload baselines |
| **Deload week and Weekly Snapshot** | §6 Deload Week (completion rules) · §6 Accessory Rotation · §6 Main Lift Variation Pools · §7 plateau detection |
| **A lift has held its load 3+ sessions, or the user says "stuck"** | §7 plateau detection |
| **A lift is at, or being tested for, an equipment ceiling** | §5 ceiling ladder |
| **`lastSessionDate` more than 9 days ago** | §9 missed-time decay |

A section not on today's list is not applied today. A situation not in this table means
the full file.

---

## 1. Effort → RIR Mapping

When the user reports effort, convert to Reps In Reserve (RIR):

| Effort | RIR | Meaning |
|--------|-----|---------|
| easy | 4 | Could do 4+ more reps |
| good | 2.5 | Could do 2-3 more reps |
| **good-hard (DEFAULT)** | **2** | **Between good and hard — the assumed value** |
| hard | 1 | Could do 0-1 more reps |
| failed | 0 | Missed target reps |

### Default Effort Rule (added 2026-08-12)

The user reports effort **by exception only.** Do NOT ask for a per-exercise rating.

- **Silence = "good-hard" (RIR 2), all prescribed reps completed cleanly.**
- The user flags "easy" or "too light" when a load needs to go up faster.
- The user flags a failure or a missed rep count when one occurs.
- The user flags pain, which triggers the Pain Response Protocol in `injury-protocols.md`.

If the user says only "did it" or "hit everything," treat every prescribed set as
completed at the prescribed reps with RIR 2 and run the decision tree. Only ask for
clarification when the report is internally contradictory or a rep count is genuinely
unknown — never as a routine follow-up.

---

## 2. e1RM Formula (RIR-Adjusted Epley)

```
e1RM = weight × (1 + (reps + RIR) / 30)
```

**Only calculate e1RM from qualifying sets:**
- Kind = "working" or "amrap" (never warmup or deload)
- reps > 0, weight > 0
- reps + RIR ≤ 12 (Epley invalid above this)
- RIR ≤ 4
- NOT during endurance blocks (Epley breaks at 12-20 reps)

**Session e1RM** = highest e1RM across all qualifying sets in the session.

---

## 3. Double Progression (Primary Method)

This is the core progression model for all exercises with external load.

### Rep Windows

| Exercise Type | Low | High |
|---------------|-----|------|
| Compound | 6 | 10 |
| Accessory/Isolation | 8 | 12 |

### Decision Tree (apply in this exact order)

**Step 1 — Check for Failure:**
If ANY set is below the low end of the rep window, OR effort = "failed":
- Increment `failCount`
- If `failCount ≥ 2` (consecutive sessions):
  - **Stage Fallback**: Drop rep window by 2 on both ends (e.g., 6-10 → 4-8), add 1 set (cap at 5). Reset failCount.
  - If stage options exhausted (window low would go below 4): **Reset** weight to 90% of current, restore default window and 3 sets, reset all counters.
- If `failCount < 2`: Repeat same weight next session.

**Forced-increment exception (added 2026-09-03, approved).** If the only available next
load is a jump of ≥25% and the FIRST session at that load lands below the rep-window
floor, do NOT increment `failCount`. Hold the load and rebuild reps from wherever they
landed up into the window, then resume normal double progression. This applies only to
the first session at the new load; a second consecutive session below the floor is a
genuine failure and Step 1 applies as written. The rationale is that the lifter did not
fail a progression the engine set — the equipment had no smaller step, and a stage
fallback is the wrong response to a coarse rack.

**Step 2 — Check for Advancement:**
If ALL sets hit the HIGH end of the rep window AND effort is NOT "easy" (quality gate):
- Find the next available weight increment
- If no heavier weight exists → enter **Ceiling Mode** (see §5)
- Otherwise: increase weight to next increment, reset reps to LOW end of window
- Set `successCount += 1`, `failCount = 0`

**Step 3 — Effort Quality Gate:**
If ALL sets hit high end BUT effort = "easy":
- Hold same weight (the "easy" rating suggests the RIR estimate may be off)
- Tell user: "All reps hit but effort was easy — holding weight until a 'good' effort session confirms readiness"
- Reset failCount

**Step 4 — Inside Window (Normal Progress):**
If reps are within the window but haven't hit the top on all sets:
- Same weight next session, aim for ≥1 more total rep
- Reset failCount

### Post-Progression Bookkeeping

After applying the decision tree:

**Stall Tracking:**
- If weight increased: reset `stallCounter` and `exerciseStalled` flag
- If effort was "hard" or "failed" AND weight did NOT increase: increment `stallCounter`
- If `stallCounter ≥ 3`: set `exerciseStalled = true`

**e1RM Update:**
- Calculate session e1RM from all qualifying sets
- Update the stored e1RM if the new value is the session best

---

## 4. AMRAP Training Max Adjustment

Applies to **main compound lifts only** (bench, squat, deadlift, OHP, row).

The adjustment is scored on a main lift's rep-out set: the Strength-block rep-out (§4a) every
loading week, including the Week 4 AMRAP. Hypertrophy, Endurance and Deload blocks have no
rep-out and no TM adjustment.

Calculate: `delta = actual_amrap_reps - target_reps`

| Delta | TM Multiplier | Action |
|-------|---------------|--------|
| ≥ +5 | × 1.03 | Increase TM by 3% |
| +4 | × 1.02 | Increase TM by 2% |
| +3 | × 1.015 | Increase TM by 1.5% |
| +2 | × 1.01 | Increase TM by 1% |
| +1 | × 1.005 | Increase TM by 0.5% |
| 0 | × 1.0 | No change |
| -1 | × 0.98 | Decrease TM by 2% |
| ≤ -2 | × 0.95 | Decrease TM by 5% |

Always round the new TM to the nearest available weight.

---

## 4a. APRE Rep-Out (Strength blocks, added 2026-10-25, approved)

Autoregulatory Progressive Resistance Exercise (Knight's DAPRE; Mann et al., *J Strength Cond
Res* 2010, 24(7):1718-23: APRE beat linear periodization on bench and squat 1RM over 6 weeks in
college athletes). One capped all-out set per lift per session sets the next session's load,
so the wave tracks what the lifter can do now, not the e1RM from weeks ago. This replaces the
once-per-block Week 4 feedback with a feedback step every loading week. It runs
**session-to-session only**: the rep-out never changes a load within the same session.

**Scope.** Strength blocks, loading Weeks 1-4, **main lifts on the wave only** (both branches of
the §6 transition table). Not accessories or secondary compounds (they stay on §3), not the
pull-up's McGill clusters, not Bone Doubles, not deload weeks, not Hypertrophy or Endurance
blocks. A block already in progress adopts it from its next loading week; earlier weeks are
not rescored.

**The set.** The **last prescribed working set** of the lift becomes the rep-out, at the same
load and rest as the other sets:

| Week | Prescription | Rep-out set | Target |
|------|--------------|-------------|--------|
| 1 | 4 × 5 @ 77.5% | Set 4: 5+ | 5 |
| 2 | 4 × 4 @ 82.5% | Set 4: 4+ | 4 |
| 3 | 5 × 3 @ 85% | Set 5: 3+ | 3 |
| 4 | 3 × 2 @ 87.5% + AMRAP @ 85% | the AMRAP set: 3+ | 3 |

**The cap is RIR 1, never failure.** Stop when one more clean rep is all that is left, or at the
first form break, whichever comes first. **Per-lift override:** the user's `training-state.md`
may set a lift's cap to RIR 2 (e.g. a recently closed back event on a hinge); the cap is
never lower than RIR 1. Every injury stop rule in the user's
`injury-protocols.md` still ends the set at once. A set ended by a stop rule, or with any pain
or joint-sensation report, is **not scored**: the lift holds its load next week and the Pain
Response Protocol applies as usual.

**Scoring.** `delta = rep-out reps + (cap − 1) − target`, i.e. reps as logged at a RIR-1 cap,
+1 at a RIR-2 cap, so both caps score on the same scale (the RIR-1 cap leaves the §4 table one
rep conservative, on purpose). Then, for the next loading week:

- **Branch 1 (lift has an e1RM):** `scaled = stored e1RM × §4 multiplier`. The rep-out is also a
  qualifying set at its cap (§2): `epley = load × (1 + (reps + cap) / 30)`, valid while
  reps + cap ≤ 12. **New e1RM = max(scaled, epley) when delta ≥ 0; = scaled when delta < 0.**
  Next week's load = next week's % × new e1RM, rounded to the equipment increment.
- **Branch 2 (no e1RM):** the step replaces the table's "+1 increment if clean":

  | Delta | Next week's load |
  |-------|-----------------|
  | ≤ −2 | −1 increment |
  | −1 | hold |
  | 0 to +2 | +1 increment |
  | ≥ +3 | +2 increments |

  Log the rep-out's Epley value so the lift can move to branch 1 at the next block boundary
  (§6 transition rule 4).

**Interactions.**
- A rep-out below target is scored by the table, not by §3: it does not increment `failCount`.
  A straight (non-rep-out) set below its prescribed reps still follows §3 Step 1.
- §13a needs no "easy" flag here: the rep count is the effort report. An "easy" note on a
  straight set still triggers §13a for that week's straight sets.
- After a Week 4 rep-out, the new e1RM is the value the next block (Hypertrophy maintenance
  set, §6 Strength → Hypertrophy transition) reads.
- The rep-out counts as one set at its load for `bone-loading.md` axial exposure, like any
  other working set.

**Reporting.** The checklist shows the target with a `+` and the cap
(`Bench — Set 4 (rep-out, RIR 1) — 115 lb — 4+`). The user writes the reps actually done. An
**unchanged** line means exactly the target (delta 0), per the effort-by-exception rule. Ask
only if the number is ambiguous.

---

## 5. Equipment Ceiling Ladder

When the user hits the heaviest available weight and can't increase load, progression shifts to other variables. Apply these **rungs in order** — only advance to the next rung when the current one is exhausted.

### Ceiling Test (run BEFORE entering ceiling mode)

An exercise is at its ceiling only when **no combination of available implements** can
add load — not merely when the heaviest single implement is in use. Before declaring a
ceiling, check:

1. **Paired loading**: two DBs instead of one (2 × 30 lb = 60 lb beats a 53 lb KB)
2. **Mixed implements**: DB + KB together (30 + 35 = 65 lb)
3. **Worn or carried load**: backpack, weight vest, DB held at chest
4. **Unilateral conversion**: same absolute load on one limb doubles relative load

Only when all four are exhausted does the ladder below apply. Misdeclaring a ceiling
sends the user into tempo and density work while real load is still on the floor.

### Rung 1: Extend Rep Window
- Widen the rep window: [8-12] → [8-15] → [10-20] → [isolation: up to 25]
- Advance when all sets hit the new high end at target RIR

### Rung 2: Add Sets
- Increase sets: 3 → 4 → 5 (cap at 5)
- Reset rep window to [8-12] when entering this rung
- **Recovery gate**: if effort = "hard", do NOT add sets yet

### Rung 3: Harder Variation / Unilateral Swap
- Swap to a harder or unilateral variation of the exercise
- Reset window to [6-10], sets to 3
- Restart the ladder from Rung 1 within the new variation
- Example: DB bench → single-arm DB bench (effectively doubles relative load)

### Rung 4: Tempo / ROM Manipulation
- Apply one level at a time (reset window to [8-12] each change):
  - Level 0: Standard tempo
  - Level 1: 3-second eccentric (lowering phase)
  - Level 2: 2-second pause at stretch position
  - Level 3: 1.5 reps (full rep + half rep in lengthened position)
- Never reduce rest periods as a progression tool

### Rung 5: Density (Terminal)
- Add rest-pause or mechanical drop set on final set
- This is maintenance — no further escalation
- Never use pre-exhaust or shortened rest as progression

### Ceiling Regression
On failure, deload, or layoff: step DOWN within the ladder (reduce tempo level, drop a set, narrow window) rather than reducing weight.

---

## 6. Block Periodization

Training is organized into repeating blocks of 4 loading weeks + 1 deload week.

### Block Types by Goal

| Goal | Block Rotation |
|------|---------------|
| Build Muscle (Hypertrophy) | H, H, S, H, H, S... |
| Get Stronger (Strength) | S, S, H, S, S, H... |
| General Fitness (Balanced) | H, S, H, S... (strict alternation) |
| Conditioning | H, S, E, H, S, E... (endurance every 3rd) |

### Hypertrophy Block (4 weeks)

**Rep ranges:** Compounds 6-12, Isolation 8-15 (up to 20)
**Weekly volume:** Start at 11 hard sets/muscle, add 2/week, cap at 20

**RIR Ramp (effort intensifies each week):**
| Week | Target RIR | Meaning |
|------|-----------|---------|
| 1 | 3 | Conservative, technique focus |
| 2 | 2 | Moderate effort |
| 3 | 1-2 | Hard but controlled |
| 4 | 0-1 | Near failure (isolation: 0, compounds: 1 minimum) |

**Main lifts get +1 maintenance strength set:** 4 reps @ 82.5% e1RM (keeps strength during hypertrophy focus).

**Progression:** Double progression (§3) drives load increases.

### Strength Block (4-week wave)

| Week | Sets × Reps | % e1RM | Rest |
|------|------------|--------|------|
| 1 | 4 × 5 | 77.5% | 180s |
| 2 | 4 × 4 | 82.5% | 210s |
| 3 | 5 × 3 | 85% | 240s |
| 4 | 3 × 2 + AMRAP | 87.5% + 85% | 270s |

**Week 4 AMRAP:** After the 3×2 heavy sets, do 1 AMRAP set at 85% e1RM, capped at RIR 1.

**Rep-out every week (§4a).** On main lifts the last working set of each loading week is a
rep-out capped at RIR 1 (the Week 4 AMRAP is that week's rep-out). Its score sets next week's
load through the §4 table.

**Accessories during strength blocks:** 4-8 sets/muscle/week at 6-10 reps (maintenance hypertrophy).

### Endurance Block (optional, 3-4 weeks)

- 12-20 reps @ 40-60% e1RM
- Target RIR: 0-2 (light loads only effective near failure)
- Rest: 30-90 seconds
- e1RM updates: **DISABLED** (Epley breaks at high reps)
- 2-3 sets per exercise

### Deload Week (week 5 of each block)

- Sets: 50% of normal (round up, minimum 1)
- Load: 65% of normal working weight (60-70% band)
- Reps: Same targets as normal
- RIR: ≥ 4 (everything should feel easy)
- No AMRAP sets
- Duration: 5-7 days

**When the deload is COMPLETE (clarified 2026-08-20).** "5-7 days" alone was ambiguous
for anyone training a rotating split, because a full rotation can finish in 3 days.
Both conditions must be met before loading resumes:

1. **Rotation coverage** — every day type in the split has had one deload session. No
   muscle group returns to loading without having been deloaded.
   **HIIT is excluded from coverage** (clarified 2026-09-25): only lifting day types count.
   A HIIT session inside the deload window runs once at half volume, same intensity
   (`system/conditioning-hiit.md` §3), and neither opens nor closes the window.
2. **Calendar floor** — at least 5 days have elapsed, counting the FIRST deload session
   as Day 1. Loading resumes on the first session on Day 6 or later.

Any session that falls inside the window after the rotation is already covered is
**also a deload session** at deload parameters — a second deload push, for example. It
is not an extra deload week and costs almost nothing; the asymmetry runs the same
direction as §8's deload timing (the cost of one extra light session is far lower than
the cost of opening a heavy block under-recovered).

Day 7 is the ceiling, not a target. Rest days count toward the window.

**Deload rep targets (clarified 2026-08-19):** Use the rep target that applied at the
*pre-deload performed* load. Where a pending load advance has reset reps to the window
floor and that advance is not being taken into the deload, use the top of the standard
rep window instead — the rep reset travels with the advance to the next block.

**Deload loads on assistance machines (assisted pull-up, assisted dip):** the scale
inverts — lower offset = harder. Deloading means MORE assist, so the offset goes UP.
Step to the previous, easier offset rung rather than computing 65% of the offset number.

**Post-deload baselines:**
- Strength blocks: resume at 97.5% of pre-deload weights
- Hypertrophy blocks: resume at 100%

### Hypertrophy → Strength Transition (added 2026-08-21)

The Strength wave above is %e1RM-driven, but most accessory and machine lifts carry no
valid stored e1RM — deload sets do not qualify (§2), and hypertrophy-range sets often
exceed the reps + RIR ≤ 12 cutoff. Without this rule the first session of a Strength
block requires improvisation. Apply as follows:

1. **Lifts WITH a valid stored e1RM**: use the §6 Strength wave table as written
   (Wk1 4×5 @ 77.5%, Wk2 4×4 @ 82.5%, Wk3 5×3 @ 85%, Wk4 3×2 @ 87.5% + AMRAP @ 85%).
2. **Lifts WITHOUT a valid stored e1RM**: carry the banked double-progression load
   forward and convert by rep target only —

   | Week | Sets × Reps | Load |
   |------|------------|------|
   | 1 | 4 × 5 | banked load |
   | 2 | 4 × 4 | +1 increment if Wk1 reps were hit clean |
   | 3 | 5 × 3 | +1 increment if Wk2 reps were hit clean |
   | 4 | 3 × 2 | +1 increment if Wk3 reps were hit clean |

   "Clean" = all sets at the prescribed reps, effort not "failed", no form flag. If reps
   are missed, hold the load; the §3 failure branch still applies.

   **Pain override on "clean" (added 2026-08-24).** A pain or joint-sensation report
   anywhere in the session holds the load for the following week on every lift sharing
   that joint's primary pattern, regardless of reps hit. The wave's rep drop supplies the
   intensity increase instead. This is narrower than the Pain Response Protocol, which
   still applies in full to the specific exercise that hurt — this clause governs the
   *neighbouring* lifts that were fine on the day. Example: a shoulder report on incline
   press holds the overhead press load too, even though the overhead press was clean.

   **Week 4 AMRAP on branch 2 (added 2026-09-03, approved).** §6 defines Week 4 as
   3×2 + one AMRAP set, but the branch-2 table above gives no load for the AMRAP —
   branch 2 has no e1RM to take 85% of. Run the AMRAP set at the **Week 3 load**, i.e.
   one increment below the Week 4 3×2 load. This reproduces the 87.5% / 85% relationship
   the %-driven branch uses, without requiring an e1RM. Apply the §4 TM adjustment table
   to the result against a **target of 3 reps** (the Week 3 rep count). Rest before the
   AMRAP set is the Week 4 value (270s).
   **Pull-up exception (added 2026-10-13).** The pull-up does not take this branch-2 table in
   Strength blocks. It runs McGill clusters (max-intent bodyweight singles/doubles) per
   `system/mcgill-pullups.md`, unless a back Pain Response Protocol is open, in which case
   this table applies to the Assisted Pull-up as written.
3. **Accessories and isolation** (§6: 4-8 sets/muscle/week at 6-10 reps): remain on
   double progression (§3) unchanged. Do not put them on the wave.
4. **Recompute e1RM** at the first Week-1 session from any qualifying set, so the lift
   can move to branch 1 at the next block boundary.
5. Rep windows narrow for the block: compounds on the wave use the prescribed rep count,
   not a window. Restore the standard windows at the next Hypertrophy block.

### Strength → Hypertrophy Transition (added 2026-09-21, approved)

The Strength wave ends on a Week 4 intensity peak (3×2 @ 87.5%). That load is not a
hypertrophy working weight, and "Hypertrophy blocks resume at 100%" (post-deload baselines,
above) would otherwise prescribe ~8 reps at a load built for doubles. Apply as follows at the
first loading session of a Hypertrophy block that follows a Strength block:

1. **Lifts WITH a valid stored e1RM** (§2): set the opening load by inverting the §2 formula
   for the Week 1 rep target and Week 1 RIR (3):
   `load = e1RM ÷ (1 + (reps + 3) / 30)`, **rounded DOWN** to the available increment. Open at
   the low-middle of the rep window (7 for compounds, 9 for isolation). If rounding down
   costs more than one rep of RIR, keep the load and lower the rep target to the window
   floor instead. The maintenance set (§6 Hypertrophy) runs at 82.5% of the same e1RM.
2. **Lifts WITHOUT a valid e1RM** (accessories, machines, anything that stayed on double
   progression through the wave): resume at the banked double-progression load, 100%, as
   the post-deload baseline rule already says.
3. **Lifts that rotated implement at this boundary** (§6 Variation Pools): calibration
   session. No e1RM carries over, so there is no maintenance set until the calibration
   session opens one.
4. **Week 1 is the confirmation.** Double progression (§3) takes over from the first session.
   A load that lands clearly off the target (all sets "easy", or below the window floor) is
   corrected by §13a or §3 Step 1 at the next session — the formula is a starting estimate,
   not a guarantee.

**Source cross-reference — Stronger By Science.**
- SBS, "How Many Reps Can People Really Do at Specific 1RM Percentages?" (2024,
  strongerbyscience.com/reps-percentage/): reps at a given %1RM vary substantially between
  individuals, generally exceed the classic loading chart, differ by exercise (fewer on bench
  than leg press at the same %), and vary more at lower percentages. Hence rounding DOWN and
  treating Week 1 as confirmation (points 1 and 4).
- SBS, "Overshooting, Undershooting, Or Just Right? How To Perfect Your Ability To Predict
  Repetitions In Reserve" (2024, strongerbyscience.com/reps-in-reserve/): lifter RIR
  estimates are typically off by about one rep and are more accurate near the end of a set.
  Week 1's RIR 3 target absorbs that error without risking a near-failure set.
- No SBS source was found that prescribes this exact Strength → Hypertrophy load conversion;
  the formula itself is this file's §2 RIR-adjusted Epley, inverted. SBS's own programs set
  loads as %1RM/training max by rep target, which is the same principle.

**Worked example (2026-09-21, Seated DB OHP):** e1RM 46.7 lb/arm, target 7 reps @ RIR 3 →
46.7 ÷ (1 + 10/30) = 35.0 → **35 lb × 7**. Maintenance 82.5% × 46.7 = 38.5 → 40 lb × 4. The
Week 4 peak (40 lb × 2) was not used as a working weight.

### Block Transition Rules

- **Main lifts**: see Main Lift Variation Pools below. No longer a flat "never rotate" —
  rotation is scheduled, gated, and tracked per variation.
- **Secondary compounds and accessories**: rotation is scheduled, not optional. See
  Accessory Rotation below (supersedes the earlier "may rotate" wording, 2026-10-18).

### Accessory Rotation (added 2026-10-18)

Everything that is not a main lift (main lifts use the Variation Pools below) rotates on a
schedule. A user who is free to customize will tend to settle into the same comfortable
accessories indefinitely; this rule makes change the default and keeping the deliberate
choice.

**Why, in short (evidence):**
- Structured exercise variation produces more complete *regional* growth: varying the
  exercise grew all four quadriceps heads, a single exercise did not, at equal total growth
  (Fonseca et al. 2014, JSCR). A systematic review of 8 trials agrees: planned variation
  helps regional hypertrophy and strength (Kassiano et al. 2022, JSCR 36(6):1753-62).
- **Too much** variation costs gains. Swapping exercises at random every session matched
  fixed selection on most measures but lost growth in one quadriceps head (Baz-Valle et al.
  2019, PLoS One e0226989), and the 2022 review warns against frequent or random rotation.
  The first 2-3 exposures to a new movement are mostly skill learning, and progressive
  overload needs repeated exposures to the same movement to measure.
- Variation measurably raises the motivation to train (Baz-Valle 2019). Adherence is the
  biggest driver of long-term results, so this counts.
- Muscles grow differently depending on where in the range they are loaded: e.g. overhead
  triceps extensions grew the triceps more than pushdowns (Maeo et al. 2023, EJSS). Rotating
  *position*, not just novelty, is the point.
- Total growth is not reliably bigger with variation. Rotation is for coverage, freshness
  and adherence, not a magic stimulus. Never rotate so often that loads cannot be tracked.

**Cadence (each exercise carries its own age, counted in completed blocks):**

| Tier | Minimum hold | Due for rotation | Hard ceiling |
|------|--------------|------------------|--------------|
| Accessories and isolation | 1 block | at its 2nd block boundary (~10 weeks) | 3 blocks (~15 weeks) |
| Secondary compounds | 1 block | at its 3rd block boundary (~15 weeks) | 4 blocks (~20 weeks) |

1. **Never mid-block.** Rotation happens only at a block boundary (decided during the
   deload, takes effect in Week 1 of the next block). Exceptions: pain (route to the Pain
   Response Protocol), missing equipment, or a form failure that the exercise's own stage
   fallback cannot fix.
2. **Due = rotate by default.** At the boundary where an exercise is due, the coaching view
   lists it with its proposed replacement. It rotates unless the user keeps it.
3. **Keep, once.** A due exercise may be kept for one more block only if it is still
   progressing (double progression advanced at least once in the block, or §7 status
   PROGRESSING). Record the keep and its reason in the user's state file. A stalled exercise
   cannot be kept: §7 step 5 already wants it swapped.
4. **Hard ceiling.** At the ceiling the exercise rotates out. The user can still override
   (their program, their call), but the override is recorded as "kept past ceiling by user"
   and resurfaced at every boundary until it rotates. The engine never keeps silently.
5. **Rest, then return.** A rotated-out exercise may return after at least one full block
   away. It returns with a fresh calibration (§2 Unknown exercise gate), starting from its
   last logged load × 0.90, rounded down to equipment increments.
6. **Turnover cap per boundary.** Rotate between one third and one half of each day type's
   accessories at any one boundary, oldest and stalled first. If more are due than the cap
   allows, the overflow is due first at the next boundary and cannot be kept again. Never
   swap every accessory at once: it erases the progression record and stacks novel-exercise
   soreness into one week.

**Choosing the replacement (in order):**
1. **Same target muscle, different stimulus.** Change at least one of: position bias
   (lengthened vs shortened, e.g. incline curl vs preacher curl, overhead vs pushdown),
   modality family (DB / barbell / cable-machine / band / bodyweight / kettlebell /
   suspension trainer, per `modality-rotation.md` §1), unilateral vs bilateral, or angle.
   A same-movement, different-implement swap counts only if the resistance profile
   genuinely changes. An exercise that has sat in one family for 2+ blocks prefers a
   family change (`modality-rotation.md` §2 rule 2).
2. **Lengthened coverage.** Across the block, each trained muscle should have at least one
   exercise that loads it hard in the stretched position.
3. **No redundancy.** Not a near-duplicate of another movement on the same day.
4. **Prefer unused.** Prefer a movement absent for the previous 2 blocks.
5. **Equipment and injury.** Must be available at the day type's location
   (`equipment-profiles.md`) and allowed by `injury-protocols.md`. Rotation never
   overrides an exclusion or an open Pain Response Protocol.
6. **First session is a calibration.** Conservative load, labelled in the progression note,
   confirmed before progressing.

**Exempt from rotation:** the fixed prehab block, any exercise held by an injury or pain
protocol, bodyweight ladders still climbing (the `BW` family only: they vary through their own
Rung 3 swap; `TRX` and `KB` ladders rotate on the accessory cadence and keep their step in
state, `suspension-trainer.md` §6, `kettlebell.md` §8), and the conditioning day type (it has
its own format cycle in `conditioning-hiit.md`).

**Beyond "due" (added 2026-10-18):** `modality-rotation.md` adds a coverage floor of two
families per day type, one *proposed* variety swap per boundary even when nothing is due,
an optional deload-week variety session, and user-declared modality-forward blocks. It
layers on this rule and never overrides its cadence, turnover cap or exemptions.

**Tracking:** the user's state file keeps one line per non-main exercise per day type:
name, modality family tag, block it entered, keep used (y/n). Where no entry exists yet, derive the entry block
from the first workout-log session using that exercise in its current form. The Weekly
Snapshot (operating protocol §5) and every deload coaching view list what is due at the
coming boundary.

### Main Lift Variation Pools (added 2026-08-28, supersedes prior "never rotate" rule)

Each main lift belongs to a variation pool — movements training the same pattern,
treated as interchangeable for programming purposes. Rotation happens only at block
boundaries, never mid-block, and only to a pool member available at the day's location.

**Synchronized implement tiers.** All three main-lift slots share a single Implement
Tier (tracked in `training-state.md`, not per-slot) so the program is never on DB bench
while on cable row — when the tier advances, all three slots advance together, one
rotation event, not three independent ones.

| Main Lift Slot    | Tier 1 (DB)             | Tier 2 (Barbell)     | Tier 3 (Machine/Cable) |
|--------------------|--------------------------|------------------------|--------------------------|
| Push (horizontal)  | DB Flat Bench Press      | Barbell Bench Press   | Machine Chest Press     |
| Push (vertical)    | Seated DB Overhead Press | Barbell OHP           | Machine Shoulder Press  |
| Pull (horizontal)  | Chest-Supported DB Row   | Barbell Row           | Cable Row               |

**Cadence: every 2 blocks (~10 weeks)**, advancing Tier 1 → 2 → 3 → 1 at the block
boundary where the shared rotation counter reaches 2 (increment by 1 at each boundary,
reset to 0 on rotation). Home-only sessions substitute that slot's Tier-1 (DB) member
for the session without advancing or breaking the shared tier state — home has no
barbell or machine/cable equipment.

**e1RM tracking across a rotation:**
1. First session on a newly-rotated variation = calibration session (§2 Unknown
   Exercise handling): conservative start, confirm the load before continuing.
2. That calibration opens a new e1RM thread for that variation. Plateau detection (§7)
   restarts at DATA_INSUFFICIENT for that variation until 3 weeks of data exist on it.
3. The slot's deload schedule does NOT reset on rotation — only the variation-specific
   e1RM thread does.
4. Weekly Snapshot (§5) reports e1RM trend per variation, not blended across variations,
   and notes explicitly when a slot is mid-calibration.

**Overrides that still apply regardless of cadence or shared tier:**
- **Shoulder flag exception**: the vertical push slot stays on DB OHP even if the shared
  tier advances to Barbell or Machine (`injury-protocols.md`). This is a deliberate,
  flagged exception to synchronization, not drift — note it explicitly in the coaching
  view whenever the other two slots are on a different tier than OHP.
- An exercise under an active Pain Response Protocol is not eligible for rotation into
  or out of until cleared.
- Rotation never overrides an injury exclusion.

**Leg-day main lift (KB Sumo Deadlift) is not in a pool** — out of scope for this
rotation scheme unless added later.

---

## 7. Plateau Detection

### e1RM Trend Classification

Compare trailing 3-week best e1RM vs prior 3-week best:

| Condition | Status |
|-----------|--------|
| Adherence < 80% (missed >1 in 5 sessions) | DATA_INSUFFICIENT |
| Trailing best ≥ prior best × 1.005 | PROGRESSING |
| Trailing best ≥ prior best × 0.975 | STALLED |
| Trailing best < prior best × 0.975 | REGRESSING |

### Response Ladder (apply ONE step per block, top to bottom)

1. **DATA_INSUFFICIENT** → "Train more consistently. No program change."
2. **PROGRESSING** → "No action needed."
3. **STALLED/REGRESSING but < 4 weeks since deload** → "Schedule deload — fatigue may be masking progress."
4. **Stalled after recent deload** → "Reset to 90% of best working weight. Rebuild via double progression."
5. **Stalled ≥ 2 blocks on same exercise** → "Swap to a close variation OR shift rep window."
6. **Systemic stalls (most lifts stalled, multiple blocks):**
   - If recovery flags (poor sleep, high stress, weight loss) → cut weekly volume by 20%
   - If weekly sets < 15 and recovery is fine → add 2-4 sets/muscle/week
7. **Otherwise** → "Monitor. Next deload on schedule."

---

## 8. Reactive Deload Triggers

These override the scheduled deload and trigger one immediately:

1. **e1RM regressing** — status = REGRESSING on any main lift
2. **Multiple lifts declining** — ≥ 2 main lifts with e1RM down 2+ consecutive weeks
3. **RPE overshoot** — ≥ 2 consecutive sessions where average effort exceeds target by 1.5+ RIR levels (e.g., everything "hard" when target was RIR 3)

**Early-block reactive deload (week ≤ 2):** Also reduce next block's volume by 1-2 sets/muscle/week.

**Deload deferral:** Can extend loading by 1 week (to 5 loading weeks) if ALL signals are green (all lifts progressing, effort on target) AND deload hasn't been deferred already. Hard cap: never exceed 6 loading weeks without a deload.

---

## 9. Missed Time Decay

When the user hasn't trained an exercise for more than 9 days, apply these adjustments BEFORE generating the workout:

### External Load (Full Gym Mode)

| Days Since Last Session | Weight Adjustment | Other |
|------------------------|-------------------|-------|
| 0-9 | No change | — |
| 10-17 | × 0.95 (95%) | — |
| 18-31 | × 0.90 (90%) | Reduce sets by 1 for first week back |
| 32-60 | × 0.80 (80%) | Restart progression counters |
| 61+ | × 0.70 (70%) | Full re-onboard (first week is ramp-up) |

### Equipment Ceiling Mode

| Days Since | Adjustment |
|-----------|-----------|
| 10-17 | Tempo level −1 |
| 18-31 | Tempo level −1, sets −1 for first week |
| 32-60 | Rung −2, restart counters |
| 61+ | Reset to rung 1, tempo 0, restart |

### Bodyweight Ladder Mode

Handled by the ladder system: regress one step if > 14 days since last session (see `bodyweight-ladders.md`).

---

## 10. Warmup Ramp

For the first compound exercise(s) of the session, prescribe automatic warmup sets:

| Set | % of Working Weight | Reps |
|-----|-------------------|------|
| 1 | 40% | 5 |
| 2 | 60% | 5 |
| 3 | 80% | 3 |

Round each warmup weight to the nearest available load. Skip warmup sets that would duplicate a heavier warmup or exceed the working weight. Rest between warmup sets: 45 seconds.

Bodyweight exercises: no warmup ramp (general warmup is sufficient).

---

## 11. Volume Guidelines

| Parameter | Value |
|-----------|-------|
| Starting hard sets/muscle/week | 10-12 |
| Maximum hard sets/muscle/week | 20 |
| Maximum sets/muscle in one session | 10 |
| Minimum muscle frequency | 2×/week |
| Minimum pull sessions/week | 2 |
| Synergist counting | 0.5× (e.g., triceps during bench = 0.5 sets) |
| Primary counting | 1.0× |

---

## 12. Rest Period Guidelines

| Context | Rest (seconds) |
|---------|---------------|
| Hypertrophy compounds | 150 (120-180 range) |
| Isolation exercises | 90 (60-120 range) |
| Strength work | 210 (180-300 range) |
| Heavy strength (≥85% or ≤3 reps) | 270 (240-300 range) |
| Endurance block | 60 (30-90 range) |

---

## 13a. Undershoot Fast-Track

The mirror of §13. If the user reports an exercise as "easy," "too light," or "not near
failure":

- If all sets are **within one rep of the window top**: advance to the next load
  immediately, reps reset to the window low end. Do not spend a session confirming
  the top of the window.
- If sets are **more than one rep below the top**: hold the load, raise the rep target
  to the window top for the next session, and re-evaluate.
- Log the trigger as a user-reported effort flag, not an engine-generated advance.

## 13. Same-Day Overshoot Reduction

If a user's effort in the current session is significantly harder than prescribed (e.g., everything "hard" when target RIR was 3):
- Reduce remaining exercises' prescribed weight by 5% for TODAY ONLY
- Do NOT change the persistent training state
- Note: "Reduced today's remaining loads 5% due to elevated fatigue. Your training state is unchanged."
