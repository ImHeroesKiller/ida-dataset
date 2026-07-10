# Git Reliability Report

**Time:** 2026-07-10T19:03:17Z

## Failure observed

`cannot pull with rebase: You have unstaged changes`

## Fix summary

| Item | Status |
|------|--------|
| Worktree tracing | `automation/ci/worktree_trace.py` + `reports/reliability/git_worktree_trace.md` |
| Atomic commit staging | Full factory footprint in learn.yml |
| Post-commit clean check | `git diff` + porcelain (tracked) |
| Safe rebase + stash | `scripts/git_safe_sync_push.sh` |
| Generated conflict resolve | prefer-ours for reports/state/sessions |
| Double publish gate | progressive_publish skipped when session already published |
| Force push | Refused |

## Scripts

- `scripts/git_safe_sync_push.sh`
- `scripts/test_git_recovery.sh`
- `automation/lib/git_safe.py` (delegates to shell script)
