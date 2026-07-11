# Validation Trace

**Generated:** 2026-07-11T13:10:45+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-A2586EE1B9E4 · Startup Ecosystem

dataset=`industry_library` · confidence=`0.8375` · threshold=`0.8` · document=`DOC-C325082A3272`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000054 | non-empty Industry ID | IND-000054 | Industry ID='IND-000054' |
| primary_id_pattern | PASS | IND-000054 | ^IND- | IND-000054 | pattern ^IND- vs 'IND-000054' |
| duplicate_id_in_batch | PASS | IND-000054 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000054 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.84 | >= 0.8 | 0.84 | threshold=0.8; conf=0.84 |
| confidence_present | PASS | 0.84 | optional numeric confidence in Notes/Data Sources/Confidence | 0.84 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.84} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=; retrieved_date=2026-07-11T12:49:26+00:00; confidence=0.84; version=acquisition-grounded-2. |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=; retrieved_date=2026-07-11T12:4 | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=; retrieved_date=2026-07-11T12:49:26+00:00; confidence=0.84; version=acquisition-grounded-2. |
| freshness | N/A | 2026-07-11 | not enforced by integrity_guard | 2026-07-11 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000054 | primary id present | IND-000054 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000054', 'confidence': 0.84} | validate_row ok | duplicate_id:IND-000054 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000054 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000054`

## CAND-18CCB68EA40E · Cybersecurity Industry

dataset=`industry_library` · confidence=`0.8375` · threshold=`0.8` · document=`DOC-DED8E51BC76A`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000055 | non-empty Industry ID | IND-000055 | Industry ID='IND-000055' |
| primary_id_pattern | PASS | IND-000055 | ^IND- | IND-000055 | pattern ^IND- vs 'IND-000055' |
| duplicate_id_in_batch | PASS | IND-000055 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000055 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.84 | >= 0.8 | 0.84 | threshold=0.8; conf=0.84 |
| confidence_present | PASS | 0.84 | optional numeric confidence in Notes/Data Sources/Confidence | 0.84 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.84} | SRC-/source text OR conf present | ok | provenance: source=SRC-CISA; published_date=; retrieved_date=2026-07-11T13:07:20+00:00; confidence=0.84; version=acquisition-grounded-2.0.0; |
| provenance_present | PASS | provenance: source=SRC-CISA; published_date=; retrieved_date=2026-07-11T13:07:20 | Notes/Data Sources contain source markers | present | provenance: source=SRC-CISA; published_date=; retrieved_date=2026-07-11T13:07:20+00:00; confidence=0.84; version=acquisition-grounded-2.0.0; |
| freshness | N/A | 2026-07-11 | not enforced by integrity_guard | 2026-07-11 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000055 | primary id present | IND-000055 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000055', 'confidence': 0.84} | validate_row ok | duplicate_id:IND-000055 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000055 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000055`
