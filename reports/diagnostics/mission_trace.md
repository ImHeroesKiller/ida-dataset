# Mission Trace

**Generated:** 2026-08-18T16:43:35+00:00
**Selected:** `industry_library` · score=908.1
**Reason:** mode=BOOTSTRAP · gap_score=0.0 · stretch_cov=0.4% · priority=100 · deps_met · sources=13 · continuous=true
**Instruction:** Produce Industry Dataset — expand industry_library toward product target

## All datasets

| Dataset | Rows | Coverage% | Gap score | Priority score | Eligible | Selected | Skip reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| industry_library | 19 | 0.4 | 87.568 | 908.1 | True | True | — |
| buyer_persona_library | 0 | 0.0 | 129.75 | — | False | False | dependency_not_met: industry_library<50 (have 19); company_profile<25 (have 0) |
| case_study_library | 0 | 0.0 | 132.75 | — | False | False | dependency_not_met: company_profile<25 (have 0); solution_library empty |
| company_profile | 0 | 0.0 | 134.25 | — | False | False | dependency_not_met: industry_library<50 (have 19) |
| competitor_library | 0 | 0.0 | 129.75 | — | False | False | dependency_not_met: industry_library<50 (have 19); company_profile<25 (have 0) |
| decision_maker_library | 0 | 0.0 | 125.25 | — | False | False | dependency_not_met: industry_library<50 (have 19); company_profile<25 (have 0) |
| framework_library | 0 | 0.0 | 125.25 | — | False | False | dependency_not_met: solution_library empty |
| opportunity_analysis | 0 | 0.0 | 131.25 | — | False | False | dependency_not_met: company_profile<25 (have 0); pain_point_library empty; solution_library empty |
| pain_point_library | 0 | 0.0 | 132.75 | — | False | False | dependency_not_met: industry_library<50 (have 19); company_profile<25 (have 0) |
| product_catalog | 0 | 0.0 | 125.25 | — | False | False | dependency_not_met: industry_library<50 (have 19) |
| regulation_library | 0 | 0.0 | 125.25 | — | False | False | dependency_not_met: industry_library<50 (have 19) |
| risk_library | 0 | 0.0 | 125.25 | — | False | False | dependency_not_met: industry_library<50 (have 19) |
| service_library | 0 | 0.0 | 125.25 | — | False | False | dependency_not_met: industry_library<50 (have 19) |
| solution_library | 0 | 0.0 | 133.5 | — | False | False | dependency_not_met: pain_point_library empty |
| trend_library | 0 | 0.0 | 125.25 | — | False | False | dependency_not_met: industry_library<50 (have 19) |

## Evidence

- Manufacturing mode: `BOOTSTRAP`
- Active sources: `13`
- Continuous: `True`
