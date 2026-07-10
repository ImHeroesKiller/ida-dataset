# Runtime Troubleshooting

## Root cause: HTTP 503 on `/api/live/start`

The old route returned a generic 503 whenever `VERCEL` or `ECC_DISABLE_PYTHON=1` was set, and returned `ok: true` even when the Python process died immediately (`stdio: ignore`).

### Diagnosed failure components

| `failure.component` | HTTP | Cause | Recovery |
|---------------------|------|-------|----------|
| `host.vercel` | 503 | Vercel serverless — no long-lived Python subprocess | Run live learning on local/VM host |
| `host.ecc_disable_python` | 503 | `ECC_DISABLE_PYTHON=1` | Unset env or run CLI directly |
| `host.python_missing` | 503 | No `python3` / `IDA_PYTHON` on PATH | Install Python 3 or set `IDA_PYTHON` |
| `host.python_import` | 503 | `import automation.learning.live_runtime` fails | Fix PYTHONPATH/cwd/dependencies |
| `runtime.spawn` | 503 | `spawn()` threw (permissions, OS) | Check execute rights, disk, process limits |
| `runtime.process` / `EarlyExit` | 503 | Process exited within ~600ms | Read `automation/runtime/logs/spawn_<corr>.stderr.log` |
| `runtime.lock` / `AlreadyRunning` | 409 | Live session already held lock | Wait; do not double-start |

Every 503/409 body includes:

```json
{
  "ok": false,
  "message": "…",
  "correlation_id": "CORR-…",
  "failure": {
    "timestamp": "…",
    "component": "…",
    "exception": "…",
    "message": "…",
    "stack_trace": "…",
    "correlation_id": "…",
    "session_id": "…",
    "recovery_action": "…",
    "recovery_suggestion": "…"
  },
  "recovery_suggestion": "…"
}
```

### Diagnostic procedure

1. `GET /api/runtime/status` — lifecycle, `last_error`, `host_capabilities`
2. `GET /api/runtime/logs?channel=errors&correlation_id=CORR-…`
3. Inspect `automation/runtime/logs/spawn_<corr>.stderr.log`
4. CLI control:  
   `python3 -m automation.learning.live_runtime --instruction "test" --pace 0.2`
5. Confirm lock: `automation/runtime/state/runtime.lock.json`  
   If PID is dead, status reclaim will clear it on next status read/start

## MaxListenersExceededWarning / SSE leaks

### Root cause

- `LiveDashboard` and `BottomConsole` each called `useLiveLearning()`
- Each mount opened its own `EventSource("/api/live")`
- React Strict Mode remounts doubled connections
- Server stream `cancel()` set `closed=true` but did not always clear intervals / remove abort listeners immediately

### Fix

- Shared bus: `lib/live-sse-bus.ts` — one `EventSource`, ref-counted
- Server: clear intervals + remove abort listener on abort **and** cancel
- **Do not** increase `setMaxListeners()`

### Verify

```bash
node automation/runtime/tests/test_sse_bus.mjs
```

Refresh the dashboard repeatedly — learning must not restart; SSE refCount must return to 0 on leave.

## Runtime never starts

| Symptom | Check |
|---------|--------|
| Button says started but no events | Process early-exit; status `failed` + spawn stderr |
| Stuck `starting` | PID dead → stale; status should flip to `failed` |
| 409 on start | Another session running — intended |
| Dashboard silent retry | Fixed — failures show Runtime Failed panel |

## Zombie processes / duplicate sessions

- Lock prevents concurrent API starts
- Python releases lock on success and failure
- Stale lock reclaimed when holder PID is dead
- Spawn logs retained per correlation id

## Memory / long sessions

- Journal tail is offset-based (not full re-read)
- Client keeps last 300 events only
- Channel logs are append-only JSONL — rotate operationally if needed

## Recovery flow

```text
Failure occurs
  → record_failure() → automation/runtime/logs/error_*.json
  → status = failed
  → activity.status = error
  → Dashboard: Runtime Failed + reason + recovery + Retry / View Logs / Copy Diagnostic

If recoverable (IO/connector/queue):
  → run_with_recovery retries with backoff
  → only escalates to failed after max attempts
```

## Health matrix

| Component | healthy | warning | failed | disabled |
|-----------|---------|---------|--------|----------|
| runtime | idle/running ok | — | crash / early exit | Vercel / ECC_DISABLE_PYTHON |
| scheduler | construct/tick ok | soft errors | init failure | — |
| connector | search ok | timeouts | hard failure | — |
| queue | dirs present | missing dir | IO failure | — |
| sse | endpoint up | reconnecting | — | — |
| publisher | publish ok | — | CSV write failure | waiting review |

## Quick commands

```bash
curl -s localhost:3000/api/runtime/status | jq .
curl -s 'localhost:3000/api/runtime/logs?channel=errors&limit=20' | jq .
curl -s localhost:3000/api/runtime/session | jq .
python3 -m automation.runtime.tests.test_runtime_stability
node automation/runtime/tests/test_sse_bus.mjs
```
