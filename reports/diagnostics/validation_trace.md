# Validation Trace

**Generated:** 2026-07-16T06:39:12+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-F14F3D2E38D5 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000297 | non-empty Signal ID | SIG-000297 | Signal ID='SIG-000297' |
| primary_id_pattern | N/A | SIG-000297 | no pattern for dataset | SIG-000297 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000297 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000297 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260716 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260716-7C1DE1; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000297 | primary id present | SIG-000297 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000297', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000297 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000297 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000297`

## CAND-DD38BC5C1A47 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-2430A598BF3B`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000299 | non-empty Signal ID | SIG-000299 | Signal ID='SIG-000299' |
| primary_id_pattern | N/A | SIG-000299 | no pattern for dataset | SIG-000299 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000299 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000299 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260716-7 | optional | present | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260716-7C1DE1; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000299 | primary id present | SIG-000299 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000299', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000299 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000299 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000299`

## CAND-105D33F3B5D9 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000296 | non-empty Signal ID | SIG-000296 | Signal ID='SIG-000296' |
| primary_id_pattern | N/A | SIG-000296 | no pattern for dataset | SIG-000296 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000296 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000296 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260716-7 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260716-7C1DE1; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000296 | primary id present | SIG-000296 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000296', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000296 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000296 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000296`

## CAND-66E64CF02399 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000298 | non-empty Signal ID | SIG-000298 | Signal ID='SIG-000298' |
| primary_id_pattern | N/A | SIG-000298 | no pattern for dataset | SIG-000298 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000298 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000298 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260716 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260716-7C1DE1; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000298 | primary id present | SIG-000298 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000298', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000298 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000298 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000298`

## CAND-0A5AE35D151F · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000295 | non-empty Signal ID | SIG-000295 | Signal ID='SIG-000295' |
| primary_id_pattern | N/A | SIG-000295 | no pattern for dataset | SIG-000295 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000295 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000295 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260716 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260716-7C1DE1; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000295 | primary id present | SIG-000295 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000295', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000295 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000295 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000295`
