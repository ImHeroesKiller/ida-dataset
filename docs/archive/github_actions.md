# GitHub Actions Automation

## Purpose

CI/CD and **continuous learning execution** for the IDA Knowledge Repository.

Learning is no longer hosted inside the dashboard process. GitHub Actions is the runtime.

## Status: Active

## Overview

Architecture is unchanged. Execution model:

```text
GitHub Actions → Learning Session → Repository Update → Dashboard Refresh
```

Workflows live under `.github/workflows/`.

| Workflow | File | Trigger | Mutates datasets? |
| --- | --- | --- | --- |
| Validate | `validate.yml` | `push`, `pull_request`, manual | No |
| Learning | `learning.yml` | **Hourly**, daily 06:00 UTC, manual, mission | Yes when not dry-run |
| Planner | `planner.yml` | Daily schedule, manual | No |
| Review | `review.yml` | Daily 07:00 UTC, manual | No |
| Publish | `publish.yml` | Daily 08:00 UTC, manual | Append-only when allowed |

## Continuous Learning Scheduler

The Continuous Learning Scheduler still exists (`automation/scheduler/`).

It is now **triggered by GitHub Actions schedule** (and manual dispatch) instead of a long-running Python process inside ECC.

Each learning job:

1. Creates a Session ID (`SESSION-…`)  
2. Runs Scheduler → … → Telemetry (existing engines)  
3. Writes `automation/sessions/YYYY-MM-DD/SESSION-….json`  
4. Commits session (+ knowledge when allowed) back to the repo  

## Execution order (recommended)

```text
validate  →  learning  →  planner  →  review  →  publish
```

## Environment profiles

```text
config/environments/
  development.yaml
  staging.yaml
  production.yaml
```

Select with workflow input `environment` or `IDA_ENVIRONMENT`.

| Environment | Default dry-run | Publish | Commit | Push |
| --- | --- | --- | --- | --- |
| development | true | false | false | false |
| staging | false | true | true | true |
| production | false | true | true | true |

## Dry run

Every workflow supports `dry_run=true`.

When dry-run is enabled:

- No dataset mutations  
- Session JSON and reports are still written  
- learning.yml can still commit session artifacts for dashboard visibility  

## Manual execution / Mission trigger

### Learning

GitHub → Actions → **Learning** → Run workflow  

Or from the ECC dashboard **Start Learning** button (workflow_dispatch via API).

Locally:

```bash
python automation/ci/learning_session.py \
  --environment development \
  --dry-run \
  --instruction "Learn everything about SAP ERP" \
  --trigger mission
```

Artifacts:

- `automation/sessions/YYYY-MM-DD/SESSION-*.json`  
- `reports/learning/learning_session_*.md`  
- `reports/learning/learning_session_*.json`  

### Review / Publish / Planner / Validate

Unchanged entry points — see previous sections. Review and Publish now also have daily schedules.

## Dashboard integration (Vercel)

| Action | Mechanism |
| --- | --- |
| Monitor sessions | Read `automation/sessions/` + Actions runs API |
| Start learning | `POST /repos/{repo}/actions/workflows/learning.yml/dispatches` |
| Replay | Client paces events from session JSON |

Env for dispatch / status:

```text
IDA_GITHUB_TOKEN=ghp_...   # actions:write, actions:read
GITHUB_REPOSITORY=owner/ida-dataset
```

## Exit codes

| Code | Meaning |
| ---: | --- |
| 0 | Success |
| 1 | Validation / session error |
| 2 | Configuration error |
| 3 | Policy violation |
| 4 | Publisher blocked |

## Tooling map

| Concern | Script |
| --- | --- |
| Learning session | `automation/ci/learning_session.py` |
| Session store | `automation/learning/session_store.py` |
| Validate | `automation/ci/validate_repo.py` |
| Planner | `automation/ci/planner.py` |
| Review | `automation/ci/review_summary.py` |
| Publish | `automation/ci/publish_ci.py` |
| Shared helpers | `automation/ci/common.py` |

## Related docs

- `docs/runtime.md` — execution model  
- `docs/learning_dashboard.md` — ECC monitor  
- `docs/learning_scheduler.md` — scheduler architecture (unchanged)  
- `docs/vercel.md` — deploy notes  
