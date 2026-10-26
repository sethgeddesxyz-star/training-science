# Readiness — what the opener says about today, and what the engine does with it (added 2026-10-25, user request)

Until this file, nothing a user said about sleep, soreness, stress or illness changed the
session in front of them. Sleep appeared only as a HIIT cut (`conditioning-hiit.md` §6) and
fatigue only after the fact, as a reactive-deload trigger (`sbs-progression-rules.md` §8).
This file adds a session-start adjustment that is **by exception, same-day only, and never a
questionnaire**: the user volunteers a flag in the opener or not at all; the engine never
asks; persistent state never changes because of one flag.

Read it whenever the opener, or anything the user says before the prescription, carries a
readiness word (§1). Otherwise it does not apply and is not read.

---

## 1. Flags

The engine never asks "how did you sleep". It reads the opener. These words, or anything
plainly meaning them, raise a flag:

| Flag | Opener says, for example |
|---|---|
| `SLEEP` | "slept badly", "4 hours", "up all night", "jet-lagged" |
| `FATIGUE` | "wiped", "exhausted", "stressed out", "long day", "no energy" |
| `SORE` | "still sore from Tuesday", "legs are wrecked", "DOMS" (a muscle, not a joint) |
| `ILL` | "getting a cold", "sick", "fever", "stomach bug", "chest cough" |

A joint, a sharp or stabbing sensation, or anything the user calls pain is **not** a
readiness flag: it goes to the Pain Response Protocol in `injury-protocols.md`, which wins.
"Tired but fine" and "a bit sore, nothing bad" are not flags either; the user has already
said so. When in doubt, no flag. The dose below is small on purpose, so an unflagged
mediocre day costs little.

---

## 2. What each flag does today

All adjustments are **today only**. `training-state.md` loads, rep windows, e1RM and
counters are not edited by a flag. The adjusted session is logged as performed with the
flag noted, and the §3 decision tree runs on what was actually done, as always.

