# Relationship Model

## Purpose

Define directed semantic relationships between entity classes and the rules that allow or forbid them.

## Status: Active (Sprint 2)

## Relationship registry

File: `metadata/ontology/relationships.csv`

| Column | Meaning |
| --- | --- |
| Relationship ID | Stable ID (`REL-###`) |
| Source Entity / ID | Origin class |
| Relationship | Edge type name (e.g. `BELONGS_TO`) |
| Relationship Type ID | FK to `relationship_types.csv` |
| Target Entity / ID | Destination class |
| Description | Semantic meaning |
| Direction | `forward` or `bidirectional` |
| Status / Version | Lifecycle + ontology version |

These rows define **class-level patterns**, not instance triples.

Example patterns:

| Source | Relationship | Target |
| --- | --- | --- |
| Company | BELONGS_TO | Industry |
| Company | USES | Technology |
| Company | HAS | Opportunity |
| Opportunity | HAS | Pain Point |
| Pain Point | SOLVED_BY | Solution |
| Solution | IMPLEMENTED_USING | Product |
| Company | HAS | Department |
| Company | COMPETES_WITH | Company |
| Competitor | OFFERS | Product |
| Project | GENERATES | Case Study |

## Relationship types

File: `relationship_types.csv`

Core vocabulary includes:

HAS, BELONGS_TO, USES, OWNS, PROVIDES, GENERATES, IMPLEMENTS, SUPPORTS, DEPENDS_ON, COMPETES_WITH, REPORTS_TO, LOCATED_IN, MANAGES, RELATED_TO, SOLVED_BY, IMPLEMENTED_USING, OFFERS, EMPLOYS, TARGETS, REFERENCES.

### Direction semantics

| Direction | Meaning |
| --- | --- |
| forward | Edge is asserted source → target |
| bidirectional | Either orientation is semantically valid; store one canonical orientation in instances when possible |

## Relationship rules

File: `relationship_rules.csv`

| Constraint | Meaning |
| --- | --- |
| Allowed | Pattern may be used by datasets / agents |
| Forbidden | Pattern must be rejected by validators |

Examples:

| Source | Relationship | Target | Constraint |
| --- | --- | --- | --- |
| Company | BELONGS_TO | Industry | Allowed |
| Pain Point | SOLVED_BY | Solution | Allowed |
| Industry | SOLVED_BY | Company | Forbidden |

## Relationship semantics guidelines

1. Prefer precise verbs over `RELATED_TO` when meaning is known  
2. Do not encode instance data in ontology relationships  
3. Forbidden rules document anti-patterns for automated validation  
4. Cardinality is intentionally deferred (export-specific)  
5. Inverse edges are not duplicated unless direction is bidirectional  

## Mapping to future graphs

| KOE concept | Graph mapping |
| --- | --- |
| Entity Name | Node label / RDF class |
| Relationship | Edge type / object property |
| Direction | Edge orientation |
| Relationship rule Allowed | Schema allow-list |
| Relationship rule Forbidden | Schema deny-list |
