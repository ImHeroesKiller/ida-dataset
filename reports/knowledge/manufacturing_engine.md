# Knowledge Manufacturing Engine

**Milestone 2 · Commit 4**  
**Date:** 2026-07-12  
**Status:** Implemented  
**Constraint:** Candidates only · publisher unchanged · no domain CSV writes

## Pipeline

```text
Knowledge Graph (entities + relationships)
        ↓
  manufacture_* API
        ↓
  Multi-dataset payloads
        ↓
  Quality Engine (assess_candidate)
        ↓
  Manufacturing Queue
    ready/ | enrichment/ | pending/
        ↓
  (future) existing Publisher — NOT wired this commit
```

## API

```python
from automation.knowledge import (
    manufacture,
    manufacture_entity,
    manufacture_relationship,
    manufacture_document,
    queue_stats,
)

manufacture_entity("ENT-…")
manufacture_relationship("REL-…")
manufacture_document("DOC-…")
manufacture(entity_ids=[…], document_ids=[…], session_id="SES-…")
```

No scheduler integration.

## Multi-dataset generation

One entity expands to **all** mapped datasets (never stop after first):

| Entity type | Datasets |
|-------------|----------|
| Company | company_profile, competitor_library |
| Industry | industry_library |
| Technology | product_catalog, trend_library |
| Framework / Standard | framework_library |
| Regulation | regulation_library |
| Job Title | decision_maker_library, buyer_persona_library |

Relationships add more datasets (e.g. `provides` → product_catalog, solution_library).

## Knowledge reuse

Ledger: `automation/knowledge/store/manufacturing_ledger.json`  

Key = `sha1(source_id + target_dataset + payload)`.  
Identical graph knowledge is **not** manufactured twice unless `force=True`.

## Manufacturing queue

```text
automation/queue/manufacturing/
  ready/         # quality disposition = publish
  enrichment/    # needs enrichment
  pending/       # held / other
```

Does **not** write to `automation/queue/publish/`.

## Quality

Every candidate runs through existing `assess_candidate` / Quality Engine.  
Mandatory fields + completeness/confidence thresholds apply.

## Compatibility

| Surface | Impact |
|---------|--------|
| Publisher | Untouched |
| Domain CSV | Untouched |
| Scheduler / GHA / Mission | Untouched |
| Dashboard / Export / HF | Untouched |

## Production risk

| Risk | Mitigation |
|------|------------|
| Sparse payloads → enrichment queue | Expected; enrichment sprint fills fields |
| Competitor rows for all companies | Mapping intentional; quality gate filters |
| Ledger growth | Append-only keys; prune later if needed |

## Projection

With full graph density, one document’s entities/relationships can yield  
**multiple candidates × multiple datasets** without extra Tavily calls  
(knowledge reuse from existing graph).
