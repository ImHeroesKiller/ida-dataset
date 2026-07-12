# Validation Trace

**Generated:** 2026-07-12T23:10:05+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-04491DF02914 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000132 | non-empty Signal ID | SIG-000132 | Signal ID='SIG-000132' |
| primary_id_pattern | N/A | SIG-000132 | no pattern for dataset | SIG-000132 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000132 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000132 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260712 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260712-9F9D1A; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000132 | primary id present | SIG-000132 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000132', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000132 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000132 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000132`

## CAND-8E5A6A0C789D · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-2430A598BF3B`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000133 | non-empty Signal ID | SIG-000133 | Signal ID='SIG-000133' |
| primary_id_pattern | N/A | SIG-000133 | no pattern for dataset | SIG-000133 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000133 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000133 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260712-9 | optional | present | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260712-9F9D1A; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000133 | primary id present | SIG-000133 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000133', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000133 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000133 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000133`

## CAND-474BB1F8935A · [PDF] State-Owned Enterprise Reform Program II - Asian Development Bank

dataset=`business_signal_library` · confidence=`0.85` · threshold=`0.8` · document=`DOC-9DEEE6C56766`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000134 | non-empty Signal ID | SIG-000134 | Signal ID='SIG-000134' |
| primary_id_pattern | N/A | SIG-000134 | no pattern for dataset | SIG-000134 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000134 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000134 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000006; document=DOC-9DEEE6C56766; mission=MIS-20260712-9 | optional | present | provenance: source=SRC-000006; document=DOC-9DEEE6C56766; mission=MIS-20260712-9F9D1A; discovery_provider=DISC-TAVILY; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000134 | primary id present | SIG-000134 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000134', 'confidence': 0.85} | validate_row ok | duplicate_id:SIG-000134 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000134 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000134`

## CAND-289F50BD8B9A · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000131 | non-empty Signal ID | SIG-000131 | Signal ID='SIG-000131' |
| primary_id_pattern | N/A | SIG-000131 | no pattern for dataset | SIG-000131 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000131 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000131 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260712-9 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260712-9F9D1A; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000131 | primary id present | SIG-000131 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000131', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000131 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000131 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000131`

## CAND-09B740BB67FC · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000130 | non-empty Signal ID | SIG-000130 | Signal ID='SIG-000130' |
| primary_id_pattern | N/A | SIG-000130 | no pattern for dataset | SIG-000130 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000130 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000130 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260712 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260712-9F9D1A; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000130 | primary id present | SIG-000130 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000130', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000130 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000130 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000130`
