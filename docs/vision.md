# IDA Vision — From Architecture to Learning

## Status: Active

## Principle

Architecture foundation is **complete and frozen**.

The objective of IDA is **not** to build more framework.

The objective is to **continuously build a high-quality AI knowledge repository**.

> **Increase IDA Knowledge.** Everything must be measurable.

## Frozen architecture

Do **not** create new engines, pipelines, frameworks, or orchestration layers unless explicitly requested.

Existing stack (stable):

```text
Repository
→ Continuous Learning Scheduler
→ Priority Engine
→ Knowledge Planner
→ Knowledge Policy Engine
→ Connector Manager / Knowledge Network
→ Document Queue
→ Pipeline
→ Review
→ Publisher
→ Brain Telemetry / Learning Journal
→ Executive Control Center (Learning Dashboard)
```

Every future development must **plug into** this path.

## Development priorities

1. Make the existing architecture work  
2. Increase dataset quality  
3. Increase learning speed  
4. Improve dashboard visualization  
5. Improve automation  

Never invert these priorities.

## Continuous + Directed learning

- Continuous Learning **always runs** and never stops  
- Directed Learning is an additional priority stream  
- Directed Learning never replaces Continuous Learning  
- Scheduler allocation only shifts capacity  

## Learning Dashboard questions

1. How much knowledge does IDA currently have?  
2. What is IDA learning right now?  
3. How much smarter is IDA compared to yesterday?  
4. Which datasets are growing?  
5. Which datasets still have knowledge gaps?  
6. What missions are currently active?  
7. Which documents are being processed?  
8. What knowledge is waiting for review?  

## Learning Journal (console)

The bottom console is **not** a system log. It is IDA’s learning journal:

Searching → Downloading → Reading → Understanding → Extracting → Validating → Publishing → Learning Completed

## First knowledge milestone

First successful cycle: **Industry Library** (`IND-000001` Manufacturing).

```bash
python -m automation.learning.first_cycle
```

## Live learning runtime

Activate the frozen pipeline with realtime journal events:

```bash
python -m automation.learning.live_runtime --instruction "Learn Banking industry"
```

Or from the Learning Dashboard: **Start live learning** (SSE stream at `/api/live`).

Path executed:

Mission → Scheduler → Planner intent → Connector → Document Queue → Review → Publish → CSV updated → Dashboard + Journal + Telemetry

## Repository goal

Every commit should ideally increase:

- knowledge  
- coverage  
- quality  
- relationships  
- confidence  

—not framework complexity.
