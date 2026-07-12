# Relationship Intelligence Layer

**Milestone 2 · Commit 3**  
**Date:** 2026-07-12  
**Status:** Implemented  
**Constraint:** No dataset rows · no manufacturing wiring · additive only

## Flow

```text
Knowledge Atom + Canonical Entities
        ↓
  Co-occurrence + verb cues + type-pair defaults
        ↓
  Relationship candidate
        ↓
  Edge key lookup (source|type|target)
        ↓
  Create OR merge (↑ confidence, append provenance)
```

## Taxonomy (no `related_to`)

| Family | Predicates |
|--------|------------|
| Business | provides, offers, manufactures, distributes |
| Organization | owns, managed_by, subsidiary_of, founded_by |
| Market | targets, serves, competes_with |
| Technology | uses, depends_on, integrates_with, replaces, implements |
| Governance | regulated_by, certified_by, audited_by |
| Geography | located_in, operates_in, headquartered_in |
| Supply Chain | supplied_by, partner_of, purchased_from |

## Relationship object

| Field | Notes |
|-------|--------|
| relationship_id | `REL-{sha1-12}` of edge key |
| source_entity / target_entity | Canonical entity ids |
| relationship_type | Taxonomy predicate only |
| confidence | Grows on repeated evidence |
| knowledge_score | conf + evidence + sources |
| provenance.evidence[] | atom_id, session, confidence, at |
| atom_id / atom_ids | Evidence links |
| session_id | Last writer session |
| first_seen / last_seen | first_seen immutable on merge |
| status | ACTIVE · MERGED · SUPERSEDED · ARCHIVED |
| evidence_count | Merge counter |

## Resolution

Duplicate edges **do not** create new rows. Merge:

- `confidence` increases (capped)
- `evidence_count` += 1  
- provenance trail append  
- `last_seen` update  
- `first_seen` preserved  

## Edge store

```text
automation/knowledge/store/relationships.json
automation/knowledge/store/indexes/
  edge_key.json
  outgoing.json
  incoming.json
  rel_type.json
```

## Query API

```python
from automation.knowledge import (
    find_relationship,
    incoming,
    outgoing,
    neighbors,
    relationship_stats,
    process_document_relationships,
    taxonomy_catalog,
)

process_document_relationships(doc, session_id="SES-…")
find_relationship(src, "targets", tgt)
outgoing(entity_id)
incoming(entity_id)
neighbors(entity_id)
relationship_stats()
```

## Non-goals

- Dataset row generation  
- Manufacturing pipeline hooks  
- Reasoning / inference beyond stored edges  
