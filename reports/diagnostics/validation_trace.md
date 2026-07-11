# Validation Trace

**Generated:** 2026-07-11T22:15:37+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-E03F85458730 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000063 | non-empty Signal ID | SIG-000063 | Signal ID='SIG-000063' |
| primary_id_pattern | N/A | SIG-000063 | no pattern for dataset | SIG-000063 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000063 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000063 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260711 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260711-525F54; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000063 | primary id present | SIG-000063 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000063', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000063 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000063 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000063`

## CAND-F556140ED8F3 · [PDF] State-Owned Enterprise Reform Program II - Asian Development Bank

dataset=`business_signal_library` · confidence=`0.85` · threshold=`0.8` · document=`DOC-9DEEE6C56766`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000061 | non-empty Signal ID | SIG-000061 | Signal ID='SIG-000061' |
| primary_id_pattern | N/A | SIG-000061 | no pattern for dataset | SIG-000061 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000061 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000061 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000006; document=DOC-9DEEE6C56766; mission=MIS-20260711-5 | optional | present | provenance: source=SRC-000006; document=DOC-9DEEE6C56766; mission=MIS-20260711-525F54; discovery_provider=DISC-TAVILY; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000061 | primary id present | SIG-000061 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000061', 'confidence': 0.85} | validate_row ok | duplicate_id:SIG-000061 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000061 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000061`

## CAND-E85253D083C6 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000060 | non-empty Signal ID | SIG-000060 | Signal ID='SIG-000060' |
| primary_id_pattern | N/A | SIG-000060 | no pattern for dataset | SIG-000060 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000060 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000060 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260711 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260711-525F54; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000060 | primary id present | SIG-000060 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000060', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000060 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000060 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000060`

## CAND-FE1019F45EAB · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000062 | non-empty Signal ID | SIG-000062 | Signal ID='SIG-000062' |
| primary_id_pattern | N/A | SIG-000062 | no pattern for dataset | SIG-000062 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000062 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000062 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260711-5 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260711-525F54; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000062 | primary id present | SIG-000062 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000062', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000062 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000062 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000062`

## CAND-67DC6F00E281 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000064 | non-empty Signal ID | SIG-000064 | Signal ID='SIG-000064' |
| primary_id_pattern | N/A | SIG-000064 | no pattern for dataset | SIG-000064 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000064 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000064 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260711 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260711-525F54; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000064 | primary id present | SIG-000064 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000064', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000064 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000064 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000064`
