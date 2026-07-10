# GitHub Actions Automation

## Purpose

Document the CI/CD automation layer for the IDA Knowledge Repository.

## Status: Active (Sprint 1)

## Overview

Sprint 1 establishes a **safe CI/CD foundation** only:

- No crawler
- No browser automation
- No search APIs
- No LLM extraction
- No unsupervised dataset generation

Workflows live under `.github/workflows/`.

| Workflow | File | Trigger | Mutates datasets? |
| --- | --- | --- | --- |
| Validate | `validate.yml` | `push`, `pull_request`, manual | No |
| Planner | `planner.yml` | Daily schedule, manual | No |
| Review | `review.yml` | Manual only | No |
| Publish | `publish.yml` | Manual only | Append-only when allowed |

## Execution order (recommended)

```text
validate  →  planner  →  review  →  publish
```

1. **validate** — gate every change; fail closed on data quality issues  
2. **planner** — identify gaps and priorities (read-only)  
3. **review** — summarize human review queues (read-only)  
4. **publish** — append approved rows only under policy gates  

## Environment profiles

Configuration is external (never hard-coded in workflow logic):

```text
config/environments/
  development.yaml
  staging.yaml
  production.yaml
```

Select with:

- Workflow input `environment`
- Or env var `IDA_ENVIRONMENT`

| Environment | Default dry-run | Publish | Commit | Push |
| --- | --- | --- | --- | --- |
| development | true | false | false | false |
| staging | false | true | true | true |
| production | false | true | true | true |

All environments still honor `automation/config/policies.yaml` (e.g. `publishing_enabled`, `review_required`).

## Exit codes

Every workflow tool returns meaningful codes:

| Code | Meaning |
| ---: | --- |
| 0 | Success |
| 1 | Validation error |
| 2 | Configuration error |
| 3 | Policy violation |
| 4 | Publisher blocked |

## Dry run

Every workflow supports `dry_run=true`.

When dry-run is enabled:

- No dataset mutations
- No git commits
- No git pushes
- Reports and JSON logs are still written for visibility

## Manual execution

### Validate

GitHub → Actions → **Validate** → Run workflow  
Or push / open a pull request.

Locally:

```bash
python automation/ci/validate_repo.py --environment development --dry-run
```

### Planner

GitHub → Actions → **Planner** → Run workflow  
Also runs daily at 06:00 UTC.

```bash
python automation/ci/planner.py --environment development --dry-run
```

Artifacts:

- `reports/planner/planning_report.md`
- `reports/planner/planning_report.json`

### Review

GitHub → Actions → **Review** → Run workflow (manual only).

```bash
python automation/ci/review_summary.py --environment development --dry-run
```

Artifact:

- `reports/review/review_summary.md`

Shows pending / approved / rejected counts, confidence, and datasets affected.

### Publish

GitHub → Actions → **Publish** → Run workflow (manual only).

Gates (all must pass for a real publish):

1. `review_required == false` **OR** approved candidates exist  
2. Environment `allow_publish: true` (when not dry-run)  
3. `policies.features.publishing_enabled: true` (when not dry-run)  
4. Publisher remains **append-only** (never overwrite)

```bash
# Safe simulation
python automation/ci/publish_ci.py --environment development --dry-run

# Real publish (requires policy + approved queue + env allow)
python automation/ci/publish_ci.py \
  --environment staging \
  --no-dry-run \
  --commit \
  --push
```

Artifact:

- `reports/publish/publish_report.md` (includes git diff stats)

## Logging

Each run writes:

- **JSON log** — timestamp, duration, status, exit code, metrics  
- **Markdown report** — human-readable summary  

Locations:

```text
reports/validation/
reports/planner/
reports/review/
reports/publish/
```

## Failure handling

| Failure | Exit | Recovery |
| --- | ---: | --- |
| Invalid CSV / UTF-8 / CRLF / schema / duplicate IDs / broken relationships | 1 | Fix data in a PR; re-run validate |
| Missing environment config or bad `IDA_ENVIRONMENT` | 2 | Add/fix `config/environments/*.yaml` |
| Publish disallowed by environment or push denied | 3 | Adjust env profile or stop the publish attempt |
| Review required and no approved candidates / publishing feature off | 4 | Approve candidates in KAS queue; enable publishing in policies intentionally |

## Recovery playbooks

### Validation red on PR

1. Download `validation-reports` artifact  
2. Open `validation_report.md`  
3. Fix listed paths only — never bulk-rewrite unrelated datasets  
4. Push fix; validate must go green before merge  

### Publish blocked (exit 4)

1. Open `reports/publish/publish_report.md`  
2. Check `review_required` and approved queue counts  
3. Run **Review** workflow to inspect queues  
4. Approve candidates via KAS (`python -m automation review ...`)  
5. Ensure `policies.features.publishing_enabled` is intentionally true  
6. Re-run **Publish** with `dry_run=true` first, then real publish  

### Accidental publish attempt on development

Development profile sets `allow_publish: false`. Real publishes should use staging/production with human confirmation.

## Tooling map

| Concern | Script |
| --- | --- |
| Validate | `automation/ci/validate_repo.py` |
| Planner | `automation/ci/planner.py` |
| Review | `automation/ci/review_summary.py` |
| Publish | `automation/ci/publish_ci.py` |
| Shared helpers | `automation/ci/common.py` |
| Exit codes | `automation/ci/__init__.py` |

## Related docs

- `docs/kas.md` — Knowledge Acquisition System principles  
- `automation/README.md` — KAS CLI  
- `config/environments/*.yaml` — environment protection profiles  
