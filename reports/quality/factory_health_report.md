# Factory Health Report

**Batch:** Production Batch-Q1  
**Generated:** 2026-07-10T15:45:44.143356+00:00  

---

## Overall Factory Health Score

# **72.0 / 100**

Weighted by product target size across audited dataset classes.

### Score components (per dataset)

| Dataset | Rows | Target | Coverage | Readiness | Conf | Dup | Fresh | Orphan% | Connect% | Schema | Valid | Export |
|---------|-----:|-------:|---------:|----------:|-----:|----:|------:|--------:|---------:|-------:|------:|-------:|
| industry_library | 50 | 250 | 20.0% | 77.2 | 0.859 | 0.0 | 100.0% | 28.0% | 89.0% | 100.0% | 100.0 | 100.0 |
| company_profile | 86 | 10000 | 0.9% | 69.4 | 0.895 | 0.0 | 100.0% | 29.1% | 53.0% | 85.0% | 70.9 | 90.8 |
| product_catalog | 123 | 5000 | 2.5% | 71.1 | 0.891 | 0.0 | 100.0% | 0.0% | 90.6% | 90.7% | 83.7 | 100.0 |
| service_library(logical) | 65 | 2000 | 3.2% | 71.6 | 0.89 | 0.0 | 100.0% | 0.0% | 50.0% | 92.1% | 70.8 | 100.0 |
| pain_point_library | 58 | 3000 | 1.9% | 70.8 | 0.888 | 0.0 | 100.0% | 0.0% | 92.6% | 90.3% | 100.0 | 100.0 |
| solution_library | 58 | 3000 | 1.9% | 69.2 | 0.879 | 0.0 | 100.0% | 0.0% | 50.0% | 84.4% | 100.0 | 90.1 |
| framework_library | 40 | 500 | 8.0% | 74.9 | 0.894 | 0.0 | 100.0% | 100.0% | 0.0% | 100.0% | 100.0 | 100.0 |
| case_study_library | 40 | 1000 | 4.0% | 71.1 | 0.86 | 0.0 | 100.0% | 0.0% | 100.0% | 91.7% | 100.0 | 100.0 |
| opportunity_analysis | 25 | 2000 | 1.2% | 65.3 |  | 0.0 | 100.0% | 0.0% | 100.0% | 100.0% | 0.0 | 85.0 |
| competitor_library | 0 | 1000 | 0.0% | 0.0 |  | 0.0 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0 | 0.0 |
| business_signal_library | 0 | 1000 | 0.0% | 0.0 |  | 0.0 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0 | 0.0 |
| discovery_question_library | 0 | 500 | 0.0% | 0.0 |  | 0.0 | 0.0% | 0.0% | 0.0% | 0.0% | 0.0 | 0.0 |

CSV: [`dataset_health.csv`](./dataset_health.csv)

---

## Which datasets are healthiest?

1. **industry_library** — readiness 77.2, validation 100.0, export 100.0
2. **framework_library** — readiness 74.9, validation 100.0, export 100.0
3. **service_library(logical)** — readiness 71.6, validation 70.8, export 100.0
4. **product_catalog** — readiness 71.1, validation 83.7, export 100.0
5. **case_study_library** — readiness 71.1, validation 100.0, export 100.0

## Which datasets have the most orphan pressure?

1. **framework_library** — orphan 100.0% (40 records)
2. **company_profile** — orphan 29.1% (25 records)
3. **industry_library** — orphan 28.0% (14 records)
4. **product_catalog** — orphan 0.0% (0 records)
5. **service_library(logical)** — orphan 0.0% (0 records)

## Lowest coverage (product targets)

- **competitor_library**: 0.0% (0/1000)
- **business_signal_library**: 0.0% (0/1000)
- **discovery_question_library**: 0.0% (0/500)
- **company_profile**: 0.9% (86/10000)
- **opportunity_analysis**: 1.2% (25/2000)
- **pain_point_library**: 1.9% (58/3000)
- **solution_library**: 1.9% (58/3000)
- **product_catalog**: 2.5% (123/5000)

---

## Factory answers (measurable)

| Question | Answer |
|----------|--------|
| Healthiest datasets? | See readiness ranking above |
| Most orphan entities? | See orphan ranking + orphan_entities.csv |
| Weakest relationships? | Solution→Framework; Persona/Reg/Competitor (0%); soft Company→Product |
| Ready for Batch-009? | **YES** — Industry+Company baselines met; persona deps satisfied at matrix gate |
| Factory Health Score | **72.0** |

---

## Notes

- Coverage always uses **product targets** from `automation/config/product_targets.yaml` (not sprint milestones).
- Freshness window: **90 days**.
- Service health is reported as logical class `service_library(logical)` counting `Product Type` containing Service.
