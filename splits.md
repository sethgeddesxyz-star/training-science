# Splits and Rotation — full body, upper/lower, push/pull/legs (added 2026-10-25, user request)

`operating-protocol.md` §2 picks a split from days per week, but until this file every
day-type rule in the system (HIIT placement, prehab blocks, McGill clusters, Bone Doubles,
carries, the modality floor, deload coverage) was written against one rotation,
PUSH → LEGS → PULL → HIIT. A user on 2–4 days a week had a split name and nothing behind it.
This file defines the three splits, their day types and rotations, and how every per-day-type
rule maps onto each. Read it at intake, whenever the user's days per week change, and when an
opener names a day type that does not exist in the current split.

---

## 1. Choosing the split

| Days / week | Split | Day types | Rotation (lifting) |
|---|---|---|---|
| 2–3 | Full body | `FB-A`, `FB-B` | FB-A → FB-B |
| 4 | Upper / lower | `UPPER`, `LOWER` | UPPER → LOWER |
| 5+ | Push / pull / legs | `PUSH`, `PULL`, `LEGS` | PUSH → LEGS → PULL |

1. Days per week means **lifting** days the user can actually keep, stated at intake. HIIT
   and quick sessions do not count toward it.
2. The user may override the table ("I want upper/lower on 3 days"). Record the override in
   `training-state.md`; the day-type rules below follow the split, not the day count.
3. **Changing split.** When days per week change, the split changes at the **next block
   boundary** (decided in the deload). Mid-block only when the schedule forces it, and then
   the current block is finished on the new rotation without restarting. Per-exercise state
   (loads, rep windows, e1RM, accessory age in blocks) belongs to the exercise, not the day
   type, and carries over unchanged. Only the day-type assignments are remapped, by pattern,
   per §2.
4. The current split, its rotation order and the next day type due are written in
   `training-state.md` under *Split & Rotation*. The rotation advances by one on every
   performed lifting session and never on a quick session (`quick-sessions.md`) or a HIIT
   session.

---

## 2. What each day type contains

Pattern requirements come from `exercise-library.md` (Exercise Selection Rules). This table
adds the A/B alternation that full body needs and says where the fixed add-ons go.

| Day type | Main patterns | Accessories | McGill clusters (`mcgill-pullups.md`) | Bone Doubles (`bone-loading.md` §2) | Carry (`exercise-library.md` rule 8) |
|---|---|---|---|---|---|
| `FB-A` | h_push, h_pull, **squat**, **v_pull** | 1–2 | yes (Strength blocks; first working exercise) | no | no |
| `FB-B` | h_push, h_pull, **hinge**, **v_push** | 1–2 | no | yes (gym, Hypertrophy blocks) | yes |
| `UPPER` | h_push, h_pull, v_push, v_pull | 1–2 arm | yes | no | no |
| `LOWER` | squat, hinge | 1–2 (calves, core, leg isolation) | no | yes | yes |
| `PUSH` | h_push, v_push | triceps | no | no | no |
| `PULL` | h_pull, v_pull | biceps | yes | no | yes (or LEGS) |
| `LEGS` | squat, hinge | 2–3 leg | no | yes | yes (or PULL) |

1. **Full body alternates, not repeats.** `FB-A` and `FB-B` are distinct day types so that
   squat and hinge, and vertical pull and vertical push, each appear every rotation. A main
   lift lives on one of them and keeps its own progression; it is not performed on both.
2. **Upper and lower are single day types.** Both weekly `UPPER` sessions carry the same
   prehab block and the same accessory list; the §3 variety rules and the accessory
   turnover cap treat "UPPER" as one list. A user who wants an A/B accessory alternation
   may have one; it is then two accessory lists under one day type, each on the normal
   rotation cadence.
3. **Volume still binds.** `sbs-progression-rules.md` §11 (10–20 hard sets per muscle per
   week, max 10 per session, every muscle at least twice a week, pull sessions at least
   twice a week) is a check on the whole week, whatever the split. Full body on 2 days meets
   the frequency floor only because every session trains everything; it meets the set floor
   only with the maximum per-session count, so on 2 days the engine fills accessories to the
   §11 session cap before it adds anything optional.
4. **Carries** default to the day that holds the hinge (`FB-B`, `LOWER`, or `PULL`/`LEGS` as
   the user prefers), one per week.

---

## 3. HIIT placement by split

`conditioning-hiit.md` §2 is written for push/pull/legs and stays the rule there. The
principle it encodes is: **HIIT lands as far from a leg-loading session as the rotation
allows, never the day before one, and never stacked after one.** Per split:

