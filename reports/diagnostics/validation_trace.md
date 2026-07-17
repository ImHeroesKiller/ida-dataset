# Validation Trace

**Generated:** 2026-07-17T12:15:10+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-9819CBD6F48B · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000371 | non-empty Signal ID | SIG-000371 | Signal ID='SIG-000371' |
| primary_id_pattern | N/A | SIG-000371 | no pattern for dataset | SIG-000371 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000371 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000371 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260717-5 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260717-56CCB7; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000371 | primary id present | SIG-000371 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000371', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000371 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000371 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000371`

## CAND-77B1F26BB6AE · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-2430A598BF3B`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000374 | non-empty Signal ID | SIG-000374 | Signal ID='SIG-000374' |
| primary_id_pattern | N/A | SIG-000374 | no pattern for dataset | SIG-000374 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000374 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000374 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260717-5 | optional | present | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260717-56CCB7; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000374 | primary id present | SIG-000374 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000374', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000374 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000374 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000374`

## CAND-2BD7862F1812 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000370 | non-empty Signal ID | SIG-000370 | Signal ID='SIG-000370' |
| primary_id_pattern | N/A | SIG-000370 | no pattern for dataset | SIG-000370 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000370 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000370 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260717 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260717-56CCB7; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000370 | primary id present | SIG-000370 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000370', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000370 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000370 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000370`

## CAND-E0AA2401D8DC · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000373 | non-empty Signal ID | SIG-000373 | Signal ID='SIG-000373' |
| primary_id_pattern | N/A | SIG-000373 | no pattern for dataset | SIG-000373 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000373 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000373 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260717 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260717-56CCB7; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000373 | primary id present | SIG-000373 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000373', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000373 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000373 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000373`

## CAND-AAA89471219C · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000372 | non-empty Signal ID | SIG-000372 | Signal ID='SIG-000372' |
| primary_id_pattern | N/A | SIG-000372 | no pattern for dataset | SIG-000372 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000372 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000372 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260717 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260717-56CCB7; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000372 | primary id present | SIG-000372 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000372', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000372 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000372 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000372`
