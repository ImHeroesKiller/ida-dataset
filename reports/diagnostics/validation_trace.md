# Validation Trace

**Generated:** 2026-07-26T13:45:43+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-E67AA2435539 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000902 | non-empty Signal ID | SIG-000902 | Signal ID='SIG-000902' |
| primary_id_pattern | N/A | SIG-000902 | no pattern for dataset | SIG-000902 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000902 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000902 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260726 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260726-014AB0; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000902 | primary id present | SIG-000902 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000902', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000902 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000902 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000902`

## CAND-4121AD4A8A6C · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000903 | non-empty Signal ID | SIG-000903 | Signal ID='SIG-000903' |
| primary_id_pattern | N/A | SIG-000903 | no pattern for dataset | SIG-000903 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000903 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000903 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260726 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260726-014AB0; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000903 | primary id present | SIG-000903 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000903', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000903 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000903 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000903`

## CAND-23F8F11C5691 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000901 | non-empty Signal ID | SIG-000901 | Signal ID='SIG-000901' |
| primary_id_pattern | N/A | SIG-000901 | no pattern for dataset | SIG-000901 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000901 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000901 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260726-0 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260726-014AB0; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000901 | primary id present | SIG-000901 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000901', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000901 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000901 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000901`

## CAND-44F6E1AB82A9 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000904 | non-empty Signal ID | SIG-000904 | Signal ID='SIG-000904' |
| primary_id_pattern | N/A | SIG-000904 | no pattern for dataset | SIG-000904 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000904 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000904 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260726-0 | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260726-014AB0; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000904 | primary id present | SIG-000904 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000904', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000904 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000904 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000904`

## CAND-D49E017CDC5B · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000900 | non-empty Signal ID | SIG-000900 | Signal ID='SIG-000900' |
| primary_id_pattern | N/A | SIG-000900 | no pattern for dataset | SIG-000900 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000900 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000900 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260726 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260726-014AB0; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000900 | primary id present | SIG-000900 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000900', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000900 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000900 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000900`
