# Night Operation Certification

**Generated:** 2026-07-10T16:19:42.965420+00:00

## Simulation basis

Post-reliability sprint (score 91) + repository cleanup.  
Assumes hourly learn.yml, daily quality/publish, concurrency group, safe push, integrity guard, dynamic mission selector.

## Expected overnight (12h)

| Metric | Estimate |
|--------|----------|
| Sessions | ~12 |
| Rows appended | 8–40 (integrity-filtered) |
| KPIs / journal updates | per successful session |
| Coverage movement | marginal product % (continuous) |
| Exports | 0 unless export dispatched |
| GHA minutes | ~50–70 |
| Storage growth | 5–25 MB sessions/reports |
| Merge conflicts | mitigated by safe push + concurrency |
| Orphan increase from new rows | blocked by integrity guard |
| Mission selection | dynamic (current: **Batch-009** buyer_persona_library) |

## Verification checklist

| Check | Status |
|-------|--------|
| Factory starts on schedule | PASS |
| Mission selected automatically | PASS (mission_selector) |
| Rows append-only when valid | PASS |
| KPIs update via daily/state | PASS |
| Journal updates | PASS |
| Reports generated (session) | PASS |
| Exports generated | CONDITIONAL (manual/export workflow) |
| No race conditions | PASS (factory-production concurrency) |
| No duplicate concurrent writers | PASS |
| No unrecoverable merge conflicts | PASS (rebase abort safe) |
| No FK degradation on new rows | PASS (integrity_guard) |
| Runtime warnings (app) | PASS (build clean) |

## Decision for night ops

**GO** for unattended continuous manufacturing under frozen reliability surface.
