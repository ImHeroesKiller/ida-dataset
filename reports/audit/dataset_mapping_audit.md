# Dataset Mapping Audit

**Generated:** 2026-07-11T13:38:49+00:00

## Expected multi-library behavior (product)

A rich document (e.g. annual report) should feed many libraries (company, service, industry, buyer, decision maker, trend, risk, competitor, technology, framework, case, regulation, …).

## Measured mapping

| Pattern | Documents | % |
|---------|----------:|--:|
| Contributes to **0** datasets | 57 | 54.29% |
| Contributes to **1** dataset | 45 | 42.86% |
| Contributes to **≥2** datasets | 3 | 2.86% |

## Why single-dataset dominance

Measured causes:

1. **Mission selects one `dataset`** per session (trace field `dataset`). 8/23 traces show candidates confined to the mission dataset.  
2. **Extractor versions** emit one entity_type aligned to mission (`acquisition-library-1.0.0`).  
3. **Source body is bibliographic JSON**, not multi-section reports — limited entities present.  
4. **57 docs** never receive a candidate (zero mapping).

## Dataset contribution counts (from candidates)

| Dataset | Candidate rows |
|---------|---------------:|
| competitor_library | 36 |
| risk_library | 18 |
| business_signal_library | 18 |
| trend_library | 11 |
| buyer_persona_library | 8 |
| industry_library | 6 |
| regulation_library | 6 |
| decision_maker_library | 3 |

## Domain CSV sizes (published knowledge)

| Dataset | CSV rows |
|---------|--------:|
| guidance | 249 |
| product_catalog | 123 |
| company_profile | 86 |
| pain_point_library | 58 |
| solution_library | 58 |
| industry_library | 53 |
| business_signal_library | 44 |
| case_study_library | 40 |
| framework_library | 40 |
| opportunity_analysis | 25 |
| risk_library | 10 |
| trend_library | 10 |
| competitor_library | 6 |
| regulation_library | 5 |
| buyer_persona_library | 4 |
| decision_maker_library | 3 |
| discovery_question_library | 0 |

## Example expectation vs reality

| Expected | Measured |
|----------|----------|
| 1 annual report → 10+ libraries | 1 API work JSON → 1 mission dataset (typical) |
| Multi-entity graph | Mean 1.01 candidates/doc |

## Conclusion

**Documents only contribute to one dataset primarily because extraction is mission-scoped and inputs are thin metadata records — not because validation strips multi-dataset rows.**
