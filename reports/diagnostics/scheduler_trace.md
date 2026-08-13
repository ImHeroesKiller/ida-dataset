# Scheduler Trace

**Generated:** 2026-08-13T00:05:10+00:00

## Current mode

`BOOTSTRAP`

## Current mission

- Dataset: `industry_library`
- Title: `procurement — industry knowledge for Procurement`
- Instruction: procurement — industry knowledge for Procurement — continuous knowledge manufacturing for industry_library across enterprise function Procurement (function_gap=59.0; not BD-only); dataset_gap=87.823; mode=BOOTSTRAP
- Reason: mode=BOOTSTRAP · gap_score=87.823 · stretch_cov=0.3% · priority=100 · deps_met · sources=13 · continuous=true

## Heartbeat

| Field | Value |
| --- | --- |
| status | Idle |
| last_heartbeat | 2026-08-13T00:03:57+00:00 |
| last_success | 2026-08-13T00:03:57+00:00 |
| last_failure | — |
| current_job | — |
| job_duration_seconds | 1226.0 |
| last_error | — |

## Missions not selected (eligible or not)

| Dataset | Eligible | Score | Skip / not-selected reason |
| --- | --- | --- | --- |
| solution_library | True | 877.53 | eligible_but_not_selected; score=877.53 < selected=industry_library score=1904.83 |
| opportunity_analysis | True | 853.38 | eligible_but_not_selected; score=853.38 < selected=industry_library score=1904.83 |
| framework_library | True | 836.0 | eligible_but_not_selected; score=836.0 < selected=industry_library score=1904.83 |
| case_study_library | True | 831.0 | eligible_but_not_selected; score=831.0 < selected=industry_library score=1904.83 |
| buyer_persona_library | False | — | dependency_not_met: industry_library<50 (have 14) |
| company_profile | False | — | dependency_not_met: industry_library<50 (have 14) |
| competitor_library | False | — | dependency_not_met: industry_library<50 (have 14) |
| decision_maker_library | False | — | dependency_not_met: industry_library<50 (have 14) |
| pain_point_library | False | — | dependency_not_met: industry_library<50 (have 14) |
| product_catalog | False | — | dependency_not_met: industry_library<50 (have 14) |
| regulation_library | False | — | dependency_not_met: industry_library<50 (have 14) |
| risk_library | False | — | dependency_not_met: industry_library<50 (have 14) |
| service_library | False | — | dependency_not_met: industry_library<50 (have 14) |
| trend_library | False | — | dependency_not_met: industry_library<50 (have 14) |

## Next mission (rank #2 if any)
- `solution_library` score=877.53 cov=0.2