| Flag | Lifting session | HIIT session |
|---|---|---|
| `SLEEP` or `FATIGUE` | **Loads −5%** on every working set (rounded down to the increment; a load that cannot drop one increment stays and drops its rep target to the window floor instead). **No rep-out, no AMRAP, no maintenance set.** RIR target +1. Rest unchanged. Prehab, warmup ramp unchanged | Swap for 20 min easy zone 2 or skip (`conditioning-hiit.md` §6, as written). HIIT stays due |
| `SORE` (muscle on today's sheet) | Warmup ramp gets a fourth set at 40% × 8 for the lifts that use that muscle. If the user says *very* sore: also drop the maintenance set and Bone Doubles on those lifts; working sets unchanged | Run it if the modality spares the muscle (bike with sore pecs); otherwise swap per §6 |
| `SORE` (muscle not on today's sheet) | No change. One line in Session Notes acknowledging it | No change |
| `ILL`, above the neck only (runny nose, sore throat, no fever) | User's choice, said in one line: skip, or run the day at **deload parameters** (`sbs-progression-rules.md` §6 Deload Week: 50% sets, 65% load, RIR ≥ 4, no AMRAP). A deload-parameter session advances the rotation and is logged; it opens no e1RM thread and advances nothing else | Skip. HIIT stays due |
| `ILL`, below the neck or fever (chest, gut, aches, temperature) | **No session.** Say so in one line and stop. Not a miss; `lastSessionDate` does not move, so missed-time decay (§9) runs on the normal calendar if the illness is long | Skip |

Any flag also drops the day's power work, primer included, while the Power Module is active
(`power-and-plyometrics.md` §5; added 2026-10-26). `SLEEP` or `FATIGUE` caps balance work
at eyes-open, firm-floor rungs for the day (`balance.md` §2); the warm-up line stays. Two flags at once: apply the larger
adjustment, not both. A flag plus a pain report: the
Pain Response Protocol governs that exercise, the flag governs the rest.

**Output.** A flagged session adds one line to Session Notes, before the duration line:
`Readiness: SLEEP — loads −5% today, no maintenance sets; your state is unchanged.` The
checklist carries the adjusted loads with no annotation; the log entry carries the flag.

**§13 same-day overshoot still applies** on top: if a flagged session is still coming in
"hard" everywhere, §13 cuts the remaining loads a further 5% for the day.

---

## 3. When flags accumulate

Readiness flags are kept as a short rolling list in `training-state.md` under *Current
Block*: `Readiness flags (last 4 sessions): SLEEP 10-22 · — · FATIGUE 10-18 · —`.

- **3 flags in the last 4 lifting sessions** (any kind but `SORE`) is a 4th reactive-deload
  trigger, added to `sbs-progression-rules.md` §8. The deload opens at the next session
  exactly as for the other triggers.
- Below that threshold flags are just noted. The Weekly Snapshot (`operating-protocol.md`
  §5) lists the count when it is 2 or more.
- `ILL` with no session does not add to the list (there was no session); a deload-parameter
  session under `ILL` does.

The list is the user's own words, dated, nothing more. The engine never infers a flag from
performance; a bad session with no flag is handled by the decision tree alone.

---

## 4. What this file never does

- Never asks a readiness question, a scale, or a questionnaire. By exception only.
- Never changes a stored load, window, e1RM or counter because of a flag.
- Never cuts prehab or the warmup ramp.
- Never turns a joint or pain report into a readiness flag.
- Never skips a session on its own for `SLEEP`, `FATIGUE` or `SORE`. The user trains; the
  engine makes the day cheaper.

---

## 5. Why (evidence, brief)

- **Subjective reports track training stress better than the objective markers most
  people can access.** Across 56 studies, self-reported well-being (sleep, fatigue, soreness,
  stress) responded to acute and chronic training load more sensitively and consistently
  than HRV, resting HR or blood markers (Saw 2016, systematic review). That is why the flag
  is the user's own words and why the engine does not demand a wearable.
- **Acute sleep loss costs performance, modestly and reliably.** Meta-analysis of 77
  studies: sleep loss reduced next-day exercise performance, with a larger effect for
  evening sessions and for partial sleep restriction (Craven 2022). For strength
  specifically, the effect of a single short night is small and inconsistent, while
  repeated inadequate sleep impairs strength and probably hypertrophy (Knowles 2018). Hence
  a small same-day cut (−5%, no rep-outs) rather than a skip, and the escalation to a
  deload only when flags repeat.
- **Autoregulated loading is at least as good as fixed loading**, and better when the
  day's readiness differs from the plan's assumption (Greig 2020 review; Helms 2018 RPE vs
  %1RM, matched volume). The engine already autoregulates by RIR on the report side; this
  file adds the same on the prescription side, bounded so it cannot drift state.
- **DOMS impairs force output in the sore muscle and raises injury risk if ignored**, but
  light activity on the sore muscle does no harm and may help (Cheung 2003 review). A longer
  ramp and no heavy single costs nothing; cancelling the session costs a rotation slot.
- **The neck check holds up.** Moderate exercise during a mild upper-respiratory infection
  neither lengthened nor worsened it in a randomised trial (Weidner 1998); systemic symptoms
  (fever, myalgia, chest involvement) are the standard contraindication in sports-medicine
  guidance, and the rule here defers to that line.

**References**
1. Saw AE, Main LC, Gastin PB. 2016. Monitoring the athlete training response: subjective
   self-reported measures trump commonly used objective measures: a systematic review.
   *Br J Sports Med* 50(5):281–291. doi:10.1136/bjsports-2015-094758
2. Craven J, McCartney D, Desbrow B, Sabapathy S, Bellinger P, Roberts L, Irwin C. 2022.
   Effects of acute sleep loss on physical performance: a systematic and meta-analytical
   review. *Sports Med* 52(11):2669–2690. doi:10.1007/s40279-022-01706-y
3. Knowles OE, Drinkwater EJ, Urwin CS, Lamon S, Aisbett B. 2018. Inadequate sleep and
   muscle strength: implications for resistance training. *J Sci Med Sport* 21(9):959–968.
   doi:10.1016/j.jsams.2018.01.012
4. Greig L, Stephens Hemingway BH, Aspe RR, Cooper K, Comfort P, Swinton PA. 2020.
   Autoregulation in resistance training: addressing the inconsistencies. *Sports Med*
   50(11):1873–1887. doi:10.1007/s40279-020-01330-8
5. Helms ER, Byrnes RK, Cooke DM, et al. 2018. RPE vs. percentage 1RM loading in periodized
   programs matched for sets and repetitions. *Front Physiol* 9:247.
   doi:10.3389/fphys.2018.00247
6. Cheung K, Hume PA, Maxwell L. 2003. Delayed onset muscle soreness: treatment strategies
   and performance factors. *Sports Med* 33(2):145–164. doi:10.2165/00007256-200333020-00005
7. Weidner TG, Cranston T, Schurr T, Kaminsky LA. 1998. The effect of exercise training on
   the severity and duration of a viral upper respiratory illness. *Med Sci Sports Exerc*
   30(11):1578–1583. doi:10.1097/00005768-199811000-00004
