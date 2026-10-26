# Balance Module — OPTIONAL (added 2026-10-26, user request)

An optional add-on that trains **staying upright**: static holds, stepping and reactive
drills, one line in the leg-day warm-up, and a weekly minutes target. Nothing in the SBS
engine, the bone module or the power module trains balance on purpose; a fracture is a fall
plus a fragile bone, and the bone module only covers the second half. Balance is cheap,
needs no equipment, can be done while the kettle boils, and has the strongest
fall-prevention evidence of any exercise type (§10).

**Optional means:** offered at intake, never required, and skipping it is never a miss and
never costs progression anywhere else. It is **offered again, once**, when any of these
appear later: the bone module is activated, the user turns 60, the user reports a fall,
near-fall or trip, or a lower-limb Pain Response Protocol closes. **Encouraged means:** a
rolling weekly tally with a one-line nudge below minimum (§6).

Read this file whenever a session is prescribed **while the module is active** (a rung or
tally recorded under **Balance Module** in `training-state.md`), when the opener says
"balance", "stability", "wobbly", "tripped", "fell" or "near fall", and once at intake to
offer it. While the state says "Not started" the file is not read and no balance line
prints. Injury gates live in `users/<name>/injury-protocols.md` and **always win**.

---

## 1. What the science says (short version; references in §10)

- **Exercise prevents falls, and the balance component is what does it.** Across 108
  trials (n = 23,407), exercise cut the rate of falls in community-dwelling older adults by
  23%; programmes built on balance and functional exercise cut it by 24%, tai chi by 19%,
  and resistance training alone had no clear effect (Sherrington 2019, Cochrane). Programmes
  that reached **3 or more hours a week** of mostly high-challenge balance work cut falls by
  39% (Sherrington 2017).
- **Reactive stepping is the single most effective ingredient.** Step training (volitional
  and reactive stepping drills) roughly halved falls in a meta-analysis of seven trials
  (Okubo 2017), and perturbation-based training did the same in preliminary RCTs (Mansfield
  2015). Hence the dynamic ladder's upper rungs.
- **Balance is task-specific.** Gains transfer poorly from one balance task to another
  (Kümmel 2016), so a programme has to contain the tasks that matter: standing on one leg,
  walking narrow, stepping fast, turning the head, thinking about something else. The two
  ladders here cover those.
- **Dose in healthy older adults**: the best results came from 11–12 weeks, 3 sessions a
  week, 31–45 min per session (Lesinski 2015a); young adults respond to similar doses
  (Lesinski 2015b). Short daily bouts add up to the same minutes with better adherence,
  which is why §3 counts bouts from 2 minutes.
- **One-leg stance is a vital sign.** In 1,702 adults aged 51–75, failing to stand on one
  leg for 10 s roughly doubled all-cause mortality over 7 years, independent of age, sex and
  health (Araujo 2022). One-leg balance also predicts injurious falls (Vellas 1997).
  Normal values fall from about 40 s eyes-open in the 50s to under 10 s in the 80s (Springer
  2007). The §7 benchmark is this test.
- **Dual-task training** (balancing while counting or talking) improves balance under the
  conditions in which people actually fall (Silsupadol 2009). The top rungs add it.
- **In younger lifters** balance training mainly reduces ankle-sprain risk and improves
  landing mechanics (Hrysomallis 2007). The module is the same at any age; the dose and the
  rungs self-regulate.

---

## 2. The ladders

Two ladders in the `bodyweight-ladders.md` sense. **Clean** = the full hold or rep count
with no touch-down, no grab, fingertips hovering not resting, and no step taken to recover.
A touch-down ends the set; the set still happened and is logged with its seconds.

### Static ladder (S)

Every rung: **2 sets per side (or per position), rest as needed**, within arm's reach of a
wall or counter through rung 6, hands hovering.

