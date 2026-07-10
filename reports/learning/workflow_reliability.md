# Workflow Reliability Report

**Generated:** 2026-07-10T15:57:32.871218+00:00

---

## Concurrency (P0-2)

```yaml
concurrency:
  group: factory-production
  cancel-in-progress: false
```

Applied to: **learn**, **publish**, **quality**, **export**.  
Queued execution — never concurrent dataset writers.

validate.yml remains read-only and may run in parallel (no write).

---

## Workflow matrix

| Workflow | Cron | Dispatch | Concurrency | Safe push | Self-trigger loop |
|----------|------|----------|-------------|-----------|-------------------|
| learn.yml | hourly + 06:00 UTC | yes | factory-production | yes | no (schedule only; commits do not re-fire learn) |
| publish.yml | 08:00 UTC | yes | factory-production | yes (python) | no |
| quality.yml | 07:00 UTC | yes | factory-production | n/a (read) | no |
| export.yml | none | yes | factory-production | n/a | no |
| validate.yml | on push/PR | yes | none (read-only) | n/a | no (does not commit) |

---

## Commit loop prevention

- learn commits → may trigger **validate** only (read-only)
- validate never commits
- publish commits only after explicit publish path
- No workflow_call from learn → learn

## Exit codes preserved

validate/publish 0–4; learn 0/1/2 — unchanged semantics.
