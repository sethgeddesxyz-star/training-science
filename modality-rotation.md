# Modality Rotation — rotating the *kind* of training, not just the exercise (added 2026-10-18, user request)

The Accessory Rotation rule (`sbs-progression-rules.md` §6) decides *which exercise* rotates
and *when*. This file adds one layer above it: the program should also rotate the **kind** of
training it uses, actively, so that over a few blocks a user has trained with dumbbells,
cables, bodyweight, kettlebells, straps and bands rather than settling into one implement for
a year. The reason is the same as §6's (regional coverage, freshness, adherence), and the
dose is still conservative: variety at block boundaries, never random variety session to
session.

Read this file during every deload week (that is when boundaries are decided) and whenever
the Weekly Snapshot runs.

---

## 1. Modality families

Every non-main exercise in the user's state carries one tag:

| Tag | Family | Catalogue |
|---|---|---|
| `DB` | Dumbbells | `exercise-library.md` |
| `BB` | Barbell (incl. EZ, trap bar) | `exercise-library.md` |
| `MC` | Machine / cable | `exercise-library.md` |
| `BW` | Bodyweight ladder | `bodyweight-ladders.md` |
| `KB` | Kettlebell | `kettlebell.md` |
| `TRX` | Suspension trainer / rings | `suspension-trainer.md` |
| `BAND` | Resistance band | `exercise-library.md` |

Conditioning modalities (bike / rower / stairs / incline) already rotate inside
`conditioning-hiit.md` §4 and quick-session families inside `quick-sessions.md` §4; this
file does not touch them. Main lifts rotate through their own Variation Pools (§6).

---

## 2. Rules

1. **Coverage floor per block.** Across any block, each lifting day type's accessory list
   uses **at least 2 families**, and the whole program uses **at least 3**. A day type that
   fails the floor gets its next rotation replacement (whatever is due under §6) from a
   family missing on that day; a program that fails it gets one replacement from a family
   unused anywhere.
2. **Family is a replacement criterion.** In §6 "Choosing the replacement", read criterion 1
   as: change position bias, **or family**, or unilateral/bilateral, or angle. A family
   change that also changes the resistance profile (cable → KB, DB → TRX) is the preferred
   swap when the exercise has sat in one family for **2 or more blocks**.
3. **One proposed variety swap per boundary, even when nothing is due.** At each deload the
   coaching view lists, per day type, one accessory proposed to move to a family not used on
   that day in the last 2 blocks. It carries §6's "due = rotate by default" semantics: it
   rotates unless the user keeps it, the keep is recorded, and a kept swap is proposed again
   at the next boundary at most once more. The §6 turnover cap (one third to one half of a
   day type's accessories per boundary) still binds; the variety swap counts toward it and
   is the lowest priority when due and stalled exercises fill the cap.
4. **Variety session in the deload week (optional).** One lifting session of the deload week
   may be run as a **kettlebell or suspension-trainer full-body session** at deload
   parameters (`kettlebell.md` §6, `suspension-trainer.md` §5; RIR ≥ 4 or ladder deload).
   It counts for deload rotation coverage of the day type it replaces **only if** it includes
   that day type's patterns (push: h_push + v_push + triceps; pull: h_pull + v_pull + biceps;
   legs: squat + hinge; full body: all of them). Otherwise it is a bonus session and the day
   type is still owed its deload. HIIT is unaffected.
5. **Modality-forward block (optional, user-declared).** A user may declare the next block
   "KB-forward" or "TRX-forward": every accessory slot defaults to that family for the block
   where an equivalent exists, main lifts and prehab unchanged. At most one such block in
   three. The block's accessories each start as a calibration (§2 Unknown exercise gate)
   and the previous accessories are *parked*, returning afterwards under §6 rule 5
   (fresh calibration at 0.90 × last load). Volume targets (§11) apply unchanged.
6. **Not when.** No family change on an exercise under a Pain Response Protocol, no family
   change that violates `injury-protocols.md`, and no change that the day type's location
   cannot equip. A ladder still climbing stays in `BW`.
7. **Never mid-block, never random.** The whole point of the evidence below is that
   *planned* variation helps and *random* variation costs. All changes here take effect in
   Week 1 of a block.

---

## 3. Tracking

`users/<name>/training-state.md` keeps a short section:

```
## Variety
- Families in use (last 2 blocks): Push DB, MC, BW · Pull DB, MC · Legs BB, MC, KB
- Floor check: Pull uses 2 families (ok) · program uses 5 (ok)
- Last variety swap: 2026-10-21 — Pull: Cable Curl (MC) → TRX Curl (TRX), kept: no
- Modality-forward block: none (last: —)
```

The **Weekly Snapshot** (`operating-protocol.md` §5) adds one line: families per day type
and any floor failure. The **deload coaching view** adds the proposed variety swaps next to
the §6 due list.

---

## 4. Why (evidence, brief)

- The hypertrophy and strength case for *planned* variation, and the cost of *random*
  variation, is already laid out in `sbs-progression-rules.md` §6 (Fonseca 2014; Kassiano
  2022; Baz-Valle 2019). Different implements load a muscle at different lengths and with
  different resistance curves, which is the mechanism behind regional growth differences
  (Maeo 2023, cited there).
- **Variety raises adherence.** Inactive adults randomised to a high-variety exercise
  programme adhered better over 6 weeks than those on a low-variety one, with perceived
  variety mediating the effect (Sylvester 2016, RCT, n = 121). Cross-sectionally, adults with
  access to more varied activity options were more active (Juvancic-Heltzel 2013), and
  varying the mode of cardio improved adherence versus a fixed mode (Glaros & Janelle 2001).
  Adherence is the largest driver of long-term results, so this counts as a training
  variable.
- **Instability and bodyweight families are not inferior for general strength in the
  untrained**, but they do cap maximal loading (Behm 2010 position stand on instability
  training), which is why main lifts stay in their pools and this rule governs accessories.
- The dose here is deliberately small: one proposed swap per boundary, a floor of two
  families, an optional forward block. Enough to keep the program from calcifying, not
  enough to erase progression records.

**References**
1. Sylvester BD, Standage M, McEwan D, Wolf SA, Lubans DR, Eather N, Kaulius M, Ruissen GR, Crocker PRE, Zumbo BD, Beauchamp MR. 2016. Variety support and exercise adherence behavior: experimental and mediating effects. *J Behav Med* 39(2):214–224. doi:10.1007/s10865-015-9688-4
2. Juvancic-Heltzel JA, Glickman EL, Barkley JE. 2013. The effect of variety on physical activity: a cross-sectional study. *J Strength Cond Res* 27(1):244–251. doi:10.1519/JSC.0b013e3182518010
3. Glaros NM, Janelle CM. 2001. Varying the mode of cardiovascular exercise to increase adherence. *J Sport Behav* 24(1):42–62.
4. Behm DG, Drinkwater EJ, Willardson JM, Cowley PM. 2010. The use of instability to train the core musculature (Canadian Society for Exercise Physiology position stand). *Appl Physiol Nutr Metab* 35(1):91–108. doi:10.1139/H09-127
5. Fonseca 2014, Kassiano 2022, Baz-Valle 2019, Maeo 2023: see `sbs-progression-rules.md` §6.
