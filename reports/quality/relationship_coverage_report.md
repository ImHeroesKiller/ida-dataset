# Relationship Coverage Report

**Batch:** Production Batch-Q1  
**Generated:** 2026-07-10T15:45:44.143356+00:00  

---

## Connectivity matrix

| Relationship | Current Links | Possible Links | Coverage % | Missing Links | Orphan Count | Notes |
|--------------|--------------:|---------------:|-----------:|--------------:|-------------:|-------|
| Industry → Company | 63 | 86 | 73.3% | 23 | 23 | Company rows with resolvable Industry ID/name |
| Industry → Pain Point | 58 | 58 | 100.0% | 0 | 0 | Pain.Industry ID ∈ industry_library |
| Industry → Service | 55 | 65 | 84.6% | 10 | 10 | Service rows with Target Industry matching industry names |
| Industry → Product | 57 | 58 | 98.3% | 1 | 1 | Non-service product rows with Target Industry match |
| Company → Product | 57 | 63 | 90.5% | 6 | 29 | Soft link via shared industry (no Company ID on product schema) |
| Company → Service | 56 | 63 | 88.9% | 7 | 30 | Soft link via shared industry |
| Company → Pain Point | 49 | 63 | 77.8% | 14 | 37 | Soft link via Industry ID |
| Pain Point → Solution | 58 | 58 | 100.0% | 0 | 0 | solution.Related Pain ID → pain |
| Solution → Framework | 0 | 58 | 0.0% | 58 | 58 | Supporting Framework populated and resolvable |
| Company → Case Study | 40 | 40 | 100.0% | 0 | 46 | case.Company ID ∈ company_profile; many companies still without cases |
| Opportunity → Company | 25 | 25 | 100.0% | 0 | 0 | opportunity.Company ID ∈ company_profile |
| Regulation → Industry | 0 | 0 | 0.0% | 0 | 0 | regulation_library not produced yet (Batch-011) |
| Buyer Persona → Company | 0 | 0 | 0.0% | 0 | 0 | buyer_persona_library not produced yet (Batch-009) |
| Decision Maker → Company | 0 | 0 | 0.0% | 0 | 0 | decision_maker_library not produced yet (Batch-010) |
| Risk → Company | 0 | 0 | 0.0% | 0 | 0 | risk library not produced yet (Batch-013) |
| Competitor → Company | 0 | 86 | 0.0% | 86 | 86 | competitor_library empty (Batch-015) |
| Trend → Industry | 50 | 50 | 100.0% | 0 | 0 | trend library not produced; industry Industry Trends field only |

---

## Strongest relationships

- **Industry → Pain Point**: 100.0%
- **Pain Point → Solution**: 100.0%
- **Company → Case Study**: 100.0%
- **Opportunity → Company**: 100.0%
- **Trend → Industry**: 100.0%

## Weakest relationships

- **Competitor → Company**: 0.0% — competitor_library empty (Batch-015)
- **Solution → Framework**: 0.0% — Supporting Framework populated and resolvable
- **Regulation → Industry**: 0.0% — regulation_library not produced yet (Batch-011)
- **Buyer Persona → Company**: 0.0% — buyer_persona_library not produced yet (Batch-009)
- **Decision Maker → Company**: 0.0% — decision_maker_library not produced yet (Batch-010)
- **Risk → Company**: 0.0% — risk library not produced yet (Batch-013)
- **Industry → Company**: 73.3% — Company rows with resolvable Industry ID/name
- **Company → Pain Point**: 77.8% — Soft link via Industry ID

---

## Interpretation

1. **Pain Point → Solution** should be near 100% after Batch-006 (1:1 spine).
2. **Industry → Company** quality depends on resolving seed Industry ID mismatches.
3. **Company → Product/Service** are **soft** links only (no Company ID on product schema) — measured via shared industry.
4. **Solution → Framework** is the weakest produced-library link (Supporting Framework empty).
5. **Persona / Regulation / Competitor / Risk** relationships are **0%** because datasets are not produced yet.

Detail samples: [`missing_relationships.csv`](./missing_relationships.csv)
