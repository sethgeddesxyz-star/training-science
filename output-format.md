# Output Format

Every session produces **two blocks, in this order, unprompted**: coaching view, then
checklist. The checklist is never offered or skipped. Within both, sections appear in
performance order — prehab is activation before loading, never a cooldown.

---

## Block 1 — Coaching view

```
## [Day of Week] — [Location] ([Split Label])
Block: [Hypertrophy/Strength/Deload] | Week [N] of [Total]

### Prehab (if injury flags active)
- [Prehab exercise]: [sets] x [reps]

### Warmup Ramp (if compounds prescribed)
- [Exercise]: [weight] x [reps] (warmup)

### Working Sets
1. **[Exercise Name]** — [sets] x [reps] @ [weight] | Rest: [seconds]s
   > Progression note: [why this weight/rep target]
   > Last session: [what they did last time]

### Bone (optional) — any time today, ideally ≥4 h from this session
- Bone week (last 7 days): impact [n]/[target] · axial [n]/[target] · upper [n]/[target]
- Impact Rung [N] — [movement]: [dose]
- Upper Rung [N] — [movement]: [dose] (only if the upper tally is under target)
  > [one line: rung status / gate / nudge if below minimum]

### Session Notes
- Estimated duration: ~[X] min (excludes the optional Bone section)
- Today's focus: [what the block/week emphasizes]
- Effort target: RIR [N] ([easy/good/hard])
```

**Estimated duration must be COMPUTED, not asserted (added 2026-09-12, approved).** Sum,
per exercise: (sets × reps × tempo seconds) + (sets − 1) × rest + 60s setup/transition.
Add the prehab block at 60s per item per round plus 30s transitions, and the warmup ramp
at its own rest values. Then add a **15% overhead margin** before comparing against the
user's stated limit. If the total exceeds the limit, cut from the end of the accessory
order until it fits — cutting is the §2 mechanism, and a sheet that only fits without
margin is a sheet that will not get finished. Two consecutive home leg days (2026-09-08,
2026-09-12) ended with unperformed accessories after being built to fit the stated limit;
that is the failure this rule exists to prevent.

---

**HIIT days** use the coaching and checklist variants in `system/conditioning-hiit.md` §9
(warm-up / main set / cool-down in place of prehab / warmup ramp / working sets).

---

## Block 2 — Checklist view

A worksheet the user copies into a notes app, annotates, and pastes back. Fenced code
block. No progression notes, no commentary.

- **One line per set.** "3 x 10" becomes three lines.
- **Every line is self-contained** — exercise, set number, load, rep target. The user
  must never need the coaching view to know what to do.
- Fields separated by ` — `. Field order identical every time.
- Unilateral work stays on one line with `/side` or `/leg`. Never split into L and R.
- Prehab and warmup lines included, above working sets, in performance order.
- **Rest time appears once per exercise**, on its own line directly above that
  exercise's set lines, formatted compactly (`R1m30s`, `R45s`, `R2m`). Never repeated
  on every set line.
- **Prehab renders as rounds, not as stacked sets** (added 2026-08-30; see
  `users/<n>/injury-protocols.md` rule 0b). The PREHAB section is split by `ROUND 1` /
  `ROUND 2` subheadings, each listing one line per item in that round. Never emit two
  consecutive set lines for the same prehab exercise — that is the pattern the rule
  exists to prevent.
- **Blank line between each exercise's block of lines**, within every section. This
  applies even inside PREHAB or WARMUP if more than one exercise appears there. The
  checklist must never read as one solid block of text.
- Header carries date, location, split, block and week so a pasted-back block is
  self-identifying.
- Nothing after the code block except a one-line instruction to annotate and paste back.

```
[YYYY-MM-DD] — [Location] ([Split]) — [Block] Wk [N]/[Total]

PREHAB
[Exercise] — [reps]

[Exercise] — [reps]/side

WARMUP
[Exercise] — [weight] — [reps]

WORKING
[Exercise] — R[rest]
[Exercise] — Set 1 — [weight] — [reps]
[Exercise] — Set 2 — [weight] — [reps]

[Next exercise] — R[rest]
[Next exercise] — Set 1 — [weight] — [reps]

BONE (optional — any time today)
[Impact movement] — R[rest between sets]
[Impact movement] — Set 1 — [reps]
[Impact movement] — Set 2 — [reps]

[Upper movement] — Set 1 — [reps]
```

**BONE section (added 2026-09-25, `system/bone-loading.md`).** Always the last section of
the checklist, same line format as working sets (no load field on bodyweight impact lines).
Bone Doubles are NOT here — they are working-set lines on their lift, labelled
`[Lift] (Bone Double) — Set 1 — [weight] — 3`.
