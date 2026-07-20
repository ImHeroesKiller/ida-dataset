# Validation Trace

**Generated:** 2026-07-20T09:45:20+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-4BE602C3945C · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000563 | non-empty Signal ID | SIG-000563 | Signal ID='SIG-000563' |
| primary_id_pattern | N/A | SIG-000563 | no pattern for dataset | SIG-000563 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000563 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000563 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260720 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260720-AA4668; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000563 | primary id present | SIG-000563 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000563', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000563 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000563 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000563`

## CAND-A9E110DF3597 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000561 | non-empty Signal ID | SIG-000561 | Signal ID='SIG-000561' |
| primary_id_pattern | N/A | SIG-000561 | no pattern for dataset | SIG-000561 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000561 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000561 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260720-A | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260720-AA4668; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000561 | primary id present | SIG-000561 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000561', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000561 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000561 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000561`

## CAND-72F03042AF64 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000560 | non-empty Signal ID | SIG-000560 | Signal ID='SIG-000560' |
| primary_id_pattern | N/A | SIG-000560 | no pattern for dataset | SIG-000560 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000560 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000560 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260720 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260720-AA4668; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000560 | primary id present | SIG-000560 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000560', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000560 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000560 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000560`

## CAND-51AA6CAE4A5A · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000564 | non-empty Signal ID | SIG-000564 | Signal ID='SIG-000564' |
| primary_id_pattern | N/A | SIG-000564 | no pattern for dataset | SIG-000564 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000564 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000564 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260720-A | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260720-AA4668; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000564 | primary id present | SIG-000564 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000564', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000564 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000564 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000564`

## CAND-DCADF6F71579 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000562 | non-empty Signal ID | SIG-000562 | Signal ID='SIG-000562' |
| primary_id_pattern | N/A | SIG-000562 | no pattern for dataset | SIG-000562 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000562 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000562 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260720 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260720-AA4668; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000562 | primary id present | SIG-000562 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000562', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000562 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000562 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000562`
