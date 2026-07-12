# Validation Trace

**Generated:** 2026-07-12T09:23:07+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-153880E3AA52 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000091 | non-empty Signal ID | SIG-000091 | Signal ID='SIG-000091' |
| primary_id_pattern | N/A | SIG-000091 | no pattern for dataset | SIG-000091 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000091 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000091 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260712-B | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260712-BDB527; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000091 | primary id present | SIG-000091 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000091', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000091 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000091 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000091`

## CAND-C5625A7A6429 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-2430A598BF3B`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000094 | non-empty Signal ID | SIG-000094 | Signal ID='SIG-000094' |
| primary_id_pattern | N/A | SIG-000094 | no pattern for dataset | SIG-000094 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000094 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000094 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260712-B | optional | present | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260712-BDB527; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000094 | primary id present | SIG-000094 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000094', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000094 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000094 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000094`

## CAND-0D27D86BDE8A · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000090 | non-empty Signal ID | SIG-000090 | Signal ID='SIG-000090' |
| primary_id_pattern | N/A | SIG-000090 | no pattern for dataset | SIG-000090 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000090 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000090 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260712 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260712-BDB527; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000090 | primary id present | SIG-000090 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000090', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000090 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000090 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000090`

## CAND-06D3CD95EE5D · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000093 | non-empty Signal ID | SIG-000093 | Signal ID='SIG-000093' |
| primary_id_pattern | N/A | SIG-000093 | no pattern for dataset | SIG-000093 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000093 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000093 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260712 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260712-BDB527; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000093 | primary id present | SIG-000093 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000093', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000093 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000093 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000093`

## CAND-D1FB4715F0BE · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000092 | non-empty Signal ID | SIG-000092 | Signal ID='SIG-000092' |
| primary_id_pattern | N/A | SIG-000092 | no pattern for dataset | SIG-000092 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000092 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000092 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260712 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260712-BDB527; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000092 | primary id present | SIG-000092 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000092', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000092 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000092 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000092`