| Rung | Position | Hold |
|---|---|---|
| S1 | Feet together, eyes open | 30 s |
| S2 | Semi-tandem (one foot half a foot-length ahead), each side | 30 s |
| S3 | Tandem (heel to toe), each foot in front | 30 s |
| S4 | **Single-leg stance**, eyes open, each side | 30 s |
| S5 | Single-leg, slow head turns (left-right, then up-down), each side | 30 s |
| S6 | Single-leg, **eyes closed**, each side | 20 s |
| S7 | Single-leg on a folded towel or cushion, eyes open, each side | 30 s |
| S8 | Single-leg on the cushion with a dual task (count back from 100 by 7s, or name animals), each side | 30 s |

### Dynamic ladder (D)

Every rung: **2 rounds**, a clear 4–5 m of floor, rest as needed.

| Rung | Drill | Dose |
|---|---|---|
| D1 | **Heel-to-toe walk** along a line, forward | 10 steps × 2 |
| D2 | Heel-to-toe walk **backward** | 10 steps × 2 |
| D3 | **Side-step and crossover** (carioca at a walk), each direction | 4 m × 2 |
| D4 | **Step and stick**: step forward onto one foot, hold 2 s, then sideways | 8/side forward, 8/side lateral |
| D5 | **Lean and catch**: lean forward, sideways or backward past the point of balance and catch yourself with one quick step, each direction | 6/direction |
| D6 | **Lateral hop and stick**, low, soft knee, hold 2 s | 6/side |
| D7 | Walking with slow head turns, then with a dual task (talk, count) | 2 × 20 steps each |
| D8 | **Figure-of-eight walk at pace** with direction changes, then D5 with a partner's unexpected nudge or cue when one is available | 2 × 1 min |

### Progression and gates

- **Advance after 3 clean bouts at the rung** (not necessarily consecutive); rungs S1–S3
  and D1–D2 after 1 clean bout, since they calibrate rather than train most users.
- **Entry rung at intake**: S4 and D3 for anyone who can already stand on one leg for 30 s
  (ask them to try, next to a counter); S1 and D1 otherwise, or on any fall history.
- **Ceiling.** S8 and D8 are the top. Beyond them progress by combining (S5 on the
  cushion, D5 with eyes-closed start), never by hold time past 30 s: the benchmark measures
  time, the training does not need to.
- **Single-leg rungs run both sides; the weaker side gets the second set first.** A side
  that is two rungs behind the other is reported in the Weekly Snapshot once.
- **Eyes-closed and cushion rungs (S6–S8) unlock only after 3 clean bouts at S5** and
  never on a `SLEEP` or `FATIGUE` day (`readiness.md`), when the fall risk of the drill
  itself is higher. D6 is a jump: it follows the knee gate of `power-and-plyometrics.md` §4
  when that module is active, and otherwise needs no open knee, ankle or foot Pain Response
  Protocol.
- **Dizziness or vertigo** mentioned during head-turn or eyes-closed rungs is not a
  readiness flag and not a pain report: those rungs stop for the day, the ladder caps at S4
  / D4 until the user says it has been looked at, and the trainer says once, in one line,
  that new dizziness is worth mentioning to a clinician. No other advice.
- **Ankle, knee, hip or foot protocol open** (any state but CLOSED): the static ladder
  continues at any pain-free rung up to S5 (standing still loads little); the dynamic ladder
  is paused and resumes one rung down when the protocol closes.
- **Layoff**: more than 14 days since the last bout → drop one rung on each ladder.
- **Setup.** Shoes or bare feet both count (bare feet add foot input; log which). Never on a
  wet floor, a rug that slides, or near stairs. A counter, wall or sturdy chair within
  reach through S6 and D5.

---

## 3. The dose

| Level | Weekly target | Typical shape | Who |
|---|---|---|---|
| **Floor** | 30 min | 5 × 6 min, or 10 × 3 min | default at intake |
| **Build** | 90 min | 3 × 20 min, or daily 10–15 | after 4 clean weeks at the floor, if the user wants it |
| **Fall-prevention** | 180 min | the trial dose (§1): daily 20–30 min, class included | on a reported fall, age 70+, or by request |

