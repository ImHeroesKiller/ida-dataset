# Validation Trace

**Generated:** 2026-07-18T22:14:01+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-F5A82C597F45 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000469 | non-empty Signal ID | SIG-000469 | Signal ID='SIG-000469' |
| primary_id_pattern | N/A | SIG-000469 | no pattern for dataset | SIG-000469 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000469 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000469 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260718-D | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260718-D23C77; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000469 | primary id present | SIG-000469 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000469', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000469 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000469 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000469`

## CAND-9FAFF8D842A5 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000465 | non-empty Signal ID | SIG-000465 | Signal ID='SIG-000465' |
| primary_id_pattern | N/A | SIG-000465 | no pattern for dataset | SIG-000465 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000465 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000465 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260718 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260718-D23C77; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000465 | primary id present | SIG-000465 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000465', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000465 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000465 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000465`

## CAND-67D1020D67BA · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000467 | non-empty Signal ID | SIG-000467 | Signal ID='SIG-000467' |
| primary_id_pattern | N/A | SIG-000467 | no pattern for dataset | SIG-000467 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000467 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000467 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260718 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260718-D23C77; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000467 | primary id present | SIG-000467 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000467', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000467 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000467 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000467`

## CAND-8B96638C998B · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000466 | non-empty Signal ID | SIG-000466 | Signal ID='SIG-000466' |
| primary_id_pattern | N/A | SIG-000466 | no pattern for dataset | SIG-000466 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000466 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000466 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260718-D | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260718-D23C77; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000466 | primary id present | SIG-000466 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000466', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000466 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000466 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000466`

## CAND-29C8C08F7663 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000468 | non-empty Signal ID | SIG-000468 | Signal ID='SIG-000468' |
| primary_id_pattern | N/A | SIG-000468 | no pattern for dataset | SIG-000468 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000468 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000468 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260718 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260718-D23C77; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000468 | primary id present | SIG-000468 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000468', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000468 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000468 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000468`
