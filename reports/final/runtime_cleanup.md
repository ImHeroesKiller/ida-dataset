# Runtime Cleanup

**Generated:** 2026-07-10T16:19:42.965420+00:00

## Audited registrations

| Location | Mechanism | Cleanup |
|----------|-----------|---------|
| hooks/use-learning-monitor.ts | setInterval poll 5s | clearInterval on unmount |
| features/dashboard/factory-dashboard.tsx | setInterval 5s refresh | clearInterval on unmount |
| features/dashboard/factory-dashboard.tsx | toast setTimeout | one-shot |
| components/console/bottom-console.tsx | setInterval 5s journal tail | clearInterval on unmount (was 2s → aligned to 5s) |
| components/layout/topbar.tsx | setTimeout debounce search | clearTimeout on change/unmount |
| components/chunk-error-recovery.tsx | window error/rejection | removeEventListener on unmount |
| hooks/use-learning-monitor.ts | replay setTimeout pace | sequential await, no leak |
| lib/orchestration.ts | setInterval (server CLI path) | cleared in try/finally of same function |

## Findings fixed / verified

- Single LearningProvider poll (no dual useLearningMonitor)
- Journal poll slowed to **5s** (no faster than architecture)
- No EventSource / WebSocket / ResizeObserver / MutationObserver in factory UI
- Chunk recovery listeners cleaned up

## Memory leak status

**PASS** — all known UI intervals/listeners have teardown.
