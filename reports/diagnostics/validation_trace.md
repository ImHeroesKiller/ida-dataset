# Validation Trace

**Generated:** 2026-08-19T09:54:14+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-4D9509F76F88 · Figure 1.18. Indonesia needs to expand its protected areas to reach the Aichi target

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-9CF2639B264C`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000657 | non-empty Signal ID | SIG-000657 | Signal ID='SIG-000657' |
| primary_id_pattern | N/A | SIG-000657 | no pattern for dataset | SIG-000657 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000657 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000657 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-9CF2639B264C; mission=MIS-20260819 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-9CF2639B264C; mission=MIS-20260819-C813F1; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000657 | primary id present | SIG-000657 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000657', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000657 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000657 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000657`

## CAND-16E0F0017282 · Expand Target Market in Business

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-AFB055C754E2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000658 | non-empty Signal ID | SIG-000658 | Signal ID='SIG-000658' |
| primary_id_pattern | N/A | SIG-000658 | no pattern for dataset | SIG-000658 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000658 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000658 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-AFB055C754E2; mission=MIS-20260819 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-AFB055C754E2; mission=MIS-20260819-C813F1; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020 | not enforced by integrity_guard | 2020 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000658 | primary id present | SIG-000658 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000658', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000658 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000658 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000658`

## CAND-D60A26CE580C · Consumer Attitudes Toward Imported and Local Produce in Indonesia: The Role of Country of Origin and Perception in Shapi

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-23B61DA3B184`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000660 | non-empty Signal ID | SIG-000660 | Signal ID='SIG-000660' |
| primary_id_pattern | N/A | SIG-000660 | no pattern for dataset | SIG-000660 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000660 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000660 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-23B61DA3B184; mission=MIS-20260819 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-23B61DA3B184; mission=MIS-20260819-C813F1; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2025 | not enforced by integrity_guard | 2025 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000660 | primary id present | SIG-000660 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000660', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000660 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000660 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000660`

## CAND-178B313E1B52 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-9C3FE7A510A0`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000656 | non-empty Signal ID | SIG-000656 | Signal ID='SIG-000656' |
| primary_id_pattern | N/A | SIG-000656 | no pattern for dataset | SIG-000656 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000656 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000656 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-9C3FE7A510A0; mission=MIS-20260819-C | optional | present | provenance: source=SRC-000004; document=DOC-9C3FE7A510A0; mission=MIS-20260819-C813F1; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000656 | primary id present | SIG-000656 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000656', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000656 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000656 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000656`

## CAND-4C7EF9116D0C · Product Innovation Toward MSME’s Market Performance On Creative Industry

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-8DEAD915EF6F`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000659 | non-empty Signal ID | SIG-000659 | Signal ID='SIG-000659' |
| primary_id_pattern | N/A | SIG-000659 | no pattern for dataset | SIG-000659 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000659 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000659 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-8DEAD915EF6F; mission=MIS-20260819 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-8DEAD915EF6F; mission=MIS-20260819-C813F1; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2023 | not enforced by integrity_guard | 2023 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000659 | primary id present | SIG-000659 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000659', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000659 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000659 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000659`
