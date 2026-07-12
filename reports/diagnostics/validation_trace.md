# Validation Trace

**Generated:** 2026-07-12T11:31:27+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-F88023CF0DFE · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000096 | non-empty Signal ID | SIG-000096 | Signal ID='SIG-000096' |
| primary_id_pattern | N/A | SIG-000096 | no pattern for dataset | SIG-000096 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000096 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000096 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260712-6 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260712-66AB8E; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000096 | primary id present | SIG-000096 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000096', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000096 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000096 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000096`

## CAND-EB74A7F042D0 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000098 | non-empty Signal ID | SIG-000098 | Signal ID='SIG-000098' |
| primary_id_pattern | N/A | SIG-000098 | no pattern for dataset | SIG-000098 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000098 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000098 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260712 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260712-66AB8E; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000098 | primary id present | SIG-000098 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000098', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000098 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000098 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000098`

## CAND-6D09CFF0C911 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000097 | non-empty Signal ID | SIG-000097 | Signal ID='SIG-000097' |
| primary_id_pattern | N/A | SIG-000097 | no pattern for dataset | SIG-000097 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000097 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000097 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260712 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260712-66AB8E; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000097 | primary id present | SIG-000097 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000097', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000097 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000097 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000097`

## CAND-0353C4B3311E · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D733F4309CB6`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000099 | non-empty Signal ID | SIG-000099 | Signal ID='SIG-000099' |
| primary_id_pattern | N/A | SIG-000099 | no pattern for dataset | SIG-000099 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000099 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000099 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D733F4309CB6; mission=MIS-20260712-6 | optional | present | provenance: source=SRC-000004; document=DOC-D733F4309CB6; mission=MIS-20260712-66AB8E; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000099 | primary id present | SIG-000099 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000099', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000099 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000099 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000099`

## CAND-6E760DFEF276 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000095 | non-empty Signal ID | SIG-000095 | Signal ID='SIG-000095' |
| primary_id_pattern | N/A | SIG-000095 | no pattern for dataset | SIG-000095 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000095 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000095 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260712 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260712-66AB8E; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000095 | primary id present | SIG-000095 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000095', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000095 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000095 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000095`
