# Validation Trace

**Generated:** 2026-08-11T04:05:47+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-DF4287F714EB · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001866 | non-empty Signal ID | SIG-001866 | Signal ID='SIG-001866' |
| primary_id_pattern | N/A | SIG-001866 | no pattern for dataset | SIG-001866 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001866 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001866 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260811-F | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260811-FD301D; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001866 | primary id present | SIG-001866 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001866', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001866 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001866 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001866`

## CAND-6D39D1C14DC1 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001867 | non-empty Signal ID | SIG-001867 | Signal ID='SIG-001867' |
| primary_id_pattern | N/A | SIG-001867 | no pattern for dataset | SIG-001867 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001867 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001867 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260811 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260811-FD301D; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001867 | primary id present | SIG-001867 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001867', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-001867 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001867 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001867`

## CAND-F09E0DF164D5 · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001865 | non-empty Signal ID | SIG-001865 | Signal ID='SIG-001865' |
| primary_id_pattern | N/A | SIG-001865 | no pattern for dataset | SIG-001865 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001865 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001865 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260811 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260811-FD301D; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001865 | primary id present | SIG-001865 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001865', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001865 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001865 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001865`

## CAND-644069F7A29A · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001868 | non-empty Signal ID | SIG-001868 | Signal ID='SIG-001868' |
| primary_id_pattern | N/A | SIG-001868 | no pattern for dataset | SIG-001868 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001868 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001868 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260811 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260811-FD301D; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001868 | primary id present | SIG-001868 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001868', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001868 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001868 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001868`

## CAND-04076EA94FA9 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001869 | non-empty Signal ID | SIG-001869 | Signal ID='SIG-001869' |
| primary_id_pattern | N/A | SIG-001869 | no pattern for dataset | SIG-001869 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001869 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001869 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260811-F | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260811-FD301D; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001869 | primary id present | SIG-001869 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001869', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001869 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001869 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001869`
