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
mcgill-pullups.md           McGill pull-up clusters: Strength-block pull-up method
bone-loading.md             OPTIONAL bone-density module: research summary, impact
                            and upper-limb ladders, Bone Doubles, weekly tally
templates/                  starting files for a new personal repo
```

## Set up your own trainer

1. Create a **private** GitHub repo for yourself (e.g. `dug-trainer-<yourname>`).
2. In it, mount this repo and copy the templates:

   ```bash
   git submodule add https://github.com/sethgeddesxyz-star/training-science.git system
   mkdir -p users/<yourname>
   cp system/templates/user/* users/<yourname>/
   cp system/templates/personal-repo/CLAUDE.md system/templates/personal-repo/PROJECT-INSTRUCTIONS.md .
   ```

   Replace `<yourname>` and `<you>/<your-repo>` inside the two copied files. Commit and push.
3. Run it one of two ways:
   - **Claude Code** (local or claude.ai/code): open your personal repo. `CLAUDE.md`
     is the bootstrap.
   - **claude.ai Project**: paste `PROJECT-INSTRUCTIONS.md` into the project
     instructions field, with a fine-grained GitHub token for your personal repo
     (Contents: Read and write). Never commit the token.
4. Say "Gym day, 60 minutes" (or "Home workout today"). The first session runs a short
   intake to fill in your profile, equipment and injury flags, then starts every lift
   conservatively and calibrates from what you report.

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
