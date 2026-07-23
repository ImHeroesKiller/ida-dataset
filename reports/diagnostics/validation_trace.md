# Validation Trace

**Generated:** 2026-07-23T22:23:04+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-AC3B74F2B850 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000752 | non-empty Signal ID | SIG-000752 | Signal ID='SIG-000752' |
| primary_id_pattern | N/A | SIG-000752 | no pattern for dataset | SIG-000752 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000752 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000752 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260723 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260723-666283; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000752 | primary id present | SIG-000752 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000752', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000752 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000752 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000752`

## CAND-D2A64B10192D · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000751 | non-empty Signal ID | SIG-000751 | Signal ID='SIG-000751' |
| primary_id_pattern | N/A | SIG-000751 | no pattern for dataset | SIG-000751 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000751 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000751 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260723-6 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260723-666283; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000751 | primary id present | SIG-000751 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000751', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000751 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000751 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000751`

## CAND-5ABAB050B32B · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000750 | non-empty Signal ID | SIG-000750 | Signal ID='SIG-000750' |
| primary_id_pattern | N/A | SIG-000750 | no pattern for dataset | SIG-000750 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000750 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000750 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260723 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260723-666283; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000750 | primary id present | SIG-000750 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000750', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000750 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000750 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000750`

## CAND-3328277DE0CF · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000753 | non-empty Signal ID | SIG-000753 | Signal ID='SIG-000753' |
| primary_id_pattern | N/A | SIG-000753 | no pattern for dataset | SIG-000753 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000753 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000753 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260723 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260723-666283; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000753 | primary id present | SIG-000753 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000753', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000753 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000753 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000753`

## CAND-1CEB4B1790DF · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000754 | non-empty Signal ID | SIG-000754 | Signal ID='SIG-000754' |
| primary_id_pattern | N/A | SIG-000754 | no pattern for dataset | SIG-000754 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000754 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000754 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260723-6 | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260723-666283; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000754 | primary id present | SIG-000754 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000754', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000754 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000754 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000754`
