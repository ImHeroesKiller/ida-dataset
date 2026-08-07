# Validation Trace

**Generated:** 2026-08-07T21:01:04+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-0965B1BC78DC · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001545 | non-empty Signal ID | SIG-001545 | Signal ID='SIG-001545' |
| primary_id_pattern | N/A | SIG-001545 | no pattern for dataset | SIG-001545 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001545 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001545 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260807 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260807-16F23A; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001545 | primary id present | SIG-001545 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001545', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001545 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001545 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001545`

## CAND-515F969C737D · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001548 | non-empty Signal ID | SIG-001548 | Signal ID='SIG-001548' |
| primary_id_pattern | N/A | SIG-001548 | no pattern for dataset | SIG-001548 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001548 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001548 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260807 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260807-16F23A; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001548 | primary id present | SIG-001548 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001548', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001548 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001548 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001548`

## CAND-62F1B995C858 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001546 | non-empty Signal ID | SIG-001546 | Signal ID='SIG-001546' |
| primary_id_pattern | N/A | SIG-001546 | no pattern for dataset | SIG-001546 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001546 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001546 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260807-1 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260807-16F23A; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001546 | primary id present | SIG-001546 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001546', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001546 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001546 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001546`

## CAND-B92E57CDB3B3 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001549 | non-empty Signal ID | SIG-001549 | Signal ID='SIG-001549' |
| primary_id_pattern | N/A | SIG-001549 | no pattern for dataset | SIG-001549 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001549 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001549 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260807-1 | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260807-16F23A; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001549 | primary id present | SIG-001549 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001549', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001549 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001549 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001549`

## CAND-0BDC5EEA2C5F · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001547 | non-empty Signal ID | SIG-001547 | Signal ID='SIG-001547' |
| primary_id_pattern | N/A | SIG-001547 | no pattern for dataset | SIG-001547 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001547 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001547 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260807 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260807-16F23A; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001547 | primary id present | SIG-001547 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001547', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-001547 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001547 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001547`
