# Bone Loading Module — OPTIONAL (added 2026-09-25, user request)

An optional add-on that loads the skeleton the way the research says builds bone mineral
density (BMD). It rides alongside the SBS program; it does not replace or reshape any part of
it. **Optional means:** it is always offered, never required, and skipping it is never a miss
and never costs progression anywhere else. **Encouraged means:** the trainer keeps a weekly
tally and nudges toward a regular rhythm (§5), because bone responds to consistency over
months and loses its gains when loading stops.

Read this file whenever a session is prescribed **while the module is active** (a rung or
tally recorded in the user's state), and once at intake to offer it. While the state says
"Not started", the file is not read and no BONE section prints (clarified 2026-10-25: it was
being read on every session for users who had never opted in). The user's current rungs and tally live in
`users/<name>/training-state.md` under **Bone Loading Module**. Injury gates for impact live in
`users/<name>/injury-protocols.md` and **always win** over this file.

---

## 1. What the science says (short version — references in §9)

- **Bone responds to strain that is high, fast, brief and unusual.** Normal daily loading keeps
  bone where it is (Frost's mechanostat). Only loading above the habitual level adds bone, and
  a stimulus that becomes routine stops working — so it has to progress (Turner 1998; Turner &
  Robling 2003; ACSM, Kohrt 2004).
- **Heavy lifting works, especially at the spine.** LIFTMOR (Watson 2018): deadlift, squat and
  overhead press at 5×5 > 80–85% 1RM, plus jumping chin-ups, 2×/week, 30 min, 8 months →
  lumbar spine +2.9% vs −1.2% in controls, femoral neck +0.3% vs −1.9%. LIFTMOR-M (Harding 2020,
  men): lumbar spine +4.1% vs +0.9%. Men-specific RCTs agree (Kukuljan 2009; Hinton 2015; Menkes
  1993). The ESSA position stand (Beck 2017) sets the threshold at **≥ 80–85% 1RM**.
- **Only axially loaded lifts load the spine and hip.** Squat, deadlift and *standing* overhead
  press load them. Leg press, machines and seated work mostly bypass them.
- **Impact works, especially at the hip.** Very small doses are enough: 10 max jumps/day, 3×/week
  (Kato 2006: femoral neck +2.6% in 6 months). In men around age 70, 50 multidirectional
  single-leg hops/day raised femoral-neck BMD in the hopping leg vs the control leg (Allison
  2013, 2015). Meta-analysis: femoral neck about +1.5%; jumping alone does little for the spine.
  Hip gains appeared only for impacts above roughly **3.9 g / 3–4× bodyweight** (Vainionpää
  2006).
- **Bone stops responding after about 20–50 cycles in a bout and recovers in 4–8 h** (Robling
  2000–2002; Umemura 1997). Extra reps add little; **two short bouts a day beat one long one**.
  Resting about 10–30 s between individual impacts restores the response (Robling 2001; Tucker
  2015 used 30 s rests twice daily in humans).
- **Odd, multidirectional impact** (squash, soccer-type loading) thickens the femoral neck all
  the way round. Repetitive running, cycling and swimming do not (Nikander 2005, 2010). So hops
  go sideways, diagonal and backward, not only straight up.
- **Heavy lifting plus impact beats either one alone** (Martyn-St James & Carroll 2009; ESSA).
  In osteopenic men, only resistance training raised total-hip BMD (Hinton 2015). So the lifting
  is the core of the module and the impact is the add-on.
- **Timescale.** A bone remodeling cycle takes 3–6 months. DXA picks up change at about 6 months
  at the earliest; credible trials run 8–18 months. Expected true gain is **about 1–4%/year at
  the spine and 0–3% at the hip**. **Detraining reverses it:** 6 months off erased hip gains
  (Winters & Snow 2000). Maintenance needs far less than building did (rat data: about 30
  jumps/week, plus continued heavy lifting).
- **Honest caveat.** Almost all the RCTs are in older adults and postmenopausal women. There are
  no good trials in already-trained healthy men, who likely have some of the adaptation already;
  further gains most plausibly come from more load, a higher strain rate and new loading
  directions, which is exactly what this module adds. It is low-cost and low-risk, and the
  expected payoff is a few percent at the sites that fracture.

---

## 2. Component A — Heavy axial lifting (the core; lives inside the existing program)

**Qualifying exposure** = at least **2 working sets at ≥ 80% e1RM** on an axially loaded lift:
Barbell Deadlift, any barbell squat, standing overhead press, or trap-bar deadlift. Loaded
carries (suitcase, farmer's) count as a **bonus** exposure (odd loading through the spine and
hips), never as a substitute.

**Target: 2 qualifying exposures per week** (LIFTMOR ran 2×/week). Report the week's count in
the tally (§5).

### How the existing block structure already fits

| Block / week | Axial lift at | Qualifies? |
|---|---|---|
| Strength Wk 1 (4×5 @ 77.5%) | 77.5% | Borderline — count it; the wave climbs from here |
| Strength Wk 2 (4×4 @ 82.5%) | 82.5% | ✅ LIFTMOR-range |
| Strength Wk 3 (5×3 @ 85%) | 85% | ✅ — the most bone-specific week of the program |
| Strength Wk 4 (3×2 @ 87.5% + AMRAP @ 85%) | 87.5% | ✅ |
| Hypertrophy (maintenance 1×4 @ 82.5%) | 82.5%, one set | ❌ one set — see **Bone Doubles** |
| Deload (65%) | — | ❌ by design; not a miss |

**The Strength block is effectively a LIFTMOR block for the deadlift.** No change is needed
there. What the module adds is a way to keep the bone stimulus alive during Hypertrophy
blocks.

### Bone Doubles (optional, Hypertrophy blocks only)

On a qualifying axial lift in a Hypertrophy block (currently the **Barbell Deadlift** on gym leg
day), after the maintenance set add **2 × 3 @ 85% e1RM**, rest 210 s, RIR ≥ 2. Round to the
equipment increment. That makes the lift's heavy exposure 3 sets at ≥ 82.5%, and it counts as a
qualifying exposure.

- Performance order: warmup ramp → maintenance set → Bone Doubles → hypertrophy working sets.
- Rule 5 of `injury-protocols.md` applies: any knee or back sensation ends the doubles and the
  lift.
- Volume: count at 1.0× like any other working set (§11).
- **Not on the wave; no e1RM or TM effect.** The doubles run at RIR ≥ 2 and are *not* AMRAPs.
  They can open an e1RM thread only through the normal §2 qualifying-set rules.
- Time limit: Bone Doubles are the **first thing cut** on a time-limited leg day, before any
  accessory. They are optional and must never push a programmed lift off the sheet.
- Deload: no Bone Doubles.

---

## 3. Component B — Impact ladder (lower body)

The impact work is a **ladder** in the `bodyweight-ladders.md` sense: ordered rungs from lowest
to highest ground reaction force (GRF), each unlocked by clean bouts on the one below. It
respects any knee flag by starting ankle-driven and stiff-kneed, and by gating every
knee-flexion landing.

| Rung | Movement | Dose (per bout) | Approx. GRF | Knee demand |
|---|---|---|---|---|
| 1 | **Heel drops** — rise onto the toes, drop the heels hard to the floor, knees soft but nearly straight | 2 × 15, 10 s between sets | ~2–3× BW | Minimal |
| 2 | **Pogo hops, bilateral, in place** — small hops (2–4"), ankle-driven, knees nearly straight, quiet landings | 3 × 10, 30 s between sets | ~3× BW | Minimal |
| 3 | **Multidirectional pogo hops, bilateral** — 10 each: forward/back, side-to-side, diagonal, quarter-turns | 4 × 10, 30 s between sets | ~3–4× BW, odd-impact | Low |
| 4 | **Single-leg hops, multidirectional** — Allison protocol: in place, forward/back, side, diagonal; low height | 3 × 10/leg, 30 s between sets | ~2–3× BW on one leg | Low-moderate |
| 5 | **Countermovement jumps** — max-effort vertical jump from a quarter-squat dip, landing softly back to a quarter squat. **Single reps, reset 10–15 s between each.** | 10–20 reps | ~4–5× BW | **Moderate — knee-gated** |
| 6 | **Drop landings** — step (don't jump) off a box, land on both feet to a quarter squat and stick it. Box 6" → 12". **Never the 18" box.** | 10–20 reps, 10–15 s between | ~5–7× BW | **High — knee-gated** |

**Rungs 5–6 are not the excluded "deep squat jumps or plyometric squat variations"**: the dip
and the landing both stop at a quarter squat, and there is no loaded or repeated rebound. They
still load the knee in flexion, which is why they are gated (§3 gates below and the injury
file).

### Dose and bout rules
- **A bout = the prescribed dose for the current rung, ~5 min.** Warm up with 30 s of easy
  bouncing or the prehab block first. Do not do it cold.
- **Quality over count.** Stop the set when landings get loud, heavy or sloppy; the set counts.
- **Two bouts in a day is better than one double bout.** A second bout must be **≥ 4 h** after
  the first (ideally 6–8 h). Never do more than 2 bouts/day.
- **Rungs can be mixed downward.** A Rung 4 bout may include Rung 3 hops as its warmup set. The
  bout is logged at the highest rung performed.
- Hard or shock-absorbing floor both work; avoid very soft mats (they absorb the stimulus).
  Shoes on.

### Progression
- **Rungs 1–2: advance after 1 clean bout.** They exist to calibrate tissue tolerance, not to
  build bone on their own.
- **Rungs 3–6: advance after 3 clean bouts at the rung** (not necessarily consecutive days).
- **Clean** = full dose, landings quiet and controlled, and **no knee, Achilles, shin or foot
  sensation during the bout or the next morning.**
- **Next-morning check.** Tendon and bone-stress symptoms show up late. If the user reports
  next-morning Achilles, shin or foot soreness that is *not* ordinary muscle soreness, drop one
  rung.
- **Ceiling.** Rung 6 at 12" is the top of this module. Beyond it, progress by rotating
  directions and mixing Rungs 4 and 6 in the same bout (novel strain), never by adding reps
  or height.

### Gates (checked before prescribing)
- **Pain.** Any joint sensation during a bout ends the bout and drops one rung. Pain → the Pain
  Response Protocol in `injury-protocols.md`, as for any exercise.
- **Knee gate for Rungs 5–6.** Unlocks only when **no knee Pain Response Protocol is open** AND
  the knee was quiet throughout the **last 2 legs sessions** AND the user has completed 3 clean
  bouts at Rung 4. If a knee protocol opens later, cap at Rung 4 until it closes.
- **Layoff.** More than 14 days since the last bout → drop one rung (same as the ladder layoff
  rule).
- **Deload weeks.** Impact continues at the **same rung, half the dose**. The module's deload is
  load-light, not absent, because bone gains are lost to inactivity, not to fatigue.
- **Leg-day interaction.** An impact bout before a leg session is fine at Rungs 1–4. At Rungs
  5–6, if it is done before a legs session, it must follow the leg prehab block, and it replaces
  the general warmup, not the warmup ramp.

---

## 4. Component C — Upper-limb loading (wrist, forearm, shoulder girdle)

Wrist fractures from a fall on an outstretched hand are the most common early fragility
fracture, and the forearm only adapts when it is loaded itself (Troy 2020). The program already
loads it (dead hang, pull-ups, carries, wrist curls). This component adds a short impact dose.

| Rung | Movement | Dose |
|---|---|---|
| 1 | **Wall fall-catch** — stand an arm's length plus a step from a wall, fall forward, catch on the palms, press back | 2 × 10, 10 s between reps |
| 2 | **Bench / counter fall-catch** — same drill, hands landing on a bench or counter (hip height) | 2 × 10 |
| 3 | **Low-box fall-catch** — hands on the 18" box | 2 × 10 |
| 4 | **Incline plyo push-up** — hands on the bench or 18" box, push explosively so the hands leave the surface, catch soft | 2 × 8, reset 5–10 s between reps |
| 5 | **Floor plyo push-up** — hands leave the floor, no clap; catch soft into the next rep's descent | 2 × 6–8, reset 5–10 s between reps |
| 6 | **Clap push-up** | 2 × 5–6, reset 10 s between reps |

- **Shoulder gate:** every rung lands with the elbows soft and the shoulders packed. Any
  shoulder sensation ends the set and drops a rung; pain → the Pain Response Protocol.
- **Rungs 4–6 unlock** only when no shoulder Pain Response Protocol is open AND the shoulder
  was quiet through the last 2 push sessions AND the rung below has had 3 clean bouts. If a
  shoulder protocol opens later, cap at Rung 3 until it closes.
- Advance after 3 clean bouts. Rung 6 is the top; beyond it, progress by mixing rungs, not
  by adding reps.
- Runs as part of an impact bout (after the lower-body sets) or on its own. It counts toward the
  weekly tally as an upper-limb bout.

## 4b. Back extensors

Back-extensor strength is linked to fewer vertebral fractures (Too Fit To Fracture; ROS Strong,
Steady and Straight). The **Sorenson Hold** on pull day already covers this; no addition is
needed. Being isometric, it counts for posture and fracture protection, not as a bone-loading
exposure.

---

## 5. Rhythm — the weekly tally (how "encouraged" is implemented)

The trainer never plans a week ahead (operating-protocol). Instead it keeps a **rolling 7-day
tally** in `training-state.md` and shows it in the coaching view:

```
Bone week (last 7 days): impact 2/4 · axial 1/2 · upper 1/2 · last bout 2026-09-23 (Rung 3)
```

| Item | Minimum (maintain) | Target (build) |
|---|---|---|
| Impact bouts (Component B) | 3 / week | 4–7 / week (up to 2/day, ≥ 4 h apart) |
| Qualifying axial exposures (Component A) | 1 / week | 2 / week |
| Upper-limb bouts (Component C) | 1 / week | 2 / week |

**Prescribing the module:**
- **Every session** gets a `BONE (optional)` section: the current impact rung at full dose, plus
  the upper-limb rung if the tally is under target. It prints last in the checklist and can be
  done **any time that day** — best at least 4 h from the session, or straight after prehab if
  that is easier. It is **outside the session's time budget**: it is never cut for time and
  never forces anything else to be cut.
- **Bone Doubles** print inside the working sets (§2), on the lift they belong to.
- **Standalone bouts.** "Bone snack", "impact bout" or "bone day" as an opener → prescribe only
  the BONE section (coaching lines + checklist). No prehab block is required unless the rung is
  5–6 (then the leg prehab block, gym or home version, runs first).
- **Nudge rule.** If the rolling tally is below the **minimum** on any line, say so in one line
  in the Session Notes (e.g. "Bone: 1 impact bout in the last 7 days — minimum is 3"). One line,
  no lecture, no repetition within the same session.

**Daily phone ping (optional, added 2026-10-13; general mechanism 2026-10-18).** A user may
receive a daily push listing the day's bout. The shared mechanism is a `kind: "bone"` entry
in `users/<name>/reminders.json` sent by `system/scripts/remind.py` (`system/reminders.md`);
an older personal `users/<name>/bone-ping.json` plus its own script does the same job and
may stay until the user moves it. Whichever file exists is the ping's only source:
**whenever an impact or upper-limb rung advances or drops, edit the matching `moves` entry in
the same commit as the state change**, or the phone keeps prescribing the old rung. Dose in
the file may follow a user directive rather than the rung table. A reported ping bout is logged like any standalone bout.

**Reporting.** Unchanged `BONE` lines = performed at the prescribed dose (the standard
reporting rule). A deleted or `x` line = not performed: **not a miss** and no effect on anything
else. A standalone bout reported in natural language ("did my hops this morning") is logged
with its date and rung. Record every bout in the state's **Bout log** so the tally can be
computed.

---

**Balance Module (added 2026-10-26).** Activating this module re-offers `balance.md` once,
in one line: a fracture is a fall plus a fragile bone, and this file covers only the bone.

**Power Module interaction (added 2026-10-26).** When `power-and-plyometrics.md` is also
active, one jump bout a day feeds both tallies under its §9 mapping (power rung 1 = bone
Rung 2; power rungs 2–6 = bone Rung 5), and the two files share one knee gate. Heel drops
(Rung 1) and multidirectional single-leg hops (Rung 4) stay bone-only.

---

## 6. Lifestyle levers (mention when relevant; never prescribe as program)

Evidence grade in brackets. This is general information, not medical advice.

- **Energy availability [A for bone markers].** Long or deep caloric deficits suppress bone
  formation and testosterone. During a cut: keep the deficit modest (about 0.5–1% of body weight
  per week), protein high, and keep lifting heavy.
- **Protein [A, no harm]** 1.6–2.2 g/kg is fine for bone; the "acid-ash" idea that protein
  leaches calcium from bone is not supported (Shams-White 2017).
- **Calcium [A, small effect]** about 1,000 mg/day, mostly from food; supplement only to fill a
  gap, ≤ 500 mg per dose (Bolland 2015).
- **Vitamin D [A, only if deficient]** — correct a deficiency; extra D in replete adults did
  nothing for BMD (VITAL, LeBoff 2020).
- **Creatine [B, mixed]** 3–5 g/day for training; any bone effect is a bonus (Chilibeck 2015;
  Forbes 2018 meta-analysis null).
- **Alcohol [A, observational]** more than 2 drinks/day raises fracture risk; 2 or fewer does
  not (Kanis 2005). Smoking roughly doubles hip-fracture risk.
- **Not worth it:** whole-body vibration for a trained lifter (no effect in young adults), and
  passively wearing a weighted vest (INVEST, Beavers 2025: no hip benefit).
- **Measuring.** DXA on the **same machine**, no more often than every 12–24 months; changes under
  about 2–3% (spine) or 3–5% (femoral neck) are inside measurement error. Bone turnover markers
  (P1NP, CTX) are too noisy to track training gains.

---

## 7. What this module never does

- Never overrides an injury exclusion, a Pain Response Protocol, or a time limit.
- Never changes the rotation, block, rep windows, RIR ramp or any lift's progression.
- Never counts impact, fall-catch or plyo push-up reps toward weekly muscle volume.
- Never logs a bout that was not reported.

---

## 8. Session-end review hooks

Flag for review (per operating-protocol §6) if: the user skips the BONE section for 3
consecutive weeks (ask whether to keep offering it, or shrink it to the minimum), or a rung
produces a sensation twice (ask whether that rung stays in the ladder).

---

## 9. References

Resistance training
- Watson SL et al. 2018. LIFTMOR. *J Bone Miner Res* 33:211–220. doi:10.1002/jbmr.3284
- Harding AT et al. 2020. LIFTMOR-M. *J Bone Miner Res* 35:1404–1414. doi:10.1002/jbmr.4008
- Kistler-Fischbacher M et al. 2021. MEDEX-OP. *J Bone Miner Res*. doi:10.1002/jbmr.4334
- Kistler-Fischbacher M, Weeks BK, Beck BR. 2021. Meta-analysis. *Bone* 143:115697
- Kukuljan S et al. 2009. *Osteoporos Int*. doi:10.1007/s00198-008-0776-y
- Hinton PS et al. 2015. *Bone* 79:203–212. doi:10.1016/j.bone.2015.06.008
- Menkes A et al. 1993. *J Appl Physiol* 74:2478–2484
- Almstedt HC et al. 2011. *J Strength Cond Res* 25:1098–1103
- Kemmler W et al. 2018. *Osteoporos Int* 29:1493–1504

Impact
- Kato T et al. 2006. *J Appl Physiol* 100:839–843. doi:10.1152/japplphysiol.00666.2005
- Allison SJ et al. 2013. *Bone*; Allison SJ et al. 2015. *J Bone Miner Res* 30:1709. doi:10.1002/jbmr.2499
- Vainionpää A et al. 2005, 2006. *Osteoporos Int*. doi:10.1007/s00198-005-0005-x
- Tucker LA et al. 2015. *Am J Health Promot*. doi:10.4278/ajhp.130430-QUAN-200
- Bassey EJ et al. 1998. *J Bone Miner Res* 13:1805–1813
- Nikander R et al. 2005. *J Bone Miner Res* 20:520–528; 2010. *BMC Med* 8:47
- Zhao R et al. 2014. *Sports Med* 44:1393–1402
- Suominen TH et al. 2017. *Osteoporos Int* 28:2663–2673 (sprint + strength, men)
- Troy KL et al. 2020. *J Bone Miner Res* 35:1300–1312 (forearm loading)

Mechanism and dosing
- Frost HM 1987. *Anat Rec* 219:1–9; 2003. *Anat Rec A* 275:1081
- Turner CH 1998. *Bone* 23:399–407; Turner CH, Robling AG 2003. *Exerc Sport Sci Rev* 31:45–50
- Robling AG et al. 2000 *Bone*; 2001 *J Exp Biol* 204:3389; 2002 *J Bone Miner Res* 17:1545
- Umemura Y et al. 1997. *J Bone Miner Res* 12:1480
- Rubin CT, Lanyon LE 1984. *J Bone Joint Surg Am* 66:397–402
- Winters KM, Snow CM 2000. *J Bone Miner Res* 15:2495–2503 (detraining)

Position stands
- Kohrt WM et al. 2004. ACSM Position Stand. *Med Sci Sports Exerc* 36:1985–1996
- Beck BR et al. 2017. ESSA. *J Sci Med Sport* 20:438–445
- Giangregorio LM et al. 2014, 2015. Too Fit To Fracture. *Osteoporos Int*
- Brooke-Wavell K et al. 2022. ROS Strong, Steady and Straight. *Br J Sports Med* 56:837–846

Nutrition and lifestyle
- Bolland MJ et al. 2015. *BMJ* 351:h4183 · LeBoff MS et al. 2020. *J Bone Miner Res* 35:883
- Shams-White MM et al. 2017. *Am J Clin Nutr* 105:1528 · Chilibeck PD et al. 2015. *MSSE* 47:1587
- Forbes SC et al. 2018. *Front Nutr* 5:27 · Papageorgiou M et al. 2018. *Bone* 105:191
- Mountjoy M et al. 2023. IOC REDs. *Br J Sports Med* 57:1073 · Kanis JA et al. 2005. *Osteoporos Int* 16:737
- Beavers KM et al. 2025. INVEST. *JAMA Netw Open*