1. **A bout counts from 2 minutes.** One static rung both sides (about 2 min) while the
   kettle boils is a bout. The target is minutes a week; frequency is what the evidence
   rewards, so ten short bouts beat one long one.
2. **A standalone balance session** is the static rung at full dose, then the dynamic rung
   at full dose: about 6–8 min. "Balance today", "stability", or a `balance` reminder
   prescribes one.
3. **The leg-day warm-up line (§4)** counts as a 1-min bout.
4. **Classes and practices count**: tai chi, yoga with standing balance, slackline, dance,
   martial arts. Logged as "balance, [kind], [minutes]"; they do not advance a rung.
5. **Deload weeks: no change.** Balance work costs no recovery. `ILL` below the neck: none.
6. Minutes are never converted from anything else: a leg session, a walk or a carry does
   not feed this ledger.

---

## 4. Inside the lifting session: the warm-up line

While the module is active, every **leg-loading** session (`LEGS`, `LOWER`, `FB-A`, `FB-B`)
appends one item to the general warm-up's joint-prep round (`warmup-and-mobility.md` §2):
the current **static rung, one set per side**, about 60 s. It is part of `GENERAL`,
fixed **+60 s** in the duration estimate, never cut, and it reads in the checklist as
`Balance: [position] (S[rung]) — [hold]/side`. Push, pull and upper days carry nothing.

Nothing else inside a session changes. The module does not add exercises to the sheet.
It does, however, check one thing at the Weekly Snapshot: **while active, the week should
carry at least one unilateral lower-body lift** (split squat, lunge, step-up, single-leg
RDL, single-leg squat ladder step) among the main lifts and accessories. If it does not,
the Snapshot says so in one line and the next Accessory Rotation boundary
(`sbs-progression-rules.md` §6) proposes one. No sheet is changed mid-block for it.

---

## 5. Placement

Any time, any day. Balance work is low-cost and is best **fresh**, so before lifting (the
§4 line) or on its own, not after HIIT. A standalone session the day before legs is fine.
It never counts toward the weekly cardio cap, is never the HIIT slot, never a rotation
day, and never a miss.

---

## 6. Rhythm: the weekly tally

A rolling 7-day tally in `training-state.md`, printed in the coaching view whenever a
balance line or section prints:

```
Balance week (last 7 days): 18/30 min · 4 bouts · S4 (clean 2/3) · D3 (clean 1/3) · last 2026-10-24
```

| Item | Minimum (maintain) | Target (build) |
|---|---|---|
| Minutes | half the level's target | the level's target |
| Bouts | 2 / week | 4+ / week |

