# Graph → Dataset Mapping

**Commit 4** · Knowledge Manufacturing

## Entity → datasets

See `ENTITY_DATASET_MAP` in `automation/knowledge/manufacturing.py`.

## Relationship → extra datasets

| Predicate | Extra datasets |
|-----------|----------------|
| provides / offers / manufactures | product_catalog, solution_library |
| targets / serves | industry_library, opportunity_analysis |
| competes_with / partner_of | competitor_library, case_study_library |
| uses / integrates_with / depends_on | product_catalog, trend_library |
| implements / certified_by | framework_library |
| regulated_by | regulation_library, risk_library |
| managed_by | decision_maker_library, buyer_persona_library |
| located_in | company_profile |

## Neighbor enrichment

Outgoing/incoming edges fill Industry, Country, Technology fields on payloads  
before quality assessment — graph knowledge is not wasted.

## Rows generated

This layer emits **candidates**, not published rows.  
“Rows generated” in validation = candidate files in the manufacturing queue.