| Split | HIIT placement | Stacking allowed after | "Due" means |
|---|---|---|---|
| Push/pull/legs | A rotation slot: PUSH → LEGS → PULL → HIIT | PULL | next slot in the rotation (`conditioning-hiit.md` §2, unchanged) |
| Upper/lower | Not a rotation slot. Once per rotation cycle (UPPER → LOWER → UPPER → LOWER), on a non-lifting day, or stacked | UPPER | one HIIT per completed cycle; carried as "HIIT due" from the second LOWER of the cycle until performed |
| Full body | Not a rotation slot. Once per calendar week on a non-lifting day | nothing | one HIIT per calendar week; carried as "HIIT due" from the week's first lifting session until performed |

1. **Standalone day rule (upper/lower and full body).** A standalone HIIT runs at least 24 h
   after the last lower-body-loading session (`LOWER`, `FB-A`, `FB-B`) and, where the
   schedule offers such a day, at least 24 h before the next one. On a schedule with no such
   day (for example full body Mon / Wed / Fri with the weekend unavailable), the 24-h-before
   condition is waived and the HIIT runs on the day after a lifting session instead;
   `conditioning-hiit.md` §6 ("the next day is legs") then does not fire, because the
   placement was the best the schedule allowed.
2. **Stacking (upper/lower).** HIIT may be stacked after either `UPPER` session, lift first,
   HIIT after, and that satisfies the cycle's HIIT. Never after `LOWER` or any full-body
   session: both load the legs.
3. **Unperformed HIIT is not a miss.** When the cycle or week ends with HIIT still due, the
   note is dropped and a new "due" opens with the next cycle or week. The format cycle
   (A → B → A → C) advances only on performed sessions.
4. **Bonus HIIT and the weekly cap** (`conditioning-hiit.md` §2) apply unchanged: at most 3
   HIIT in 7 days, and a bonus session needs 24 h after the last leg-loading session.
5. **Openers.** "HIIT" / "intervals" / "cardio day" prescribe HIIT in any split, with the
   placement rules above applied as a check, not a veto: if today is the day after a lower
   session, say so in one Session Notes line and prescribe it anyway (the user's schedule
   wins over the ideal placement), unless a §6 fatigue trigger holds.

---

## 4. Mapping the per-day-type rules

Every rule elsewhere that says "per day type" or names a PPL day reads through this table.

