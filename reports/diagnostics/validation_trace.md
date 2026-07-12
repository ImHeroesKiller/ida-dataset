# Validation Trace

**Generated:** 2026-07-12T06:54:49+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-B01FF3661621 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000082 | non-empty Signal ID | SIG-000082 | Signal ID='SIG-000082' |
| primary_id_pattern | N/A | SIG-000082 | no pattern for dataset | SIG-000082 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000082 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000082 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260712 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260712-27FCB6; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000082 | primary id present | SIG-000082 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000082', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000082 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000082 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000082`

## CAND-DBA61E770828 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000083 | non-empty Signal ID | SIG-000083 | Signal ID='SIG-000083' |
| primary_id_pattern | N/A | SIG-000083 | no pattern for dataset | SIG-000083 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000083 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000083 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260712 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260712-27FCB6; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000083 | primary id present | SIG-000083 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000083', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000083 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000083 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000083`

## CAND-3E27E3F8FA68 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000081 | non-empty Signal ID | SIG-000081 | Signal ID='SIG-000081' |
| primary_id_pattern | N/A | SIG-000081 | no pattern for dataset | SIG-000081 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000081 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000081 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260712-2 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260712-27FCB6; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000081 | primary id present | SIG-000081 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000081', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000081 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000081 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000081`

## CAND-1B872BD3F954 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000080 | non-empty Signal ID | SIG-000080 | Signal ID='SIG-000080' |
| primary_id_pattern | N/A | SIG-000080 | no pattern for dataset | SIG-000080 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000080 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000080 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260712 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260712-27FCB6; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000080 | primary id present | SIG-000080 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000080', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000080 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000080 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000080`

## CAND-9FE40C8ECC48 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-2430A598BF3B`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000084 | non-empty Signal ID | SIG-000084 | Signal ID='SIG-000084' |
| primary_id_pattern | N/A | SIG-000084 | no pattern for dataset | SIG-000084 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000084 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000084 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260712-2 | optional | present | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260712-27FCB6; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000084 | primary id present | SIG-000084 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000084', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000084 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000084 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000084`
