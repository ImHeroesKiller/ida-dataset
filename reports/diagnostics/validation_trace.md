# Validation Trace

**Generated:** 2026-07-15T05:56:25+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-ED2E6F2683D9 · The biodiversity and ecosystem service contributions and trade-offs of forest restoration approaches

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-C8336B1CF486`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000241 | non-empty Signal ID | SIG-000241 | Signal ID='SIG-000241' |
| primary_id_pattern | N/A | SIG-000241 | no pattern for dataset | SIG-000241 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000241 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000241 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260715 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260715-EF13DC; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2022-03-17 | not enforced by integrity_guard | 2022-03-17 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000241 | primary id present | SIG-000241 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000241', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000241 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000241 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000241`

## CAND-5E0BC5BBDE48 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000240 | non-empty Signal ID | SIG-000240 | Signal ID='SIG-000240' |
| primary_id_pattern | N/A | SIG-000240 | no pattern for dataset | SIG-000240 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000240 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000240 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260715 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260715-EF13DC; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000240 | primary id present | SIG-000240 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000240', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000240 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000240 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000240`

## CAND-F0E234340EAA · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000242 | non-empty Signal ID | SIG-000242 | Signal ID='SIG-000242' |
| primary_id_pattern | N/A | SIG-000242 | no pattern for dataset | SIG-000242 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000242 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000242 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260715-E | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260715-EF13DC; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000242 | primary id present | SIG-000242 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000242', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000242 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000242 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000242`

## CAND-E4D897A4A916 · Corporate Governance In Middle East Family Businesses

dataset=`business_signal_library` · confidence=`0.85` · threshold=`0.8` · document=`DOC-E689A7156EBC`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000243 | non-empty Signal ID | SIG-000243 | Signal ID='SIG-000243' |
| primary_id_pattern | N/A | SIG-000243 | no pattern for dataset | SIG-000243 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000243 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000243 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000001; document=DOC-E689A7156EBC; mission=MIS-20260715-E | optional | present | provenance: source=SRC-000001; document=DOC-E689A7156EBC; mission=MIS-20260715-EF13DC; discovery_provider=DISC-TAVILY; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000243 | primary id present | SIG-000243 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000243', 'confidence': 0.85} | validate_row ok | duplicate_id:SIG-000243 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000243 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000243`

## CAND-821AE26795AA · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000244 | non-empty Signal ID | SIG-000244 | Signal ID='SIG-000244' |
| primary_id_pattern | N/A | SIG-000244 | no pattern for dataset | SIG-000244 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000244 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000244 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260715 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260715-EF13DC; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000244 | primary id present | SIG-000244 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000244', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000244 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000244 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000244`
