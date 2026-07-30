# Validation Trace

**Generated:** 2026-07-30T16:47:07+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-407122850648 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001110 | non-empty Signal ID | SIG-001110 | Signal ID='SIG-001110' |
| primary_id_pattern | N/A | SIG-001110 | no pattern for dataset | SIG-001110 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001110 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001110 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260730 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260730-522584; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001110 | primary id present | SIG-001110 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001110', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001110 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001110 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001110`

## CAND-82F7532AEFAC · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001112 | non-empty Signal ID | SIG-001112 | Signal ID='SIG-001112' |
| primary_id_pattern | N/A | SIG-001112 | no pattern for dataset | SIG-001112 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001112 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001112 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260730 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260730-522584; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001112 | primary id present | SIG-001112 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001112', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-001112 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001112 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001112`

## CAND-5362ED51506C · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001113 | non-empty Signal ID | SIG-001113 | Signal ID='SIG-001113' |
| primary_id_pattern | N/A | SIG-001113 | no pattern for dataset | SIG-001113 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001113 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001113 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260730 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260730-522584; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001113 | primary id present | SIG-001113 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001113', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001113 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001113 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001113`

## CAND-9A027E7A50B6 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001114 | non-empty Signal ID | SIG-001114 | Signal ID='SIG-001114' |
| primary_id_pattern | N/A | SIG-001114 | no pattern for dataset | SIG-001114 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001114 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001114 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260730-5 | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260730-522584; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001114 | primary id present | SIG-001114 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001114', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001114 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001114 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001114`

## CAND-F116DFEA6F4E · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001111 | non-empty Signal ID | SIG-001111 | Signal ID='SIG-001111' |
| primary_id_pattern | N/A | SIG-001111 | no pattern for dataset | SIG-001111 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001111 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001111 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260730-5 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260730-522584; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001111 | primary id present | SIG-001111 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001111', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001111 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001111 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001111`
