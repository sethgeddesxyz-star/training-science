# Aerobic Base — easy aerobic work as a tracked weekly dose (added 2026-10-25, user request)

`aerobic-heart-rate.md` says how hard easy aerobic work should be (MAF 180, Zone 2). Until
this file nothing said how much, when, or where it was logged, and `conditioning-hiit.md` §2
explicitly left incline-walk zone-2 work outside everything. This file makes easy aerobic
work a **weekly minutes target with its own log line**, not a day type: it never sits in the
rotation, never advances the block, and an unmet week is never a miss. HIIT builds the top
of the aerobic engine; this builds the floor under it and is the part most people can do
most days.

Read it when the opener asks for easy cardio by any name ("zone 2", "easy ride", "long
walk", "40 min on the bike, easy", "aerobic"), when `conditioning-hiit.md` §6 swaps a HIIT
for easy work, at intake to set the target, and for the Weekly Snapshot line.

---

## 1. The dose

| Level | Weekly target | Typical shape | Who |
|---|---|---|---|
| **Floor** | 90 min | 3 × 30 min, or 2 × 45 | default at intake |
| **Build** | 150 min | 3 × 45–50, or 2 × 60 + 1 × 30 | after 4 clean weeks at the floor, if the user wants it |
| **Hold** | 60 min | 2 × 30 | deload weeks, `ILL` above the neck, or a week the user declares "lifting only" |

1. **A session counts from 20 minutes.** Under 20 min it is a walk-break or stair snack
   (`quick-sessions.md` §3.7, §3.8) and logs there. There is no upper limit on a session, but
   the target is minutes per week, and a single 150-min outing does not buy a week off: the
   point is frequency.
2. **Intensity is the `aerobic-heart-rate.md` ceiling**: at or under MAF (180 − age, with its
   adjustments), or the talk test (full sentences, would rather not sing). Over the ceiling
   for more than a few minutes and the session is logged as "aerobic, over ceiling" and still
   counts, but the Session Notes line says so once. It never counts as HIIT.
3. **Any modality the joints allow**: walk, incline walk, hike, bike, rower, swim, easy jog,
   ruck. The `conditioning-hiit.md` §4 joint notes apply (knee: bike or incline before flat
   running). Modality is logged because pace numbers are modality-specific.
4. **Progress the target, not the pace.** Weeks are judged on minutes. Pace at the ceiling
   HR rises on its own over months; the Weekly Snapshot reports it when the user logs it,
   and the engine never prescribes a pace.
5. **Steps are not minutes.** A step count the user reports is noted, not converted. (It is
   good evidence for health, §5, but it is not this dose.)

---

## 2. Placement

Easy aerobic work is low-interference by design, so placement is loose:

1. **Any day, including lifting days.** After a lifting session is fine (lift first). Before
   a lifting session only if at least 6 h separate them, otherwise after.
2. **The day before legs is fine.** This is the one way it differs from HIIT: at ceiling
   intensity there is no next-day cost worth programming around (§5).
3. **It is not a HIIT substitute**, except where `conditioning-hiit.md` §6 swaps a HIIT for
   "20 min of easy zone 2" on a fatigue signal; that swap is logged here as 20 min and HIIT
   stays due.
4. **It does not count toward the HIIT weekly cap** (3 in 7 days), and HIIT minutes do not
   count toward this target. The two are separate ledgers.
5. **Deload weeks** drop to the Hold level automatically; the user may do more.

---

## 3. Prescribing a session

When the opener asks for one, or the user asks what to do on a rest day, the coaching view
is three lines and the checklist is one block. Nothing else prints: no prehab block (a
5-min easy start is the warmup), no bone section, no working sets.

```
## [Day] — [Location] (Aerobic — easy)
Block: [from the lifting block] | Aerobic this week: [done]/[target] min

### Session
- [Modality]: [minutes] min at or under [MAF ceiling] bpm (talk test: full sentences)
  > First 5 min easy, last 3 min easy. If HR drifts over the ceiling, slow down; do not stop.
  > Week so far: [n] min of [target]. After today: [n + minutes].

### Session Notes
- Estimated duration: [minutes + 5] min
- Not a rotation day. Next lifting day due: [day type].
```

```
[YYYY-MM-DD] — [Location] (Aerobic — easy)

AEROBIC
[Modality] — [minutes] min — ≤ [ceiling] bpm
```

The minutes prescribed are whatever the user asked for, or the smallest session that keeps
the week on target (target minus done, divided by the sessions left that the user's week
plausibly holds, rounded to 5 min, minimum 20, default 30).

---

## 4. Reporting and tracking

- **Checklist line unchanged** = done at the prescribed minutes under the ceiling. A changed
  number = actual minutes. Appended HR or pace = logged as data. "Over" or an HR above the
  ceiling = "over ceiling", still counts.
- **Natural language** ("walked 40 min at lunch", "easy 30 on the bike yesterday") logs the
  same way with its date. A session under 20 min is routed to the quick-session log.
- `training-state.md` keeps:

```
## Aerobic Base
Rules: `system/aerobic-base.md`. Level: Floor (90 min/week; set 2026-10-25).
Ceiling: MAF 140 bpm (180 − 40, no adjustment). Preferred modality: incline walk.
Rolling 7 days: 60 / 90 min · last: 2026-10-23 30 min bike.
Weeks at or over target (consecutive): 2
```

- **Weekly Snapshot** adds one line: minutes vs target, sessions, and consecutive weeks on
  target. At 4 consecutive weeks on the Floor it asks once whether to move to Build; the
  user says yes or it stays. An under-target week is reported in the same line and nothing
  else happens: no counter, no deload, no nag.
- **Reminders.** `kind: "aerobic"` in `reminders.md` §2, opt-in like every reminder: "Aerobic
  this week: 30/90 min, 2 days left" on the user's stated rest days.

---

## 5. Why (evidence, brief)

- **Easy aerobic volume is where most of the health return is.** Leisure-time activity and
  all-cause mortality follow a dose-response curve that is steepest at the low end and
  flattens around 3–5 × the guideline minimum (Arem 2015, pooled cohorts, n = 661,137).
  Device-measured data say the same for light and moderate activity (Ekelund 2019). The WHO
  guideline is 150–300 min/week moderate (Bull 2020); the Floor here is the bottom of that
  range split across the week, because the engine already provides HIIT and lifting on top.
- **Zone 2 work trains the fat-oxidation and lactate-clearance side of the engine** that
  HIIT does not fully reach: mitochondrial density and function in slow-twitch fibres,
  measured as higher fat oxidation and lower lactate at a given output (San-Millán & Brooks
  2018). Endurance athletes at every level spend about 80% of training time at this
  intensity, and the polarised distribution (mostly easy, some very hard, little in between)
  outperforms threshold-heavy training in controlled comparisons (Seiler 2010; Stöggl &
  Sperlich 2014). HIIT supplies the 20%; this file supplies the 80%.
- **Interference is intensity- and duration-dependent.** The concurrent-training cost to
  lower-body strength grows with endurance frequency and session length and is largest for
  high-intensity or long running (Wilson 2012); easy cycling or walking at these durations
  sits at the low end of every moderator. That is why §2 allows it next to leg days and
  only asks for lift-first on a shared day.
- **Steps matter but are a different measure.** Daily steps show the same dose-response
  with mortality, flattening around 6,000–8,000 for adults over 60 and 8,000–10,000 below
  (Paluch 2022), so a reported step count is worth noting. Minutes under a heart-rate
  ceiling are what this module can prescribe and progress; steps are not.

**References**
1. Arem H, Moore SC, Patel A, et al. 2015. Leisure time physical activity and mortality: a
   detailed pooled analysis of the dose-response relationship. *JAMA Intern Med*
   175(6):959–967. doi:10.1001/jamainternmed.2015.0533
2. Ekelund U, Tarp J, Steene-Johannessen J, et al. 2019. Dose-response associations between
   accelerometry measured physical activity and sedentary time and all cause mortality:
   systematic review and harmonised meta-analysis. *BMJ* 366:l4570. doi:10.1136/bmj.l4570
3. Bull FC, Al-Ansari SS, Biddle S, et al. 2020. World Health Organization 2020 guidelines on
   physical activity and sedentary behaviour. *Br J Sports Med* 54(24):1451–1462.
   doi:10.1136/bjsports-2020-102955
4. San-Millán I, Brooks GA. 2018. Assessment of metabolic flexibility by means of measuring
   blood lactate, fat, and carbohydrate oxidation responses to exercise in professional
   endurance athletes and less-fit individuals. *Sports Med* 48(2):467–479.
   doi:10.1007/s40279-017-0751-x
5. Seiler S. 2010. What is best practice for training intensity and duration distribution in
   endurance athletes? *Int J Sports Physiol Perform* 5(3):276–291. doi:10.1123/ijspp.5.3.276
6. Stöggl T, Sperlich B. 2014. Polarized training has greater impact on key endurance
   variables than threshold, high intensity, or high volume training. *Front Physiol* 5:33.
   doi:10.3389/fphys.2014.00033
7. Paluch AE, Bajpai S, Bassett DR, et al. 2022. Daily steps and all-cause mortality: a
   meta-analysis of 15 international cohorts. *Lancet Public Health* 7(3):e219–e228.
   doi:10.1016/S2468-2667(21)00302-9
8. Wilson 2012: see `conditioning-hiit.md` §10.
