# Mission Trace

**Generated:** 2026-08-13T00:05:10+00:00
**Selected:** `industry_library` · score=1904.83
**Reason:** mode=BOOTSTRAP · gap_score=87.823 · stretch_cov=0.3% · priority=100 · deps_met · sources=13 · continuous=true
**Instruction:** procurement — industry knowledge for Procurement — continuous knowledge manufacturing for industry_library across enterprise function Procurement (function_gap=59.0; not BD-only); dataset_gap=87.823; mode=BOOTSTRAP

## All datasets

| Dataset | Rows | Coverage% | Gap score | Priority score | Eligible | Selected | Skip reason |
| --- | --- | --- | --- | --- | --- | --- | --- |
| industry_library | 14 | 0.3 | 87.823 | 1904.83 | True | True | — |
| solution_library | 58 | 0.2 | 78.268 | 877.53 | True | False | eligible_but_not_selected; score=877.53 < selected=industry_library score=1904.83 |
| opportunity_analysis | 25 | 0.1 | 77.176 | 853.38 | True | False | eligible_but_not_selected; score=853.38 < selected=industry_library score=1904.83 |
| framework_library | 40 | 0.8 | 79.188 | 836.0 | True | False | eligible_but_not_selected; score=836.0 < selected=industry_library score=1904.83 |
| case_study_library | 40 | 0.4 | 77.693 | 831.0 | True | False | eligible_but_not_selected; score=831.0 < selected=industry_library score=1904.83 |
| buyer_persona_library | 4 | 0.1 | 83.547 | — | False | False | dependency_not_met: industry_library<50 (have 14) |
| company_profile | 86 | 0.1 | 89.563 | — | False | False | dependency_not_met: industry_library<50 (have 14) |
| competitor_library | 6 | 0.0 | 89.305 | — | False | False | dependency_not_met: industry_library<50 (have 14) |
| decision_maker_library | 3 | 0.1 | 81.115 | — | False | False | dependency_not_met: industry_library<50 (have 14) |
| pain_point_library | 58 | 0.2 | 88.031 | — | False | False | dependency_not_met: industry_library<50 (have 14) |
| product_catalog | 123 | 0.2 | 88.606 | — | False | False | dependency_not_met: industry_library<50 (have 14) |
| regulation_library | 5 | 0.1 | 80.401 | — | False | False | dependency_not_met: industry_library<50 (have 14) |
| risk_library | 10 | 0.2 | 81.852 | — | False | False | dependency_not_met: industry_library<50 (have 14) |
| service_library | 65 | 0.1 | 112.922 | — | False | False | dependency_not_met: industry_library<50 (have 14) |
| trend_library | 10 | 0.2 | 80.502 | — | False | False | dependency_not_met: industry_library<50 (have 14) |

## Evidence

- Manufacturing mode: `BOOTSTRAP`
- Active sources: `13`
- Continuous: `True`
