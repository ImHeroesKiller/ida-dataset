# Validation Trace

**Generated:** 2026-07-22T19:42:25+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-CB49AB834D1F · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000696 | non-empty Signal ID | SIG-000696 | Signal ID='SIG-000696' |
| primary_id_pattern | N/A | SIG-000696 | no pattern for dataset | SIG-000696 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000696 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000696 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260722-2 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260722-296991; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000696 | primary id present | SIG-000696 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000696', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000696 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000696 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000696`

## CAND-3D1283D9D7F7 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000698 | non-empty Signal ID | SIG-000698 | Signal ID='SIG-000698' |
| primary_id_pattern | N/A | SIG-000698 | no pattern for dataset | SIG-000698 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000698 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000698 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260722-2 | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260722-296991; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000698 | primary id present | SIG-000698 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000698', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000698 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000698 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000698`

## CAND-A67D5C7BA37C · Library Service Quality and Student Trust A Case Study of the University of Sumatera Utara Library, Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-05E7BC8EA754`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000699 | non-empty Signal ID | SIG-000699 | Signal ID='SIG-000699' |
| primary_id_pattern | N/A | SIG-000699 | no pattern for dataset | SIG-000699 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000699 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000699 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-05E7BC8EA754; mission=MIS-20260722 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-05E7BC8EA754; mission=MIS-20260722-296991; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2021 | not enforced by integrity_guard | 2021 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000699 | primary id present | SIG-000699 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000699', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000699 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000699 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000699`

## CAND-EF90D1E6493C · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000697 | non-empty Signal ID | SIG-000697 | Signal ID='SIG-000697' |
| primary_id_pattern | N/A | SIG-000697 | no pattern for dataset | SIG-000697 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000697 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000697 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260722 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260722-296991; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000697 | primary id present | SIG-000697 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000697', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000697 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000697 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000697`

## CAND-2C87EB53EBAD · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000695 | non-empty Signal ID | SIG-000695 | Signal ID='SIG-000695' |
| primary_id_pattern | N/A | SIG-000695 | no pattern for dataset | SIG-000695 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000695 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000695 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260722 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260722-296991; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000695 | primary id present | SIG-000695 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000695', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000695 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000695 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000695`
