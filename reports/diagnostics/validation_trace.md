# Validation Trace

**Generated:** 2026-08-12T21:05:20+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-5A918C6A9299 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-002002 | non-empty Signal ID | SIG-002002 | Signal ID='SIG-002002' |
| primary_id_pattern | N/A | SIG-002002 | no pattern for dataset | SIG-002002 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-002002 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-002002 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260812 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260812-BFDF73; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-002002 | primary id present | SIG-002002 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-002002', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-002002 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-002002 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-002002`

## CAND-B040608D017A · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-002001 | non-empty Signal ID | SIG-002001 | Signal ID='SIG-002001' |
| primary_id_pattern | N/A | SIG-002001 | no pattern for dataset | SIG-002001 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-002001 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-002001 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260812-B | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260812-BFDF73; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-002001 | primary id present | SIG-002001 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-002001', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-002001 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-002001 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-002001`

## CAND-B6424A3DF845 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-002003 | non-empty Signal ID | SIG-002003 | Signal ID='SIG-002003' |
| primary_id_pattern | N/A | SIG-002003 | no pattern for dataset | SIG-002003 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-002003 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-002003 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260812 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260812-BFDF73; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-002003 | primary id present | SIG-002003 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-002003', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-002003 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-002003 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-002003`

## CAND-037741AC48DC · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-002004 | non-empty Signal ID | SIG-002004 | Signal ID='SIG-002004' |
| primary_id_pattern | N/A | SIG-002004 | no pattern for dataset | SIG-002004 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-002004 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-002004 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260812-B | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260812-BFDF73; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-002004 | primary id present | SIG-002004 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-002004', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-002004 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-002004 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-002004`

## CAND-B9F344241504 · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-002000 | non-empty Signal ID | SIG-002000 | Signal ID='SIG-002000' |
| primary_id_pattern | N/A | SIG-002000 | no pattern for dataset | SIG-002000 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-002000 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-002000 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260812 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260812-BFDF73; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-002000 | primary id present | SIG-002000 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-002000', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-002000 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-002000 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-002000`
