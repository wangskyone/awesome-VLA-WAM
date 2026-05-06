param(
    [string]$ExpectedBranch = "main",
    [string]$ExpectedRemote = "origin",
    [string]$ExpectedRemoteUrl = "git@github.com:wangskyone/awesome-VLA-WAM.git"
)

$ErrorActionPreference = "Stop"

function Assert-Command {
    param([string]$Name)
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "Missing required command: $Name"
    }
}

function Write-Check {
    param(
        [string]$Label,
        [string]$Value
    )
    Write-Host ("[OK] {0}: {1}" -f $Label, $Value)
}

Assert-Command git
Assert-Command ssh

$codexHome = $env:CODEX_HOME
if (-not $codexHome) {
    $fallbackCodexHome = Join-Path $HOME ".codex"
    if (Test-Path $fallbackCodexHome) {
        $codexHome = $fallbackCodexHome
    } else {
        throw "CODEX_HOME is not set and fallback path '$fallbackCodexHome' does not exist."
    }
}
Write-Check "CODEX_HOME" $codexHome

$repoRoot = git rev-parse --show-toplevel
if (-not $repoRoot) {
    throw "Current directory is not inside a git repository."
}
Write-Check "Repository root" $repoRoot.Trim()

$branch = git rev-parse --abbrev-ref HEAD
if ($branch.Trim() -ne $ExpectedBranch) {
    throw "Expected branch '$ExpectedBranch' but found '$($branch.Trim())'."
}
Write-Check "Branch" $branch.Trim()

$remoteUrl = git remote get-url $ExpectedRemote
if ($remoteUrl.Trim() -ne $ExpectedRemoteUrl) {
    throw "Remote '$ExpectedRemote' is '$($remoteUrl.Trim())', expected '$ExpectedRemoteUrl'."
}
Write-Check "Remote URL" $remoteUrl.Trim()

$sshOutput = cmd /c "ssh -T git@github.com 2>&1"
$sshText = ($sshOutput | Out-String).Trim()
if ($LASTEXITCODE -ne 1 -and $LASTEXITCODE -ne 0) {
    throw "SSH handshake with GitHub failed. Output: $sshText"
}
if ($sshText -notmatch "successfully authenticated") {
    throw "SSH reached GitHub but did not authenticate successfully. Output: $sshText"
}
Write-Check "SSH auth" "GitHub authentication succeeded"

$worktree = git status --short
if ($LASTEXITCODE -ne 0) {
    throw "git status failed."
}
Write-Check "Git status" "available"

$memoryPath = Join-Path $codexHome "automations/daily-arxiv-vla-wam-update/memory.md"
Write-Check "Memory path" $memoryPath

if ($worktree) {
    Write-Host "[WARN] Working tree is not clean:"
    $worktree
} else {
    Write-Host "[OK] Working tree is clean"
}

Write-Host ""
Write-Host "Preflight complete. Local shell, Git, CODEX_HOME, and SSH push prerequisites look usable."
