# Validation Trace

**Generated:** 2026-07-26T09:32:11+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-ED35848A74B3 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000893 | non-empty Signal ID | SIG-000893 | Signal ID='SIG-000893' |
| primary_id_pattern | N/A | SIG-000893 | no pattern for dataset | SIG-000893 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000893 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000893 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260726 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260726-89B3FE; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000893 | primary id present | SIG-000893 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000893', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000893 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000893 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000893`

## CAND-3759CD8C90FA · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000890 | non-empty Signal ID | SIG-000890 | Signal ID='SIG-000890' |
| primary_id_pattern | N/A | SIG-000890 | no pattern for dataset | SIG-000890 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000890 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000890 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260726 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260726-89B3FE; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000890 | primary id present | SIG-000890 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000890', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000890 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000890 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000890`

## CAND-7FE8FC01326C · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000891 | non-empty Signal ID | SIG-000891 | Signal ID='SIG-000891' |
| primary_id_pattern | N/A | SIG-000891 | no pattern for dataset | SIG-000891 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000891 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000891 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260726-8 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260726-89B3FE; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000891 | primary id present | SIG-000891 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000891', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000891 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000891 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000891`

## CAND-EF38178C413D · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000894 | non-empty Signal ID | SIG-000894 | Signal ID='SIG-000894' |
| primary_id_pattern | N/A | SIG-000894 | no pattern for dataset | SIG-000894 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000894 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000894 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260726-8 | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260726-89B3FE; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000894 | primary id present | SIG-000894 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000894', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000894 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000894 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000894`

## CAND-E03A7612AE91 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000892 | non-empty Signal ID | SIG-000892 | Signal ID='SIG-000892' |
| primary_id_pattern | N/A | SIG-000892 | no pattern for dataset | SIG-000892 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000892 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000892 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260726 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260726-89B3FE; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000892 | primary id present | SIG-000892 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000892', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000892 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000892 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000892`
