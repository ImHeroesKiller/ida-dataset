# Validation Trace

**Generated:** 2026-07-15T11:16:54+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-2D8A81CCB806 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000250 | non-empty Signal ID | SIG-000250 | Signal ID='SIG-000250' |
| primary_id_pattern | N/A | SIG-000250 | no pattern for dataset | SIG-000250 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000250 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000250 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260715 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260715-104BE5; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000250 | primary id present | SIG-000250 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000250', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000250 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000250 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000250`

## CAND-517F72A8C9B6 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000252 | non-empty Signal ID | SIG-000252 | Signal ID='SIG-000252' |
| primary_id_pattern | N/A | SIG-000252 | no pattern for dataset | SIG-000252 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000252 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000252 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260715-1 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260715-104BE5; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000252 | primary id present | SIG-000252 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000252', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000252 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000252 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000252`

## CAND-F3BB1542ED2A · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000254 | non-empty Signal ID | SIG-000254 | Signal ID='SIG-000254' |
| primary_id_pattern | N/A | SIG-000254 | no pattern for dataset | SIG-000254 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000254 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000254 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260715 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260715-104BE5; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000254 | primary id present | SIG-000254 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000254', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000254 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000254 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000254`

## CAND-511785536996 · Corporate Governance of State-Owned Enterprises

dataset=`business_signal_library` · confidence=`0.85` · threshold=`0.8` · document=`DOC-39ED6A991AD1`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000253 | non-empty Signal ID | SIG-000253 | Signal ID='SIG-000253' |
| primary_id_pattern | N/A | SIG-000253 | no pattern for dataset | SIG-000253 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000253 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000253 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-39ED6A991AD1; mission=MIS-20260715-1 | optional | present | provenance: source=SRC-000004; document=DOC-39ED6A991AD1; mission=MIS-20260715-104BE5; discovery_provider=DISC-TAVILY; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000253 | primary id present | SIG-000253 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000253', 'confidence': 0.85} | validate_row ok | duplicate_id:SIG-000253 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000253 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000253`

## CAND-FF817076E24D · The biodiversity and ecosystem service contributions and trade-offs of forest restoration approaches

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-C8336B1CF486`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000251 | non-empty Signal ID | SIG-000251 | Signal ID='SIG-000251' |
| primary_id_pattern | N/A | SIG-000251 | no pattern for dataset | SIG-000251 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000251 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000251 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260715 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260715-104BE5; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2022-03-17 | not enforced by integrity_guard | 2022-03-17 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000251 | primary id present | SIG-000251 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000251', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000251 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000251 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000251`
