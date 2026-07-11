# GHA Forensic Evidence

**Generated:** 2026-07-11T15:03:27+00:00

## Run 29156446436 (workflow_dispatch, success)

| Step | Conclusion |
|------|------------|
| Run learning session | success |
| Certify worktree and atomic commit | success |
| Safe git sync and push | success |
| **Publish Hugging Face dataset** | **skipped** |
| Upload Hugging Face publish reports | skipped |

### Environment evidence from logs

- `DRY_RUN: true` (job env)
- `cfg dry_run=true` / `commit_session=true`
- Session JSON: `"dry_run": true`, `"published": 0`
- HF step `if` required `dry_run != true` → **skipped**

## Run 29152804840 (schedule, before HF step existed)

No "Publish Hugging Face dataset" step in job — workflow predates HF integration.

## Secrets (names only)

`gh api .../actions/secrets` lists **`HF_TOKEN`** among secrets.

## Remote Hub (public API, no token)

```
id: ariew/ida-dataset
siblings: .gitattributes, README.md only
usedStorage: 0
lastModified: 2026-07-11T14:18:21Z
```

**Conclusion:** No CSV/JSONL ever uploaded. Token exists. Step never ran on a completed post-merge production path.

## Root cause (ranked)

1. **Gate skip:** `steps.cfg.outputs.dry_run != 'true'` blocked all workflow_dispatch runs (default dry_run=true).
2. **No completed schedule** with HF step after merge (cancelled / pre-merge).
3. **Silent skip** — GHA shows skipped with no publish_trace report.

## Fix

- Always run HF step when learning succeeds + commit_session.
- Learning dry_run no longer blocks Hub export of existing domains.
- Loud diagnostics + forensic reports; manufacturing still non-blocking.
