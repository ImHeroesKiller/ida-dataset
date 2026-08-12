# Validation Trace

**Generated:** 2026-08-12T05:07:55+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-240682538B19 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001946 | non-empty Signal ID | SIG-001946 | Signal ID='SIG-001946' |
| primary_id_pattern | N/A | SIG-001946 | no pattern for dataset | SIG-001946 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001946 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001946 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260812-D | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260812-D33BFC; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001946 | primary id present | SIG-001946 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001946', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001946 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001946 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001946`

## CAND-3FAE1DF83DA2 · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001945 | non-empty Signal ID | SIG-001945 | Signal ID='SIG-001945' |
| primary_id_pattern | N/A | SIG-001945 | no pattern for dataset | SIG-001945 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001945 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001945 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260812 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260812-D33BFC; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001945 | primary id present | SIG-001945 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001945', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001945 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001945 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001945`

## CAND-7155E6FE26AC · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001949 | non-empty Signal ID | SIG-001949 | Signal ID='SIG-001949' |
| primary_id_pattern | N/A | SIG-001949 | no pattern for dataset | SIG-001949 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001949 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001949 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260812-D | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260812-D33BFC; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001949 | primary id present | SIG-001949 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001949', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001949 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001949 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001949`

## CAND-257E51F49F03 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001948 | non-empty Signal ID | SIG-001948 | Signal ID='SIG-001948' |
| primary_id_pattern | N/A | SIG-001948 | no pattern for dataset | SIG-001948 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001948 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001948 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260812 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260812-D33BFC; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001948 | primary id present | SIG-001948 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001948', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001948 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001948 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001948`

## CAND-B4FC156E9B91 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001947 | non-empty Signal ID | SIG-001947 | Signal ID='SIG-001947' |
| primary_id_pattern | N/A | SIG-001947 | no pattern for dataset | SIG-001947 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001947 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001947 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260812 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260812-D33BFC; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001947 | primary id present | SIG-001947 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001947', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-001947 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001947 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001947`
