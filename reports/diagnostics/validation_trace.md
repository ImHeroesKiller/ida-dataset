# Validation Trace

**Generated:** 2026-07-28T02:59:20+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-A0F43FB5B469 · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000980 | non-empty Signal ID | SIG-000980 | Signal ID='SIG-000980' |
| primary_id_pattern | N/A | SIG-000980 | no pattern for dataset | SIG-000980 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000980 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000980 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260728 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260728-48056C; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000980 | primary id present | SIG-000980 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000980', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000980 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000980 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000980`

## CAND-A8DC4938F56F · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000983 | non-empty Signal ID | SIG-000983 | Signal ID='SIG-000983' |
| primary_id_pattern | N/A | SIG-000983 | no pattern for dataset | SIG-000983 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000983 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000983 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260728 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260728-48056C; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000983 | primary id present | SIG-000983 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000983', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000983 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000983 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000983`

## CAND-DBA6EF2FBD52 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000982 | non-empty Signal ID | SIG-000982 | Signal ID='SIG-000982' |
| primary_id_pattern | N/A | SIG-000982 | no pattern for dataset | SIG-000982 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000982 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000982 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260728 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260728-48056C; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000982 | primary id present | SIG-000982 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000982', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000982 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000982 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000982`

## CAND-29E0C835FA8D · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000981 | non-empty Signal ID | SIG-000981 | Signal ID='SIG-000981' |
| primary_id_pattern | N/A | SIG-000981 | no pattern for dataset | SIG-000981 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000981 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000981 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260728-4 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260728-48056C; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000981 | primary id present | SIG-000981 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000981', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000981 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000981 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000981`

## CAND-A57D11D39C45 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000984 | non-empty Signal ID | SIG-000984 | Signal ID='SIG-000984' |
| primary_id_pattern | N/A | SIG-000984 | no pattern for dataset | SIG-000984 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000984 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000984 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260728-4 | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260728-48056C; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000984 | primary id present | SIG-000984 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000984', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000984 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000984 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000984`
