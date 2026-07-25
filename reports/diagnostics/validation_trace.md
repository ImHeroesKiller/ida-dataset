# Validation Trace

**Generated:** 2026-07-25T15:23:04+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-0EA64FEDB179 · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000845 | non-empty Signal ID | SIG-000845 | Signal ID='SIG-000845' |
| primary_id_pattern | N/A | SIG-000845 | no pattern for dataset | SIG-000845 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000845 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000845 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260725 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260725-A4BE9E; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000845 | primary id present | SIG-000845 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000845', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000845 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000845 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000845`

## CAND-B2E5924C2CFE · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000849 | non-empty Signal ID | SIG-000849 | Signal ID='SIG-000849' |
| primary_id_pattern | N/A | SIG-000849 | no pattern for dataset | SIG-000849 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000849 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000849 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260725-A | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260725-A4BE9E; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000849 | primary id present | SIG-000849 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000849', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000849 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000849 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000849`

## CAND-98D90CC250BA · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000846 | non-empty Signal ID | SIG-000846 | Signal ID='SIG-000846' |
| primary_id_pattern | N/A | SIG-000846 | no pattern for dataset | SIG-000846 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000846 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000846 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260725-A | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260725-A4BE9E; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000846 | primary id present | SIG-000846 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000846', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000846 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000846 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000846`

## CAND-5EBC5E009E8B · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000848 | non-empty Signal ID | SIG-000848 | Signal ID='SIG-000848' |
| primary_id_pattern | N/A | SIG-000848 | no pattern for dataset | SIG-000848 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000848 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000848 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260725 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260725-A4BE9E; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000848 | primary id present | SIG-000848 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000848', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000848 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000848 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000848`

## CAND-D06F270EA1DE · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000847 | non-empty Signal ID | SIG-000847 | Signal ID='SIG-000847' |
| primary_id_pattern | N/A | SIG-000847 | no pattern for dataset | SIG-000847 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000847 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000847 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260725 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260725-A4BE9E; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000847 | primary id present | SIG-000847 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000847', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000847 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000847 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000847`
