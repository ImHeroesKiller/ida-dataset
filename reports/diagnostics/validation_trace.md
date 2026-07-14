# Validation Trace

**Generated:** 2026-07-14T12:36:51+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-040342C45487 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000204 | non-empty Signal ID | SIG-000204 | Signal ID='SIG-000204' |
| primary_id_pattern | N/A | SIG-000204 | no pattern for dataset | SIG-000204 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000204 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000204 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260714 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260714-2204DB; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000204 | primary id present | SIG-000204 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000204', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000204 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000204 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000204`

## CAND-301A4106B6B9 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000202 | non-empty Signal ID | SIG-000202 | Signal ID='SIG-000202' |
| primary_id_pattern | N/A | SIG-000202 | no pattern for dataset | SIG-000202 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000202 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000202 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260714-2 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260714-2204DB; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000202 | primary id present | SIG-000202 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000202', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000202 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000202 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000202`

## CAND-983C177356D3 · The biodiversity and ecosystem service contributions and trade-offs of forest restoration approaches

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-C8336B1CF486`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000201 | non-empty Signal ID | SIG-000201 | Signal ID='SIG-000201' |
| primary_id_pattern | N/A | SIG-000201 | no pattern for dataset | SIG-000201 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000201 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000201 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260714 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260714-2204DB; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2022-03-17 | not enforced by integrity_guard | 2022-03-17 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000201 | primary id present | SIG-000201 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000201', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000201 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000201 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000201`

## CAND-27282FC4815B · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000200 | non-empty Signal ID | SIG-000200 | Signal ID='SIG-000200' |
| primary_id_pattern | N/A | SIG-000200 | no pattern for dataset | SIG-000200 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000200 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000200 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260714 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260714-2204DB; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000200 | primary id present | SIG-000200 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000200', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000200 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000200 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000200`

## CAND-67456BA8F0F6 · Their Potential Role in Corporate Governance

dataset=`business_signal_library` · confidence=`0.85` · threshold=`0.8` · document=`DOC-2B7A69D877EE`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000203 | non-empty Signal ID | SIG-000203 | Signal ID='SIG-000203' |
| primary_id_pattern | N/A | SIG-000203 | no pattern for dataset | SIG-000203 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000203 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000203 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000006; document=DOC-2B7A69D877EE; mission=MIS-20260714-2 | optional | present | provenance: source=SRC-000006; document=DOC-2B7A69D877EE; mission=MIS-20260714-2204DB; discovery_provider=DISC-TAVILY; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000203 | primary id present | SIG-000203 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000203', 'confidence': 0.85} | validate_row ok | duplicate_id:SIG-000203 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000203 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000203`
