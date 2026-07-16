# Validation Trace

**Generated:** 2026-07-16T00:20:44+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-50FA56B887D1 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000286 | non-empty Signal ID | SIG-000286 | Signal ID='SIG-000286' |
| primary_id_pattern | N/A | SIG-000286 | no pattern for dataset | SIG-000286 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000286 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000286 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260716-4 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260716-4ADEE6; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000286 | primary id present | SIG-000286 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000286', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000286 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000286 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000286`

## CAND-62B46CE97856 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000285 | non-empty Signal ID | SIG-000285 | Signal ID='SIG-000285' |
| primary_id_pattern | N/A | SIG-000285 | no pattern for dataset | SIG-000285 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000285 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000285 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260716 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260716-4ADEE6; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000285 | primary id present | SIG-000285 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000285', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000285 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000285 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000285`

## CAND-7253D37782F3 · Their Potential Role in Corporate Governance

dataset=`business_signal_library` · confidence=`0.85` · threshold=`0.8` · document=`DOC-8E65A51B4E13`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000288 | non-empty Signal ID | SIG-000288 | Signal ID='SIG-000288' |
| primary_id_pattern | N/A | SIG-000288 | no pattern for dataset | SIG-000288 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000288 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000288 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000006; document=DOC-8E65A51B4E13; mission=MIS-20260716-4 | optional | present | provenance: source=SRC-000006; document=DOC-8E65A51B4E13; mission=MIS-20260716-4ADEE6; discovery_provider=DISC-TAVILY; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000288 | primary id present | SIG-000288 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000288', 'confidence': 0.85} | validate_row ok | duplicate_id:SIG-000288 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000288 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000288`

## CAND-A8355028B270 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000289 | non-empty Signal ID | SIG-000289 | Signal ID='SIG-000289' |
| primary_id_pattern | N/A | SIG-000289 | no pattern for dataset | SIG-000289 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000289 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000289 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260716 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260716-4ADEE6; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000289 | primary id present | SIG-000289 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000289', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000289 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000289 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000289`

## CAND-0BE551E19876 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000287 | non-empty Signal ID | SIG-000287 | Signal ID='SIG-000287' |
| primary_id_pattern | N/A | SIG-000287 | no pattern for dataset | SIG-000287 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000287 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000287 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260716 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260716-4ADEE6; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000287 | primary id present | SIG-000287 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000287', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000287 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000287 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000287`
