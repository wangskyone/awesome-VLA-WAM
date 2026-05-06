# Daily arXiv Automation with SSH Push

This repository's daily arXiv update should use the local repository and the
existing SSH remote:

- Repository: `E:\AgenticRobo\awesome-VLA-WAM`
- Branch: `main`
- Remote: `origin`
- Push URL: `git@github.com:wangskyone/awesome-VLA-WAM.git`

## Why the previous run failed

The failed run was caused by environment readiness, not by the README update
logic:

- The local shell could not start processes reliably.
- `CODEX_HOME` was missing, so automation memory paths became unreliable.
- The task required local `git` and `ssh`, so a broken local environment blocked
  commit and push.

## Recommended push strategy

Use a strict local-first workflow with SSH-only push:

1. Run a local preflight before any search or edit work.
2. Edit `README.md` locally.
3. Validate only the intended diff with `rg`, `git diff`, and `git status`.
4. Commit with a fixed message such as `Update daily arXiv papers`.
5. Push with `git push origin main`.
6. Write the outcome to automation memory.

Do not fall back to a mixed local-plus-GitHub-API flow for this task. If local
shell or SSH preflight fails, the automation should stop early and retry later.

## Preflight command

Run this from the repo root before the main automation work:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\automation-ssh-preflight.ps1
```

The script checks:

- `git` is available.
- `ssh` is available.
- `CODEX_HOME` is set, or `~\.codex` exists as a fallback.
- The current directory is a git repo.
- The current branch is `main`.
- The `origin` remote uses the expected SSH URL.
- `ssh -T git@github.com` authenticates successfully.
- `git status` works before any edits.

## One-time machine setup

Run these checks once on the machine that executes the automation:

```powershell
git --version
ssh -V
git remote get-url origin
ssh -T git@github.com
```

Expected remote:

```text
git@github.com:wangskyone/awesome-VLA-WAM.git
```

If `CODEX_HOME` is not injected by the automation runner, set it permanently:

```powershell
setx CODEX_HOME "C:\Users\wangskyone\.codex"
```

Then open a new shell and verify:

```powershell
echo $env:CODEX_HOME
```

If SSH authentication is missing, load the key into the current user profile:

```powershell
Get-Service ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent
ssh-add $HOME\.ssh\id_ed25519
ssh -T git@github.com
```

## Suggested automation prompt pattern

Use wording like this in the automation:

```text
In the local Git repository at E:\AgenticRobo\awesome-VLA-WAM, first run
.\scripts\automation-ssh-preflight.ps1. If preflight fails, stop immediately
and report the failing check. If preflight passes, update README.md from arXiv,
validate with `rg`, `git diff -- README.md`, and `git status --short`, commit
only the intended README change with message "Update daily arXiv papers", and
push with `git push origin main` over SSH. At the end, write which papers were
added, the commit SHA, and whether push succeeded.
```

## SSH requirements

The machine running the automation should satisfy all of these:

- `ssh.exe` is on `PATH`.
- A GitHub-capable SSH key is installed for the current user.
- The public key is added to the target GitHub account.
- `ssh -T git@github.com` returns the standard authenticated GitHub message.
- The repo remote remains `git@github.com:wangskyone/awesome-VLA-WAM.git`.

## Manual recovery steps

If a future run fails before push:

1. Open a shell in `E:\AgenticRobo\awesome-VLA-WAM`.
2. Run `.\scripts\automation-ssh-preflight.ps1`.
3. Fix the first failing check.
4. Re-run the automation only after preflight is clean.

If the failure happens after edits but before push:

1. Inspect `git status --short`.
2. Inspect `git diff -- README.md`.
3. Commit with `git commit -m "Update daily arXiv papers"`.
4. Push with `git push origin main`.

## Operational recommendation

For this specific automation, reliability is better if the run is treated as
"fail fast on environment, then do normal local git work" rather than trying to
recover through alternate write paths. The preflight script is intentionally
small so the automation can run it first and abort with a precise error message.
