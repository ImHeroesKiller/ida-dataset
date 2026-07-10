# Atomic Commit Report

**Time:** 2026-07-10T19:03:17Z

## Production order (learn.yml)

1. Acquire / Validate / Publish / Export-deferred / Reports (inside learning_session)
2. Flush writers (session finalize + growth snapshot)
3. Worktree trace `post_session_pre_commit`
4. **Atomic commit** — stage all factory outputs once
5. Verify clean tracked tree
6. Fetch → rebase (safe) → push

## Guarantees

- No intentional file writes after the atomic commit step
- Residual dirt is recovered by stash/rebase/pop inside `git_safe_sync_push.sh` only
- Never force-push
