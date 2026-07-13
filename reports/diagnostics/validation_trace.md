# Validation Trace

**Generated:** 2026-07-13T03:49:36+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-0E154371F102 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000142 | non-empty Signal ID | SIG-000142 | Signal ID='SIG-000142' |
| primary_id_pattern | N/A | SIG-000142 | no pattern for dataset | SIG-000142 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000142 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000142 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260713 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260713-FE8C0B; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000142 | primary id present | SIG-000142 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000142', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000142 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000142 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000142`

## CAND-057E0F95E4F2 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000140 | non-empty Signal ID | SIG-000140 | Signal ID='SIG-000140' |
| primary_id_pattern | N/A | SIG-000140 | no pattern for dataset | SIG-000140 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000140 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000140 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260713 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260713-FE8C0B; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000140 | primary id present | SIG-000140 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000140', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000140 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000140 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000140`

## CAND-B59CEE88B30C · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000141 | non-empty Signal ID | SIG-000141 | Signal ID='SIG-000141' |
| primary_id_pattern | N/A | SIG-000141 | no pattern for dataset | SIG-000141 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000141 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000141 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260713-F | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260713-FE8C0B; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000141 | primary id present | SIG-000141 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000141', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000141 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000141 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000141`

## CAND-97CA4973200A · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-2430A598BF3B`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000144 | non-empty Signal ID | SIG-000144 | Signal ID='SIG-000144' |
| primary_id_pattern | N/A | SIG-000144 | no pattern for dataset | SIG-000144 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000144 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000144 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260713-F | optional | present | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260713-FE8C0B; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000144 | primary id present | SIG-000144 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000144', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000144 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000144 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000144`

## CAND-A60C102E97F0 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000143 | non-empty Signal ID | SIG-000143 | Signal ID='SIG-000143' |
| primary_id_pattern | N/A | SIG-000143 | no pattern for dataset | SIG-000143 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000143 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000143 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260713 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260713-FE8C0B; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000143 | primary id present | SIG-000143 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000143', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000143 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000143 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000143`
