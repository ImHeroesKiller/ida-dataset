# Validation Trace

**Generated:** 2026-07-12T18:23:54+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-0D1D5D7F7FD4 · Green Industry

dataset=`industry_library` · confidence=`0.8375` · threshold=`0.8` · document=`DOC-DC77D354F7EF`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000058 | non-empty Industry ID | IND-000058 | Industry ID='IND-000058' |
| primary_id_pattern | PASS | IND-000058 | ^IND- | IND-000058 | pattern ^IND- vs 'IND-000058' |
| duplicate_id_in_batch | PASS | IND-000058 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000058 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.84 | >= 0.8 | 0.84 | threshold=0.8; conf=0.84 |
| confidence_present | PASS | 0.84 | optional numeric confidence in Notes/Data Sources/Confidence | 0.84 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.84} | SRC-/source text OR conf present | ok | provenance: source=SRC-000007; published_date=; retrieved_date=2026-07-12T18:21:46+00:00; confidence=0.84; version=acquisition-grounded-2.0. |
| provenance_present | PASS | provenance: source=SRC-000007; published_date=; retrieved_date=2026-07-12T18:21: | Notes/Data Sources contain source markers | present | provenance: source=SRC-000007; published_date=; retrieved_date=2026-07-12T18:21:46+00:00; confidence=0.84; version=acquisition-grounded-2.0. |
| freshness | N/A | 2026-07-12 | not enforced by integrity_guard | 2026-07-12 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000058 | primary id present | IND-000058 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000058', 'confidence': 0.84} | validate_row ok | duplicate_id:IND-000058 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000058 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000058`
