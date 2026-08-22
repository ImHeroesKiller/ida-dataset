# Validation Trace

**Generated:** 2026-08-22T20:42:42+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-EAAAB56AB09A · Product Innovation Toward MSME’s Market Performance On Creative Industry

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-8DEAD915EF6F`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001054 | non-empty Signal ID | SIG-001054 | Signal ID='SIG-001054' |
| primary_id_pattern | N/A | SIG-001054 | no pattern for dataset | SIG-001054 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001054 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001054 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-8DEAD915EF6F; mission=MIS-20260822 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-8DEAD915EF6F; mission=MIS-20260822-19955E; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2023 | not enforced by integrity_guard | 2023 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001054 | primary id present | SIG-001054 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001054', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001054 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001054 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001054`

## CAND-02CB67A3C06F · Consumer Attitudes Toward Imported and Local Produce in Indonesia: The Role of Country of Origin and Perception in Shapi

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-23B61DA3B184`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001055 | non-empty Signal ID | SIG-001055 | Signal ID='SIG-001055' |
| primary_id_pattern | N/A | SIG-001055 | no pattern for dataset | SIG-001055 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001055 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001055 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-23B61DA3B184; mission=MIS-20260822 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-23B61DA3B184; mission=MIS-20260822-19955E; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2025 | not enforced by integrity_guard | 2025 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001055 | primary id present | SIG-001055 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001055', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001055 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001055 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001055`

## CAND-0B6D550C4861 · Expand Target Market in Business

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-AFB055C754E2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001053 | non-empty Signal ID | SIG-001053 | Signal ID='SIG-001053' |
| primary_id_pattern | N/A | SIG-001053 | no pattern for dataset | SIG-001053 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001053 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001053 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-AFB055C754E2; mission=MIS-20260822 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-AFB055C754E2; mission=MIS-20260822-19955E; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020 | not enforced by integrity_guard | 2020 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001053 | primary id present | SIG-001053 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001053', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001053 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001053 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001053`

## CAND-D256C3477CFA · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-9C3FE7A510A0`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001051 | non-empty Signal ID | SIG-001051 | Signal ID='SIG-001051' |
| primary_id_pattern | N/A | SIG-001051 | no pattern for dataset | SIG-001051 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001051 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001051 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-9C3FE7A510A0; mission=MIS-20260822-1 | optional | present | provenance: source=SRC-000004; document=DOC-9C3FE7A510A0; mission=MIS-20260822-19955E; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001051 | primary id present | SIG-001051 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001051', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001051 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001051 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001051`

## CAND-9BCBA85DA2B0 · Figure 1.18. Indonesia needs to expand its protected areas to reach the Aichi target

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-9CF2639B264C`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001052 | non-empty Signal ID | SIG-001052 | Signal ID='SIG-001052' |
| primary_id_pattern | N/A | SIG-001052 | no pattern for dataset | SIG-001052 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001052 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001052 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-9CF2639B264C; mission=MIS-20260822 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-9CF2639B264C; mission=MIS-20260822-19955E; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001052 | primary id present | SIG-001052 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001052', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001052 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001052 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001052`
