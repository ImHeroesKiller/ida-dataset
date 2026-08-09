# Validation Trace

**Generated:** 2026-08-09T05:25:14+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-FE1B7B8AFA81 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001687 | non-empty Signal ID | SIG-001687 | Signal ID='SIG-001687' |
| primary_id_pattern | N/A | SIG-001687 | no pattern for dataset | SIG-001687 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001687 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001687 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260809 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260809-7D2AAA; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001687 | primary id present | SIG-001687 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001687', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-001687 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001687 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001687`

## CAND-714EA768C8AF · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001686 | non-empty Signal ID | SIG-001686 | Signal ID='SIG-001686' |
| primary_id_pattern | N/A | SIG-001686 | no pattern for dataset | SIG-001686 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001686 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001686 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260809-7 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260809-7D2AAA; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001686 | primary id present | SIG-001686 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001686', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001686 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001686 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001686`

## CAND-BC43C1233A8C · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001685 | non-empty Signal ID | SIG-001685 | Signal ID='SIG-001685' |
| primary_id_pattern | N/A | SIG-001685 | no pattern for dataset | SIG-001685 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001685 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001685 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260809 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260809-7D2AAA; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001685 | primary id present | SIG-001685 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001685', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001685 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001685 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001685`

## CAND-AFB22C3F061C · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001689 | non-empty Signal ID | SIG-001689 | Signal ID='SIG-001689' |
| primary_id_pattern | N/A | SIG-001689 | no pattern for dataset | SIG-001689 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001689 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001689 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260809-7 | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260809-7D2AAA; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001689 | primary id present | SIG-001689 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001689', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001689 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001689 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001689`

## CAND-6FF092643723 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001688 | non-empty Signal ID | SIG-001688 | Signal ID='SIG-001688' |
| primary_id_pattern | N/A | SIG-001688 | no pattern for dataset | SIG-001688 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001688 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001688 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260809 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260809-7D2AAA; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001688 | primary id present | SIG-001688 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001688', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001688 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001688 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001688`
