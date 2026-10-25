# Return to Training — what happens after a pain flag (added 2026-10-25, user request)

The Pain Response Protocol in each user's `injury-protocols.md` says what to do in the
session where pain shows up (stop, substitute, note it) and gives one line for the session
after ("test with lighter weight and controlled tempo"). Nine files say "while a Pain
Response Protocol is open" or "until cleared", and none said what open, cleared, or the
way back looked like. This file defines the protocol's states, the test session exactly,
the ramp back to the pre-flag load, exclusion and re-entry, and what the neighbouring lifts
do meanwhile. It changes nothing about the trigger: any mention of pain still opens the
protocol, and the user's `injury-protocols.md` still wins where it is more conservative.

Read it whenever `training-state.md` carries a protocol in any state but CLOSED, and in
the session that opens one.

---

## 1. States

```
OPEN ──► TEST ──► RAMP ──► CLOSED
          │
          └──► EXCLUDED ──► RE-ENTRY (= TEST again) ──► RAMP ──► CLOSED
```

| State | Meaning | Counts as "open" for every other file's gate? |
|---|---|---|
| `OPEN` | Pain reported this session on this exercise (protocol steps 1–3 done) | yes |
| `TEST` | The next session of that exercise is the §2 test | yes |
| `RAMP` | Test passed; climbing back to the pre-flag load (§3) | yes |
| `CLOSED` | Back at the pre-flag load, pain-free; normal rules resume | no |
| `EXCLUDED` | Pain on the test too (protocol step 5): exercise out, substitute in (§4) | yes, on the joint |
| `RE-ENTRY` | The excluded exercise coming back (§4): a test session, then ramp | yes |

"Open" in `mcgill-pullups.md` §5, `kettlebell.md`, `suspension-trainer.md`, `bone-loading.md`,
`modality-rotation.md` §2 rule 6, `quick-sessions.md` and the Variation Pools means any state
but `CLOSED`. A protocol is per exercise; a joint has an open protocol if any exercise on
that joint does.

---

## 2. The test session (`TEST` and `RE-ENTRY`)

The next session on which the exercise is due, whatever day type that is:

| Parameter | Test value |
|---|---|
| Load | one increment below the pre-flag working load, or two if one increment is under 10%; for a `RE-ENTRY`, 0.80 × the pre-flag load rounded down (the §9 missed-time value for 32–60 days) |
| Sets | as the block prescribes |
| Reps | window floor as the target; RIR ≥ 3 |
| Tempo | 3-s eccentric, 1-s pause at the hardest point, no bounce |
| Maintenance set, Bone Doubles, rep-out, AMRAP | none on this exercise |
| Warmup ramp | as normal, plus one set at 40% × 8 |
| Ladders (`BW`, `TRX`, `KB` steps) | one step down (the ladder's own pain rule), start target, 3-s eccentric |

**Pass** = the user reports nothing on that exercise, and nothing the next day. Silence is a
pass, as with effort. **Fail** = any sensation reported on it, during or after. A fail on a
`TEST` is pain on two consecutive sessions: protocol step 5, the exercise goes to `EXCLUDED`
(§4). A fail on a `RE-ENTRY` returns it to `EXCLUDED` for at least one more block.

A test session is logged like any session. Its sets do not update e1RM, do not move
`failCount` or `stallCounter`, and do not count as a ladder stall.

---

## 3. The ramp (`RAMP`)

After a pass, one increment per session back toward the pre-flag load, with these held
until the pre-flag load is reached:

- rep target stays at the window floor, RIR ≥ 2, normal tempo from the second ramp session;
- no maintenance set, Bone Doubles, rep-out or AMRAP on the exercise;
- `failCount` and `stallCounter` frozen; e1RM thread continues from qualifying sets but a
  lower session e1RM during the ramp never overwrites the stored value;
- any sensation reported during the ramp → back to `TEST` at the load where it was clean;
  a second sensation in the same ramp → `EXCLUDED`.

At the pre-flag load with a clean session: `CLOSED`. The exercise resumes exactly where the
protocol found it: the pending §3 decision (whatever the decision tree said before the flag)
applies at the next session, the maintenance set returns, and the Strength-wave position is
the block's current week. For a ladder, `CLOSED` is a clean session at the pre-flag step.

A ramp across a block boundary continues; the boundary's rotation rules skip the exercise
(it is "open", and `sbs-progression-rules.md` §6 already says so).

---

## 4. Exclusion, substitution and re-entry (`EXCLUDED`)

1. **Substitute at once.** Same pattern, pain-free, chosen by the replacement criteria in
   `sbs-progression-rules.md` §6 Accessory Rotation (or the Variation Pool for a main-lift
   slot: the pool member the user can do without the sensation, at the same tier where
   possible, otherwise the DB member). The substitute starts as a calibration (Unknown
   exercise gate) and inherits nothing from the excluded lift.
2. **Hold the exclusion for at least one full block**, pain-free on the substitute and in
   daily life. Not before, and not by the engine's initiative: the user asks, or says yes
   when the deload coaching view asks once at the first boundary where re-entry is allowed.
3. **Re-entry is a `TEST`** at 0.80 × the pre-flag load (§2), then the ramp (§3).
4. **Three protocols on the same joint inside two blocks**, or any `EXCLUDED` that fails
   re-entry, is the "persistent pain" case in the user's protocol: say so in one line, write
   it to the flag in `injury-protocols.md` as a standing note, and leave the exercise out
   until the user reports a clinician's clearance. The engine never diagnoses.

---

## 5. Neighbouring lifts

In the session that opens a protocol and in the test session, every other lift whose
primary pattern loads the same joint (shoulder: h_push, v_push; elbow: pushes and arm
isolation; back: hinge, squat, carries, rows; knee: squat, hinge, lunges; ankle: impact,
calves, lunges) **holds its load**: no §3 Step 2 advance, no §13a fast-track, even on a
clean session. Its counters and e1RM update normally. This generalises the "pain override on
clean" rule written for the Hypertrophy → Strength transition
(`sbs-progression-rules.md` §6); that rule is unchanged where it is stricter. Prehab is never
held or cut: it is the one thing that runs in full.

HIIT and quick sessions follow their own 48-h rules (`conditioning-hiit.md` §6,
`quick-sessions.md` §2) and are not otherwise affected.

---

## 6. Tracking

`training-state.md`, one block per protocol, under the exercise:

```
PRP: shoulder (right) · opened 2026-10-25 on maintenance set 45 × 4 · state TEST
     pre-flag: 40 × 3 × 6–10, pending Step 4 (aim +1) · test: 35 × 3 × 6, 3-s ecc, RIR ≥ 3
     log: 10-25 opened · —
```

Each session on the exercise appends one dated entry to the `log:` line (`test pass`,
`ramp 35→40`, `closed`, `fail → EXCLUDED`, `re-entry test pass`). When `CLOSED`, the block
stays for the rest of the block, then is reduced to one line in the exercise's history
(`PRP shoulder 10-25 → closed 11-08`). The Weekly Snapshot lists every protocol not
`CLOSED` with its state and the next step.

---

## 7. What this file never does

- Never opens a protocol on its own: the user's words do that.
- Never pushes through pain to finish a ramp. A sensation always steps back.
- Never reads a sensation as a readiness flag (`readiness.md` §1), or the reverse.
- Never diagnoses, and never substitutes for the clinician line in the user's protocol.

---

## 8. Why (evidence, brief)

- **A graded return beats a cliff edge.** Return-to-sport consensus (Ardern 2016) frames
  return as a continuum of staged exposure, with each stage earned by tolerating the last,
  rather than a single "cleared / not cleared" decision; the states in §1 are that continuum
  for one exercise. Load management research says the same from the other side: abrupt
  spikes in load relative to what the tissue has recently tolerated are where injury risk
  concentrates (Gabbett 2016), which is why §2 steps down first and §3 climbs one increment
  per session instead of restoring the old load in one go.
- **Tendon and joint tissues tolerate, and often need, loading during recovery**, provided
  the dose is controlled. Tendinopathy management is built on progressive loading rather
  than rest (Cook & Purdam 2009), and in Achilles tendinopathy a pain-monitoring model that
  kept patients training within a tolerated pain level recovered as well as rest-based care
  (Silbernagel 2007). A review of chronic musculoskeletal pain found exercise into tolerable
  pain slightly better than pain-free exercise in the short term, with no harm (Smith 2017).
  The engine is not a clinician, so it stays stricter than those protocols: a sensation is
  a fail, not a number to manage. The evidence is what justifies testing and ramping at
  all, instead of excluding at the first pinch.
- **Why the slow eccentric and the window floor in the test.** Slow eccentrics let the user
  feel the hardest point of the range at a controlled force, which is where a sensation
  shows if it is going to (Cook & Purdam 2009, on the loading continuum); the window floor
  keeps the set short of fatigue, where form drifts.
- **Why hold the neighbours.** Lifts on the same joint share the irritated tissue. Holding
  their load for one or two sessions costs at most one missed advance; advancing them on
  the day a protocol opens is the one way the engine could make a flag worse. This is the
  existing Strength-transition rule applied generally.

**References**
1. Ardern CL, Glasgow P, Schneiders A, et al. 2016. 2016 Consensus statement on return to
   sport from the First World Congress in Sports Physical Therapy, Bern. *Br J Sports Med*
   50(14):853–864. doi:10.1136/bjsports-2016-096278
2. Gabbett TJ. 2016. The training-injury prevention paradox: should athletes be training
   smarter and harder? *Br J Sports Med* 50(5):273–280. doi:10.1136/bjsports-2015-095788
3. Cook JL, Purdam CR. 2009. Is tendon pathology a continuum? A pathology model to explain
   the clinical presentation of load-induced tendinopathy. *Br J Sports Med* 43(6):409–416.
   doi:10.1136/bjsm.2008.051193
4. Silbernagel KG, Thomeé R, Eriksson BI, Karlsson J. 2007. Continued sports activity, using
   a pain-monitoring model, during rehabilitation in patients with Achilles tendinopathy: a
   randomized controlled study. *Am J Sports Med* 35(6):897–906.
   doi:10.1177/0363546506298279
5. Smith BE, Hendrick P, Smith TO, et al. 2017. Should exercises be painful in the
   management of chronic musculoskeletal pain? A systematic review and meta-analysis.
   *Br J Sports Med* 51(23):1679–1687. doi:10.1136/bjsports-2016-097383
