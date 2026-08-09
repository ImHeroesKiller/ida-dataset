# Validation Trace

**Generated:** 2026-08-09T20:59:10+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-B4A503AA9CFE · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001764 | non-empty Signal ID | SIG-001764 | Signal ID='SIG-001764' |
| primary_id_pattern | N/A | SIG-001764 | no pattern for dataset | SIG-001764 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001764 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001764 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260809-3 | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260809-3AC9C5; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001764 | primary id present | SIG-001764 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001764', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001764 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001764 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001764`

## CAND-511A46538066 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001762 | non-empty Signal ID | SIG-001762 | Signal ID='SIG-001762' |
| primary_id_pattern | N/A | SIG-001762 | no pattern for dataset | SIG-001762 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001762 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001762 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260809 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260809-3AC9C5; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001762 | primary id present | SIG-001762 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001762', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-001762 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001762 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001762`

## CAND-27ED6EBF1C37 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001763 | non-empty Signal ID | SIG-001763 | Signal ID='SIG-001763' |
| primary_id_pattern | N/A | SIG-001763 | no pattern for dataset | SIG-001763 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001763 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001763 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260809 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260809-3AC9C5; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001763 | primary id present | SIG-001763 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001763', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001763 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001763 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001763`

## CAND-316BBBDB1899 · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001760 | non-empty Signal ID | SIG-001760 | Signal ID='SIG-001760' |
| primary_id_pattern | N/A | SIG-001760 | no pattern for dataset | SIG-001760 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001760 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001760 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260809 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260809-3AC9C5; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001760 | primary id present | SIG-001760 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001760', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001760 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001760 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001760`

## CAND-798DC8D891A1 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001761 | non-empty Signal ID | SIG-001761 | Signal ID='SIG-001761' |
| primary_id_pattern | N/A | SIG-001761 | no pattern for dataset | SIG-001761 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001761 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001761 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260809-3 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260809-3AC9C5; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001761 | primary id present | SIG-001761 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001761', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001761 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001761 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001761`
