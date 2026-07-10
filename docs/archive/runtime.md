# Learning Runtime → GitHub Actions Sessions

The always-on local Python runtime has been **removed** as the execution model.

Architecture is **unchanged**. Only the execution strategy changed.

## Architecture

```text
GitHub Actions (schedule | manual | mission)
    │
    ▼
Learning Session (automation/ci/learning_session.py)
    │
    ├─ Scheduler → Planner → Policy → Connector
    │     → Document Queue → Pipeline → Review → Publisher → Telemetry
    │
    ▼
Repository Update
  automation/sessions/YYYY-MM-DD/SESSION-xxxxx.json
  (+ knowledge / reports when not dry-run)
    │
    ▼
Dashboard Refresh (Vercel / local ECC)
  polls /api/sessions · dispatches learning.yml on "Start Learning"
```

### What was removed from the dashboard host

| Former | Now |
|--------|-----|
| `python -m automation.learning.live_runtime` spawned by Next.js | GitHub Actions job |
| Long-lived process + lock file | Ephemeral GHA runner |
| Server-side SSE journal tailer | Poll session JSON + Actions status |
| Vercel serverless limitation on spawn | Dashboard is read-only monitor |

### What was kept

Scheduler · Planner · Policy · Connector Manager · Pipeline · Review · Publisher · Telemetry

## Workflows

| Workflow | File | Triggers |
|----------|------|----------|
| Learning | `.github/workflows/learning.yml` | Hourly, daily 06:00 UTC, manual, mission |
| Review | `.github/workflows/review.yml` | Daily 07:00 UTC, manual |
| Publish | `.github/workflows/publish.yml` | Daily 08:00 UTC, manual |
| Planner | `.github/workflows/planner.yml` | Daily 06:00 UTC, manual |
| Validate | `.github/workflows/validate.yml` | push / PR / manual |

### learning.yml inputs

- `environment` — development | staging | production  
- `dry_run` — true | false  
- `mission` — instruction text (mission trigger)  
- `trigger` — manual | mission | hourly | daily | schedule  
- `commit_session` — commit session artifacts to the repo  

## Session storage

```text
automation/sessions/
  YYYY-MM-DD/
    SESSION-YYYYMMDD-XXXXXX.json
  index.json
```

Each session stores:

- Session ID, start/end, duration  
- Knowledge added / updated / rejected  
- Mission, status, errors, summary  
- Planner output, connector output, knowledge delta  
- Publish summary, telemetry, logs, ordered events (replay)  

## Dashboard APIs (Vercel-safe)

| Endpoint | Role |
|----------|------|
| `GET /api/sessions` | Status, history, session list + GHA run state |
| `GET /api/sessions?session_id=` | Full session + events for journal/replay |
| `POST /api/live/start` | `workflow_dispatch` on `learning.yml` |
| `GET /api/live/replay` | List / load session events |
| `GET /api/runtime/status` | Compatibility status (no local PID) |

### Manual learning from the UI

"Start Learning" → `POST /api/live/start` → GitHub workflow_dispatch.

Requires env:

```text
IDA_GITHUB_TOKEN   # PAT with actions:write (+ contents if needed)
GITHUB_REPOSITORY  # owner/repo   (or VERCEL_GIT_REPO_OWNER + VERCEL_GIT_REPO_SLUG)
```

## Local CLI (same session writer as GHA)

```bash
python automation/ci/learning_session.py \
  --environment development \
  --dry-run \
  --instruction "Learn Industry Library knowledge for Banking" \
  --trigger manual
```

## Console

Bottom console is the **Learning Session Journal** — real events from stored session files. Replay preserves timestamps and order. No fake live stream.

## Related docs

- [github_actions.md](./github_actions.md)
- [learning_dashboard.md](./learning_dashboard.md)
- [learning_scheduler.md](./learning_scheduler.md)
- [vercel.md](./vercel.md)
