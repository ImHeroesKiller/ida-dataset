# Knowledge Integrity Report

**Batch:** Production Batch-Q1  
**Generated:** 2026-07-10T15:45:44.143356+00:00  
**Mode:** Observe / validate / measure only  
**Schema changes:** none  
**Dataset rewrites:** none  

---

## Executive summary

| Metric | Value |
|--------|------:|
| Datasets audited | 11 |
| Integrity issues | 268 |
| Orphan entity records | 79 |
| High severity | 104 |
| Medium severity | 101 |
| Low severity | 55 |
| Info | 8 |

### Issue type breakdown

| Issue type | Count |
|------------|------:|
| orphan | 79 |
| missing_provenance_confidence | 70 |
| missing_version | 45 |
| broken_reference | 36 |
| missing_provenance | 20 |
| weak_industry_link | 10 |
| missing_validation_status_field | 8 |

---

## Checks performed

- Orphan entities (missing/broken required links)
- Broken references (FK-like ID references)
- Missing foreign keys
- Duplicate IDs and duplicate canonical names
- Alias / name conflicts
- Invalid ID patterns
- Invalid dataset references
- Invalid confidence (&lt; 0.80)
- Missing provenance (sources / SRC / Data Sources)
- Missing freshness (Last Updated)
- Missing version markers in Notes
- Missing validation status (**field absent in frozen schemas** — inferred only)

---

## Critical findings

1. **Industry ID scheme mismatch on seed companies:** many seed `company_profile` rows use short IDs (e.g. `IND-001`) while `industry_library` uses `IND-000001`. Batch-004 companies link correctly; seed rows often soft-match by name only.
2. **Product → Pain/Solution seed refs** may point to non-existent PAIN/SOL IDs from pre-production seed data.
3. **Opportunity seed rows** frequently reference Company IDs not present in expanded company set → broken FKs.
4. **Solution → Framework** links are almost empty (`Supporting Framework` not populated) → frameworks orphaned from solutions.
5. **No Validation Status column** exists in domain schemas (frozen). Validation is inferred from confidence + provenance.
6. **Pain points without solutions** should be zero after Batch-006; remaining orphans are mostly frameworks, industries without downstream, and soft industry mismatches.

---

## Orphan summary by dataset

| Dataset | Orphan count |
|---------|-------------:|
| framework_library | 40 |
| company_profile | 25 |
| industry_library | 14 |
| product_catalog | 0 |
| service_library(logical) | 0 |
| pain_point_library | 0 |
| solution_library | 0 |
| case_study_library | 0 |
| opportunity_analysis | 0 |
| competitor_library | 0 |
| business_signal_library | 0 |
| discovery_question_library | 0 |

Full detail: [`orphan_entities.csv`](./orphan_entities.csv)  
Full issues: [`integrity_issues.csv`](./integrity_issues.csv)

---

## Append-only correction policy

This batch **does not rewrite** datasets.  
Allowed later (separate production commits only):

- Append corrected rows with new IDs (never overwrite)
- Append alias / mapping notes via mission reports
- Do **not** silent-fix seed IDs in place without versioned audit

---

## Conclusion

Integrity is **good enough to continue Batch-009** for net-new libraries (persona), while **relationship hardening** (Solution→Framework, Company industry IDs, Opportunity FKs) should be prioritized in parallel expansion batches.

**Ready for Batch-009?** **YES** (with known integrity debt documented).
