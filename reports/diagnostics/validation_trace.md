# Validation Trace

**Generated:** 2026-07-11T17:10:54+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-F217859B8182 · An Integrative Conceptual Model of Vietnam as an Emerging Destination for Offshore Outsourcing of Software Development f

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-3C3A81B007BB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000049 | non-empty Signal ID | SIG-000049 | Signal ID='SIG-000049' |
| primary_id_pattern | N/A | SIG-000049 | no pattern for dataset | SIG-000049 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000049 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000049 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-3C3A81B007BB; mission=MIS-20260711 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-3C3A81B007BB; mission=MIS-20260711-A8B8B6; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2010-01-01 | not enforced by integrity_guard | 2010-01-01 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000049 | primary id present | SIG-000049 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000049', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000049 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000049 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000049`

## CAND-C781226E4FF8 · Introducing the Company-State

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-1812CCB384B2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000048 | non-empty Signal ID | SIG-000048 | Signal ID='SIG-000048' |
| primary_id_pattern | N/A | SIG-000048 | no pattern for dataset | SIG-000048 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000048 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000048 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-1812CCB384B2; mission=MIS-20260711 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-1812CCB384B2; mission=MIS-20260711-A8B8B6; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020 | not enforced by integrity_guard | 2020 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000048 | primary id present | SIG-000048 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000048', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000048 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000048 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000048`

## CAND-8FC4C3383B9A · Introducing the Company-State

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-1502C0214AB9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000046 | non-empty Signal ID | SIG-000046 | Signal ID='SIG-000046' |
| primary_id_pattern | N/A | SIG-000046 | no pattern for dataset | SIG-000046 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000046 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000046 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-1502C0214AB9; mission=MIS-20260711 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-1502C0214AB9; mission=MIS-20260711-A8B8B6; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020 | not enforced by integrity_guard | 2020 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000046 | primary id present | SIG-000046 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000046', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000046 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000046 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000046`

## CAND-9ADA504ABA88 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000045 | non-empty Signal ID | SIG-000045 | Signal ID='SIG-000045' |
| primary_id_pattern | N/A | SIG-000045 | no pattern for dataset | SIG-000045 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000045 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000045 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260711-A | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260711-A8B8B6; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000045 | primary id present | SIG-000045 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000045', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000045 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000045 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000045`

## CAND-F02A999980DE · Analysis of Trends and Challenges in the Indonesian Labor Market

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-0E9CB131E8BA`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000047 | non-empty Signal ID | SIG-000047 | Signal ID='SIG-000047' |
| primary_id_pattern | N/A | SIG-000047 | no pattern for dataset | SIG-000047 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000047 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000047 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-0E9CB131E8BA; mission=MIS-20260711 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-0E9CB131E8BA; mission=MIS-20260711-A8B8B6; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2016-03-31 | not enforced by integrity_guard | 2016-03-31 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000047 | primary id present | SIG-000047 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000047', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000047 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000047 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000047`
