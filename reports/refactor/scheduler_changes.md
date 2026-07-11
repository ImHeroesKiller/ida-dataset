# Scheduler Changes

**Generated:** 2026-07-11  
**Sprint:** IDA Dataset Factory Simplification v2.0

## Change

| Item | Before | After |
|------|--------|------:|
| GHA `learn.yml` continuous cron | `*/15 * * * *` (every 15 min) | `0 * * * *` (hourly) |
| Daily deep pass | `0 6 * * *` | unchanged |
| Concurrency | `factory-production` non-overlapping | unchanged (`cancel-in-progress: false`) |
| UI Settings cadence | Every 15 minutes | Every 1 hour |
| Next-run hint (`lib/github-actions.ts`, `lib/sessions.ts`) | 15-min slots | next UTC hour |
| Dashboard production card | "15-minute schedule" | "1-hour schedule" |

## Rationale

- Deeper sessions → higher knowledge per run  
- Lower GitHub Actions minutes + API spend  
- Less overlap risk with long learning jobs  
- Still continuous manufacturing (no stop condition)

## Overlap prevention

```yaml
concurrency:
  group: factory-production
  cancel-in-progress: false
```

Only one production writer at a time; new hourly ticks queue behind an in-flight session.

## Not rewritten

Scheduler package / mission lifecycle engines untouched (production freeze).
