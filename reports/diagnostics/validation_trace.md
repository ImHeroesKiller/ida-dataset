# Validation Trace

**Generated:** 2026-08-11T22:10:26+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-AA24EFB54793 · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001925 | non-empty Signal ID | SIG-001925 | Signal ID='SIG-001925' |
| primary_id_pattern | N/A | SIG-001925 | no pattern for dataset | SIG-001925 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001925 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001925 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260811 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260811-BF03A5; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001925 | primary id present | SIG-001925 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001925', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001925 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001925 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001925`

## CAND-5FBC4BA175E5 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001928 | non-empty Signal ID | SIG-001928 | Signal ID='SIG-001928' |
| primary_id_pattern | N/A | SIG-001928 | no pattern for dataset | SIG-001928 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001928 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001928 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260811 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260811-BF03A5; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001928 | primary id present | SIG-001928 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001928', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001928 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001928 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001928`

## CAND-73CD0042554A · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001926 | non-empty Signal ID | SIG-001926 | Signal ID='SIG-001926' |
| primary_id_pattern | N/A | SIG-001926 | no pattern for dataset | SIG-001926 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001926 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001926 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260811-B | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260811-BF03A5; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001926 | primary id present | SIG-001926 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001926', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001926 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001926 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001926`

## CAND-90841643451B · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001929 | non-empty Signal ID | SIG-001929 | Signal ID='SIG-001929' |
| primary_id_pattern | N/A | SIG-001929 | no pattern for dataset | SIG-001929 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001929 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001929 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260811-B | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260811-BF03A5; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001929 | primary id present | SIG-001929 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001929', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001929 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001929 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001929`

## CAND-A0978E389F13 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001927 | non-empty Signal ID | SIG-001927 | Signal ID='SIG-001927' |
| primary_id_pattern | N/A | SIG-001927 | no pattern for dataset | SIG-001927 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001927 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001927 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260811 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260811-BF03A5; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001927 | primary id present | SIG-001927 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001927', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-001927 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001927 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001927`
