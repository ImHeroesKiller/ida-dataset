# Validation Trace

**Generated:** 2026-07-15T03:02:01+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-CDF033653832 · Their Potential Role in Corporate Governance

dataset=`business_signal_library` · confidence=`0.85` · threshold=`0.8` · document=`DOC-2B7A69D877EE`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000238 | non-empty Signal ID | SIG-000238 | Signal ID='SIG-000238' |
| primary_id_pattern | N/A | SIG-000238 | no pattern for dataset | SIG-000238 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000238 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000238 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000006; document=DOC-2B7A69D877EE; mission=MIS-20260715-8 | optional | present | provenance: source=SRC-000006; document=DOC-2B7A69D877EE; mission=MIS-20260715-8CFDA1; discovery_provider=DISC-TAVILY; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000238 | primary id present | SIG-000238 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000238', 'confidence': 0.85} | validate_row ok | duplicate_id:SIG-000238 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000238 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000238`

## CAND-8BDDC31129B6 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000235 | non-empty Signal ID | SIG-000235 | Signal ID='SIG-000235' |
| primary_id_pattern | N/A | SIG-000235 | no pattern for dataset | SIG-000235 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000235 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000235 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260715 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260715-8CFDA1; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000235 | primary id present | SIG-000235 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000235', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000235 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000235 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000235`

## CAND-C6A1D7676555 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000239 | non-empty Signal ID | SIG-000239 | Signal ID='SIG-000239' |
| primary_id_pattern | N/A | SIG-000239 | no pattern for dataset | SIG-000239 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000239 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000239 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260715 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260715-8CFDA1; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000239 | primary id present | SIG-000239 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000239', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000239 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000239 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000239`

## CAND-6E5663346717 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000237 | non-empty Signal ID | SIG-000237 | Signal ID='SIG-000237' |
| primary_id_pattern | N/A | SIG-000237 | no pattern for dataset | SIG-000237 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000237 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000237 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260715-8 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260715-8CFDA1; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000237 | primary id present | SIG-000237 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000237', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000237 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000237 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000237`

## CAND-DB2A8FC5CD05 · The biodiversity and ecosystem service contributions and trade-offs of forest restoration approaches

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-C8336B1CF486`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000236 | non-empty Signal ID | SIG-000236 | Signal ID='SIG-000236' |
| primary_id_pattern | N/A | SIG-000236 | no pattern for dataset | SIG-000236 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000236 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000236 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260715 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260715-8CFDA1; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2022-03-17 | not enforced by integrity_guard | 2022-03-17 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000236 | primary id present | SIG-000236 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000236', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000236 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000236 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000236`
