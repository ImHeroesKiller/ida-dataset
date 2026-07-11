# Validation Trace

**Generated:** 2026-07-11T08:50:31+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-F04B1DEAECD0 · Industry 4.0 in Management Studies: A Systematic Literature Review

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-BC12979C0BEE`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000026 | non-empty Signal ID | SIG-000026 | Signal ID='SIG-000026' |
| primary_id_pattern | N/A | SIG-000026 | no pattern for dataset | SIG-000026 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000026 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000026 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-BC12979C0BEE; mission=MIS-20260711 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-BC12979C0BEE; mission=MIS-20260711-1B1B1E; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2018-10-22 | not enforced by integrity_guard | 2018-10-22 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000026 | primary id present | SIG-000026 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000026', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000026 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000026 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000026`

## CAND-D03DE2F0A439 · K-popnomics: How Indonesia and other nations can learn from Korean pop music industry

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-030B58207BDD`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000027 | non-empty Signal ID | SIG-000027 | Signal ID='SIG-000027' |
| primary_id_pattern | N/A | SIG-000027 | no pattern for dataset | SIG-000027 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000027 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000027 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-030B58207BDD; mission=MIS-20260711 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-030B58207BDD; mission=MIS-20260711-1B1B1E; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000027 | primary id present | SIG-000027 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000027', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000027 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000027 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000027`

## CAND-7528E4183942 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-1C7ABF5820D1`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000025 | non-empty Signal ID | SIG-000025 | Signal ID='SIG-000025' |
| primary_id_pattern | N/A | SIG-000025 | no pattern for dataset | SIG-000025 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000025 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000025 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-1C7ABF5820D1; mission=MIS-20260711-1 | optional | present | provenance: source=SRC-000004; document=DOC-1C7ABF5820D1; mission=MIS-20260711-1B1B1E; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000025 | primary id present | SIG-000025 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000025', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000025 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000025 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000025`
