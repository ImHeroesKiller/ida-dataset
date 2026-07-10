# Ontology Rules

## Purpose

Define integrity rules for KOE CSV validation and future agent checks.

## Status: Active (Sprint 2)

## Scope

Validation is **CSV-only** in Sprint 2. No graph database is required.

Validator entrypoint:

```bash
python automation/ci/validate_ontology.py
```

## Integrity checks

| Check | Severity | Description |
| --- | --- | --- |
| Duplicate entities | error | Same Entity ID or Entity Name twice |
| Duplicate relationships | error | Same source + relationship + target twice |
| Missing parents | error | Parent Entity set but ID/name unresolved |
| Orphan entities | warning | Entity never used in relationships, properties, synonyms, or aliases (may be intentional) |
| Invalid relationship types | error | Relationship label not in `relationship_types.csv` |
| Cyclic parent hierarchy | error | Parent chain loops |
| Invalid references | error | FK-like IDs pointing to missing rows |
| Forbidden rule conflicts | error | Same triple marked both Allowed and Forbidden |
| Synonym uniqueness | error | Same synonym maps to two different entities |
| Status/version presence | warning | Missing status or version fields |

## Relationship rule evaluation

For a proposed triple `(Source, Relationship, Target)`:

1. If an **Forbidden** rule matches → reject  
2. Else if an **Allowed** rule matches → accept  
3. Else → reject by default (allow-list mode)

This fail-closed posture keeps agents from inventing edges.

## Parent hierarchy rules

- Parent references must resolve to an existing entity  
- Cycles are forbidden  
- Depth is unlimited but should stay shallow in practice  
- Parent is class specialization, not an instance edge  

## Compatibility rules

From `ontology_version.json`:

- `compatible_dataset_version` — repository `VERSION` lineage supported  
- `compatible_kas_version` — KAS package lineage supported  

Breaking ontology changes require a version bump and migration notes.

## Non-goals for this validator

- Does not validate business dataset contents under `domains/`  
- Does not write or rewrite ontology files  
- Does not call external APIs  
- Does not require Neo4j/RDF tooling  

## Extension rules

When adding ontology content:

1. Append new IDs; do not renumber  
2. Add Allowed rules for every new relationship  
3. Add Forbidden rules for known anti-patterns when discovered  
4. Update `ontology_version.json` counts and `updated` date  
5. Run `validate_ontology.py` before commit  
