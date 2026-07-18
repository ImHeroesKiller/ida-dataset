# Validation Trace

**Generated:** 2026-07-18T05:47:09+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-F505032B3A22 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000416 | non-empty Signal ID | SIG-000416 | Signal ID='SIG-000416' |
| primary_id_pattern | N/A | SIG-000416 | no pattern for dataset | SIG-000416 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000416 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000416 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260718-C | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260718-CADF5A; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000416 | primary id present | SIG-000416 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000416', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000416 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000416 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000416`

## CAND-4197FA6C1C4C · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-C59E093AE6F0`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000419 | non-empty Signal ID | SIG-000419 | Signal ID='SIG-000419' |
| primary_id_pattern | N/A | SIG-000419 | no pattern for dataset | SIG-000419 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000419 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000419 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-C59E093AE6F0; mission=MIS-20260718-C | optional | present | provenance: source=SRC-000004; document=DOC-C59E093AE6F0; mission=MIS-20260718-CADF5A; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000419 | primary id present | SIG-000419 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000419', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000419 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000419 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000419`

## CAND-5D6B8AA04843 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000415 | non-empty Signal ID | SIG-000415 | Signal ID='SIG-000415' |
| primary_id_pattern | N/A | SIG-000415 | no pattern for dataset | SIG-000415 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000415 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000415 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260718 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260718-CADF5A; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000415 | primary id present | SIG-000415 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000415', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000415 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000415 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000415`

## CAND-73D1AE6539B6 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000417 | non-empty Signal ID | SIG-000417 | Signal ID='SIG-000417' |
| primary_id_pattern | N/A | SIG-000417 | no pattern for dataset | SIG-000417 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000417 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000417 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260718 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260718-CADF5A; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000417 | primary id present | SIG-000417 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000417', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000417 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000417 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000417`

## CAND-827778244A56 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000418 | non-empty Signal ID | SIG-000418 | Signal ID='SIG-000418' |
| primary_id_pattern | N/A | SIG-000418 | no pattern for dataset | SIG-000418 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000418 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000418 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260718 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260718-CADF5A; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000418 | primary id present | SIG-000418 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000418', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000418 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000418 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000418`
