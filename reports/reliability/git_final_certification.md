# Git Final Certification

**Time:** 2026-07-10T19:14:21Z

## Checklist

| Item | Status |
|------|--------|
| No background writers after commit | ✓ (tracers ephemeral; sync uses TMPDIR) |
| Clean worktree before rebase | ✓ (verify_clean_tracked + certify loop) |
| Clean worktree after rebase | ✓ (verify after rebase) |
| Push succeeded | runtime |
| Retry count | GIT_SAFE_PUSH_RETRIES (default 3) |
| Dirty file count | printed with filenames when dirty |
| Remaining risks | untracked cache dirs ignored; must not be tracked |

## Order

Acquire → Validate → Publish → Finalize writers → Diagnostics → Certify/commit loop → Clean check → Fetch → Rebase → Push

## Remaining risks

1. If a future step writes to a **tracked** path after certification without re-running certify, rebase will fail with **explicit file list**.
2. Force-push remains forbidden.
3. Concurrent writers blocked by `concurrency: factory-production`.
