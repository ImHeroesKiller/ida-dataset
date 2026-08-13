# Mission Trace

**Generated:** 2026-08-13T01:08:35+00:00
**Selected:** `industry_library` · score=908.2
**Reason:** mode=BOOTSTRAP · gap_score=0.0 · stretch_cov=0.4% · priority=100 · deps_met · sources=13 · continuous=true
**Instruction:** Produce Industry Dataset — expand industry_library toward product target

## All datasets

| Dataset | Rows | Coverage% | Gap score | Priority score | Eligible | Selected | Skip reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| industry_library | 18 | 0.4 | 87.563 | 908.2 | True | True | — |
| buyer_persona_library | 0 | 0.0 | 129.75 | — | False | False | dependency_not_met: industry_library<50 (have 18); company_profile<25 (have 0) |
| case_study_library | 0 | 0.0 | 132.75 | — | False | False | dependency_not_met: company_profile<25 (have 0); solution_library empty |
| company_profile | 0 | 0.0 | 134.25 | — | False | False | dependency_not_met: industry_library<50 (have 18) |
| competitor_library | 0 | 0.0 | 129.75 | — | False | False | dependency_not_met: industry_library<50 (have 18); company_profile<25 (have 0) |
| decision_maker_library | 0 | 0.0 | 125.25 | — | False | False | dependency_not_met: industry_library<50 (have 18); company_profile<25 (have 0) |
| framework_library | 0 | 0.0 | 125.25 | — | False | False | dependency_not_met: solution_library empty |
| opportunity_analysis | 0 | 0.0 | 131.25 | — | False | False | dependency_not_met: company_profile<25 (have 0); pain_point_library empty; solution_library empty |
| pain_point_library | 0 | 0.0 | 132.75 | — | False | False | dependency_not_met: industry_library<50 (have 18); company_profile<25 (have 0) |
| product_catalog | 0 | 0.0 | 125.25 | — | False | False | dependency_not_met: industry_library<50 (have 18) |
| regulation_library | 0 | 0.0 | 125.25 | — | False | False | dependency_not_met: industry_library<50 (have 18) |
| risk_library | 0 | 0.0 | 125.25 | — | False | False | dependency_not_met: industry_library<50 (have 18) |
| service_library | 0 | 0.0 | 125.25 | — | False | False | dependency_not_met: industry_library<50 (have 18) |
| solution_library | 0 | 0.0 | 133.5 | — | False | False | dependency_not_met: pain_point_library empty |
| trend_library | 0 | 0.0 | 125.25 | — | False | False | dependency_not_met: industry_library<50 (have 18) |

## Evidence

- Manufacturing mode: `BOOTSTRAP`
- Active sources: `13`
- Continuous: `True`
