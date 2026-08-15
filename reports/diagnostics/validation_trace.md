# Validation Trace

**Generated:** 2026-08-15T09:41:51+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-90C1F80EE911 · Product Innovation Toward MSME’s Market Performance On Creative Industry

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-8DEAD915EF6F`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000209 | non-empty Signal ID | SIG-000209 | Signal ID='SIG-000209' |
| primary_id_pattern | N/A | SIG-000209 | no pattern for dataset | SIG-000209 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000209 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000209 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-8DEAD915EF6F; mission=MIS-20260815 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-8DEAD915EF6F; mission=MIS-20260815-B5CDB5; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2023 | not enforced by integrity_guard | 2023 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000209 | primary id present | SIG-000209 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000209', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000209 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000209 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000209`

## CAND-E0A49C854440 · Expand Target Market in Business

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-AFB055C754E2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000208 | non-empty Signal ID | SIG-000208 | Signal ID='SIG-000208' |
| primary_id_pattern | N/A | SIG-000208 | no pattern for dataset | SIG-000208 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000208 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000208 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-AFB055C754E2; mission=MIS-20260815 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-AFB055C754E2; mission=MIS-20260815-B5CDB5; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020 | not enforced by integrity_guard | 2020 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000208 | primary id present | SIG-000208 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000208', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000208 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000208 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000208`

## CAND-3D80B53FE14D · Figure 1.18. Indonesia needs to expand its protected areas to reach the Aichi target

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-9CF2639B264C`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000207 | non-empty Signal ID | SIG-000207 | Signal ID='SIG-000207' |
| primary_id_pattern | N/A | SIG-000207 | no pattern for dataset | SIG-000207 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000207 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000207 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-9CF2639B264C; mission=MIS-20260815 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-9CF2639B264C; mission=MIS-20260815-B5CDB5; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000207 | primary id present | SIG-000207 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000207', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000207 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000207 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000207`

## CAND-18391326BBE3 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-9C3FE7A510A0`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000206 | non-empty Signal ID | SIG-000206 | Signal ID='SIG-000206' |
| primary_id_pattern | N/A | SIG-000206 | no pattern for dataset | SIG-000206 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000206 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000206 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-9C3FE7A510A0; mission=MIS-20260815-B | optional | present | provenance: source=SRC-000004; document=DOC-9C3FE7A510A0; mission=MIS-20260815-B5CDB5; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000206 | primary id present | SIG-000206 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000206', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000206 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000206 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000206`

## CAND-CE43E3FE2ACE · Consumer Attitudes Toward Imported and Local Produce in Indonesia: The Role of Country of Origin and Perception in Shapi

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-23B61DA3B184`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000210 | non-empty Signal ID | SIG-000210 | Signal ID='SIG-000210' |
| primary_id_pattern | N/A | SIG-000210 | no pattern for dataset | SIG-000210 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000210 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000210 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-23B61DA3B184; mission=MIS-20260815 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-23B61DA3B184; mission=MIS-20260815-B5CDB5; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2025 | not enforced by integrity_guard | 2025 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000210 | primary id present | SIG-000210 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000210', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000210 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000210 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000210`
