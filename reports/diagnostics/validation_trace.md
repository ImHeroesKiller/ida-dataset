# Validation Trace

**Generated:** 2026-07-29T17:36:52+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-68A0CE1C3679 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001058 | non-empty Signal ID | SIG-001058 | Signal ID='SIG-001058' |
| primary_id_pattern | N/A | SIG-001058 | no pattern for dataset | SIG-001058 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001058 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001058 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260729 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260729-536726; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001058 | primary id present | SIG-001058 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001058', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001058 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001058 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001058`

## CAND-2D19BDB5865A · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001057 | non-empty Signal ID | SIG-001057 | Signal ID='SIG-001057' |
| primary_id_pattern | N/A | SIG-001057 | no pattern for dataset | SIG-001057 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001057 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001057 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260729 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260729-536726; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001057 | primary id present | SIG-001057 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001057', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-001057 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001057 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001057`

## CAND-5310A82B5B37 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001056 | non-empty Signal ID | SIG-001056 | Signal ID='SIG-001056' |
| primary_id_pattern | N/A | SIG-001056 | no pattern for dataset | SIG-001056 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001056 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001056 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260729-5 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260729-536726; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001056 | primary id present | SIG-001056 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001056', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001056 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001056 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001056`

## CAND-CE894317FA03 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001059 | non-empty Signal ID | SIG-001059 | Signal ID='SIG-001059' |
| primary_id_pattern | N/A | SIG-001059 | no pattern for dataset | SIG-001059 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001059 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001059 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260729-5 | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260729-536726; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001059 | primary id present | SIG-001059 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001059', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001059 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001059 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001059`

## CAND-19D4BF893B29 · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001055 | non-empty Signal ID | SIG-001055 | Signal ID='SIG-001055' |
| primary_id_pattern | N/A | SIG-001055 | no pattern for dataset | SIG-001055 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001055 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001055 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260729 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260729-536726; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001055 | primary id present | SIG-001055 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001055', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001055 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001055 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001055`
