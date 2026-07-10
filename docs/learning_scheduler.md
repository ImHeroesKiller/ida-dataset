# Continuous Learning Scheduler

## Purpose

Define the single orchestration entry point above the Knowledge Planner.

## Status: Active (Sprint 4)

## Principle

```text
Human → Learning Mission → Scheduler → Priority Engine → Planner
→ Policy → Pipeline → Review → Publisher → Telemetry
```

- Continuous Learning **never stops**
- Directed Learning **never disables** Continuous Learning
- Planner **never starts directly**
- Everything starts from the Scheduler

## Execution (GitHub Actions)

The scheduler module is unchanged. It is **invoked by GitHub Actions**
(`.github/workflows/learning.yml`) on hourly/daily schedule and manual dispatch,
not by a long-running dashboard Python process.

Each GHA run produces a durable session under `automation/sessions/`.

## Modules

| File | Role |
| --- | --- |
| `automation/scheduler/scheduler.py` | Central orchestrator |
| `resource_allocator.py` | Configurable allocation profiles |
| `priority_engine.py` | Queue scoring / selection |
| `mission_dispatcher.py` | NL → mission + contract |
| `learning_queue.py` | Unified task queue |
| `scheduler_metrics.py` | Brain telemetry |

## Config

`automation/config/learning.yaml` — allocation ratios, priorities, continuous catalog. Never hardcode.

## CLI

```bash
python -m automation.scheduler mission "Learn everything about SAP ERP."
python -m automation.scheduler tick --dry-run
python -m automation.scheduler dashboard
python -m automation.scheduler complete MIS-...
```

## Tick behavior

1. Seed continuous catalog (always)  
2. Recompute allocation from active missions  
3. Rank unified queue  
4. Dispatch top tasks toward Planner path (policy + review still required)  
5. Emit telemetry; write `reports/learning/`  

Dry-run records intent without invoking crawlers or publishers.
