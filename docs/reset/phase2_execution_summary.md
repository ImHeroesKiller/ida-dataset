# Phase 2 Execution Summary — IDA Dataset Factory v2.0

**Commit:** `refactor(core): transform repository into IDA Dataset Factory v2.0`  
**Date:** 2026-07-10

## What changed

### Product
- Rebranded to **IDA Dataset Factory**
- Navigation reduced to 8 factory surfaces
- Factory KPIs and dashboard

### Removed (legacy / non-goal)
- Pages: knowledge, review, reports, ontology, planner, network*, connectors*, policies, system, documents, learning, publisher, queue, search
- APIs: runtime UI museum routes kept only if required by learn engine internals; public UI APIs for live/ontology/planner/network/etc removed
- Features: executive-dashboard, knowledge, review, reports clients
- Shared clients: ontology, planner, network, policy, run-actions
- Top-level: reasoning/, examples/, templates/, plugins/
- Docs: archived under `docs/archive/`
- Workflow: planner.yml removed; learning→learn, review→quality; export.yml added

### Added
- Pages: quality, exports, logs
- API: `/api/factory/status`
- Factory packages: collector, extractor, validator, publisher, quality, export
- Export packager (JSONL / OpenAI / HuggingFace)
- Charter docs at repo root
- `scripts/factory-health.mjs`

### Protected
- `domains/**` datasets (append-only knowledge intact)
- `metadata/schema`, source registry
- Learn pipeline engine (live_runtime + dependencies) for GHA learn job

## Factory tree (after)

```text
app/          # 8 factory pages + factory APIs
automation/   # collector/extractor/validator/publisher/quality/export + pipeline
domains/      # datasets
metadata/     # schemas + sources
exports/      # training packages
docs/         # charter + archive
.github/      # validate learn quality publish export
```

## Official pipeline

Mission → Source Discovery → Document Collection → Extraction → Normalization →
Validation → Schema Mapping → Append Dataset → Quality Validation → Export → Dashboard

## KPI set

Rows today/week/month · Coverage · Quality · Confidence · Duplicates · Schema completeness · Freshness · Mission success · Exports  

## Notes

- `automation/runtime` retained as **dependency of learn engine** (not a product surface).
- `automation/search` retained as **collector support** for learn pipeline.
- No public UI for runtime/search/ontology/network.
