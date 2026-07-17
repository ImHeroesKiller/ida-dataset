# Validation Trace

**Generated:** 2026-07-17T21:17:01+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-4BCFDAB440A0 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000398 | non-empty Signal ID | SIG-000398 | Signal ID='SIG-000398' |
| primary_id_pattern | N/A | SIG-000398 | no pattern for dataset | SIG-000398 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000398 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000398 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260717 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260717-FE7E63; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000398 | primary id present | SIG-000398 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000398', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000398 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000398 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000398`

## CAND-267F0F640438 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000397 | non-empty Signal ID | SIG-000397 | Signal ID='SIG-000397' |
| primary_id_pattern | N/A | SIG-000397 | no pattern for dataset | SIG-000397 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000397 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000397 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260717 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260717-FE7E63; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000397 | primary id present | SIG-000397 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000397', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000397 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000397 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000397`

## CAND-88379B983854 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000396 | non-empty Signal ID | SIG-000396 | Signal ID='SIG-000396' |
| primary_id_pattern | N/A | SIG-000396 | no pattern for dataset | SIG-000396 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000396 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000396 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260717-F | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260717-FE7E63; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000396 | primary id present | SIG-000396 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000396', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000396 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000396 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000396`

## CAND-E28AB473F669 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-2430A598BF3B`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000399 | non-empty Signal ID | SIG-000399 | Signal ID='SIG-000399' |
| primary_id_pattern | N/A | SIG-000399 | no pattern for dataset | SIG-000399 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000399 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000399 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260717-F | optional | present | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260717-FE7E63; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000399 | primary id present | SIG-000399 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000399', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000399 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000399 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000399`

## CAND-8E57E1555839 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000395 | non-empty Signal ID | SIG-000395 | Signal ID='SIG-000395' |
| primary_id_pattern | N/A | SIG-000395 | no pattern for dataset | SIG-000395 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000395 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000395 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260717 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260717-FE7E63; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000395 | primary id present | SIG-000395 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000395', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000395 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000395 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000395`
