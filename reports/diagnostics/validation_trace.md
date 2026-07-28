# Validation Trace

**Generated:** 2026-07-28T14:28:37+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-122311A8BD1E · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000997 | non-empty Signal ID | SIG-000997 | Signal ID='SIG-000997' |
| primary_id_pattern | N/A | SIG-000997 | no pattern for dataset | SIG-000997 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000997 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000997 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260728 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260728-5E97DB; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000997 | primary id present | SIG-000997 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000997', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000997 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000997 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000997`

## CAND-9A17A5C71185 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000999 | non-empty Signal ID | SIG-000999 | Signal ID='SIG-000999' |
| primary_id_pattern | N/A | SIG-000999 | no pattern for dataset | SIG-000999 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000999 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000999 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260728-5 | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260728-5E97DB; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000999 | primary id present | SIG-000999 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000999', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000999 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000999 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000999`

## CAND-1BA7FE00FA0B · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000996 | non-empty Signal ID | SIG-000996 | Signal ID='SIG-000996' |
| primary_id_pattern | N/A | SIG-000996 | no pattern for dataset | SIG-000996 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000996 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000996 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260728-5 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260728-5E97DB; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000996 | primary id present | SIG-000996 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000996', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000996 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000996 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000996`

## CAND-85ED54C0307F · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000995 | non-empty Signal ID | SIG-000995 | Signal ID='SIG-000995' |
| primary_id_pattern | N/A | SIG-000995 | no pattern for dataset | SIG-000995 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000995 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000995 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260728 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260728-5E97DB; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000995 | primary id present | SIG-000995 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000995', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000995 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000995 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000995`

## CAND-93557F3F4CA5 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000998 | non-empty Signal ID | SIG-000998 | Signal ID='SIG-000998' |
| primary_id_pattern | N/A | SIG-000998 | no pattern for dataset | SIG-000998 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000998 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000998 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260728 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260728-5E97DB; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000998 | primary id present | SIG-000998 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000998', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000998 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000998 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000998`
