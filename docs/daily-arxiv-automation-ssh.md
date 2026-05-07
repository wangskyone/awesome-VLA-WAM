# Daily arXiv Automation for README Updates

This automation should only discover new VLA-WAM papers and update
`README.md`. It should not commit, push, or depend on helper scripts inside
this repository.

## Repository scope

- Repository: `E:\AgenticRobo\awesome-VLA-WAM`
- The automation may edit only `README.md`.
- Git commit and push are handled manually outside the automation.
- The repository should not keep automation helper scripts under `scripts/`.

## Current automation contract

Each run should:

1. Search arXiv for the newest relevant paper in these three directions:
   - World Action Models for robotics.
   - VLA failure detection/correction, including feedback, recovery,
     verification, self-improvement, closed-loop correction, robustness, or
     online adaptation.
   - Efficient VLA, including compression, quantization, action tokenization,
     small/tiny VLAs, efficient fine-tuning, deployment, or fast inference.
2. Add at most one paper per direction, and only if it is clearly relevant and
   not already present in `README.md`.
3. Prefer papers with arXiv links and project/code links when available.
4. Preserve the existing README structure and formatting.
5. Validate the result with `rg`, `git diff -- README.md`, and
   `git status --short`.
6. Report which papers were added, if any.

## Prompt guidance

The automation prompt should instruct Codex to work locally in this repository,
update only `README.md`, and stop after validation. It should not require:

- `scripts/automation-ssh-preflight.ps1`
- local SSH preflight
- `git commit`
- `git push`

## Operational note

If no clearly relevant new paper is found for one of the three directions, that
section should remain unchanged. This keeps the automation conservative and
avoids low-signal additions.
