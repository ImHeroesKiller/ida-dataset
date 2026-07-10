# Next Production Candidates

**Batch:** Production Batch-Q1 — Continuous Production Preparation  
**Generated:** 2026-07-10T15:45:44.143356+00:00  
**Execution:** **NOT executed** (queue only)

---

## Is the factory ready for Batch-009?

| Gate | Status |
|------|--------|
| DPS v1.0 | Active |
| Dependency: Industry baseline (≥50) | PASS (50 rows) |
| Dependency: Company baseline (≥25) | PASS (86 rows) |
| Integrity audit complete | PASS |
| Relationship audit complete | PASS |
| **Batch-009 go** | **YES** |

---

## Top missing entities

- buyer_persona_library (0 rows)
- decision_maker_library (0 rows)
- regulation_library (0 rows)
- competitor_library (0 rows)
- business_signal_library (0 rows)
- discovery_question_library (0 rows)
- company_profile gap 9914 rows to target
- service_library gap 1935 rows to target
- product_catalog gap 4877 rows to target

## Top missing / weak relationships

- Competitor → Company: 0.0% coverage (competitor_library empty (Batch-015))
- Solution → Framework: 0.0% coverage (Supporting Framework populated and resolvable)
- Regulation → Industry: 0.0% coverage (regulation_library not produced yet (Batch-011))
- Buyer Persona → Company: 0.0% coverage (buyer_persona_library not produced yet (Batch-009))
- Decision Maker → Company: 0.0% coverage (decision_maker_library not produced yet (Batch-010))
- Risk → Company: 0.0% coverage (risk library not produced yet (Batch-013))
- Industry → Company: 73.3% coverage (Company rows with resolvable Industry ID/name)
- Company → Pain Point: 77.8% coverage (Soft link via Industry ID)

## Highest value production opportunities

1. **Batch-009 Buyer Persona** — unlock Decision Maker path; zero coverage today.  
2. **Batch-011 Regulation** — high trust sources (OJK/Kemenperin); strengthens Industry legal context.  
3. **Service/Product/Company expansion waves** — largest absolute row gaps to product targets.  
4. **Solution → Framework linking pass** — relationship coverage lift without new entity classes.  
5. **Opportunity FK repair + expansion** — seed broken company links; Batch-012 scale.

## Lowest coverage datasets (product %)

- competitor_library: 0.0%
- business_signal_library: 0.0%
- discovery_question_library: 0.0%
- company_profile: 0.9%
- opportunity_analysis: 1.2%
- pain_point_library: 1.9%
- solution_library: 1.9%
- product_catalog: 2.5%

## Highest quality trusted sources for next batch (Buyer Persona / general)

| Source ID | Name | Why |
|-----------|------|-----|
| SRC-000012 | KADIN | Industry association buyer/employer perspective |
| SRC-000013 | APINDO | Employer association labor/buyer context |
| SRC-000004 | World Bank | Sector structural knowledge |
| SRC-000005 | OECD | Digital/economic surveys |
| SRC-000001 | BPS | Official statistics segmentation |
| SRC-000010 | OJK | For later regulation/finance personas |

---

## Ranked production queue (do not execute here)

Official sequence is prioritized when dependencies are met. Expansion waves remain high-value for absolute row gaps.

| Rank | Batch | Title | Deps met | Current | Target | Coverage | Gap | Value score | Recommended sources |
|-----:|-------|-------|----------|--------:|-------:|---------:|----:|------------:|---------------------|
| 1 | Batch-009 | Buyer Persona | True | 0 | 500 | 0.0% | 500 | 125625.0 | SRC-000012 KADIN; SRC-000013 APINDO; SRC-000004 World Bank; SRC-000005 OECD |
| 2 | Batch-011 | Regulation | True | 0 | 1000 | 0.0% | 1000 | 101250.0 | SRC-000010 OJK; SRC-000007 Kemenperin; SRC-000011 Kemnaker; SRC-000014 LKPP |
| 3 | Batch-010 | Decision Maker | False | 0 | 500 | 0.0% | 500 | 90075.0 | SRC-000012; SRC-000013; SRC-000001; public org materials |
| 4 | Batch-013 | Risk | True | 0 | 100 | 0.0% | 100 | 75125.0 | SRC-000010; SRC-000004; SRC-000006 |
| 5 | Batch-012 | Opportunity | True | 25 | 2000 | 1.2% | 1975 | 71975.0 | SRC-000014 LKPP; SRC-000008 BKPM; SRC-000004 World Bank |
| 6 | Batch-014 | Trend | True | 0 | 100 | 0.0% | 100 | 62625.0 | SRC-000004; SRC-000005; SRC-000006; SRC-000001 |
| 7 | Batch-015 | Competitor | True | 0 | 1000 | 0.0% | 1000 | 51250.0 | Official publications; annual reports; SRC-000001 |
| 8 | Batch-004b | Company expansion | True | 86 | 10000 | 0.9% | 9914 | 9914.0 | IDX issuers; SRC-000001; SRC-000008; official sites |
| 9 | Batch-003b | Product expansion | True | 123 | 5000 | 2.5% | 4877 | 4877.0 | SRC-000005; SRC-000004; SRC-000009 |
| 10 | Batch-005b | Pain expansion | True | 58 | 3000 | 1.9% | 2942 | 2942.0 | SRC-000004; SRC-000010; SRC-000007 |
| 11 | Batch-006b | Solution expansion | True | 58 | 3000 | 1.9% | 2942 | 2942.0 | From verified pains + SRC-000005 |
| 12 | Batch-002b | Service expansion | True | 65 | 2000 | 3.2% | 1935 | 1935.0 | SRC-000011; SRC-000012; SRC-000004; SRC-000005 |
| 13 | Batch-008b | Case Study expansion | True | 40 | 1000 | 4.0% | 960 | 960.0 | Public annual/sustainability reports |
| 14 | Batch-007b | Framework expansion | True | 40 | 500 | 8.0% | 460 | 460.0 | Public standards overviews; SRC-000005 |
| 15 | Batch-001b | Industry expansion | True | 50 | 250 | 20.0% | 200 | 200.0 | SRC-000001; SRC-000007; SRC-000004 |

### Rationale

**1. Batch-009 Buyer Persona** — Official next production batch — execute first

**2. Batch-011 Regulation** — Empty high-value library

**3. Batch-010 Decision Maker** — Blocked until Batch-009 personas exist

**4. Batch-013 Risk** — Empty high-value library

**5. Batch-012 Opportunity** — Official sequence after personas

**6. Batch-014 Trend** — Empty high-value library

**7. Batch-015 Competitor** — Empty high-value library

**8. Batch-004b Company expansion** — Expansion toward product target

**9. Batch-003b Product expansion** — Expansion toward product target

**10. Batch-005b Pain expansion** — Expansion toward product target

**11. Batch-006b Solution expansion** — Expansion toward product target

**12. Batch-002b Service expansion** — Expansion toward product target

**13. Batch-008b Case Study expansion** — Expansion toward product target

**14. Batch-007b Framework expansion** — Expansion toward product target

**15. Batch-001b Industry expansion** — Expansion toward product target

---

## Recommended next action

1. **Execute Batch-009 Buyer Persona Dataset** under DPS (deps met).  
2. Then Batch-010 Decision Maker.  
3. Interleave Regulation (011) and expansion waves (Company/Product/Service) for maximum long-term coverage.  
4. Relationship hygiene: populate Solution→Framework links in a dedicated quality/production commit.

**Do not start Batch-009 inside this quality batch.**
