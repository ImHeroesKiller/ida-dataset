# Validation Trace

**Generated:** 2026-07-21T08:57:38+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-8AAD6AE805BB · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000614 | non-empty Signal ID | SIG-000614 | Signal ID='SIG-000614' |
| primary_id_pattern | N/A | SIG-000614 | no pattern for dataset | SIG-000614 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000614 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000614 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260721-1 | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260721-1350C4; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000614 | primary id present | SIG-000614 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000614', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000614 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000614 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000614`

## CAND-7916F282A65A · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000613 | non-empty Signal ID | SIG-000613 | Signal ID='SIG-000613' |
| primary_id_pattern | N/A | SIG-000613 | no pattern for dataset | SIG-000613 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000613 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000613 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260721 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260721-1350C4; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000613 | primary id present | SIG-000613 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000613', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000613 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000613 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000613`

## CAND-4F4C0907B3FF · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000612 | non-empty Signal ID | SIG-000612 | Signal ID='SIG-000612' |
| primary_id_pattern | N/A | SIG-000612 | no pattern for dataset | SIG-000612 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000612 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000612 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260721 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260721-1350C4; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000612 | primary id present | SIG-000612 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000612', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000612 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000612 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000612`

## CAND-5E9AB7056F2F · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000611 | non-empty Signal ID | SIG-000611 | Signal ID='SIG-000611' |
| primary_id_pattern | N/A | SIG-000611 | no pattern for dataset | SIG-000611 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000611 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000611 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260721-1 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260721-1350C4; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000611 | primary id present | SIG-000611 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000611', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000611 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000611 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000611`

## CAND-411FAA6F5720 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000610 | non-empty Signal ID | SIG-000610 | Signal ID='SIG-000610' |
| primary_id_pattern | N/A | SIG-000610 | no pattern for dataset | SIG-000610 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000610 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000610 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260721 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260721-1350C4; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000610 | primary id present | SIG-000610 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000610', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000610 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000610 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000610`
