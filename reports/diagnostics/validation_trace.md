# Validation Trace

**Generated:** 2026-07-14T08:30:25+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-83AB144D8A36 · Their Potential Role in Corporate Governance

dataset=`business_signal_library` · confidence=`0.85` · threshold=`0.8` · document=`DOC-2B7A69D877EE`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000193 | non-empty Signal ID | SIG-000193 | Signal ID='SIG-000193' |
| primary_id_pattern | N/A | SIG-000193 | no pattern for dataset | SIG-000193 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000193 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000193 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000006; document=DOC-2B7A69D877EE; mission=MIS-20260714-B | optional | present | provenance: source=SRC-000006; document=DOC-2B7A69D877EE; mission=MIS-20260714-B8ADB7; discovery_provider=DISC-TAVILY; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000193 | primary id present | SIG-000193 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000193', 'confidence': 0.85} | validate_row ok | duplicate_id:SIG-000193 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000193 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000193`

## CAND-99B9C198D907 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000194 | non-empty Signal ID | SIG-000194 | Signal ID='SIG-000194' |
| primary_id_pattern | N/A | SIG-000194 | no pattern for dataset | SIG-000194 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000194 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000194 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260714 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260714-B8ADB7; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000194 | primary id present | SIG-000194 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000194', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000194 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000194 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000194`

## CAND-A12FE9F04895 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000192 | non-empty Signal ID | SIG-000192 | Signal ID='SIG-000192' |
| primary_id_pattern | N/A | SIG-000192 | no pattern for dataset | SIG-000192 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000192 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000192 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260714-B | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260714-B8ADB7; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000192 | primary id present | SIG-000192 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000192', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000192 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000192 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000192`

## CAND-A86881EB3F00 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000190 | non-empty Signal ID | SIG-000190 | Signal ID='SIG-000190' |
| primary_id_pattern | N/A | SIG-000190 | no pattern for dataset | SIG-000190 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000190 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000190 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260714 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260714-B8ADB7; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000190 | primary id present | SIG-000190 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000190', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000190 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000190 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000190`

## CAND-5CED4DEC7D21 · The biodiversity and ecosystem service contributions and trade-offs of forest restoration approaches

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-C8336B1CF486`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000191 | non-empty Signal ID | SIG-000191 | Signal ID='SIG-000191' |
| primary_id_pattern | N/A | SIG-000191 | no pattern for dataset | SIG-000191 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000191 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000191 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260714 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260714-B8ADB7; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2022-03-17 | not enforced by integrity_guard | 2022-03-17 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000191 | primary id present | SIG-000191 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000191', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000191 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000191 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000191`
