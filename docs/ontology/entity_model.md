# Entity Model

## Purpose

Describe entity classes, types, properties, lifecycle, and specialization via parent entities.

## Status: Active (Sprint 2)

## Entity registry

File: `metadata/ontology/entities.csv`

| Column | Meaning |
| --- | --- |
| Entity ID | Stable ID (`ENT-###`) |
| Entity Name | Canonical class name |
| Entity Type | Logical type label |
| Entity Type ID | FK to `entity_types.csv` |
| Category | Thematic category label |
| Category ID | FK to `categories.csv` |
| Description | Human definition |
| Parent Entity | Optional superclass name |
| Parent Entity ID | Optional superclass ID |
| Status | `active` / `deprecated` |
| Version | Ontology version string |

## Entity types

File: `entity_types.csv`

| Type | Use |
| --- | --- |
| Master | Durable business objects (Company, Product, Asset) |
| Reference | Lookups and classifications (Industry, Country, Role) |
| Transactional | Events and commercial objects (Opportunity, Meeting, Contract) |
| Knowledge | Reusable intellectual assets (Solution, Framework, Case Study) |
| External | Boundary objects (Vendor, Competitor, Source) |
| System | Platform objects (Dataset) |
| Configuration | Control objects (Policy) |

## Properties

File: `entity_properties.csv`

Properties describe **class attributes**, not instance values.

Example rows conceptually:

- Company **has** Company Name  
- Industry **has** Description  
- Product **has** Pricing Model  
- Pain Point **has** Severity  
- Solution **has** Implementation Complexity  

Data types used:

| Data Type | Intent |
| --- | --- |
| string | Short text |
| text | Long text |
| integer / number | Numeric |
| url | URI |
| enum | Constrained vocabulary (often `metadata/enums/`) |
| entity_ref | Reference to another entity instance |

## Entity lifecycle

```text
proposed → active → deprecated → retired
```

| State | Meaning |
| --- | --- |
| proposed | Drafted, not used by validators |
| active | Canonical and valid for new data |
| deprecated | Still resolved for old data; no new writes preferred |
| retired | Historical only; mapping required for readers |

Sprint 2 ships entities as `active`.

## Specialization (parent hierarchy)

Parent links express **is-a / specialization** between classes, for example:

- Customer → Company  
- Vendor → Company  
- Competitor → Company  
- Country → Location  
- Service → Product  

Rules:

- Parent must exist  
- No cycles  
- Parent is optional  
- Parent is for ontology reasoning, not for replacing BELONGS_TO instance edges  

## Core entity examples

Company, Industry, Product, Solution, Pain Point, Technology, Framework, Regulation, Standard, Department, Business Process, KPI, Role, Persona, Country, City, Vendor, Competitor, Project, Case Study, Document, Source, Risk, Opportunity, Meeting, Proposal, Contract, Customer, Partner, Asset.
