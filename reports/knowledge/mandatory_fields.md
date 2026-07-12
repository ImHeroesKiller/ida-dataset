# Mandatory Field Policy

**Sprint:** Dataset Quality + Knowledge Graph Manufacturing  
**Date:** 2026-07-12  
**Config:** `automation/config/knowledge_quality.yaml` → `mandatory_fields`

## Rule

Rows missing any **mandatory** field for their target dataset:

- **must not** publish directly  
- **must** enter the enrichment path (`disposition: enrichment_queue`)

## Catalog (CSV column names)

| Dataset | Required |
|---------|----------|
| company_profile | Company Name, Industry, Country |
| product_catalog | Product Name, Product Category |
| service_library | Product Name, Product Description |
| industry_library | Industry Name, Industry Category |
| buyer_persona_library | Persona Name, Industry |
| decision_maker_library | Title, Industry |
| risk_library | Risk Name, Description |
| regulation_library | Regulation Name, Jurisdiction |
| trend_library | Trend Title, Description |
| competitor_library | Competitor Name, Industry Category |
| framework_library | Framework Name, Description |
| case_study_library | Case Name, Challenge |
| solution_library | Solution Name, Solution Description |
| pain_point_library | Pain Point, Description |
| opportunity_analysis | Opportunity Name, Opportunity Description |
| business_signal_library | Signal Name, Description |

## Implementation

```python
from automation.knowledge import mandatory_fields_for, assess_row

fields = mandatory_fields_for("regulation_library")
# ["Regulation Name", "Jurisdiction"]
```

Field names match **existing** domain CSV headers exactly.  
No schema redesign.

## Threshold interaction

Mandatory failures always force enrichment queue, even if overall completeness ≥ 70%.

Completeness threshold (`min_completeness_to_publish`) applies after mandatory checks pass.
