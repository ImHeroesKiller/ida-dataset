# DRY_RUN Audit

**Time:** 2026-07-10T19:14:21Z

## learn.yml

| Trigger | dry_run | environment | commit_session |
|---------|---------|-------------|----------------|
| `schedule` | **false** | production | true |
| `workflow_dispatch` | input default **true** | input default development | input default true |

## publish.yml

| Trigger | dry_run | commit | push |
|---------|---------|--------|------|
| `schedule` | **false** | true | true |
| `workflow_dispatch` | input default **true** | input default false | input default false |

## export.yml

| Trigger | dry_run |
|---------|---------|
| `workflow_dispatch` / `workflow_call` | N/A (export only; no dry_run flag) |

## Requirement check

- [x] Manual dispatch learn defaults DRY_RUN=true
- [x] Scheduled learn sets dry_run=false
- [x] Scheduled publish sets dry_run=false
