# Runtime Lifecycle

## States

```text
Idle
  │
  ▼
Starting
  │
  ▼
Running
  │
  ▼
Stopping
  │
  ▼
Stopped ──► Idle

Any active state may transition to Failed on unrecoverable error.
Failed ──► Idle / Starting (after human Retry)
```

| State | Meaning |
|-------|---------|
| `idle` | No session; ready for start |
| `starting` | Lock acquired or process spawning |
| `running` | Live session executing pipeline stages |
| `stopping` | Graceful wind-down / lock release |
| `stopped` | Session finished cleanly |
| `failed` | Unrecoverable failure; dashboard must show reason |

## Transitions (allowed)

| From | To |
|------|-----|
| idle | starting, failed |
| starting | running, failed, stopping, stopped |
| running | stopping, failed, stopped |
| stopping | stopped, failed |
| stopped | idle, starting |
| failed | idle, starting |

## Ownership

1. **API start** (`lib/runtime-manager.ts`)
   - Probes host (Vercel / ECC_DISABLE_PYTHON / Python import)
   - Reclaims stale locks
   - Spawns `python3 -m automation.learning.live_runtime --correlation-id …`
   - Verifies process stays alive (~600ms)
   - Writes `runtime.status.json`

2. **Python process** (`live_runtime.py` + `automation.runtime.lifecycle`)
   - `acquire_lock(session_id, correlation_id)`
   - `Starting → Running` with stage/task updates
   - On success: `Stopping → Stopped → Idle`, `release_lock`
   - On failure: structured error, `Failed`, force release

## Locks

`automation/runtime/state/runtime.lock.json`:

```json
{
  "pid": 12345,
  "session_id": "SES-…",
  "correlation_id": "CORR-…",
  "status": "running",
  "instruction": "…",
  "acquired_at": "…"
}
```

- Created with `O_CREAT|O_EXCL` (atomic)
- Prevents double start, double publish races, duplicate scheduler loops from concurrent API starts
- Dead PID → reclaim → mark failed with `StaleLock`

## Recovery policy

| Class | Examples | Behavior |
|-------|----------|----------|
| Recoverable | temporary IO, connector timeout, queue busy | Retry with backoff (default 3 attempts) |
| Unrecoverable | ImportError, PermissionError, lock conflict, config | Stop safely, write failure log, notify dashboard |

Never auto-recover unrecoverable failures. Dashboard shows **Runtime Failed** with Retry / View Logs / Copy Diagnostic.

## SSE lifecycle (client)

```text
Mount LiveDashboard + BottomConsole
  → two subscribeLiveLearning() calls
  → refCount=2, ONE EventSource

Unmount one
  → refCount=1, EventSource kept

Unmount both / leave page
  → refCount=0, EventSource.close()
```

Server stream: every disconnect clears intervals and removes the abort listener. **Never** call `setMaxListeners()`.

## Correlation

Every start receives a `correlation_id` (`CORR-…`). It flows through:

- spawn env / CLI flag
- failure JSON
- channel logs
- status snapshot
- dashboard failure panel
