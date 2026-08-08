# Validation Trace

**Generated:** 2026-08-08T15:50:07+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-6AECE3D3686B · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001632 | non-empty Signal ID | SIG-001632 | Signal ID='SIG-001632' |
| primary_id_pattern | N/A | SIG-001632 | no pattern for dataset | SIG-001632 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001632 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001632 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260808 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260808-3BD19B; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001632 | primary id present | SIG-001632 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001632', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001632 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001632 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001632`

## CAND-B623A3644BA3 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001631 | non-empty Signal ID | SIG-001631 | Signal ID='SIG-001631' |
| primary_id_pattern | N/A | SIG-001631 | no pattern for dataset | SIG-001631 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001631 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001631 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260808-3 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260808-3BD19B; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001631 | primary id present | SIG-001631 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001631', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001631 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001631 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001631`

## CAND-A88774C2D0CD · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001630 | non-empty Signal ID | SIG-001630 | Signal ID='SIG-001630' |
| primary_id_pattern | N/A | SIG-001630 | no pattern for dataset | SIG-001630 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001630 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001630 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260808 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260808-3BD19B; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001630 | primary id present | SIG-001630 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001630', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001630 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001630 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001630`

## CAND-B5AC4EEBB0A9 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001633 | non-empty Signal ID | SIG-001633 | Signal ID='SIG-001633' |
| primary_id_pattern | N/A | SIG-001633 | no pattern for dataset | SIG-001633 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001633 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001633 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260808-3 | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260808-3BD19B; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001633 | primary id present | SIG-001633 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001633', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001633 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001633 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001633`

## CAND-1DBCD08404B4 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001634 | non-empty Signal ID | SIG-001634 | Signal ID='SIG-001634' |
| primary_id_pattern | N/A | SIG-001634 | no pattern for dataset | SIG-001634 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001634 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001634 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260808 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260808-3BD19B; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001634 | primary id present | SIG-001634 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001634', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001634 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001634 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001634`
