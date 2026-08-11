# Validation Trace

**Generated:** 2026-08-11T18:18:31+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-3E6B54A5E96E · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001910 | non-empty Signal ID | SIG-001910 | Signal ID='SIG-001910' |
| primary_id_pattern | N/A | SIG-001910 | no pattern for dataset | SIG-001910 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001910 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001910 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260811 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260811-92BD13; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001910 | primary id present | SIG-001910 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001910', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001910 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001910 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001910`

## CAND-02C9262ACFE9 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001914 | non-empty Signal ID | SIG-001914 | Signal ID='SIG-001914' |
| primary_id_pattern | N/A | SIG-001914 | no pattern for dataset | SIG-001914 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001914 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001914 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260811-9 | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260811-92BD13; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001914 | primary id present | SIG-001914 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001914', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001914 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001914 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001914`

## CAND-39E565C75F37 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001912 | non-empty Signal ID | SIG-001912 | Signal ID='SIG-001912' |
| primary_id_pattern | N/A | SIG-001912 | no pattern for dataset | SIG-001912 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001912 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001912 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260811 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260811-92BD13; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001912 | primary id present | SIG-001912 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001912', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-001912 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001912 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001912`

## CAND-9281BEF85D9F · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001913 | non-empty Signal ID | SIG-001913 | Signal ID='SIG-001913' |
| primary_id_pattern | N/A | SIG-001913 | no pattern for dataset | SIG-001913 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001913 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001913 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260811 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260811-92BD13; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001913 | primary id present | SIG-001913 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001913', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001913 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001913 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001913`

## CAND-4BA0FA736164 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001911 | non-empty Signal ID | SIG-001911 | Signal ID='SIG-001911' |
| primary_id_pattern | N/A | SIG-001911 | no pattern for dataset | SIG-001911 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001911 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001911 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260811-9 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260811-92BD13; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001911 | primary id present | SIG-001911 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001911', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001911 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001911 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001911`
