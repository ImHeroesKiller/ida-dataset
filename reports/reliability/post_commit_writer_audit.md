# Post-Commit Writer Audit

## Problem

`git pull --rebase` failed with:

```text
cannot pull with rebase: You have unstaged changes.
```

Root cause: **tracked files rewritten during the session were not fully staged** in the GHA commit step, leaving a dirty tree **after** `git commit` and **before** rebase/push.

## Writers during a learning session (before commit — allowed)

| Area | Modules | Paths |
|------|---------|-------|
| Acquisition | `pipeline.py`, `document_store.py` | `automation/queue/`, `domains/`, raw docs |
| Trace/reports | `trace.py`, `reports.py`, `performance.py`, discovery, manufacturing | `reports/*`, `automation/learning/state/*` |
| Session | `session_store.py`, `journal.py`, `growth.py` | `automation/sessions/`, `learning/state/` |
| Progressive publish | `progressive_publish.py` | domains + queue (now gated) |

## Writers after commit (forbidden)

GHA previously:

1. Committed only `sessions/`, `reports/learning/`, `state/`, optionally `domains/` + `queue/`
2. Left dirty tracked files under e.g. `reports/production/`, `reports/discovery/`, `reports/performance/`, `reports/manufacturing/`, reliability traces, manufacturing state

Those residual **tracked** modifications blocked rebase.

## Remediation

1. **Atomic commit** in `learn.yml` stages the full production footprint + any remaining tracked dirt
2. **Post-commit verify** fails the job if tracked tree still dirty
3. **`git_safe_sync_push.sh`** stashes include-untracked if dirt appears, rebases, pops, auto-resolves generated conflicts
4. **No intentional writers after commit** in the workflow order

## Scan notes (patterns)

Looked for post-commit hooks in workflows — none invoke Python after the commit step except `git_safe_sync_push.sh` residual auto-stage (recovery only).

## Certification

- [x] Commit step stages all factory report/state/session/domain paths
- [x] Tracked clean verification after commit
- [x] Safe push recovers residual dirt without force-push
