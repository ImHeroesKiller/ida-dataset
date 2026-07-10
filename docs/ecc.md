# Executive Control Center (ECC)

## Purpose

Document the interactive operational cockpit for the IDA Knowledge Platform.

## Status: Active (Sprint 3)

## Philosophy

IDA is **human controlled**, not autonomous.

```text
Dashboard
  → Planner
    → Policy Engine
      → Pipeline
        → Review
          → Publisher
```

No module may bypass this chain. The ECC UI is only an orchestration surface over existing automation.

## Location

```text
ecc/
```

See `ecc/README.md` for run instructions.

## Integration points

| ECC surface | Backend source of truth |
| --- | --- |
| Dashboard status cards | Live repo inventory + policies + queues + git |
| Planner | Dataset gap analysis + `automation/ci/planner.py` |
| Policies | `automation/config/policies.yaml` + sources |
| Ontology | `metadata/ontology/*.csv` |
| Datasets | `domains/**/*.csv` (read-only) |
| Review | `automation/queue/{pending,approved,rejected}` |
| Publisher | `automation/ci/publish_ci.py` dry-run |
| Reports | `reports/**` |
| Console / progress | ECC orchestration process + CI logs |

## Non-goals (Sprint 3)

- Browser automation
- Crawling
- LLM extraction
- Graph databases
- Direct production dataset editing
- Live publish from the browser without CI/policy gates

## Plugin model

Future capability lands as plugins (`ecc/lib/plugins.ts`) that attach to sidebar / dashboard / settings slots without redesigning layout or control flow.
