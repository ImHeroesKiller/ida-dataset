# Post-Commit Writer Audit

**Time:** 2026-07-10T19:14:21Z

## Confirmed root cause

After `git commit`, CI steps and `git_safe_sync_push.sh` **wrote into tracked paths** under `reports/reliability/`:

| Writer | Files | Trigger | Expected timing | Safe/Unsafe |
|--------|-------|---------|-----------------|-------------|
| `worktree_trace.py` | `reports/reliability/git_worktree_trace.md` | post_commit / before_safe_push | **after commit** | **UNSAFE** (fixed: `--ephemeral`) |
| `git_safe_sync_push.sh` log_trace | same + push_recovery_report | during fetch/rebase | **after commit** | **UNSAFE** (fixed: `$TMPDIR` only mid-sync) |
| learning_session | domains, state, reports/* | session body | before commit | SAFE |
| progressive_publish | domains/queue | gated residual | before commit | SAFE if gated |
| ThreadPoolExecutor (connectors/pipeline) | none after context exit | with-block | during acquire | SAFE (joins on exit) |
| journal lock / channels lock | learning state | session end | before commit | SAFE |
| atexit | none found | — | — | N/A |
| asyncio background | none found | — | — | N/A |
| daemon threads | none found in production path | — | — | N/A |

## Fix

1. All post-commit diagnostics use **ephemeral** temp storage until after push.
2. `finalize_writers.py` runs **before** git add.
3. `certify_worktree.py` loops stage→commit until tracked porcelain empty.
4. `git_safe_sync_push.sh` refuses to rebase unless tracked tree is clean (or one finalize commit).

## Certification

- [x] No intentional background writers after commit
- [x] Tracer cannot dirty worktree post-commit (`--ephemeral`)
- [x] Sync script does not write reports during fetch/rebase
