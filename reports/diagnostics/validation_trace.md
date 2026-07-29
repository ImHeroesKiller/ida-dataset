# Validation Trace

**Generated:** 2026-07-29T09:09:36+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-5AC593752965 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001038 | non-empty Signal ID | SIG-001038 | Signal ID='SIG-001038' |
| primary_id_pattern | N/A | SIG-001038 | no pattern for dataset | SIG-001038 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001038 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001038 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260729 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260729-BF0821; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001038 | primary id present | SIG-001038 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001038', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001038 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001038 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001038`

## CAND-91E0EBA3E646 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001039 | non-empty Signal ID | SIG-001039 | Signal ID='SIG-001039' |
| primary_id_pattern | N/A | SIG-001039 | no pattern for dataset | SIG-001039 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001039 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001039 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260729-B | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260729-BF0821; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001039 | primary id present | SIG-001039 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001039', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001039 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001039 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001039`

## CAND-4571B1F0ED5E · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001036 | non-empty Signal ID | SIG-001036 | Signal ID='SIG-001036' |
| primary_id_pattern | N/A | SIG-001036 | no pattern for dataset | SIG-001036 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001036 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001036 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260729-B | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260729-BF0821; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001036 | primary id present | SIG-001036 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001036', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001036 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001036 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001036`

## CAND-7D73F2DE14A0 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001037 | non-empty Signal ID | SIG-001037 | Signal ID='SIG-001037' |
| primary_id_pattern | N/A | SIG-001037 | no pattern for dataset | SIG-001037 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001037 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001037 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260729 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260729-BF0821; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001037 | primary id present | SIG-001037 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001037', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-001037 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001037 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001037`

## CAND-0A497AA82D72 · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001035 | non-empty Signal ID | SIG-001035 | Signal ID='SIG-001035' |
| primary_id_pattern | N/A | SIG-001035 | no pattern for dataset | SIG-001035 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001035 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001035 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260729 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260729-BF0821; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001035 | primary id present | SIG-001035 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001035', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001035 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001035 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001035`
