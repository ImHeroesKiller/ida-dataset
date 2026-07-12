# Edge Store Design

**Milestone 2 · Commit 3**  
**Date:** 2026-07-12

## Storage

| Artifact | Path |
|----------|------|
| Relationships | `automation/knowledge/store/relationships.json` |
| Edge key index | `…/indexes/edge_key.json` |
| Outgoing adjacency | `…/indexes/outgoing.json` |
| Incoming adjacency | `…/indexes/incoming.json` |
| Type index | `…/indexes/rel_type.json` |

Runtime store is gitignored (same policy as atoms/entities).

## Edge key

```text
{source_entity}|{relationship_type}|{target_entity}
```

Used for O(1) duplicate detection and `find_relationship()`.

## Confidence growth

On merge:

```text
confidence = min(0.99, max(old, new) + 0.03 * min(evidence_count, 5))
knowledge_score = 0.5*confidence + 0.3*evidence_factor + 0.2*source_factor
```

## Compatibility

| Surface | Impact |
|---------|--------|
| Scheduler / GHA / Mission / Queue | None |
| Dashboard / Export / HF | None |
| Dataset CSV schema | None |
| Entity / Atom APIs | Additive exports only |

## Production risk

| Risk | Mitigation |
|------|------------|
| Type-pair edges without verbs | Lower confidence (×0.85); competes_with requires compete cue |
| Fan-out on entity-rich atoms | Cap co-occurrence pairs (24 entities/atom) |
| Noisy company entities upstream | Edge quality inherits entity quality |
| Large JSON store | Batch upsert; shard later if needed |

## Graph growth metrics

`relationship_stats()` returns:

- relationship_count / active_count  
- by_type / by_status  
- average_degree  
- top_connected_entities  
