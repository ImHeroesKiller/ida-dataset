# Validation Trace

**Generated:** 2026-07-31T10:59:35+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-D858D01B998A · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001152 | non-empty Signal ID | SIG-001152 | Signal ID='SIG-001152' |
| primary_id_pattern | N/A | SIG-001152 | no pattern for dataset | SIG-001152 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001152 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001152 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260731 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260731-2FF91D; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001152 | primary id present | SIG-001152 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001152', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-001152 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001152 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001152`

## CAND-3798B5C941AE · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001150 | non-empty Signal ID | SIG-001150 | Signal ID='SIG-001150' |
| primary_id_pattern | N/A | SIG-001150 | no pattern for dataset | SIG-001150 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001150 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001150 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260731 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260731-2FF91D; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001150 | primary id present | SIG-001150 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001150', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001150 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001150 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001150`

## CAND-E4519FFF6C6B · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001153 | non-empty Signal ID | SIG-001153 | Signal ID='SIG-001153' |
| primary_id_pattern | N/A | SIG-001153 | no pattern for dataset | SIG-001153 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001153 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001153 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260731 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260731-2FF91D; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001153 | primary id present | SIG-001153 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001153', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001153 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001153 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001153`

## CAND-228F80A2D5DA · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001151 | non-empty Signal ID | SIG-001151 | Signal ID='SIG-001151' |
| primary_id_pattern | N/A | SIG-001151 | no pattern for dataset | SIG-001151 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001151 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001151 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260731-2 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260731-2FF91D; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001151 | primary id present | SIG-001151 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001151', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001151 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001151 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001151`

## CAND-6A6D095B64D6 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001154 | non-empty Signal ID | SIG-001154 | Signal ID='SIG-001154' |
| primary_id_pattern | N/A | SIG-001154 | no pattern for dataset | SIG-001154 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001154 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001154 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260731-2 | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260731-2FF91D; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001154 | primary id present | SIG-001154 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001154', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001154 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001154 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001154`
