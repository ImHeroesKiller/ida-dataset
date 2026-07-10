# IDA Dataset

High-quality AI knowledge repository for the IDA Executive AI platform.

## Vision

**Architecture is complete. Focus is Knowledge Growth.**

See [docs/vision.md](docs/vision.md).

## Primary goal

> Increase IDA Knowledge — measurable coverage, quality, confidence.

## Run Learning Dashboard

```bash
npm install
npm run dev
```

Open http://localhost:3000 — **IDA Learning Dashboard**.

## First knowledge cycle (Industry Library)

```bash
python -m automation.learning.first_cycle
```

This runs one end-to-end learning path using the frozen architecture:

```text
Mission → Scheduler → Planner → Connector → Document Queue
→ Review → Publish → CSV → Dashboard / Journal / Telemetry
```

## Learning control

```bash
python -m automation.scheduler mission "Learn everything about SAP ERP."
python -m automation.scheduler tick --dry-run
python -m automation.connectors health
python -m automation.search "Indonesian manufacturing" --limit 5
```

Continuous Learning never stops. Directed Learning only influences allocation.

## Frozen architecture (do not expand unless requested)

Repository · Scheduler · Planner · Policy · Knowledge Network · Document Queue · Pipeline · Review · Publisher · Telemetry · Learning Dashboard
