# Validation Trace

**Generated:** 2026-07-23T11:31:09+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-06CB15C60E4D · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000729 | non-empty Signal ID | SIG-000729 | Signal ID='SIG-000729' |
| primary_id_pattern | N/A | SIG-000729 | no pattern for dataset | SIG-000729 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000729 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000729 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260723-2 | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260723-2D6196; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000729 | primary id present | SIG-000729 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000729', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000729 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000729 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000729`

## CAND-45F9EBB55C20 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000725 | non-empty Signal ID | SIG-000725 | Signal ID='SIG-000725' |
| primary_id_pattern | N/A | SIG-000725 | no pattern for dataset | SIG-000725 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000725 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000725 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260723 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260723-2D6196; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000725 | primary id present | SIG-000725 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000725', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000725 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000725 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000725`

## CAND-A985D3AF815D · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000726 | non-empty Signal ID | SIG-000726 | Signal ID='SIG-000726' |
| primary_id_pattern | N/A | SIG-000726 | no pattern for dataset | SIG-000726 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000726 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000726 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260723-2 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260723-2D6196; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000726 | primary id present | SIG-000726 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000726', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000726 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000726 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000726`

## CAND-1A38F65BEC8F · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000728 | non-empty Signal ID | SIG-000728 | Signal ID='SIG-000728' |
| primary_id_pattern | N/A | SIG-000728 | no pattern for dataset | SIG-000728 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000728 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000728 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260723 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260723-2D6196; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000728 | primary id present | SIG-000728 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000728', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000728 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000728 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000728`

## CAND-B840056ABDCC · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000727 | non-empty Signal ID | SIG-000727 | Signal ID='SIG-000727' |
| primary_id_pattern | N/A | SIG-000727 | no pattern for dataset | SIG-000727 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000727 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000727 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260723 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260723-2D6196; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000727 | primary id present | SIG-000727 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000727', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000727 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000727 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000727`
