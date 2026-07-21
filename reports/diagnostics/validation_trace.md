# Validation Trace

**Generated:** 2026-07-21T23:19:30+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-A23E98EA074F · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000650 | non-empty Signal ID | SIG-000650 | Signal ID='SIG-000650' |
| primary_id_pattern | N/A | SIG-000650 | no pattern for dataset | SIG-000650 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000650 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000650 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260721 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260721-FEAF4F; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000650 | primary id present | SIG-000650 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000650', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000650 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000650 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000650`

## CAND-B8AC5718E1F9 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000652 | non-empty Signal ID | SIG-000652 | Signal ID='SIG-000652' |
| primary_id_pattern | N/A | SIG-000652 | no pattern for dataset | SIG-000652 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000652 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000652 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260721 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260721-FEAF4F; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000652 | primary id present | SIG-000652 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000652', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000652 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000652 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000652`

## CAND-C5EB632EA68C · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000651 | non-empty Signal ID | SIG-000651 | Signal ID='SIG-000651' |
| primary_id_pattern | N/A | SIG-000651 | no pattern for dataset | SIG-000651 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000651 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000651 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260721-F | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260721-FEAF4F; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000651 | primary id present | SIG-000651 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000651', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000651 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000651 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000651`

## CAND-1FB6EEA8DA5F · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000653 | non-empty Signal ID | SIG-000653 | Signal ID='SIG-000653' |
| primary_id_pattern | N/A | SIG-000653 | no pattern for dataset | SIG-000653 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000653 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000653 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260721 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260721-FEAF4F; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000653 | primary id present | SIG-000653 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000653', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000653 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000653 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000653`

## CAND-BD1BDE2903BC · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000654 | non-empty Signal ID | SIG-000654 | Signal ID='SIG-000654' |
| primary_id_pattern | N/A | SIG-000654 | no pattern for dataset | SIG-000654 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000654 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000654 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260721-F | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260721-FEAF4F; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000654 | primary id present | SIG-000654 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000654', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000654 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000654 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000654`
