# Validation Trace

**Generated:** 2026-07-20T22:19:43+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-AF1AEB685C3E · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000593 | non-empty Signal ID | SIG-000593 | Signal ID='SIG-000593' |
| primary_id_pattern | N/A | SIG-000593 | no pattern for dataset | SIG-000593 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000593 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000593 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260720-1 | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260720-1CFB11; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000593 | primary id present | SIG-000593 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000593', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000593 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000593 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000593`

## CAND-558E0CECD07B · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000591 | non-empty Signal ID | SIG-000591 | Signal ID='SIG-000591' |
| primary_id_pattern | N/A | SIG-000591 | no pattern for dataset | SIG-000591 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000591 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000591 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260720-1 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260720-1CFB11; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000591 | primary id present | SIG-000591 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000591', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000591 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000591 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000591`

## CAND-9621CD684E8A · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000592 | non-empty Signal ID | SIG-000592 | Signal ID='SIG-000592' |
| primary_id_pattern | N/A | SIG-000592 | no pattern for dataset | SIG-000592 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000592 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000592 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260720 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260720-1CFB11; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000592 | primary id present | SIG-000592 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000592', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000592 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000592 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000592`

## CAND-688028FB7544 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000590 | non-empty Signal ID | SIG-000590 | Signal ID='SIG-000590' |
| primary_id_pattern | N/A | SIG-000590 | no pattern for dataset | SIG-000590 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000590 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000590 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260720 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260720-1CFB11; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000590 | primary id present | SIG-000590 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000590', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000590 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000590 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000590`

## CAND-FF309FD27CB4 · Library Service Quality and Student Trust A Case Study of the University of Sumatera Utara Library, Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-05E7BC8EA754`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000594 | non-empty Signal ID | SIG-000594 | Signal ID='SIG-000594' |
| primary_id_pattern | N/A | SIG-000594 | no pattern for dataset | SIG-000594 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000594 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000594 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-05E7BC8EA754; mission=MIS-20260720 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-05E7BC8EA754; mission=MIS-20260720-1CFB11; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2021 | not enforced by integrity_guard | 2021 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000594 | primary id present | SIG-000594 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000594', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000594 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000594 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000594`
