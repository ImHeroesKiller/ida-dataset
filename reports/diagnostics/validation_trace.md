# Validation Trace

**Generated:** 2026-07-19T00:13:16+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-2F0DD0970F41 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000477 | non-empty Signal ID | SIG-000477 | Signal ID='SIG-000477' |
| primary_id_pattern | N/A | SIG-000477 | no pattern for dataset | SIG-000477 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000477 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000477 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260718-E | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260718-EEF05C; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000477 | primary id present | SIG-000477 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000477', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000477 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000477 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000477`

## CAND-4DBE3AE87C34 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000476 | non-empty Signal ID | SIG-000476 | Signal ID='SIG-000476' |
| primary_id_pattern | N/A | SIG-000476 | no pattern for dataset | SIG-000476 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000476 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000476 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260718 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260718-EEF05C; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000476 | primary id present | SIG-000476 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000476', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000476 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000476 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000476`

## CAND-B3243225A342 · MEWUJUDKAN GOOD GOVERNANCE MELALUI PELAYANAN PUBLIK

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-362992E54B77`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000479 | non-empty Signal ID | SIG-000479 | Signal ID='SIG-000479' |
| primary_id_pattern | N/A | SIG-000479 | no pattern for dataset | SIG-000479 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000479 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000479 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-362992E54B77; mission=MIS-20260718 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-362992E54B77; mission=MIS-20260718-EEF05C; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2021-04-05 | not enforced by integrity_guard | 2021-04-05 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000479 | primary id present | SIG-000479 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000479', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000479 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000479 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000479`

## CAND-40085C84C1E7 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000478 | non-empty Signal ID | SIG-000478 | Signal ID='SIG-000478' |
| primary_id_pattern | N/A | SIG-000478 | no pattern for dataset | SIG-000478 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000478 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000478 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260718 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260718-EEF05C; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000478 | primary id present | SIG-000478 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000478', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000478 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000478 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000478`

## CAND-193C5E63B0F0 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000475 | non-empty Signal ID | SIG-000475 | Signal ID='SIG-000475' |
| primary_id_pattern | N/A | SIG-000475 | no pattern for dataset | SIG-000475 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000475 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000475 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260718 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260718-EEF05C; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000475 | primary id present | SIG-000475 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000475', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000475 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000475 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000475`
