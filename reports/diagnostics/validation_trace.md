# Validation Trace

**Generated:** 2026-08-06T03:01:18+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-B80C05EDDD87 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001452 | non-empty Signal ID | SIG-001452 | Signal ID='SIG-001452' |
| primary_id_pattern | N/A | SIG-001452 | no pattern for dataset | SIG-001452 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001452 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001452 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260806 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260806-001B6C; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001452 | primary id present | SIG-001452 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001452', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-001452 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001452 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001452`

## CAND-43D2977EF7F5 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001453 | non-empty Signal ID | SIG-001453 | Signal ID='SIG-001453' |
| primary_id_pattern | N/A | SIG-001453 | no pattern for dataset | SIG-001453 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001453 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001453 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260806 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260806-001B6C; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001453 | primary id present | SIG-001453 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001453', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001453 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001453 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001453`

## CAND-FCC87FDEB30F · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001454 | non-empty Signal ID | SIG-001454 | Signal ID='SIG-001454' |
| primary_id_pattern | N/A | SIG-001454 | no pattern for dataset | SIG-001454 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001454 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001454 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260806-0 | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260806-001B6C; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001454 | primary id present | SIG-001454 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001454', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001454 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001454 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001454`

## CAND-EB26131F3B27 · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001450 | non-empty Signal ID | SIG-001450 | Signal ID='SIG-001450' |
| primary_id_pattern | N/A | SIG-001450 | no pattern for dataset | SIG-001450 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001450 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001450 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260806 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260806-001B6C; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001450 | primary id present | SIG-001450 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001450', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001450 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001450 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001450`

## CAND-8683BF2DA0E0 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001451 | non-empty Signal ID | SIG-001451 | Signal ID='SIG-001451' |
| primary_id_pattern | N/A | SIG-001451 | no pattern for dataset | SIG-001451 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001451 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001451 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260806-0 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260806-001B6C; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001451 | primary id present | SIG-001451 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001451', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001451 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001451 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001451`
