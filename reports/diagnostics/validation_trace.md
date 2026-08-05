# Validation Trace

**Generated:** 2026-08-05T13:14:15+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-93A3D7CC4190 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001423 | non-empty Signal ID | SIG-001423 | Signal ID='SIG-001423' |
| primary_id_pattern | N/A | SIG-001423 | no pattern for dataset | SIG-001423 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001423 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001423 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260805-1 | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260805-199512; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001423 | primary id present | SIG-001423 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001423', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001423 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001423 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001423`

## CAND-D407350299E9 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001422 | non-empty Signal ID | SIG-001422 | Signal ID='SIG-001422' |
| primary_id_pattern | N/A | SIG-001422 | no pattern for dataset | SIG-001422 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001422 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001422 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260805 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260805-199512; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001422 | primary id present | SIG-001422 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001422', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001422 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001422 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001422`

## CAND-3480E98C3CEA · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001424 | non-empty Signal ID | SIG-001424 | Signal ID='SIG-001424' |
| primary_id_pattern | N/A | SIG-001424 | no pattern for dataset | SIG-001424 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001424 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001424 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260805 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260805-199512; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001424 | primary id present | SIG-001424 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001424', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001424 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001424 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001424`

## CAND-0011AB4C4C32 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001421 | non-empty Signal ID | SIG-001421 | Signal ID='SIG-001421' |
| primary_id_pattern | N/A | SIG-001421 | no pattern for dataset | SIG-001421 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001421 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001421 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260805-1 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260805-199512; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001421 | primary id present | SIG-001421 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001421', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001421 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001421 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001421`

## CAND-A98665157EA6 · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001420 | non-empty Signal ID | SIG-001420 | Signal ID='SIG-001420' |
| primary_id_pattern | N/A | SIG-001420 | no pattern for dataset | SIG-001420 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001420 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001420 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260805 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260805-199512; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001420 | primary id present | SIG-001420 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001420', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001420 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001420 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001420`
