# Extraction Audit

**Generated:** 2026-07-11T13:38:49+00:00

## Yield per document (corpus)

| Metric | Value |
|--------|------:|
| Documents | 105 |
| Candidates total | 106 |
| Docs with candidates | 53 |
| Docs without candidates | 57 |
| Mean candidates/doc (all) | 1.01 |
| Mean candidates/doc (if any) | 2 |
| Max candidates for one doc | 24 |

## Trace extraction funnel

| Metric | Value |
|--------|------:|
| candidates_extracted | 130 |
| candidates_validated | 116 |
| candidates_rejected | 20 |
| rows_published | 110 |
| Extract→Validate | 89.23% |
| Validate→Publish | 94.83% |

## Extraction versions (candidates)

| Version | Count |
|---------|------:|
| `acquisition-library-1.0.0` | 82 |
| `acquisition-grounded-2.0.0` | 19 |
| `live-runtime-0.1.0` | 4 |
| `first-cycle-0.1.0` | 1 |

## Confidence

Mean **0.89** · Median **0.88**

| Band | N |
|------|--:|
| 0.80-0.91 manual/approved band | 87 |
| >=0.92 auto-publish band | 19 |

## Auto-publish vs manual (last lifecycle snapshot)

| Signal | Value |
|--------|------:|
| candidate_lifecycle primary block | duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000026 |
| integrity_blocked (last) | n/a |
| dry_run blocked publish (last) | True |

## Entities / signals by dataset (candidates)

| Dataset | Candidates |
|---------|----------:|
| competitor_library | 36 |
| risk_library | 18 |
| business_signal_library | 18 |
| trend_library | 11 |
| buyer_persona_library | 8 |
| industry_library | 6 |
| regulation_library | 6 |
| decision_maker_library | 3 |

## Finding

Extraction rarely multiplies knowledge: **max candidates on a single document = 24**, mean **1.01**.  
With mission-targeted datasets, one document → one library row is the dominant pattern.
