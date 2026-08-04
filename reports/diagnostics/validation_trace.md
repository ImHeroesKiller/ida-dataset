# Validation Trace

**Generated:** 2026-08-04T00:25:34+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-4ECB6AB85E95 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001349 | non-empty Signal ID | SIG-001349 | Signal ID='SIG-001349' |
| primary_id_pattern | N/A | SIG-001349 | no pattern for dataset | SIG-001349 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001349 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001349 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260804-A | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260804-AF179C; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001349 | primary id present | SIG-001349 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001349', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001349 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001349 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001349`

## CAND-B599C3EDCBD0 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001347 | non-empty Signal ID | SIG-001347 | Signal ID='SIG-001347' |
| primary_id_pattern | N/A | SIG-001347 | no pattern for dataset | SIG-001347 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001347 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001347 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260804 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260804-AF179C; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001347 | primary id present | SIG-001347 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001347', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-001347 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001347 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001347`

## CAND-ACB5FB4C3B72 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001346 | non-empty Signal ID | SIG-001346 | Signal ID='SIG-001346' |
| primary_id_pattern | N/A | SIG-001346 | no pattern for dataset | SIG-001346 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001346 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001346 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260804-A | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260804-AF179C; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001346 | primary id present | SIG-001346 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001346', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001346 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001346 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001346`

## CAND-06C20DB8962F · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001345 | non-empty Signal ID | SIG-001345 | Signal ID='SIG-001345' |
| primary_id_pattern | N/A | SIG-001345 | no pattern for dataset | SIG-001345 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001345 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001345 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260804 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260804-AF179C; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001345 | primary id present | SIG-001345 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001345', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001345 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001345 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001345`

## CAND-1CC4EFBF8AF4 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001348 | non-empty Signal ID | SIG-001348 | Signal ID='SIG-001348' |
| primary_id_pattern | N/A | SIG-001348 | no pattern for dataset | SIG-001348 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001348 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001348 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260804 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260804-AF179C; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001348 | primary id present | SIG-001348 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001348', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001348 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001348 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001348`
