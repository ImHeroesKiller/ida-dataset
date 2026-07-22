# Validation Trace

**Generated:** 2026-07-22T10:45:11+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-C0D1EB49AEA7 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000679 | non-empty Signal ID | SIG-000679 | Signal ID='SIG-000679' |
| primary_id_pattern | N/A | SIG-000679 | no pattern for dataset | SIG-000679 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000679 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000679 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260722-E | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260722-E9B88C; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000679 | primary id present | SIG-000679 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000679', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000679 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000679 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000679`

## CAND-160C8D564E36 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000676 | non-empty Signal ID | SIG-000676 | Signal ID='SIG-000676' |
| primary_id_pattern | N/A | SIG-000676 | no pattern for dataset | SIG-000676 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000676 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000676 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260722-E | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260722-E9B88C; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000676 | primary id present | SIG-000676 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000676', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000676 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000676 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000676`

## CAND-77B5DDCD57DC · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000678 | non-empty Signal ID | SIG-000678 | Signal ID='SIG-000678' |
| primary_id_pattern | N/A | SIG-000678 | no pattern for dataset | SIG-000678 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000678 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000678 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260722 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260722-E9B88C; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000678 | primary id present | SIG-000678 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000678', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000678 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000678 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000678`

## CAND-C05900938D52 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000677 | non-empty Signal ID | SIG-000677 | Signal ID='SIG-000677' |
| primary_id_pattern | N/A | SIG-000677 | no pattern for dataset | SIG-000677 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000677 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000677 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260722 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260722-E9B88C; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000677 | primary id present | SIG-000677 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000677', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000677 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000677 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000677`

## CAND-0C1DA2019826 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000675 | non-empty Signal ID | SIG-000675 | Signal ID='SIG-000675' |
| primary_id_pattern | N/A | SIG-000675 | no pattern for dataset | SIG-000675 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000675 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000675 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260722 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260722-E9B88C; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000675 | primary id present | SIG-000675 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000675', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000675 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000675 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000675`
