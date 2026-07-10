# Search Orchestrator

## Purpose

Turn Planner document requests into multi-connector searches and queue entries.

## Status: Active (Sprint 5)

```text
Receive request → plan query → select connectors → search
→ merge/dedupe → acquire docs → document queue
```

Never extracts knowledge.

Modules: `orchestrator.py`, `query_planner.py`, `source_selector.py`, `search_cache.py`, `query_history.py`.
