# Validation Trace

**Generated:** 2026-08-15T17:31:27+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-0CBFCC3693F4 · Consumer Attitudes Toward Imported and Local Produce in Indonesia: The Role of Country of Origin and Perception in Shapi

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-23B61DA3B184`

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
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-23B61DA3B184; mission=MIS-20260815 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-23B61DA3B184; mission=MIS-20260815-709A2D; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2025 | not enforced by integrity_guard | 2025 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000250 | primary id present | SIG-000250 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000250', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000250 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000250 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000250`

## CAND-6B8D381EE9E5 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-9C3FE7A510A0`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000246 | non-empty Signal ID | SIG-000246 | Signal ID='SIG-000246' |
| primary_id_pattern | N/A | SIG-000246 | no pattern for dataset | SIG-000246 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000246 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000246 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-9C3FE7A510A0; mission=MIS-20260815-7 | optional | present | provenance: source=SRC-000004; document=DOC-9C3FE7A510A0; mission=MIS-20260815-709A2D; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000246 | primary id present | SIG-000246 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000246', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000246 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000246 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000246`

## CAND-5A9582A71A21 · Expand Target Market in Business

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-AFB055C754E2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000248 | non-empty Signal ID | SIG-000248 | Signal ID='SIG-000248' |
| primary_id_pattern | N/A | SIG-000248 | no pattern for dataset | SIG-000248 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000248 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000248 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-AFB055C754E2; mission=MIS-20260815 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-AFB055C754E2; mission=MIS-20260815-709A2D; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020 | not enforced by integrity_guard | 2020 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000248 | primary id present | SIG-000248 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000248', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000248 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000248 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000248`

## CAND-9283156F2D22 · Product Innovation Toward MSME’s Market Performance On Creative Industry

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-8DEAD915EF6F`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000249 | non-empty Signal ID | SIG-000249 | Signal ID='SIG-000249' |
| primary_id_pattern | N/A | SIG-000249 | no pattern for dataset | SIG-000249 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000249 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000249 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-8DEAD915EF6F; mission=MIS-20260815 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-8DEAD915EF6F; mission=MIS-20260815-709A2D; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2023 | not enforced by integrity_guard | 2023 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000249 | primary id present | SIG-000249 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000249', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000249 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000249 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000249`

## CAND-664086CCCF41 · Figure 1.18. Indonesia needs to expand its protected areas to reach the Aichi target

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-9CF2639B264C`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000247 | non-empty Signal ID | SIG-000247 | Signal ID='SIG-000247' |
| primary_id_pattern | N/A | SIG-000247 | no pattern for dataset | SIG-000247 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000247 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000247 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-9CF2639B264C; mission=MIS-20260815 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-9CF2639B264C; mission=MIS-20260815-709A2D; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000247 | primary id present | SIG-000247 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000247', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000247 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000247 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000247`
