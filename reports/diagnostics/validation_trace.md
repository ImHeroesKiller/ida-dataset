# Validation Trace

**Generated:** 2026-07-27T12:44:10+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-989C75827272 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000952 | non-empty Signal ID | SIG-000952 | Signal ID='SIG-000952' |
| primary_id_pattern | N/A | SIG-000952 | no pattern for dataset | SIG-000952 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000952 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000952 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260727 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260727-F70EED; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000952 | primary id present | SIG-000952 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000952', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000952 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000952 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000952`

## CAND-9F369C541BE6 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000954 | non-empty Signal ID | SIG-000954 | Signal ID='SIG-000954' |
| primary_id_pattern | N/A | SIG-000954 | no pattern for dataset | SIG-000954 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000954 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000954 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260727-F | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260727-F70EED; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000954 | primary id present | SIG-000954 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000954', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000954 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000954 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000954`

## CAND-BAC271049FB4 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000951 | non-empty Signal ID | SIG-000951 | Signal ID='SIG-000951' |
| primary_id_pattern | N/A | SIG-000951 | no pattern for dataset | SIG-000951 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000951 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000951 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260727-F | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260727-F70EED; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000951 | primary id present | SIG-000951 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000951', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000951 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000951 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000951`

## CAND-E9CD4F316DD7 · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000950 | non-empty Signal ID | SIG-000950 | Signal ID='SIG-000950' |
| primary_id_pattern | N/A | SIG-000950 | no pattern for dataset | SIG-000950 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000950 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000950 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260727 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260727-F70EED; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000950 | primary id present | SIG-000950 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000950', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000950 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000950 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000950`

## CAND-0A43474D50A8 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000953 | non-empty Signal ID | SIG-000953 | Signal ID='SIG-000953' |
| primary_id_pattern | N/A | SIG-000953 | no pattern for dataset | SIG-000953 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000953 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000953 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260727 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260727-F70EED; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000953 | primary id present | SIG-000953 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000953', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000953 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000953 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000953`
