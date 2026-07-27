# Validation Trace

**Generated:** 2026-07-27T08:49:50+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-34CB8A37543B · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000942 | non-empty Signal ID | SIG-000942 | Signal ID='SIG-000942' |
| primary_id_pattern | N/A | SIG-000942 | no pattern for dataset | SIG-000942 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000942 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000942 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260727 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260727-3A1A26; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000942 | primary id present | SIG-000942 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000942', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000942 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000942 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000942`

## CAND-6685A6F605EC · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000944 | non-empty Signal ID | SIG-000944 | Signal ID='SIG-000944' |
| primary_id_pattern | N/A | SIG-000944 | no pattern for dataset | SIG-000944 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000944 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000944 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260727-3 | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260727-3A1A26; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000944 | primary id present | SIG-000944 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000944', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000944 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000944 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000944`

## CAND-C9455B88736E · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000941 | non-empty Signal ID | SIG-000941 | Signal ID='SIG-000941' |
| primary_id_pattern | N/A | SIG-000941 | no pattern for dataset | SIG-000941 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000941 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000941 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260727-3 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260727-3A1A26; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000941 | primary id present | SIG-000941 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000941', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000941 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000941 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000941`

## CAND-179F9C19D4BC · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000940 | non-empty Signal ID | SIG-000940 | Signal ID='SIG-000940' |
| primary_id_pattern | N/A | SIG-000940 | no pattern for dataset | SIG-000940 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000940 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000940 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260727 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260727-3A1A26; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000940 | primary id present | SIG-000940 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000940', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000940 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000940 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000940`

## CAND-4A6472DD0E65 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000943 | non-empty Signal ID | SIG-000943 | Signal ID='SIG-000943' |
| primary_id_pattern | N/A | SIG-000943 | no pattern for dataset | SIG-000943 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000943 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000943 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260727 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260727-3A1A26; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000943 | primary id present | SIG-000943 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000943', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000943 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000943 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000943`
