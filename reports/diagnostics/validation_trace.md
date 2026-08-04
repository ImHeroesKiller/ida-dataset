# Validation Trace

**Generated:** 2026-08-04T16:32:02+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-ACF1EBC24A56 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001376 | non-empty Signal ID | SIG-001376 | Signal ID='SIG-001376' |
| primary_id_pattern | N/A | SIG-001376 | no pattern for dataset | SIG-001376 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001376 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001376 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260804-D | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260804-DAEBD6; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001376 | primary id present | SIG-001376 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001376', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001376 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001376 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001376`

## CAND-A0CA7591273B · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001378 | non-empty Signal ID | SIG-001378 | Signal ID='SIG-001378' |
| primary_id_pattern | N/A | SIG-001378 | no pattern for dataset | SIG-001378 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001378 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001378 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260804 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260804-DAEBD6; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001378 | primary id present | SIG-001378 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001378', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001378 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001378 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001378`

## CAND-781BE6D1A2F7 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001377 | non-empty Signal ID | SIG-001377 | Signal ID='SIG-001377' |
| primary_id_pattern | N/A | SIG-001377 | no pattern for dataset | SIG-001377 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001377 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001377 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260804 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260804-DAEBD6; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001377 | primary id present | SIG-001377 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001377', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-001377 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001377 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001377`

## CAND-4266184BBD4C · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001379 | non-empty Signal ID | SIG-001379 | Signal ID='SIG-001379' |
| primary_id_pattern | N/A | SIG-001379 | no pattern for dataset | SIG-001379 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001379 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001379 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260804-D | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260804-DAEBD6; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001379 | primary id present | SIG-001379 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001379', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001379 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001379 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001379`

## CAND-7B1162808D7C · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001375 | non-empty Signal ID | SIG-001375 | Signal ID='SIG-001375' |
| primary_id_pattern | N/A | SIG-001375 | no pattern for dataset | SIG-001375 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001375 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001375 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260804 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260804-DAEBD6; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001375 | primary id present | SIG-001375 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001375', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001375 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001375 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001375`
