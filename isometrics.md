# Isometrics Module — OPTIONAL (added 2026-10-26, user request)

An optional add-on that uses **held contractions as a tool** for two jobs the rest of the
program does not do: lowering resting **blood pressure** (wall squat or handgrip, four
two-minute holds, three times a week) and taking the edge off **tendon pain** named by the
user (long, heavy holds on the sore tendon, standalone or right before the lift that loads
it). Isometrics already appear in this repo as filler and as core work: the wall sit in the
7-Minute Workout, the Sorenson hold, the McGill Big 3, planks, the dead hang. None of that
changes. This file is only the two **dosed** uses, each with its own trigger, dose, log line
and stop rule.

**Optional means:** offered once, never required, and skipping it is never a miss and never
costs progression anywhere else. The blood-pressure protocol is offered when blood pressure
comes up (a goal, a cuff, a clinician's comment, the word "hypertension" or "BP"), at intake
or later, and once only. The tendon holds are offered when the user, or a clinician the user
quotes, calls a pain **tendon** pain (§3); the engine never decides that itself.
**Encouraged means:** a rolling 7-day tally with a one-line nudge below minimum (§4).

Read this file whenever a session is prescribed **while either half is active** (a protocol
or a tendon site recorded under **Isometrics Module** in `training-state.md`), when the
opener says "blood pressure", "BP", "hypertension", "wall squat", "handgrip", "tendon",
"tendinopathy", "tendinitis", "jumper's knee", "Achilles", "tennis elbow", "golfer's
elbow", "plantar fascia" or "isometric", and once at intake when blood pressure is raised.
While the state says "Not started" the file is not read and nothing prints. Injury gates
in `users/<name>/injury-protocols.md` and the Pain Response Protocol in
`return-to-training.md` **always win**; nothing here changes a protocol's state.

---

## 1. What the science says (short version; references in §8)

Blood pressure
- **Isometric training lowers resting blood pressure more than any other exercise mode.**
  In a network meta-analysis of 270 randomised trials (n = 15,827), isometric exercise
  training cut resting systolic pressure by about 8 mmHg and diastolic by about 4 mmHg,
  ahead of combined training, dynamic resistance training, aerobic training and HIIT; the
  **isometric wall squat** was the most effective single mode in the analysis (Edwards
  2023). Earlier pooled estimates of isometric training put the systolic drop at 5–7 mmHg
  (Carlson 2014, Inder 2016), which is in the range of a single antihypertensive drug.
- **The dose is small and fixed.** Nearly every trial used the same recipe: **four holds of
  two minutes**, three days a week, for 8–12 weeks, at about 30% of maximal grip (handgrip)
  or at a knee angle that makes two minutes just completable (wall squat). Home-based wall
  squats at that dose lowered systolic pressure in four weeks (Wiles 2017); handgrip at 30%
  did the same in medicated hypertensive adults (Taylor 2003). Reviews put the mechanism on
  the vessels and the autonomic system rather than the heart (Millar 2014).
- **Breathing is the safety line.** Blood pressure rises during any held contraction and
  climbs steeply with a held breath: a Valsalva under a heavy lift has been measured above
  300 mmHg systolic (MacDougall 1985). At 30% effort with continuous breathing the rise is
  modest and brief, which is why every hold here is breathed through and a hold that forces
  a held breath is too hard (§2).
- **Thresholds the engine uses, and nothing more.** A reading of 180 systolic or 120
  diastolic or higher is the hypertensive-crisis line in the ACC/AHA guideline (Whelton
  2018) and ends the day's isometric and HIIT work with one pointer to a clinician (§2).
  The engine never interprets a reading below that line.

Tendon pain
- **A heavy isometric hold can turn tendon pain down for about 45 minutes.** Five 45-s holds
  at 70% of maximum on the patellar tendon cut pain from 7/10 to near zero during a
  single-leg decline squat, with the effect lasting at least 45 minutes and the quadriceps
  freed from pain inhibition (Rio 2015); in-season, isometrics beat isotonic sets for that
  immediate relief (Rio 2017). That is the **primer** in §3: holds right before the lift
  that loads the tendon.
- **It is relief, not the cure.** Over weeks, isometric and isotonic programmes reduced
  patellar tendon pain about equally (van Ark 2016); pooled across tendons, isometrics were
  no better than other loading for pain or function (Clifford 2020), and in Achilles
  tendinopathy the 45-s holds gave no reliable acute analgesia at all (O'Neill 2019). The
  long-term fix for a tendon is progressive loading (Cook & Purdam 2009; Malliaras 2015),
  which in this program is the test and ramp in `return-to-training.md`. The holds here
  make that path more comfortable; they do not shorten it.
- **Tolerable pain during loading is acceptable; worse the next morning is not.** The
  pain-monitoring model in Achilles tendinopathy let patients train with pain up to 5/10
  provided it settled by the next morning, with outcomes as good as rest-based care
  (Silbernagel 2007). The engine stays stricter on the lift itself (a sensation on the lift
  is a fail, `return-to-training.md` §2) and uses the next-morning rule only on the holds
  (§3).
- **Isometric strength is angle-specific** and transfers unevenly to dynamic lifts
  (Oranchuk 2019; Lum 2019), which is why this module never substitutes a hold for a main
  lift (§7).

---

## 2. Blood pressure: the protocol

### Mode

| Mode | Default when | Needs |
|---|---|---|
| **Wall squat** | the default: largest effect (§1) | a wall, a timer |
| **Handgrip** | a knee or hip flag, an open lower-limb Pain Response Protocol, no wall, or the user's preference | a hand dynamometer or grip device at best; a tennis ball, a rolled towel or a grip trainer as a stand-in |

The user picks once at opt-in; either can be swapped for the other at any boundary.

### Dose (both modes)

- **4 holds × 2 min**, three sessions a week, on any day, 8 weeks before judging it.
- Rest between holds: **2 min** (wall squat, as in Wiles 2017), **1 min** (handgrip, as in
  Taylor 2003; the hands alternate, so each hand rests while the other works).
- A session is about 14 min (wall squat) or 11 min (handgrip). It sits outside every time
  budget: it is never cut and never causes a cut.
- **Breathe the whole time.** Out loud counting or talking is the test. A hold that forces
  the breath to stop is too hard: end it, note it, drop one step next session.

### Intensity

- **Wall squat.** Back flat on the wall, feet shoulder-width and far enough out that the
  shins stay vertical, hands off the thighs, knees never past the toes. Intensity is the
  **knee angle**: start at about **135°** (a shallow sit; thighs well above horizontal).
  Steps are **10°** down to a floor of **95°**, never below 90°. The target feeling at the
  end of the fourth hold is **hard but steady, about 7 of 10**: legs burning, no shaking,
  breathing continuous.
- **Handgrip.** **30% of maximal grip**, 2 min, alternating hands each hold (left, right,
  left, right). With a dynamometer, 30% of the best reading; while the scorecard in
  `benchmarks.md` is active, that is 30% of the grip number in its table. Without one: a
  firm handshake, about a third of a full squeeze, that can be held for the full 2 min with
  the forearm burning by the end and the hand not shaking. If the hand opens before 2 min
  the squeeze was too hard; if nothing is felt at 2 min it was too light.

### Progression and regression

| Session result | Next session |
|---|---|
| All 4 holds complete, final hold ≤ 5/10 effort, breathing never broke | one step harder: wall squat −10° knee angle (to the 95° floor); handgrip +5% |
| All 4 complete, final hold 6–8/10 | same |
| Any hold ended early, or breath held | one step easier: +10° or −5% |
| Two sessions in a row ended early at the shallowest angle (135°) or the lightest useful grip | the mode is wrong for now: swap modes, or shorten holds to 4 × 1 min for two weeks and rebuild |

### Placement

- Any day, any time, **3 times a week with at least one day between sessions**; morning,
  before caffeine, is the trial convention but not a rule.
- **Wall squat** sessions sit **≥ 4 h after** a leg-loading session or on another day,
  never within 4 h **before** one (`LEGS`, `LOWER`, `FB-A`, `FB-B`), and not the day before
  a Strength-block leg session's test or heavy singles.
- **Handgrip** sessions sit **≥ 4 h before** any session with rows, deadlifts, carries,
  hangs or pull-ups, or after it. Never on a day a forearm or elbow protocol is open on that
  side.
- Not the HIIT slot, not on the weekly cardio cap, never a rotation day, never a miss. It
  runs unchanged in deload weeks. `ILL` (`readiness.md`): none that day. Other readiness
  flags: unchanged.

### Readings

The module does not need readings. If the user owns a cuff and chooses to log, the
convention is **seated, morning, before caffeine and exercise, same arm, the average of two
readings a minute apart**, reported in the user's own words ("128/82 this morning") and
written to the state with the date. Nothing is ever asked for.

- **Trend, never a single reading.** The Weekly Snapshot prints the 4-week average against
  the 4-week average before the protocol started, once both exist. Nothing is said about
  what the numbers mean.
- **≥ 180 systolic or ≥ 120 diastolic on any reading**: no isometric and no HIIT work that
  day, and one line, once: a reading at that level is one to act on today, with a clinician
  or urgent care, not to train through. No other advice, ever.
- **On blood-pressure medication** (the user says so): the protocol is unchanged, and the
  trainer says once, in one line, that their prescriber may want to know they have started
  it, since pressure can fall further than expected. Nothing else.

### Safety

- The `conditioning-hiit.md` §8 safety screen is asked once before the first session if it
  has not already been asked, and its stop list applies: chest pain or pressure, fainting or
  near-fainting, unusual breathlessness, palpitations, or a sudden severe headache during a
  hold ends the session and routes to that line.
- Never a Valsalva. Never a hold heavier than the breath allows.
- Dizziness on standing after a wall squat: stand up slowly between holds, sit if needed.
  Twice in a week → handgrip instead for two weeks.

### Review

Every 8 weeks (on the scorecard date when `benchmarks.md` is active, otherwise 8 weeks from
the start date) the Snapshot prints the readings trend if there is one, the sessions done
of those possible, and asks once whether to keep going. The module never ends the protocol
on its own.

---

## 3. Tendon pain: the holds

### Trigger

Only when the user names the pain as tendon pain, in their own words or a clinician's:
"tendon", "tendinopathy", "tendinitis", "jumper's knee", "patellar tendon", "Achilles",
"tennis elbow", "golfer's elbow", "plantar fascia", "gluteal tendon", "hamstring tendon",
"sit-bone pain", "groin" with "tendon". The engine never decides a sensation is tendon pain,
never names a tissue, and never offers holds for a joint, bone, nerve or muscle pain. A
named tendon gets a **site** entry in state (§6) and the holds below run **alongside** the
Pain Response Protocol on whatever lift opened it; the protocol's states, test and ramp
run exactly as `return-to-training.md` says. Holds never open, advance or close a protocol.

### Positions, by site

Every hold: the muscle contracts hard with no movement, the tendon in its mid-range (never
its stretched end), both sides where that is natural, the sore side last.

| Site (user's word) | Hold | Progression of load |
|---|---|---|
| Patellar / quadriceps tendon ("jumper's knee", front of the knee) | **Spanish squat**: a strap or thick band behind the knees anchored at shin height, sit back to 70–90° knee, shins vertical · *without a strap:* wall sit at 70–90° | two legs → one leg · then a backpack or a dumbbell held at the chest |
| Achilles / calf tendon | **Heel-raise hold** at mid-height, both feet, hands on a wall for balance; insertional (at the heel bone): heels never below floor level, no step edge | two feet → one foot → backpack |
| Plantar heel ("plantar fascia") | heel-raise hold with a rolled towel under the toes so they stay lifted, both feet | two feet → one foot |
| Lateral elbow ("tennis elbow") | **wrist-extension hold**: forearm supported palm-down, hand off the edge, a light dumbbell held level | 2–3 lb → +1 lb · elbow 90° → straighter |
| Medial elbow ("golfer's elbow") | **wrist-flexion hold**: as above, palm up | same |
| Proximal hamstring ("sit-bone") | **long-lever bridge hold**: heels on a chair, knees nearly straight, hips lifted a hand's width | two legs → one leg |
| Lateral hip ("gluteal tendon", outer hip) | **side-lying leg-lift hold**: top leg lifted 30°, slightly behind the body line, never crossed over; lie on the other side | bodyweight → ankle weight |
| Shoulder ("rotator cuff tendon") | **external-rotation hold**: elbow at the side at 90°, back of the wrist pressing a door frame, 30% effort to start | 30% → 50% → 70% effort |
| Adductor / groin | **ball squeeze**: lying, knees bent, a ball between the knees | 30% → 70% effort · then knees straight |

A site not in the table (biceps, triceps, wrist flexor) follows the same rule: a hard hold of
that muscle in mid-range with no movement, chosen from `exercise-library.md` by pattern.

### Dose

| Use | Dose | When |
|---|---|---|
| **Standalone bout** | 5 holds × 45 s, rest 2 min (about 14 min) | once or twice a day, any day, while the protocol is `OPEN`, `TEST` or `RAMP`; the user chooses the days |
| **Primer** | 3 holds × 45 s, rest 60 s (fixed **255 s** in the estimate, never cut) | in the session where the affected lift is due, printed immediately before the Warmup Ramp, while the protocol is `TEST` or `RAMP`; the relief window (§1) covers the lift |
| After `CLOSED` | the standalone bout 2–3 days a week for one more block, then stop; or earlier if the user says so | — |

- **Effort: hard, 7 of 10**, holdable for 10 s beyond the prescribed 45 s, no shaking. The
  trials used 70% of maximum on a machine; the effort cue is the home stand-in.
- **Pain during a hold up to 3 of 10** on the user's own scale is acceptable, and the
  number is logged. Over 3 → shorten to 30 s or lighten one step for the rest of the bout.
- **The next-morning rule.** The tendon the next morning is the real reading: **no worse
  than the day before** = the dose stands or steps up (one step per week at most); **worse**
  = one step down; **worse after two consecutive bouts** = the holds stop on that site for
  one week, said in one line, and resume one step lighter. The Pain Response Protocol on the
  lift is untouched by any of this.
- **Never stretch the sore tendon before a hold**, and no hold at the stretched end of the
  range (no heel below the step for an insertional Achilles, no deep squat for a patellar
  tendon).

### Placement and interactions

- The primer is the one thing this module puts inside a lifting session. It prints only on
  a day the affected lift is due, only while that lift's protocol is `TEST` or `RAMP`, after
  `PREHAB` and after the power primer if one prints, directly before `WARMUP`. It is never
  cut for time: it is part of the protocol path and the sheet is cut below it as usual.
- Standalone bouts count toward nothing else: not the cardio cap, not weekly volume, not a
  quick session.
- A joint under an open protocol is already closed to jumps (`power-and-plyometrics.md`
  §4, `bone-loading.md`) and the dynamic balance ladder (`balance.md` §2); holds do not
  reopen it. Those gates lift when the protocol closes, by their own rules.
- A tendon site with no improvement after two full blocks of holds and ramping is the
  persistent-pain case in `return-to-training.md` §4 rule 4: said once, written to the flag,
  left to a clinician.

---

## 4. Rhythm: the weekly tally

A rolling 7-day tally in `training-state.md`, printed in the coaching view whenever an
isometric line or section prints:

```
Isometrics week (last 7 days): BP 2/3 (wall squat 115°) · last 2026-10-24 · tendon holds 4 bouts (patellar L, wall sit 80° + 10 lb)
```

| Line | Minimum (maintain) | Target |
|---|---|---|
| BP sessions | 2 / week | 3 / week |
| Tendon bouts (while a protocol is open) | 3 / week | 5–7 / week |

- **Nudge rule.** Below the minimum → one line in Session Notes ("BP: 1 of 3 sessions this
  week; the dose that worked in the trials was 3"). Once per session, never repeated.
- **Reminders.** `kind: "isometric"` in `reminders.md` §2, opt-in like every reminder. For
  the BP protocol the natural one is a fixed three-day ping ("Wall squat 4 × 2 min at
  115°, rest 2 min, breathe; reply: did my wall squat"); for a tendon site a daily anchor
  while the protocol is open, with `until` set to the protocol's close. Message text is
  edited in the same commit as any step change (`reminders.md` §1 principle 4).

---

## 5. Placement summary

| | BP protocol | Tendon holds |
|---|---|---|
| Day | any, 3/week, a day between | any, daily, while a protocol is open |
| In a lifting session | never | the primer, before `WARMUP`, `TEST`/`RAMP` only |
| Relative to legs | wall squat ≥ 4 h after, never 4 h before | — |
| Relative to pulls | handgrip ≥ 4 h before, or after | — |
| Deload | unchanged | unchanged |
| Readiness flag | `ILL`: none; others unchanged | `ILL`: none; others unchanged |
| Cardio cap, volume, HIIT slot | none of them | none of them |

---

## 6. Output, reporting and state

**Coaching view.** A standalone session uses the quick-session header style
(`quick-sessions.md` §6):

```
## [Day] — Isometrics: wall squat (14 min)
Isometrics week (last 7 days): BP 2/3 · last [date]

### Session
- Wall squat at 115°: 4 × 2:00, rest 2:00 — back flat, shins vertical, breathe throughout
  > [one line: step status / last session's result / the 4th-hold effort target]

### Session Notes
- Not a rotation day. Next lifting day due: [day type].
```

A tendon bout reads the same with the site, position, load and the pain-number
instruction in the `>` line. In a lifting session the primer is its own section:

```
### Isometric primer — patellar tendon (L) (4 min)
- Wall sit 80° + 10 lb: 3 × 45 s, rest 60 s — hard, 7/10, breathe; pain ≤ 3/10 or lighten
```

**Checklist.** A standalone session is one `ISOMETRIC` block, one line per hold, the
duration in the last field; the user appends the seconds held if short and, on a tendon
line, the pain number:

```
ISOMETRIC
Wall squat 115° — R2m
Wall squat 115° — Hold 1 — 2:00
Wall squat 115° — Hold 2 — 2:00
Wall squat 115° — Hold 3 — 2:00
Wall squat 115° — Hold 4 — 2:00
```

Handgrip lines carry the hand (`Handgrip 30% — Hold 1 — L — 2:00`). In a lifting session the
primer is an `ISOMETRIC` block between `PREHAB` (or `POWER`) and `WARMUP`, three lines, the
load in the load field (`Wall sit 80° — Hold 1 — 10 lb — 45 s`).

**Reporting.** Unchanged = the full hold, breathing intact. A number of seconds = the hold
achieved, not full; "breath" / "held my breath" = a breath-held hold (regression rule);
"dizzy", "chest" or "headache" = the §2 stop list. A pain number on a tendon line is the
during-pain; "AM worse" or "AM same" on a later message is the next-morning reading and
attaches to the last bout. A deleted or `x` line = not performed, not a miss. A reading
("128/82 this morning") logs to the readings line with its date and is never answered,
except by the §2 threshold line.

**State** (`training-state.md`, `## Isometrics Module (OPTIONAL)`; until the user opts in:
`Rules: system/isometrics.md. Not started.`):

```
## Isometrics Module (OPTIONAL)
Rules: `system/isometrics.md`.
BP protocol: started 2026-10-26 · mode: wall squat · step: 115° · sessions this week: 2/3 · last 2026-10-24 (4/4 complete, final hold 6/10)
  readings (user-logged, seated AM): baseline 4-wk avg 138/88 · current 4-wk avg — · last 131/84 (2026-10-24) · medication: not stated · review due 2026-12-21
Tendon sites: patellar (L) · opened 2026-10-20 with the Bulgarian Split Squat protocol (state RAMP) · hold: wall sit 80° + 10 lb · bouts this week 4 · last 2026-10-24 (5 × 45 s, pain 3→1, AM same)
Bout log: 2026-10-24 BP wall squat 115° 4/4 · 2026-10-24 tendon patellar L 5 × 45 s · …
```

A half that is not in use reads `BP protocol: not started` or `Tendon sites: none`.

**Weekly Snapshot** adds one line: BP sessions vs 3, the step, the readings trend once two
4-week averages exist, every open tendon site with its bouts and next-morning trend, and
the 8-week review question when due.

---

## 7. What this module never does

- Never overrides an injury exclusion, a Pain Response Protocol or a time limit, and never
  opens, advances or closes a protocol: holds are company for the protocol, not a shortcut.
- Never decides that a pain is tendon pain, names a tissue, or offers holds for a pain the
  user has not named as tendon pain.
- Never interprets a blood-pressure reading below the §2 threshold, never comments on
  medication beyond the one line in §2, and never asks for a reading.
- Never substitutes a hold for a main lift, a ramp set or a test session, and never counts
  a hold toward weekly volume, the cardio cap or a quick session.
- Never prescribes a hold heavier than continuous breathing allows, or at the stretched end
  of a sore tendon's range.
- Never logs a bout or a reading that was not reported.

**Session-end review hooks** (per `operating-protocol.md` §6): flag for review if the BP
protocol is below minimum for 3 consecutive weeks (ask whether to keep it, swap modes or
drop it), if a tendon site has stopped holds twice under the next-morning rule (ask whether
to pause the holds for the rest of the protocol), or if the user reports a reading at the
§2 threshold (the one line is said; nothing else is proposed).

---

## 8. References

Blood pressure
- Edwards JJ, Deenmamode AHP, Griffiths M, et al. 2023. Exercise training and resting blood
  pressure: a large-scale pairwise and network meta-analysis of randomised controlled
  trials. *Br J Sports Med* 57(20):1317–1326. doi:10.1136/bjsports-2022-106503
- Carlson DJ, Dieberg G, Hess NC, Millar PJ, Smart NA. 2014. Isometric exercise training for
  blood pressure management: a systematic review and meta-analysis. *Mayo Clin Proc*
  89(3):327–334. doi:10.1016/j.mayocp.2013.10.030
- Inder JD, Carlson DJ, Dieberg G, McFarlane JR, Hess NC, Smart NA. 2016. Isometric
  exercise training for blood pressure management: a systematic review and meta-analysis to
  optimize benefit. *Hypertens Res* 39(2):88–94. doi:10.1038/hr.2015.111
- Wiles JD, Goldring N, Coleman D. 2017. Home-based isometric exercise training induced
  reductions resting blood pressure. *Eur J Appl Physiol* 117(1):83–93.
  doi:10.1007/s00421-016-3501-0
- Taylor AC, McCartney N, Kamath MV, Wiley RL. 2003. Isometric training lowers resting
  blood pressure and modulates autonomic control. *Med Sci Sports Exerc* 35(2):251–256.
  doi:10.1249/01.MSS.0000048725.15026.B5
- Millar PJ, McGowan CL, Cornelissen VA, Araujo CG, Swaine IL. 2014. Evidence for the role
  of isometric exercise training in reducing blood pressure: potential mechanisms and
  future directions. *Sports Med* 44(3):345–356. doi:10.1007/s40279-013-0118-x
- MacDougall JD, Tuxen D, Sale DG, Moroz JR, Sutton JR. 1985. Arterial blood pressure
  response to heavy resistance exercise. *J Appl Physiol* 58(3):785–790.
  doi:10.1152/jappl.1985.58.3.785
- Whelton PK, Carey RM, Aronow WS, et al. 2018. 2017 ACC/AHA/AAPA/ABC/ACPM/AGS/APhA/ASH/
  ASPC/NMA/PCNA guideline for the prevention, detection, evaluation, and management of high
  blood pressure in adults. *Hypertension* 71(6):e13–e115. doi:10.1161/HYP.0000000000000065

Tendon pain
- Rio E, Kidgell D, Purdam C, et al. 2015. Isometric exercise induces analgesia and reduces
  inhibition in patellar tendinopathy. *Br J Sports Med* 49(19):1277–1283.
  doi:10.1136/bjsports-2014-094386
- Rio E, van Ark M, Docking S, et al. 2017. Isometric contractions are more analgesic than
  isotonic contractions for patellar tendon pain: an in-season randomized clinical trial.
  *Clin J Sport Med* 27(3):253–259. doi:10.1097/JSM.0000000000000364
- van Ark M, Cook JL, Docking SI, et al. 2016. Do isometric and isotonic exercise programs
  reduce pain in athletes with patellar tendinopathy in-season? A randomised clinical trial.
  *J Sci Med Sport* 19(9):702–706. doi:10.1016/j.jsams.2015.11.006
- Clifford C, Challoumas D, Paul L, Syme G, Millar NL. 2020. Effectiveness of isometric
  exercise in the management of tendinopathy: a systematic review and meta-analysis of
  randomised trials. *BMJ Open Sport Exerc Med* 6(1):e000760.
  doi:10.1136/bmjsem-2020-000760
- O'Neill S, Radia J, Bird K, et al. 2019. Acute sensory and motor response to 45-s heavy
  isometric holds for the plantar flexors in patients with Achilles tendinopathy. *Knee
  Surg Sports Traumatol Arthrosc* 27(9):2765–2773. doi:10.1007/s00167-018-5050-z
- Malliaras P, Cook J, Purdam C, Rio E. 2015. Patellar tendinopathy: clinical diagnosis,
  load management, and advice for challenging case presentations. *J Orthop Sports Phys
  Ther* 45(11):887–898. doi:10.2519/jospt.2015.5987
- Cook JL, Purdam CR. 2009. Is tendon pathology a continuum? *Br J Sports Med*
  43(6):409–416. doi:10.1136/bjsm.2008.051193
- Silbernagel KG, Thomeé R, Eriksson BI, Karlsson J. 2007. Continued sports activity, using
  a pain-monitoring model, during rehabilitation in patients with Achilles tendinopathy.
  *Am J Sports Med* 35(6):897–906. doi:10.1177/0363546506298279

Isometric strength
- Oranchuk DJ, Storey AG, Nelson AR, Cronin JB. 2019. Isometric training and long-term
  adaptations: effects of muscle length, intensity, and intent: a systematic review. *Scand
  J Med Sci Sports* 29(4):484–503. doi:10.1111/sms.13375
- Lum D, Barbosa TM. 2019. Brief review: effects of isometric strength training on strength
  and dynamic performance. *Int J Sports Med* 40(6):363–375. doi:10.1055/a-0863-4539
