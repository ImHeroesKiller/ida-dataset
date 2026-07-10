# IDA Dataset

High-quality AI knowledge repository for the IDA Executive AI platform.

## Vision

**Architecture is complete. Focus is Knowledge Growth.**

See [docs/vision.md](docs/vision.md).

## Primary goal

> Increase IDA Knowledge — measurable coverage, quality, confidence.

## Execution model

```text
GitHub Actions → Learning Session → Repository Update → Dashboard Refresh
```

Learning is **not** executed inside the dashboard. Continuous Learning is scheduled and run by GitHub Actions (`.github/workflows/learning.yml`). The ECC dashboard is a realtime monitor of sessions under `automation/sessions/`.

Architecture is unchanged: Scheduler · Planner · Policy · Connector · Pipeline · Review · Publisher · Telemetry.

## Run Learning Dashboard

```bash
npm install
npm run dev
```

Open http://localhost:3000 — **IDA Learning Sessions** dashboard.

On Vercel, set `IDA_GITHUB_TOKEN` so **Start Learning** can dispatch `learning.yml`.

## Run a learning session (same as GHA)

```bash
python automation/ci/learning_session.py \
  --environment development \
  --dry-run \
  --instruction "Learn Industry Library knowledge for Banking"
```

## First knowledge cycle (Industry Library)

```bash
python -m automation.learning.first_cycle
```

## Learning control (local)

```bash
python -m automation.scheduler mission "Learn everything about SAP ERP."
python -m automation.scheduler tick --dry-run
python -m automation.connectors health
python -m automation.search "Indonesian manufacturing" --limit 5
```

Continuous Learning never stops (hourly + daily GHA schedules). Directed Learning only influences allocation.

## Docs

- [docs/runtime.md](docs/runtime.md) — GHA session execution model  
- [docs/github_actions.md](docs/github_actions.md) — workflows  
- [docs/learning_dashboard.md](docs/learning_dashboard.md) — ECC monitor  
- [docs/vercel.md](docs/vercel.md) — deploy  

## Frozen architecture (do not expand unless requested)

Repository · Scheduler · Planner · Policy · Knowledge Network · Document Queue · Pipeline · Review · Publisher · Telemetry · Learning Dashboard
