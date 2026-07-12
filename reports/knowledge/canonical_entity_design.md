# Canonical Entity Layer

**Milestone 2 · Commit 2**  
**Date:** 2026-07-12  
**Status:** Implemented  
**Constraint:** No relationships · no dataset rows · additive only

## Flow

```text
Knowledge Atom
      ↓
   Mention extract
      ↓
Canonical Entity Store lookup (alias / canonical index)
      ↓
   Reuse existing  OR  Create new
      ↓
Aliases · knowledge_score · indexes updated
```

## Entity fields

| Field | Purpose |
|-------|---------|
| entity_id | `ENT-{sha1-12}` of type + normalized name |
| canonical_name | Preferred display name |
| entity_type | Company, Industry, Technology, … |
| aliases | All known surface forms |
| knowledge_score | Weighted composite (configurable) |
| confidence | Max observed confidence |
| first_seen / last_seen | Lifecycle timestamps |
| sources / atom_ids / document_ids | Provenance links |
| status | ACTIVE · MERGED · SUPERSEDED · ARCHIVED |
| created_session / updated_session | Learning session ids |
| provenance | Extractor version, atom origin |

## Resolution

1. `normalize_name(mention)`  
2. Lookup `indexes/canonical.json` then `indexes/alias.json`  
3. Hit → reuse, append alias/source/atom, recompute score  
4. Miss → create canonical entity, index keys  

**Never** creates a second ACTIVE entity for the same type+normalized name.

## Alias management

Corporate suffixes (`PT`, `Inc`, `Ltd`, …) stripped for matching.  
Original surface forms retained in `aliases[]`.

Example: `IBM` · `IBM Corp` · `International Business Machines` → one entity.

## Knowledge score

Weights in `automation/config/knowledge_graph.yaml` → `knowledge_score:`

| Component | Default weight |
|-----------|---------------:|
| confidence | 0.35 |
| richness | 0.25 |
| completeness | 0.20 |
| source_quality | 0.15 |
| relationship_potential | 0.05 (future-ready; 0 until edges exist) |

Weights are normalized at runtime — not hardcoded in scoring logic.

## Indexes (O(1) lookup)

| Index | Key → Value |
|-------|-------------|
| canonical | normalized_name → entity_id |
| alias | normalized_alias → entity_id |
| document | document_id → [entity_id] |
| atom | atom_id → [entity_id] |
| source | source_id → [entity_id] |

Path: `automation/knowledge/store/indexes/*.json`

## API

```python
from automation.knowledge import (
    process_document_entities,
    find_by_canonical,
    find_by_alias,
    get_entity,
    entity_stats,
    compute_knowledge_score,
)

summary = process_document_entities(doc_dict, session_id="SES-…")
eid = find_by_alias("Telkom Indonesia")
```

## Explicit non-goals

- Relationship extraction  
- Graph traversal  
- Dataset row manufacturing  

→ **Commit 3**
