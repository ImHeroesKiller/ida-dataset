# Validation Trace

**Generated:** 2026-07-16T03:53:50+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-8B43D8239E53 · Their Potential Role in Corporate Governance

dataset=`business_signal_library` · confidence=`0.85` · threshold=`0.8` · document=`DOC-8E65A51B4E13`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000294 | non-empty Signal ID | SIG-000294 | Signal ID='SIG-000294' |
| primary_id_pattern | N/A | SIG-000294 | no pattern for dataset | SIG-000294 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000294 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000294 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000006; document=DOC-8E65A51B4E13; mission=MIS-20260716-5 | optional | present | provenance: source=SRC-000006; document=DOC-8E65A51B4E13; mission=MIS-20260716-566472; discovery_provider=DISC-TAVILY; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000294 | primary id present | SIG-000294 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000294', 'confidence': 0.85} | validate_row ok | duplicate_id:SIG-000294 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000294 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000294`

## CAND-D3D78A09E8F6 · Corporate Governance Improving Corporate Governance in India- Related ...

dataset=`business_signal_library` · confidence=`0.85` · threshold=`0.8` · document=`DOC-DA23EFA062CA`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000290 | non-empty Signal ID | SIG-000290 | Signal ID='SIG-000290' |
| primary_id_pattern | N/A | SIG-000290 | no pattern for dataset | SIG-000290 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000290 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000290 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-DA23EFA062CA; mission=MIS-20260716-5 | optional | present | provenance: source=SRC-000004; document=DOC-DA23EFA062CA; mission=MIS-20260716-566472; discovery_provider=DISC-TAVILY; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000290 | primary id present | SIG-000290 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000290', 'confidence': 0.85} | validate_row ok | duplicate_id:SIG-000290 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000290 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000290`

## CAND-58F9F2F20E69 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000291 | non-empty Signal ID | SIG-000291 | Signal ID='SIG-000291' |
| primary_id_pattern | N/A | SIG-000291 | no pattern for dataset | SIG-000291 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000291 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000291 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260716 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260716-566472; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000291 | primary id present | SIG-000291 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000291', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000291 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000291 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000291`

## CAND-DBC199765D96 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000292 | non-empty Signal ID | SIG-000292 | Signal ID='SIG-000292' |
| primary_id_pattern | N/A | SIG-000292 | no pattern for dataset | SIG-000292 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000292 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000292 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260716-5 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260716-566472; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000292 | primary id present | SIG-000292 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000292', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000292 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000292 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000292`

## CAND-59737FE42123 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000293 | non-empty Signal ID | SIG-000293 | Signal ID='SIG-000293' |
| primary_id_pattern | N/A | SIG-000293 | no pattern for dataset | SIG-000293 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000293 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000293 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260716 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260716-566472; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000293 | primary id present | SIG-000293 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000293', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000293 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000293 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000293`
