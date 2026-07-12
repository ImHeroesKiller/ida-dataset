# Validation Trace

**Generated:** 2026-07-12T15:17:23+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-ADC3EDDC466E · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000106 | non-empty Signal ID | SIG-000106 | Signal ID='SIG-000106' |
| primary_id_pattern | N/A | SIG-000106 | no pattern for dataset | SIG-000106 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000106 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000106 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260712-4 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260712-4993C5; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000106 | primary id present | SIG-000106 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000106', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000106 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000106 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000106`

## CAND-D3B42975D0FF · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000107 | non-empty Signal ID | SIG-000107 | Signal ID='SIG-000107' |
| primary_id_pattern | N/A | SIG-000107 | no pattern for dataset | SIG-000107 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000107 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000107 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260712 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260712-4993C5; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000107 | primary id present | SIG-000107 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000107', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000107 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000107 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000107`

## CAND-23A292F64415 · [PDF] Corporate Governance in South Asia: Trends and Challenges

dataset=`business_signal_library` · confidence=`0.85` · threshold=`0.8` · document=`DOC-5F2E7AF866D4`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000108 | non-empty Signal ID | SIG-000108 | Signal ID='SIG-000108' |
| primary_id_pattern | N/A | SIG-000108 | no pattern for dataset | SIG-000108 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000108 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000108 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000006; document=DOC-5F2E7AF866D4; mission=MIS-20260712-4 | optional | present | provenance: source=SRC-000006; document=DOC-5F2E7AF866D4; mission=MIS-20260712-4993C5; discovery_provider=DISC-TAVILY; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000108 | primary id present | SIG-000108 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000108', 'confidence': 0.85} | validate_row ok | duplicate_id:SIG-000108 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000108 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000108`

## CAND-2C377B36CB5C · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000109 | non-empty Signal ID | SIG-000109 | Signal ID='SIG-000109' |
| primary_id_pattern | N/A | SIG-000109 | no pattern for dataset | SIG-000109 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000109 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000109 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260712 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260712-4993C5; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000109 | primary id present | SIG-000109 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000109', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000109 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000109 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000109`

## CAND-B7628E118C61 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000105 | non-empty Signal ID | SIG-000105 | Signal ID='SIG-000105' |
| primary_id_pattern | N/A | SIG-000105 | no pattern for dataset | SIG-000105 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000105 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000105 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260712 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260712-4993C5; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000105 | primary id present | SIG-000105 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000105', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000105 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000105 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000105`
