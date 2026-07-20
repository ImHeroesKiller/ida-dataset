# Validation Trace

**Generated:** 2026-07-20T18:24:03+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-0A2AD84BB8D1 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000581 | non-empty Signal ID | SIG-000581 | Signal ID='SIG-000581' |
| primary_id_pattern | N/A | SIG-000581 | no pattern for dataset | SIG-000581 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000581 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000581 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260720-E | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260720-EBD45F; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000581 | primary id present | SIG-000581 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000581', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000581 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000581 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000581`

## CAND-93D94C9F6E56 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000582 | non-empty Signal ID | SIG-000582 | Signal ID='SIG-000582' |
| primary_id_pattern | N/A | SIG-000582 | no pattern for dataset | SIG-000582 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000582 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000582 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260720 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260720-EBD45F; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000582 | primary id present | SIG-000582 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000582', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000582 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000582 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000582`

## CAND-21543B64DA49 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000584 | non-empty Signal ID | SIG-000584 | Signal ID='SIG-000584' |
| primary_id_pattern | N/A | SIG-000584 | no pattern for dataset | SIG-000584 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000584 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000584 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260720-E | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260720-EBD45F; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000584 | primary id present | SIG-000584 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000584', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000584 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000584 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000584`

## CAND-A306E6CB64F3 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000583 | non-empty Signal ID | SIG-000583 | Signal ID='SIG-000583' |
| primary_id_pattern | N/A | SIG-000583 | no pattern for dataset | SIG-000583 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000583 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000583 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260720 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260720-EBD45F; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000583 | primary id present | SIG-000583 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000583', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000583 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000583 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000583`

## CAND-1CCE2E47DF00 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000580 | non-empty Signal ID | SIG-000580 | Signal ID='SIG-000580' |
| primary_id_pattern | N/A | SIG-000580 | no pattern for dataset | SIG-000580 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000580 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000580 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260720 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260720-EBD45F; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000580 | primary id present | SIG-000580 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000580', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000580 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000580 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000580`
