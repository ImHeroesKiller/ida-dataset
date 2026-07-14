# Validation Trace

**Generated:** 2026-07-14T20:35:59+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-CFDF901B9AC5 · The biodiversity and ecosystem service contributions and trade-offs of forest restoration approaches

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-C8336B1CF486`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000221 | non-empty Signal ID | SIG-000221 | Signal ID='SIG-000221' |
| primary_id_pattern | N/A | SIG-000221 | no pattern for dataset | SIG-000221 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000221 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000221 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260714 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260714-80EDF3; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2022-03-17 | not enforced by integrity_guard | 2022-03-17 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000221 | primary id present | SIG-000221 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000221', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000221 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000221 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000221`

## CAND-684994363B13 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000222 | non-empty Signal ID | SIG-000222 | Signal ID='SIG-000222' |
| primary_id_pattern | N/A | SIG-000222 | no pattern for dataset | SIG-000222 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000222 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000222 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260714-8 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260714-80EDF3; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000222 | primary id present | SIG-000222 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000222', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000222 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000222 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000222`

## CAND-F61211D36EA1 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000224 | non-empty Signal ID | SIG-000224 | Signal ID='SIG-000224' |
| primary_id_pattern | N/A | SIG-000224 | no pattern for dataset | SIG-000224 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000224 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000224 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260714 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260714-80EDF3; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000224 | primary id present | SIG-000224 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000224', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000224 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000224 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000224`

## CAND-84CB2600910C · Their Potential Role in Corporate Governance

dataset=`business_signal_library` · confidence=`0.85` · threshold=`0.8` · document=`DOC-8E65A51B4E13`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000223 | non-empty Signal ID | SIG-000223 | Signal ID='SIG-000223' |
| primary_id_pattern | N/A | SIG-000223 | no pattern for dataset | SIG-000223 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000223 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000223 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000006; document=DOC-8E65A51B4E13; mission=MIS-20260714-8 | optional | present | provenance: source=SRC-000006; document=DOC-8E65A51B4E13; mission=MIS-20260714-80EDF3; discovery_provider=DISC-TAVILY; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000223 | primary id present | SIG-000223 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000223', 'confidence': 0.85} | validate_row ok | duplicate_id:SIG-000223 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000223 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000223`

## CAND-4C163EF764E8 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000220 | non-empty Signal ID | SIG-000220 | Signal ID='SIG-000220' |
| primary_id_pattern | N/A | SIG-000220 | no pattern for dataset | SIG-000220 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000220 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000220 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260714 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260714-80EDF3; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000220 | primary id present | SIG-000220 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000220', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000220 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000220 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000220`
