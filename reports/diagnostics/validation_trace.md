# Validation Trace

**Generated:** 2026-07-14T23:26:23+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-1872110112B6 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000230 | non-empty Signal ID | SIG-000230 | Signal ID='SIG-000230' |
| primary_id_pattern | N/A | SIG-000230 | no pattern for dataset | SIG-000230 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000230 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000230 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260714 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260714-E62FBF; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000230 | primary id present | SIG-000230 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000230', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000230 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000230 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000230`

## CAND-6013A6C1C6A0 · The biodiversity and ecosystem service contributions and trade-offs of forest restoration approaches

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-C8336B1CF486`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000231 | non-empty Signal ID | SIG-000231 | Signal ID='SIG-000231' |
| primary_id_pattern | N/A | SIG-000231 | no pattern for dataset | SIG-000231 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000231 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000231 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260714 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260714-E62FBF; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2022-03-17 | not enforced by integrity_guard | 2022-03-17 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000231 | primary id present | SIG-000231 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000231', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000231 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000231 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000231`

## CAND-8689124EF376 · Their Potential Role in Corporate Governance

dataset=`business_signal_library` · confidence=`0.85` · threshold=`0.8` · document=`DOC-2B7A69D877EE`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000233 | non-empty Signal ID | SIG-000233 | Signal ID='SIG-000233' |
| primary_id_pattern | N/A | SIG-000233 | no pattern for dataset | SIG-000233 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000233 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000233 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000006; document=DOC-2B7A69D877EE; mission=MIS-20260714-E | optional | present | provenance: source=SRC-000006; document=DOC-2B7A69D877EE; mission=MIS-20260714-E62FBF; discovery_provider=DISC-TAVILY; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000233 | primary id present | SIG-000233 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000233', 'confidence': 0.85} | validate_row ok | duplicate_id:SIG-000233 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000233 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000233`

## CAND-83BDFEDF80B7 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000232 | non-empty Signal ID | SIG-000232 | Signal ID='SIG-000232' |
| primary_id_pattern | N/A | SIG-000232 | no pattern for dataset | SIG-000232 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000232 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000232 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260714-E | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260714-E62FBF; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000232 | primary id present | SIG-000232 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000232', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000232 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000232 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000232`

## CAND-B8B97E93685B · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000234 | non-empty Signal ID | SIG-000234 | Signal ID='SIG-000234' |
| primary_id_pattern | N/A | SIG-000234 | no pattern for dataset | SIG-000234 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000234 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000234 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260714 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260714-E62FBF; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000234 | primary id present | SIG-000234 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000234', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000234 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000234 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000234`
