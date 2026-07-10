# Ontology Naming Conventions

## Purpose

Define canonical naming, ID prefixes, synonym policy, and alias policy for KOE.

## Status: Active (Sprint 2)

## File naming

- All ontology filenames are **lowercase** with underscores  
- Encoding: **UTF-8**  
- Line endings: **LF**  
- Path: `metadata/ontology/`

## Stable ID prefixes

| Prefix | Object |
| --- | --- |
| `ENT-` | Entity |
| `ETYPE-` | Entity type |
| `EPROP-` | Entity property |
| `ESYN-` | Entity synonym |
| `EALS-` | Entity alias |
| `REL-` | Relationship |
| `RTYPE-` | Relationship type |
| `RRULE-` | Relationship rule |
| `CAT-` | Category |
| `DOM-` | Domain |

Rules:

- IDs are immutable once published  
- Never reuse an ID for a different meaning  
- Prefer append-only numbering  
- Deprecate rather than delete when possible  

## Canonical entity naming

| Rule | Example |
| --- | --- |
| Use singular nouns | `Company` not `Companies` |
| Prefer business language | `Pain Point` not `IssueRecord` |
| Title Case for multi-word names | `Business Process`, `Case Study` |
| Avoid storage jargon | no `tbl_`, no `fk_` |
| One concept per entity | do not merge Product and Solution |

## Canonical relationship naming

| Rule | Example |
| --- | --- |
| UPPER_SNAKE_CASE verbs/phrases | `BELONGS_TO`, `SOLVED_BY` |
| Directional reading source → target | Company `USES` Technology |
| Prefer strong verbs | `GENERATES` over vague `LINKS_TO` |
| Reserve `RELATED_TO` for weak links | only when no better verb exists |

## Synonym policy

File: `entity_synonyms.csv`

Synonyms map **linguistic variants** to exactly **one** canonical entity class.

| Allowed | Not allowed |
| --- | --- |
| AI → Technology | One synonym → multiple entities |
| ERP → Product | Synonym creating a new ontology class silently |
| CEO → Role | Using synonym rows for company brand aliases |

Policy:

1. Every synonym has one `Canonical Entity ID`  
2. Synonyms are not entities  
3. Language tag is required (`en`, `id`, …)  
4. Ambiguous terms must include notes  
5. Instance brands belong in aliases, not synonyms  

## Alias policy

File: `entity_aliases.csv`

Aliases map **real-world surface names** for the same instance concept pattern:

| Canonical | Alias | Entity class |
| --- | --- | --- |
| Microsoft | MSFT | Company |
| IBM | International Business Machines | Company |
| PLN | Perusahaan Listrik Negara | Company |

Policy:

1. Aliases do not create new entity classes  
2. Alias rows in KOE are illustrative / registry-level patterns  
3. Production company instances still live in `domains/**` datasets  
4. Matching should normalize case and punctuation before compare  
5. Prefer legal name as canonical when known; keep brand as alias  

## Property naming

- Use human-readable Title Case labels aligned with dataset columns when practical  
- Examples: `Company Name`, `Pricing Model`, `Implementation Complexity`  
- Do not invent parallel names for the same field without a migration note  

## Version field

Every ontology CSV row carries `Version` matching `ontology_version.json` major lineage (e.g. `1.0.0`).
