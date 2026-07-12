# Validation Trace

**Generated:** 2026-07-12T19:37:50+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-2BFAA254F9FF · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-2430A598BF3B`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000119 | non-empty Signal ID | SIG-000119 | Signal ID='SIG-000119' |
| primary_id_pattern | N/A | SIG-000119 | no pattern for dataset | SIG-000119 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000119 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000119 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260712-4 | optional | present | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260712-40A136; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000119 | primary id present | SIG-000119 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000119', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000119 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000119 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000119`

## CAND-75FE36D00C7C · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000115 | non-empty Signal ID | SIG-000115 | Signal ID='SIG-000115' |
| primary_id_pattern | N/A | SIG-000115 | no pattern for dataset | SIG-000115 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000115 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000115 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260712 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260712-40A136; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000115 | primary id present | SIG-000115 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000115', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000115 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000115 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000115`

## CAND-CB21E928D424 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000116 | non-empty Signal ID | SIG-000116 | Signal ID='SIG-000116' |
| primary_id_pattern | N/A | SIG-000116 | no pattern for dataset | SIG-000116 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000116 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000116 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260712-4 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260712-40A136; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000116 | primary id present | SIG-000116 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000116', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000116 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000116 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000116`

## CAND-B1A8E8423E1C · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000117 | non-empty Signal ID | SIG-000117 | Signal ID='SIG-000117' |
| primary_id_pattern | N/A | SIG-000117 | no pattern for dataset | SIG-000117 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000117 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000117 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260712 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260712-40A136; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000117 | primary id present | SIG-000117 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000117', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000117 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000117 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000117`

## CAND-860D075C7BEB · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000118 | non-empty Signal ID | SIG-000118 | Signal ID='SIG-000118' |
| primary_id_pattern | N/A | SIG-000118 | no pattern for dataset | SIG-000118 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000118 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000118 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260712 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260712-40A136; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000118 | primary id present | SIG-000118 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000118', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000118 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000118 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000118`
