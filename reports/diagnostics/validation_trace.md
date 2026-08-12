# Validation Trace

**Generated:** 2026-08-12T15:16:33+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-942AF5908C63 · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001980 | non-empty Signal ID | SIG-001980 | Signal ID='SIG-001980' |
| primary_id_pattern | N/A | SIG-001980 | no pattern for dataset | SIG-001980 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001980 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001980 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260812 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260812-F6EEB8; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001980 | primary id present | SIG-001980 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001980', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001980 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001980 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001980`

## CAND-F177B5BCC2BF · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001982 | non-empty Signal ID | SIG-001982 | Signal ID='SIG-001982' |
| primary_id_pattern | N/A | SIG-001982 | no pattern for dataset | SIG-001982 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001982 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001982 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260812 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260812-F6EEB8; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001982 | primary id present | SIG-001982 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001982', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-001982 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001982 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001982`

## CAND-9039943CC53D · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001984 | non-empty Signal ID | SIG-001984 | Signal ID='SIG-001984' |
| primary_id_pattern | N/A | SIG-001984 | no pattern for dataset | SIG-001984 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001984 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001984 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260812-F | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260812-F6EEB8; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001984 | primary id present | SIG-001984 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001984', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001984 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001984 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001984`

## CAND-AC71D9E4C5C4 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001981 | non-empty Signal ID | SIG-001981 | Signal ID='SIG-001981' |
| primary_id_pattern | N/A | SIG-001981 | no pattern for dataset | SIG-001981 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001981 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001981 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260812-F | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260812-F6EEB8; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001981 | primary id present | SIG-001981 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001981', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001981 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001981 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001981`

## CAND-4257AF53C692 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001983 | non-empty Signal ID | SIG-001983 | Signal ID='SIG-001983' |
| primary_id_pattern | N/A | SIG-001983 | no pattern for dataset | SIG-001983 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001983 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001983 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260812 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260812-F6EEB8; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001983 | primary id present | SIG-001983 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001983', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001983 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001983 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001983`