| Rule | Push/pull/legs (as written) | Upper/lower | Full body |
|---|---|---|---|
| **Prehab blocks** (`training-state.md`, fixed per day type) | push / pull / legs blocks | `UPPER` block = every upper-limb and shoulder-girdle flag; `LOWER` block = every hip, knee, ankle flag; back and core flags on **both** | `FB-A` and `FB-B` each carry **every** flag's prehab; the block is identical on both days |
| **Deload rotation coverage** (`sbs-progression-rules.md` §6) | PUSH, LEGS, PULL each once | `UPPER` and `LOWER` each once | `FB-A` and `FB-B` each once |
| **Calendar floor** (same section) | 5 days from the first deload session | unchanged | unchanged: on 2 days a week the floor is met before coverage is, so coverage decides |
| **Accessory turnover cap** (§6 Accessory Rotation rule 6, one third to one half of a day type's accessories per boundary) | per PPL day | per `UPPER` / `LOWER` list | per `FB-A` / `FB-B` list; with only 1–2 accessories per day the cap is **one** |
| **Modality coverage floor** (`modality-rotation.md` §2 rule 1: 2 families per day type, 3 per program) | per PPL day | per `UPPER` / `LOWER` | a day with a single accessory is exempt from the per-day floor; the program floor of 3 families still holds |
| **Deload variety session** (`modality-rotation.md` §2 rule 4) | counts for the day type whose patterns it covers | an `UPPER` session needs h_push + v_push + h_pull + v_pull; `LOWER` needs squat + hinge | counts for `FB-A` or `FB-B` only if it covers that day's four main patterns |
| **McGill clusters** (`mcgill-pullups.md`) | first working exercise on PULL | first working exercise on `UPPER`, both sessions that week | first working exercise on `FB-A` |
| **Bone Doubles** (`bone-loading.md` §2) | gym LEGS | gym `LOWER` | gym `FB-B` |
| **Bone tally and impact ladder** (`bone-loading.md` §5) | unchanged: it sits outside the session | unchanged | unchanged |
| **Time-limit cut order** (`operating-protocol.md` §2) | from the end of the accessory order | unchanged | unchanged; the two protected working exercises are the first two main patterns on the sheet |
| **Reminder `state:train`** (`reminders.md` §2) | "Next up: [PPL day]" | "Next up: UPPER / LOWER" | "Next up: FB-A / FB-B" |
| **Weekly Snapshot** (`operating-protocol.md` §5) | families per PPL day | per `UPPER` / `LOWER` | per `FB-A` / `FB-B` |

---

## 5. Openers that name the wrong day type

| Opener says | On upper/lower | On full body |
|---|---|---|
| "push day" / "pull day" | prescribe `UPPER`; one Session Notes line: "Upper/lower split: this is your upper day." | prescribe the next full-body day due; same one-line note |
| "leg day" / "legs" | prescribe `LOWER` | prescribe the next full-body day due, with the leg pattern it already carries |
| "upper" / "lower" on PPL | prescribe the next PPL day due, with the note | — |
| "full body" on PPL or upper/lower | treat as a request for the deload variety session format only if the user is in a deload week (`modality-rotation.md` §2 rule 4); otherwise prescribe the day due and note it | — |

A named day never skips the rotation silently. If the user insists ("no, I want push only
today"), prescribe it as a one-off under the current split's day-type rules (PUSH as defined
in §2), do not advance the rotation, and say so in one line.

---

## 6. Tracking

`training-state.md`, *Split & Rotation*:

```
- **Current split**: Upper/lower (4 days/week; set at intake 2026-10-25)
- **Rotation order**: UPPER → LOWER → UPPER → LOWER · HIIT: once per cycle, standalone or stacked after UPPER
- **Next due**: LOWER (cycle 2 of 2) · HIIT due: yes, since 2026-10-23
- **Last session date**: 2026-10-23
```

The template carries the same four lines with placeholders.

---

## 7. Why (evidence, brief)

- **Frequency matters less than weekly volume.** When weekly sets are equated, training a
  muscle 1, 2 or 3+ times a week produces similar hypertrophy, with a small edge for at least
  twice (Schoenfeld 2016, 2019 meta-analyses). Strength shows the same pattern
  (Grgic 2018). A direct split-versus-full-body comparison at equal volume found no
  difference in strength or size (Evangelista 2021). So the split is a scheduling decision,
  chosen by the days the user can keep, and §11's volume floor is what the engine protects.
  That is why the table in §1 is driven by days per week and why §2 rule 3 fills full-body
  sessions to the per-session cap first.
- **Full body on 2 days still meets the twice-a-week floor** only because every session
  trains everything, which is the reason `FB-A` / `FB-B` alternate patterns rather than
  drop them.
- **Interference is a same-day and next-day effect on the legs.** Concurrent endurance work
  blunts lower-body strength and power most when it is run close to, or in the same session
  as, leg training; hypertrophy is largely spared (Wilson 2012; Schumann 2022; Petré 2021,
  all already cited in `conditioning-hiit.md` §10). Hence the one principle behind §3: distance
  from leg-loading sessions. In upper/lower and full-body splits every other session, or every
  session, loads the legs, so HIIT cannot be a rotation slot without landing next to one; it
  becomes a once-per-cycle or once-per-week standalone, stacked only after an upper session.
- **The schedule beats the ideal.** A user training full body on Mon / Wed / Fri has no
  "24 h clear on both sides" day. The rule waives the lesser condition rather than silently
  dropping HIIT every week, because an unperformed HIIT is the larger cost
  (`conditioning-hiit.md` §1).

**References**
1. Schoenfeld BJ, Ogborn D, Krieger JW. 2016. Effects of resistance training frequency on
   measures of muscle hypertrophy: a systematic review and meta-analysis. *Sports Med*
   46(11):1689–1697. doi:10.1007/s40279-016-0543-8
2. Schoenfeld BJ, Grgic J, Krieger J. 2019. How many times per week should a muscle be
   trained to maximize muscle hypertrophy? A systematic review and meta-analysis of studies
   examining the effects of resistance training frequency. *J Sports Sci* 37(11):1286–1295.
   doi:10.1080/02640414.2018.1555906
3. Grgic J, Schoenfeld BJ, Davies TB, Lazinica B, Krieger JW, Pedisic Z. 2018. Effect of
   resistance training frequency on gains in muscular strength: a systematic review and
   meta-analysis. *Sports Med* 48(5):1207–1220. doi:10.1007/s40279-018-0872-x
4. Evangelista AL, Braz TV, La Scala Teixeira CV, et al. 2021. Split or full-body workout
   routine: which is best to increase muscle strength and hypertrophy? *Einstein (São Paulo)*
   19:eAO5781. doi:10.31744/einstein_journal/2021AO5781
5. Wilson 2012, Schumann 2022, Petré 2021: see `conditioning-hiit.md` §10.
