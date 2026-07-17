# Validation Trace

**Generated:** 2026-07-17T15:33:31+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-8CA6977D8E36 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000381 | non-empty Signal ID | SIG-000381 | Signal ID='SIG-000381' |
| primary_id_pattern | N/A | SIG-000381 | no pattern for dataset | SIG-000381 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000381 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000381 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260717-B | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260717-B36087; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000381 | primary id present | SIG-000381 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000381', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000381 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000381 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000381`

## CAND-FE6F4FFF3A05 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D733F4309CB6`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000383 | non-empty Signal ID | SIG-000383 | Signal ID='SIG-000383' |
| primary_id_pattern | N/A | SIG-000383 | no pattern for dataset | SIG-000383 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000383 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000383 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D733F4309CB6; mission=MIS-20260717-B | optional | present | provenance: source=SRC-000004; document=DOC-D733F4309CB6; mission=MIS-20260717-B36087; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000383 | primary id present | SIG-000383 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000383', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000383 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000383 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000383`

## CAND-20BF7B4CAADE · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000382 | non-empty Signal ID | SIG-000382 | Signal ID='SIG-000382' |
| primary_id_pattern | N/A | SIG-000382 | no pattern for dataset | SIG-000382 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000382 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000382 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260717 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260717-B36087; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000382 | primary id present | SIG-000382 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000382', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000382 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000382 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000382`

## CAND-9330E3DAEA96 · Library Service Quality and Student Trust A Case Study of the University of Sumatera Utara Library, Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-05E7BC8EA754`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000384 | non-empty Signal ID | SIG-000384 | Signal ID='SIG-000384' |
| primary_id_pattern | N/A | SIG-000384 | no pattern for dataset | SIG-000384 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000384 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000384 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-05E7BC8EA754; mission=MIS-20260717 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-05E7BC8EA754; mission=MIS-20260717-B36087; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2021 | not enforced by integrity_guard | 2021 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000384 | primary id present | SIG-000384 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000384', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000384 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000384 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000384`

## CAND-EE41532A5E80 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000380 | non-empty Signal ID | SIG-000380 | Signal ID='SIG-000380' |
| primary_id_pattern | N/A | SIG-000380 | no pattern for dataset | SIG-000380 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000380 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000380 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260717 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260717-B36087; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000380 | primary id present | SIG-000380 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000380', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000380 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000380 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000380`
