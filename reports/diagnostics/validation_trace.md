# Validation Trace

**Generated:** 2026-07-18T11:22:57+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-3F6ECD6759E7 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000432 | non-empty Signal ID | SIG-000432 | Signal ID='SIG-000432' |
| primary_id_pattern | N/A | SIG-000432 | no pattern for dataset | SIG-000432 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000432 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000432 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260718 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260718-B560A0; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000432 | primary id present | SIG-000432 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000432', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000432 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000432 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000432`

## CAND-A1F0E79330D4 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000430 | non-empty Signal ID | SIG-000430 | Signal ID='SIG-000430' |
| primary_id_pattern | N/A | SIG-000430 | no pattern for dataset | SIG-000430 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000430 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000430 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260718 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260718-B560A0; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000430 | primary id present | SIG-000430 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000430', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000430 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000430 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000430`

## CAND-82092104628F · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000433 | non-empty Signal ID | SIG-000433 | Signal ID='SIG-000433' |
| primary_id_pattern | N/A | SIG-000433 | no pattern for dataset | SIG-000433 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000433 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000433 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260718 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260718-B560A0; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000433 | primary id present | SIG-000433 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000433', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000433 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000433 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000433`

## CAND-C1D7A8DE26A9 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000431 | non-empty Signal ID | SIG-000431 | Signal ID='SIG-000431' |
| primary_id_pattern | N/A | SIG-000431 | no pattern for dataset | SIG-000431 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000431 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000431 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260718-B | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260718-B560A0; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000431 | primary id present | SIG-000431 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000431', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000431 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000431 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000431`

## CAND-3D7023F3ACD6 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-2430A598BF3B`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000434 | non-empty Signal ID | SIG-000434 | Signal ID='SIG-000434' |
| primary_id_pattern | N/A | SIG-000434 | no pattern for dataset | SIG-000434 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000434 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000434 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260718-B | optional | present | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260718-B560A0; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000434 | primary id present | SIG-000434 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000434', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000434 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000434 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000434`
