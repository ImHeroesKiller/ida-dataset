# Validation Trace

**Generated:** 2026-08-23T13:51:52+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-693523700C2B · Consumer Attitudes Toward Imported and Local Produce in Indonesia: The Role of Country of Origin and Perception in Shapi

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-23B61DA3B184`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001130 | non-empty Signal ID | SIG-001130 | Signal ID='SIG-001130' |
| primary_id_pattern | N/A | SIG-001130 | no pattern for dataset | SIG-001130 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001130 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001130 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-23B61DA3B184; mission=MIS-20260823 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-23B61DA3B184; mission=MIS-20260823-7836B8; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2025 | not enforced by integrity_guard | 2025 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001130 | primary id present | SIG-001130 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001130', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001130 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001130 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001130`

## CAND-D326170FA884 · Product Innovation Toward MSME’s Market Performance On Creative Industry

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-8DEAD915EF6F`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001129 | non-empty Signal ID | SIG-001129 | Signal ID='SIG-001129' |
| primary_id_pattern | N/A | SIG-001129 | no pattern for dataset | SIG-001129 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001129 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001129 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-8DEAD915EF6F; mission=MIS-20260823 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-8DEAD915EF6F; mission=MIS-20260823-7836B8; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2023 | not enforced by integrity_guard | 2023 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001129 | primary id present | SIG-001129 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001129', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001129 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001129 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001129`

## CAND-7A3E14917D24 · Figure 1.18. Indonesia needs to expand its protected areas to reach the Aichi target

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-9CF2639B264C`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001127 | non-empty Signal ID | SIG-001127 | Signal ID='SIG-001127' |
| primary_id_pattern | N/A | SIG-001127 | no pattern for dataset | SIG-001127 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001127 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001127 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-9CF2639B264C; mission=MIS-20260823 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-9CF2639B264C; mission=MIS-20260823-7836B8; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001127 | primary id present | SIG-001127 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001127', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001127 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001127 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001127`

## CAND-48E885258442 · Expand Target Market in Business

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-AFB055C754E2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001128 | non-empty Signal ID | SIG-001128 | Signal ID='SIG-001128' |
| primary_id_pattern | N/A | SIG-001128 | no pattern for dataset | SIG-001128 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001128 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001128 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-AFB055C754E2; mission=MIS-20260823 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-AFB055C754E2; mission=MIS-20260823-7836B8; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020 | not enforced by integrity_guard | 2020 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001128 | primary id present | SIG-001128 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001128', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001128 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001128 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001128`

## CAND-1B76D8313E52 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-9C3FE7A510A0`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001126 | non-empty Signal ID | SIG-001126 | Signal ID='SIG-001126' |
| primary_id_pattern | N/A | SIG-001126 | no pattern for dataset | SIG-001126 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001126 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001126 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-9C3FE7A510A0; mission=MIS-20260823-7 | optional | present | provenance: source=SRC-000004; document=DOC-9C3FE7A510A0; mission=MIS-20260823-7836B8; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001126 | primary id present | SIG-001126 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001126', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001126 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001126 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001126`
