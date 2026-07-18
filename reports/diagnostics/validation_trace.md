# Validation Trace

**Generated:** 2026-07-18T13:39:22+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-1EC3689B65BE · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000438 | non-empty Signal ID | SIG-000438 | Signal ID='SIG-000438' |
| primary_id_pattern | N/A | SIG-000438 | no pattern for dataset | SIG-000438 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000438 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000438 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260718 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260718-698648; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000438 | primary id present | SIG-000438 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000438', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000438 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000438 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000438`

## CAND-30C8864AD342 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000435 | non-empty Signal ID | SIG-000435 | Signal ID='SIG-000435' |
| primary_id_pattern | N/A | SIG-000435 | no pattern for dataset | SIG-000435 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000435 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000435 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260718 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260718-698648; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000435 | primary id present | SIG-000435 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000435', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000435 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000435 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000435`

## CAND-E1304F6EE41E · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D733F4309CB6`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000439 | non-empty Signal ID | SIG-000439 | Signal ID='SIG-000439' |
| primary_id_pattern | N/A | SIG-000439 | no pattern for dataset | SIG-000439 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000439 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000439 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D733F4309CB6; mission=MIS-20260718-6 | optional | present | provenance: source=SRC-000004; document=DOC-D733F4309CB6; mission=MIS-20260718-698648; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000439 | primary id present | SIG-000439 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000439', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000439 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000439 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000439`

## CAND-20210E3916D7 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000437 | non-empty Signal ID | SIG-000437 | Signal ID='SIG-000437' |
| primary_id_pattern | N/A | SIG-000437 | no pattern for dataset | SIG-000437 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000437 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000437 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260718 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260718-698648; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000437 | primary id present | SIG-000437 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000437', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000437 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000437 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000437`

## CAND-DFF82AD29449 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000436 | non-empty Signal ID | SIG-000436 | Signal ID='SIG-000436' |
| primary_id_pattern | N/A | SIG-000436 | no pattern for dataset | SIG-000436 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000436 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000436 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260718-6 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260718-698648; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000436 | primary id present | SIG-000436 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000436', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000436 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000436 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000436`
