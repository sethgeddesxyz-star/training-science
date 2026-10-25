# Training Science — Dug Trainer shared program

An SBS-based (Stronger by Science) workout engine, run through Claude. Claude reads
the rules in this repo plus your own private state, prescribes one workout, and logs
what you report back.

This repo holds **only the science and the rules**. Your training state, workout log,
equipment and injury notes live in your own **private** repo, which mounts this one as
a git submodule at `system/`. Nothing personal is ever committed here.

## What is in here

```
operating-protocol.md       ENTRY POINT. Session lifecycle, gates, git discipline,
                            and the map of which file to read when
output-format.md            coaching view + checklist specs
reporting-protocol.md       parsing reports, logging, state edits
sbs-progression-rules.md    the progression engine (double progression, blocks,
                            deloads, ceiling ladders, plateau detection)
exercise-library.md         exercises by movement pattern + equipment
bodyweight-ladders.md       bodyweight progression ladders
conditioning-hiit.md        HIIT / VO2max day type: research summary, A→B→A→C
                            format cycle, modality, progression by output
aerobic-heart-rate.md       easy aerobic HR ceiling: MAF 180 formula, Zone 2
mcgill-pullups.md           McGill pull-up clusters: Strength-block pull-up method
bone-loading.md             OPTIONAL bone-density module: research summary, impact
                            and upper-limb ladders, Bone Doubles, weekly tally
kettlebell.md               kettlebell repertoire: bells, technique-gated movement
                            chain, ladders, hardstyle benchmarks, S&S and complexes
suspension-trainer.md       TRX / rings repertoire: angle rule, catalogue, ladders,
                            travel sessions
quick-sessions.md           4–20 min sessions for home or anywhere: 7-Minute Workout,
                            core circuits, KB and strap snacks, stair/walk snacks, GtG
splits.md                   full body / upper-lower / push-pull-legs: day types, rotation,
                            HIIT placement per split, per-day-type rule mapping
modality-rotation.md        rotating the KIND of training across blocks (DB, barbell,
                            machine, bodyweight, KB, TRX, band): floor, swaps, variety week
reminders.md                opt-in phone reminders: catalogue, agreement protocol,
                            4-week review, delivery routes, reminders.json schema
scripts/remind.py           the reminder sender (ntfy + cron, or --ics for the phone)
templates/                  starting files for a new personal repo
```

## Set up your own trainer

You need a GitHub account and a Claude plan with Claude Code (claude.ai/code).

1. **Make a private repo.** At github.com/new create a **private** repo for yourself
   (e.g. `dug-trainer-<yourname>`). Tick "Add a README" so it is not empty.
2. **Open it in Claude Code.** At claude.ai/code, connect GitHub if asked, pick your new
   repo, and start a session. (Local Claude Code works the same: clone the repo and run
   `claude` inside it.)
3. **Let Claude build it.** Paste this as the first message:

   > Set this repo up as my Dug Trainer from
   > https://github.com/sethgeddesxyz-star/training-science — add it as a git submodule
   > at `system/`, copy `system/templates/user/*` into `users/<yourname>/` and
   > `system/templates/personal-repo/CLAUDE.md` to the repo root, replace the
   > placeholders, commit and push to main.

   Or by hand:

   ```bash
   git submodule add https://github.com/sethgeddesxyz-star/training-science.git system
   mkdir -p users/<yourname>
   cp system/templates/user/* users/<yourname>/
   cp system/templates/personal-repo/CLAUDE.md .
   # replace <yourname> in CLAUDE.md, then commit and push
   ```
4. **Train.** Start a new session in your repo and say "Gym push day" (or "Home workout
   today, 45 minutes"). `CLAUDE.md` loads the rules on its own. The first session runs a
   short intake (goals, equipment, injuries), then starts every lift conservatively and
   calibrates from what you report. Report results in the same session; it logs them and
   pushes.

**claude.ai Project instead of Claude Code:** copy
`templates/personal-repo/PROJECT-INSTRUCTIONS.md` into the project instructions field and
give it a fine-grained GitHub token for your personal repo (Contents: Read and write).
Never commit the token.

## Reminders (optional)

Anything with a rhythm (bone drops, a core snack, a kettlebell practice, "HIIT is due") can
become a phone ping. Tell the trainer which ones you want and when; it writes the agreed
schedule to `users/<yourname>/reminders.json`. Delivery is a 10-minute one-time setup with
the free ntfy app and a cron line on any computer that stays on, or a calendar file for the
phone if you have no such computer. Full walkthrough: `reminders.md` §5. The trainer reviews
every reminder's hit rate every four weeks and drops the ones you never act on.

## Updates

Your personal repo pins a version of this one. To take the latest rules:

```bash
git submodule update --remote system
git commit -am "Update shared rules"
```

## Contributing

Rule changes are proposed as pull requests here, never committed to `system/` inside a
personal repo and left there. A good PR says what changed, why (cite the study or the
session that exposed the gap), and contains no personal data: no names, logs, loads tied
to a person, or injury history.

This is training software, not medical advice. Anything involving pain goes to your own
injury protocol and, where it persists, a clinician.
