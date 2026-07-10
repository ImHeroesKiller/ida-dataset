# Live Learning Runtime

Stabilization layer for continuous learning without crashes, listener leaks, or silent failures.

Architecture is **frozen**. This document describes the runtime control plane only — not new engines.

## Architecture

```text
Dashboard (ECC)
    │
    ├─ POST /api/live/start  →  runtime-manager (lock + spawn + diagnostics)
    │                                │
    │                                ▼
    │                     python3 -m automation.learning.live_runtime
    │                                │
    │         Mission → Scheduler → Planner → Policy → Connector
    │              → Document Queue → Pipeline → Review → Publisher
    │                                │
    │                     journal + live_activity + runtime.status
    │
    └─ GET /api/live (SSE)  ←  tails journal / activity
           │
           └─ shared EventSource bus (one per browser tab)
                ├─ LiveDashboard
                └─ BottomConsole
```

### Components

| Layer | Path | Role |
|-------|------|------|
| Start API | `app/api/live/start/route.ts` | Delegates to runtime manager; structured failures |
| Runtime manager | `lib/runtime-manager.ts` | Host probe, lock, spawn, status, logs |
| SSE | `app/api/live/route.ts` | Journal tail; timer/listener cleanup on disconnect |
| SSE bus | `lib/live-sse-bus.ts` | Single shared `EventSource` (ref-counted) |
| Lifecycle | `automation/runtime/lifecycle.py` | Idle→Starting→Running→Stopping→Stopped→Failed |
| Errors | `automation/runtime/errors.py` | JSON failures under `automation/runtime/logs/` |
| Channels | `automation/runtime/channels.py` | system / learning / runtime / errors / publish / review / telemetry |
| Recovery | `automation/runtime/recovery.py` | Limited retries for recoverable faults only |
| Session body | `automation/learning/live_runtime.py` | Existing pipeline, lock-aware |

## Diagnostic APIs

| Endpoint | Purpose |
|----------|---------|
| `GET /api/runtime/status` | Lifecycle, session, stage, task, uptime, health, last_error |
| `GET /api/runtime/logs` | Channel logs + error records |
| `GET /api/runtime/session` | Current or named session summary |

Example status payload:

```json
{
  "status": "running",
  "session_id": "SES-20260710-ABC123",
  "correlation_id": "CORR-DEADBEEF",
  "started_at": "2026-07-10T12:00:00+00:00",
  "current_stage": "Pipeline",
  "current_task": "Reading Annual Report",
  "documents_processed": 5,
  "knowledge_candidates": 18,
  "uptime_seconds": 184,
  "health": {
    "runtime": "healthy",
    "scheduler": "healthy",
    "connector": "healthy",
    "queue": "healthy",
    "sse": "healthy",
    "publisher": "healthy"
  }
}
```

## State on disk

```text
automation/runtime/
  state/
    runtime.lock.json
    runtime.status.json
  logs/
    system.jsonl
    learning.jsonl
    runtime.jsonl
    errors.jsonl
    publish.jsonl
    review.jsonl
    telemetry.jsonl
    error_<ts>_<corr>.json
    spawn_<corr>.stdout.log
    spawn_<corr>.stderr.log
```

## Health levels

`healthy` · `warning` · `failed` · `disabled`

Exposed for: Runtime, Scheduler, Connector, Queue, SSE, Publisher.

## Single-instance rule

Only one live runtime may run unless the lock is free (or stale and reclaimed).

- Double start → `409` with `runtime.lock` failure
- Stale lock (dead PID) → reclaimed automatically
- Dashboard refresh **does not** start or stop learning

## Local CLI

```bash
python3 -m automation.learning.live_runtime \
  --instruction "Learn Industry Library knowledge for Banking" \
  --pace 0.7
```

## Tests

```bash
python3 -m automation.runtime.tests.test_runtime_stability
node automation/runtime/tests/test_sse_bus.mjs
# or
npm run test:runtime
```

## Related docs

- [runtime_lifecycle.md](./runtime_lifecycle.md)
- [runtime_troubleshooting.md](./runtime_troubleshooting.md)
