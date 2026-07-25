# Validation Trace

**Generated:** 2026-07-25T20:29:56+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-B87E9AF53D9C · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000862 | non-empty Signal ID | SIG-000862 | Signal ID='SIG-000862' |
| primary_id_pattern | N/A | SIG-000862 | no pattern for dataset | SIG-000862 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000862 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000862 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260725 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260725-C54526; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000862 | primary id present | SIG-000862 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000862', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000862 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000862 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000862`

## CAND-650F46C17F4D · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000863 | non-empty Signal ID | SIG-000863 | Signal ID='SIG-000863' |
| primary_id_pattern | N/A | SIG-000863 | no pattern for dataset | SIG-000863 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000863 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000863 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260725 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260725-C54526; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000863 | primary id present | SIG-000863 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000863', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000863 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000863 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000863`

## CAND-7F41E075AEE4 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000864 | non-empty Signal ID | SIG-000864 | Signal ID='SIG-000864' |
| primary_id_pattern | N/A | SIG-000864 | no pattern for dataset | SIG-000864 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000864 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000864 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260725-C | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260725-C54526; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000864 | primary id present | SIG-000864 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000864', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000864 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000864 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000864`

## CAND-A6A9981B71C4 · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000860 | non-empty Signal ID | SIG-000860 | Signal ID='SIG-000860' |
| primary_id_pattern | N/A | SIG-000860 | no pattern for dataset | SIG-000860 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000860 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000860 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260725 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260725-C54526; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000860 | primary id present | SIG-000860 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000860', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000860 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000860 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000860`

## CAND-852B3D49C0D2 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000861 | non-empty Signal ID | SIG-000861 | Signal ID='SIG-000861' |
| primary_id_pattern | N/A | SIG-000861 | no pattern for dataset | SIG-000861 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000861 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000861 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260725-C | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260725-C54526; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000861 | primary id present | SIG-000861 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000861', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000861 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000861 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000861`
