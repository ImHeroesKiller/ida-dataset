# Failure Analysis

**Generated:** 2026-07-11T15:03:27+00:00

## Observed root causes

- none recorded this run

## Historical production finding (GHA run 29156446436)

- Step **Publish Hugging Face dataset** conclusion: **skipped**
- Learning session `dry_run=true` (workflow_dispatch default)
- Gate required `steps.cfg.outputs.dry_run != 'true'` → HF never executed
- Hub repo `ariew/ida-dataset` existed with only `README.md` + `.gitattributes` (no CSV/JSONL)
- `HF_TOKEN` **is present** in GitHub Actions secrets (name verified via API; value never read)

## Silent-failure surfaces fixed

| Surface | Before | After |
|---------|--------|-------|
| GHA skip on dry_run | Silent skip | Always run step; log gates; publish current domains |
| `continue-on-error` + `exit 0` | Hid failures | Still non-blocking, but **full exception + reports** |
| Missing token | Brief skip message | Explicit Detected/Missing + authentication.md |
| create_commit errors | Short string | Full traceback + HTTP body in logs/api_trace |

## Recommendation

Keep learning `dry_run` independent of Hub export. Always sync domains after successful learning commits.
