# Validation Trace

**Generated:** 2026-07-31T09:29:16+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-F018F5075066 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001146 | non-empty Signal ID | SIG-001146 | Signal ID='SIG-001146' |
| primary_id_pattern | N/A | SIG-001146 | no pattern for dataset | SIG-001146 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001146 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001146 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260731-2 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260731-2192C6; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001146 | primary id present | SIG-001146 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001146', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001146 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001146 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001146`

## CAND-A9AD7E375327 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001149 | non-empty Signal ID | SIG-001149 | Signal ID='SIG-001149' |
| primary_id_pattern | N/A | SIG-001149 | no pattern for dataset | SIG-001149 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001149 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001149 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260731-2 | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260731-2192C6; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001149 | primary id present | SIG-001149 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001149', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001149 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001149 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001149`

## CAND-80F6C2C61791 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001148 | non-empty Signal ID | SIG-001148 | Signal ID='SIG-001148' |
| primary_id_pattern | N/A | SIG-001148 | no pattern for dataset | SIG-001148 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001148 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001148 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260731 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260731-2192C6; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001148 | primary id present | SIG-001148 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001148', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001148 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001148 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001148`

## CAND-47A705C38662 · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001145 | non-empty Signal ID | SIG-001145 | Signal ID='SIG-001145' |
| primary_id_pattern | N/A | SIG-001145 | no pattern for dataset | SIG-001145 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001145 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001145 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260731 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260731-2192C6; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001145 | primary id present | SIG-001145 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001145', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001145 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001145 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001145`

## CAND-0CE65281BF0F · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001147 | non-empty Signal ID | SIG-001147 | Signal ID='SIG-001147' |
| primary_id_pattern | N/A | SIG-001147 | no pattern for dataset | SIG-001147 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001147 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001147 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260731 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260731-2192C6; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001147 | primary id present | SIG-001147 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001147', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-001147 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001147 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001147`
