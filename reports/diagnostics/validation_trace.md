# Validation Trace

**Generated:** 2026-07-18T23:10:22+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-148A618804CB · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000471 | non-empty Signal ID | SIG-000471 | Signal ID='SIG-000471' |
| primary_id_pattern | N/A | SIG-000471 | no pattern for dataset | SIG-000471 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000471 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000471 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260718-4 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260718-4583FC; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000471 | primary id present | SIG-000471 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000471', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000471 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000471 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000471`

## CAND-8EE68249F6AB · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000472 | non-empty Signal ID | SIG-000472 | Signal ID='SIG-000472' |
| primary_id_pattern | N/A | SIG-000472 | no pattern for dataset | SIG-000472 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000472 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000472 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260718 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260718-4583FC; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000472 | primary id present | SIG-000472 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000472', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000472 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000472 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000472`

## CAND-F18B12F4FAE7 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-C59E093AE6F0`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000473 | non-empty Signal ID | SIG-000473 | Signal ID='SIG-000473' |
| primary_id_pattern | N/A | SIG-000473 | no pattern for dataset | SIG-000473 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000473 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000473 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-C59E093AE6F0; mission=MIS-20260718-4 | optional | present | provenance: source=SRC-000004; document=DOC-C59E093AE6F0; mission=MIS-20260718-4583FC; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000473 | primary id present | SIG-000473 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000473', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000473 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000473 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000473`

## CAND-CE114C00B870 · Library Service Quality and Student Trust A Case Study of the University of Sumatera Utara Library, Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-05E7BC8EA754`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000474 | non-empty Signal ID | SIG-000474 | Signal ID='SIG-000474' |
| primary_id_pattern | N/A | SIG-000474 | no pattern for dataset | SIG-000474 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000474 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000474 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-05E7BC8EA754; mission=MIS-20260718 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-05E7BC8EA754; mission=MIS-20260718-4583FC; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2021 | not enforced by integrity_guard | 2021 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000474 | primary id present | SIG-000474 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000474', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000474 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000474 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000474`

## CAND-0616C3422B01 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000470 | non-empty Signal ID | SIG-000470 | Signal ID='SIG-000470' |
| primary_id_pattern | N/A | SIG-000470 | no pattern for dataset | SIG-000470 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000470 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000470 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260718 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260718-4583FC; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000470 | primary id present | SIG-000470 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000470', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000470 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000470 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000470`