- **Nudge rule.** Below the minimum on either line → one line in Session Notes ("Balance:
  8 of 30 min this week, 1 bout — minimum is 15 and 2"). Once per session, never repeated.
- **Reminders.** `kind: "balance"` in `reminders.md` §2, opt-in like every reminder. The
  natural one is an **anchor** ("While the kettle boils / brushing teeth: S4, 30 s each
  side"), daily, edited in the same commit as any rung change (`reminders.md` §1
  principle 4).

---

## 7. Benchmark (every 8 weeks)

Taken fresh, before any lifting, shoes off, next to a counter:

1. **Single-leg stance, eyes open**: best of 3 per side, stopped at 60 s. Arms free, hands
   not touching. Record both sides. **Under 10 s on either side** is reported in the Weekly
   Snapshot with the Araujo 2022 line and nothing else (not medical advice; the module's
   own response is to keep going).
2. **Four-stage balance test** (CDC STEADI): feet together, semi-tandem, tandem, single-leg,
   10 s each, pass or fail per stage. Record the highest stage held.
3. **Timed Up and Go** (optional, needs a chair and 3 m): stand, walk 3 m, turn, return,
   sit. Over 12 s is a recognised fall-risk marker (Shumway-Cook 2000) and is reported once.

Record date and results in state. A benchmark that falls more than 25% from the last with
no layoff, flag or protocol in between is a Snapshot line and a question, not a rung
change. The `state:benchmark` reminder kind covers this benchmark. While the scorecard in
`benchmarks.md` is active, its due date and table own these three tests; the protocol here
is unchanged.

---

## 8. Output, reporting and state

**Coaching view.** On a leg-loading session, the general warm-up's joint-prep line gains
`· Balance: single-leg stance (S4) 30 s/side` and the Session Notes carry the tally line
once. A standalone session uses the quick-session header style (`quick-sessions.md` §6):

```
## [Day] — Balance (7 min)
Balance week (last 7 days): [min]/[target] · [bouts] bouts

### Session
- Static S[rung]: [position] — 2 × [hold]/side, hands hovering, counter in reach
- Dynamic D[rung]: [drill] — [dose]
  > [one line: rung status / clean-bout count / gate]

### Session Notes
- Not a rotation day. Next lifting day due: [day type].
```

**Checklist.** In a lifting session the line sits inside `GENERAL`, after the joint-prep
items. A standalone session is one `BALANCE` block, one line per set, hold or count in the
last field:

```
BALANCE
Single-leg stance (S4) — Set 1 — 30 s/side
Single-leg stance (S4) — Set 2 — 30 s/side

Side-step and crossover (D3) — Round 1 — 4 m each way
Side-step and crossover (D3) — Round 2 — 4 m each way
```

**Reporting.** Unchanged lines = clean at the prescribed hold or count. A number of seconds
("18 s left") = the hold achieved, not clean; "touched" / "grabbed" / "stepped" = not
clean; neither is a miss. A deleted or `x` line = not performed, not a miss. "Dizzy" routes
to the §2 dizziness rule; any joint word routes to the Pain Response Protocol. Natural
language ("did my stance bouts twice today") logs the bouts with their date and the rung
in state.

**State** (`training-state.md`, `## Balance Module (OPTIONAL)`; until the user opts in:
`Rules: system/balance.md. Not started.`):

```
## Balance Module (OPTIONAL)
Rules: `system/balance.md`. Started 2026-10-26. Level: Floor (30 min/week).
Static: S4 (single-leg stance) · clean bouts at rung: 2/3 · weaker side: left
Dynamic: D3 (side-step and crossover) · clean bouts at rung: 1/3 · paused: no
Rolling 7 days: 18 / 30 min · 4 bouts · last: 2026-10-24 (S4 clean, D3 clean)
Benchmark: SLS R 41 s / L 28 s · 4-stage: 4 · TUG 7.9 s (2026-10-20) · next due 2026-12-15
Bout log: 2026-10-24 S4 + D3, 7 min · 2026-10-23 S4 warm-up line, 1 min · …
```

**Weekly Snapshot** adds one line: minutes vs target, bouts, rung changes, the unilateral
lift check (§4), a side two rungs behind, and the benchmark when due.

---

## 9. What this module never does

- Never overrides an injury exclusion, a Pain Response Protocol or a time limit.
- Never changes the rotation, block, rep windows, RIR ramp, rest or any lift's progression;
  the §4 unilateral check only proposes, at a boundary, through the existing rotation rule.
- Never counts a hold or drill toward §11 weekly volume or the cardio cap.
- Never prescribes an eyes-closed or unstable-surface rung before S5 is clean, on a flagged
  day, or without a counter in reach.
- Never gives medical advice beyond the two one-line pointers in §2 and §7.
- Never logs a bout that was not reported.

**Session-end review hooks** (per `operating-protocol.md` §6): flag for review if the user
skips balance work for 3 consecutive weeks (ask whether to keep offering it or shrink it to
the warm-up line only), or a rung produces a touch-down on 5 consecutive bouts (ask whether
to hold a rung lower for a block).

---

## 10. References

Falls and exercise
- Sherrington C, Fairhall NJ, Wallbank GK, et al. 2019. Exercise for preventing falls in
  older people living in the community. *Cochrane Database Syst Rev* 1:CD012424.
  doi:10.1002/14651858.CD012424.pub2
- Sherrington C, Michaleff ZA, Fairhall N, et al. 2017. Exercise to prevent falls in older
  adults: an updated systematic review and meta-analysis. *Br J Sports Med*
  51(24):1750–1758. doi:10.1136/bjsports-2016-096547
- Okubo Y, Schoene D, Lord SR. 2017. Step training improves reaction time, gait and balance
  and reduces falls in older people: a systematic review and meta-analysis. *Br J Sports
  Med* 51(7):586–593. doi:10.1136/bjsports-2015-095452
- Mansfield A, Wong JS, Bryce J, Knorr S, Patterson KK. 2015. Does perturbation-based
  balance training prevent falls? Systematic review and meta-analysis of preliminary
  randomized controlled trials. *Phys Ther* 95(5):700–709. doi:10.2522/ptj.20140090
- Li F, Harmer P, Fisher KJ, et al. 2005. Tai Chi and fall reductions in older adults: a
  randomized controlled trial. *J Gerontol A Biol Sci Med Sci* 60(2):187–194.
  doi:10.1093/gerona/60.2.187

Dose and specificity
- Lesinski M, Hortobágyi T, Muehlbauer T, Gollhofer A, Granacher U. 2015a. Effects of
  balance training on balance performance in healthy older adults: a systematic review and
  meta-analysis. *Sports Med* 45(12):1721–1738. doi:10.1007/s40279-015-0375-y
- Lesinski M, Hortobágyi T, Muehlbauer T, Gollhofer A, Granacher U. 2015b. Dose-response
  relationships of balance training in healthy young adults: a systematic review and
  meta-analysis. *Sports Med* 45(4):557–576. doi:10.1007/s40279-014-0284-5
- Kümmel J, Kramer A, Giboin LS, Gruber M. 2016. Specificity of balance training in healthy
  individuals: a systematic review and meta-analysis. *Sports Med* 46(9):1261–1271.
  doi:10.1007/s40279-016-0515-z
- Silsupadol P, Shumway-Cook A, Lugade V, et al. 2009. Effects of single-task versus
  dual-task training on balance performance in older adults: a double-blind, randomized
  controlled trial. *Arch Phys Med Rehabil* 90(3):381–387. doi:10.1016/j.apmr.2008.09.559
- Hrysomallis C. 2007. Relationship between balance ability, training and sports injury
  risk. *Sports Med* 37(6):547–556. doi:10.2165/00007256-200737060-00007

Tests and norms
- Araujo CG, de Souza e Silva CG, Laukkanen JA, et al. 2022. Successful 10-second one-legged
  stance performance predicts survival in middle-aged and older individuals. *Br J Sports
  Med* 56(17):975–980. doi:10.1136/bjsports-2021-105360
- Vellas BJ, Wayne SJ, Romero L, Baumgartner RN, Rubenstein LZ, Garry PJ. 1997. One-leg
  balance is an important predictor of injurious falls in older persons. *J Am Geriatr
  Soc* 45(6):735–738. doi:10.1111/j.1532-5415.1997.tb01479.x
- Springer BA, Marin R, Cyhan T, Roberts H, Gill NW. 2007. Normative values for the
  unipedal stance test with eyes open and closed. *J Geriatr Phys Ther* 30(1):8–15.
  doi:10.1519/00139143-200704000-00003
- Shumway-Cook A, Brauer S, Woollacott M. 2000. Predicting the probability for falls in
  community-dwelling older adults using the Timed Up & Go Test. *Phys Ther* 80(9):896–903.
  doi:10.1093/ptj/80.9.896
- Centers for Disease Control and Prevention. 2017. STEADI: 4-Stage Balance Test and Timed
  Up & Go. cdc.gov/steadi
