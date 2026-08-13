# Validation Trace

**Generated:** 2026-08-13T02:17:58+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-76D8F951A184 · Information Technology Services

dataset=`industry_library` · confidence=`0.855` · threshold=`0.8` · document=`DOC-AFB055C754E2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000019 | non-empty Industry ID | IND-000019 | Industry ID='IND-000019' |
| primary_id_pattern | PASS | IND-000019 | ^IND- | IND-000019 | pattern ^IND- vs 'IND-000019' |
| duplicate_id_in_batch | PASS | IND-000019 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000019 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.85} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2020; retrieved_date=2026-08-13T02:16:31+00:00; confidence=0.85; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2020; retrieved_date=2026-08-13T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2020; retrieved_date=2026-08-13T02:16:31+00:00; confidence=0.85; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000019 | primary id present | IND-000019 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000019', 'confidence': 0.85} | validate_row ok | duplicate_id:IND-000019 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000019 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000019`
