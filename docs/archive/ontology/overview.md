# Knowledge Ontology Engine — Overview

## Purpose

Define the semantic foundation of the IDA Knowledge Repository: a shared, versioned language for every human workflow and future agent.

## Status: Active (Sprint 2)

## Philosophy

The Knowledge Ontology Engine (KOE) is **not** a database and **not** a graph product.

It is a **domain-driven semantic contract**:

- Domain-driven — entities reflect real business language, not storage tables
- Extensible — new entities, properties, and relationships can be added without breaking IDs
- Versioned — `ontology_version.json` records compatibility
- Human-readable — CSV + Markdown
- Machine-readable — stable IDs, typed relationships, explicit rules
- Implementation-independent — works with CSV, PostgreSQL, Neo4j, RDF/OWL, property graphs, and vector metadata

## What KOE defines

| Layer | Location | Role |
| --- | --- | --- |
| Entities | `metadata/ontology/entities.csv` | Canonical concept classes |
| Entity types | `entity_types.csv` | Master / Reference / Transactional / … |
| Properties | `entity_properties.csv` | Attributes of entity classes |
| Synonyms | `entity_synonyms.csv` | Alternate terms → one canonical entity |
| Aliases | `entity_aliases.csv` | Real-world name variants for instances |
| Relationships | `relationships.csv` | Allowed directed semantic edges |
| Relationship types | `relationship_types.csv` | Vocabulary of edge labels |
| Relationship rules | `relationship_rules.csv` | Allowed / Forbidden constraints |
| Categories | `categories.csv` | Cross-cutting thematic tags |
| Domains | `domains.csv` | Operating domains (BD, Sales, HR, …) |
| Version | `ontology_version.json` | Version + compatibility matrix |

## What KOE does **not** define

- Business instance rows (companies, opportunities, products)
- Crawling or extraction behavior
- Graph database schemas proprietary to one vendor
- LLM prompts

Instance data remains under `domains/`, `relationships/`, and acquisition pipelines (KAS).

## Universal language for agents

Every future IDA agent should resolve language through KOE:

1. Map free text → synonym / alias  
2. Resolve to canonical entity  
3. Validate proposed edges against relationship rules  
4. Attach provenance outside the ontology  

## Future exports (no redesign required)

| Target | Mapping approach |
| --- | --- |
| PostgreSQL | Entity tables + FK relationship tables |
| Neo4j | Labels = Entity Name; types = Relationship |
| RDF / OWL | Classes + object properties |
| Property graph | Nodes + directed edges + properties |
| Vector DB | Embeddings keyed by Entity ID / instance ID + ontology metadata |

## Related docs

- [Entity model](entity_model.md)
- [Relationship model](relationship_model.md)
- [Naming conventions](naming_conventions.md)
- [Ontology rules](ontology_rules.md)
