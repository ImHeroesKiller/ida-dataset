# Validation Trace

**Generated:** 2026-07-13T19:06:35+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-B4BEF09F0359 · Their Potential Role in Corporate Governance

dataset=`business_signal_library` · confidence=`0.85` · threshold=`0.8` · document=`DOC-2B7A69D877EE`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000168 | non-empty Signal ID | SIG-000168 | Signal ID='SIG-000168' |
| primary_id_pattern | N/A | SIG-000168 | no pattern for dataset | SIG-000168 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000168 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000168 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000006; document=DOC-2B7A69D877EE; mission=MIS-20260713-A | optional | present | provenance: source=SRC-000006; document=DOC-2B7A69D877EE; mission=MIS-20260713-A96542; discovery_provider=DISC-TAVILY; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000168 | primary id present | SIG-000168 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000168', 'confidence': 0.85} | validate_row ok | duplicate_id:SIG-000168 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000168 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000168`

## CAND-A6284C9FE7DD · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000165 | non-empty Signal ID | SIG-000165 | Signal ID='SIG-000165' |
| primary_id_pattern | N/A | SIG-000165 | no pattern for dataset | SIG-000165 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000165 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000165 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260713 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260713-A96542; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000165 | primary id present | SIG-000165 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000165', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000165 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000165 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000165`

## CAND-422D3FE54EE2 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000166 | non-empty Signal ID | SIG-000166 | Signal ID='SIG-000166' |
| primary_id_pattern | N/A | SIG-000166 | no pattern for dataset | SIG-000166 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000166 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000166 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260713-A | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260713-A96542; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000166 | primary id present | SIG-000166 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000166', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000166 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000166 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000166`

## CAND-31E135690274 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000167 | non-empty Signal ID | SIG-000167 | Signal ID='SIG-000167' |
| primary_id_pattern | N/A | SIG-000167 | no pattern for dataset | SIG-000167 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000167 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000167 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260713 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260713-A96542; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000167 | primary id present | SIG-000167 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000167', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000167 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000167 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000167`

## CAND-57F278088148 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000169 | non-empty Signal ID | SIG-000169 | Signal ID='SIG-000169' |
| primary_id_pattern | N/A | SIG-000169 | no pattern for dataset | SIG-000169 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000169 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000169 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260713 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260713-A96542; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000169 | primary id present | SIG-000169 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000169', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000169 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000169 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000169`
