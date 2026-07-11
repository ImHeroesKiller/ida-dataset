# Validation Trace

**Generated:** 2026-07-11T12:22:38+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-AB39F9418E9D · Nickel Downstream Industry

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-895A2B2798DA`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000054 | non-empty Industry ID | IND-000054 | Industry ID='IND-000054' |
| primary_id_pattern | PASS | IND-000054 | ^IND- | IND-000054 | pattern ^IND- vs 'IND-000054' |
| duplicate_id_in_batch | PASS | IND-000054 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | PASS | IND-000054 | id not in existing CSV | new_id | existing_csv_contains=False; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=1998; retrieved_date=2026-07-11T12:20:45+00:00; confidence=0.92; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=1998; retrieved_date=2026-07-11T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=1998; retrieved_date=2026-07-11T12:20:45+00:00; confidence=0.92; version=acquisition-grounde |
| freshness | N/A | 2026-07-11 | not enforced by integrity_guard | 2026-07-11 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000054 | primary id present | IND-000054 | primary id completeness |
| integrity_final_validate_row | PASS | {'Industry ID': 'IND-000054', 'confidence': 0.92} | validate_row ok | ok | automation.quality.integrity_guard.validate_row → ok |

**Integrity final:** `True` · reason=`ok`

## CAND-113BEDD08F27 · MSMEs / UMKM

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-66CDFCAF91C7`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000054 | non-empty Industry ID | IND-000054 | Industry ID='IND-000054' |
| primary_id_pattern | PASS | IND-000054 | ^IND- | IND-000054 | pattern ^IND- vs 'IND-000054' |
| duplicate_id_in_batch | PASS | IND-000054 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | PASS | IND-000054 | id not in existing CSV | new_id | existing_csv_contains=False; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-OPENALEX; published_date=2023-07-29; retrieved_date=2026-07-11T12:20:45+00:00; confidence=0.92; version=acquisition-g |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; published_date=2023-07-29; retrieved_date=2026- | Notes/Data Sources contain source markers | present | provenance: source=SRC-OPENALEX; published_date=2023-07-29; retrieved_date=2026-07-11T12:20:45+00:00; confidence=0.92; version=acquisition-g |
| freshness | N/A | 2026-07-11 | not enforced by integrity_guard | 2026-07-11 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000054 | primary id present | IND-000054 | primary id completeness |
| integrity_final_validate_row | PASS | {'Industry ID': 'IND-000054', 'confidence': 0.92} | validate_row ok | ok | automation.quality.integrity_guard.validate_row → ok |

**Integrity final:** `True` · reason=`ok`
