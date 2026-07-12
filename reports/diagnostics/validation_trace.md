# Validation Trace

**Generated:** 2026-07-12T21:12:09+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-D287F8CA1590 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D733F4309CB6`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000123 | non-empty Signal ID | SIG-000123 | Signal ID='SIG-000123' |
| primary_id_pattern | N/A | SIG-000123 | no pattern for dataset | SIG-000123 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000123 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000123 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D733F4309CB6; mission=MIS-20260712-2 | optional | present | provenance: source=SRC-000004; document=DOC-D733F4309CB6; mission=MIS-20260712-2B223F; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000123 | primary id present | SIG-000123 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000123', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000123 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000123 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000123`

## CAND-90A95C9CFC01 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000122 | non-empty Signal ID | SIG-000122 | Signal ID='SIG-000122' |
| primary_id_pattern | N/A | SIG-000122 | no pattern for dataset | SIG-000122 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000122 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000122 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260712 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260712-2B223F; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000122 | primary id present | SIG-000122 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000122', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000122 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000122 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000122`

## CAND-2D415744DAE8 · [PDF] State-Owned Enterprise Reform Program II - Asian Development Bank

dataset=`business_signal_library` · confidence=`0.85` · threshold=`0.8` · document=`DOC-9DEEE6C56766`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000124 | non-empty Signal ID | SIG-000124 | Signal ID='SIG-000124' |
| primary_id_pattern | N/A | SIG-000124 | no pattern for dataset | SIG-000124 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000124 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000124 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000006; document=DOC-9DEEE6C56766; mission=MIS-20260712-2 | optional | present | provenance: source=SRC-000006; document=DOC-9DEEE6C56766; mission=MIS-20260712-2B223F; discovery_provider=DISC-TAVILY; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000124 | primary id present | SIG-000124 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000124', 'confidence': 0.85} | validate_row ok | duplicate_id:SIG-000124 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000124 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000124`

## CAND-A3843ADEFBA8 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000120 | non-empty Signal ID | SIG-000120 | Signal ID='SIG-000120' |
| primary_id_pattern | N/A | SIG-000120 | no pattern for dataset | SIG-000120 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000120 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000120 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260712 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260712-2B223F; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000120 | primary id present | SIG-000120 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000120', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000120 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000120 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000120`

## CAND-3954E52A3898 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000121 | non-empty Signal ID | SIG-000121 | Signal ID='SIG-000121' |
| primary_id_pattern | N/A | SIG-000121 | no pattern for dataset | SIG-000121 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000121 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000121 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260712-2 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260712-2B223F; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000121 | primary id present | SIG-000121 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000121', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000121 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000121 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000121`
