# Validation Trace

**Generated:** 2026-08-09T02:10:01+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-575EA6E16423 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001678 | non-empty Signal ID | SIG-001678 | Signal ID='SIG-001678' |
| primary_id_pattern | N/A | SIG-001678 | no pattern for dataset | SIG-001678 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001678 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001678 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260809 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260809-69F877; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001678 | primary id present | SIG-001678 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001678', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001678 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001678 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001678`

## CAND-592C40F56EBF · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001679 | non-empty Signal ID | SIG-001679 | Signal ID='SIG-001679' |
| primary_id_pattern | N/A | SIG-001679 | no pattern for dataset | SIG-001679 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001679 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001679 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260809-6 | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260809-69F877; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001679 | primary id present | SIG-001679 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001679', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001679 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001679 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001679`

## CAND-101BF0FE925F · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001676 | non-empty Signal ID | SIG-001676 | Signal ID='SIG-001676' |
| primary_id_pattern | N/A | SIG-001676 | no pattern for dataset | SIG-001676 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001676 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001676 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260809-6 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260809-69F877; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001676 | primary id present | SIG-001676 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001676', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001676 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001676 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001676`

## CAND-83D6FEA2B5CA · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001675 | non-empty Signal ID | SIG-001675 | Signal ID='SIG-001675' |
| primary_id_pattern | N/A | SIG-001675 | no pattern for dataset | SIG-001675 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001675 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001675 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260809 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260809-69F877; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001675 | primary id present | SIG-001675 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001675', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001675 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001675 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001675`

## CAND-7BD775B6FCEF · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001677 | non-empty Signal ID | SIG-001677 | Signal ID='SIG-001677' |
| primary_id_pattern | N/A | SIG-001677 | no pattern for dataset | SIG-001677 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001677 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001677 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260809 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260809-69F877; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001677 | primary id present | SIG-001677 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001677', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-001677 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001677 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001677`
