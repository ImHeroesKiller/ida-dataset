# Validation Trace

**Generated:** 2026-07-31T23:21:55+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-0A7542E276F1 · MEWUJUDKAN GOOD GOVERNANCE MELALUI PELAYANAN PUBLIK

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-362992E54B77`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001183 | non-empty Signal ID | SIG-001183 | Signal ID='SIG-001183' |
| primary_id_pattern | N/A | SIG-001183 | no pattern for dataset | SIG-001183 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001183 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001183 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-362992E54B77; mission=MIS-20260731 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-362992E54B77; mission=MIS-20260731-084456; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2021-04-05 | not enforced by integrity_guard | 2021-04-05 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001183 | primary id present | SIG-001183 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001183', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-001183 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001183 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001183`

## CAND-DE80ABA82006 · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001180 | non-empty Signal ID | SIG-001180 | Signal ID='SIG-001180' |
| primary_id_pattern | N/A | SIG-001180 | no pattern for dataset | SIG-001180 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001180 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001180 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260731 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260731-084456; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001180 | primary id present | SIG-001180 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001180', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001180 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001180 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001180`

## CAND-955A2387C8EF · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001182 | non-empty Signal ID | SIG-001182 | Signal ID='SIG-001182' |
| primary_id_pattern | N/A | SIG-001182 | no pattern for dataset | SIG-001182 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001182 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001182 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260731 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260731-084456; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001182 | primary id present | SIG-001182 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001182', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001182 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001182 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001182`

## CAND-71793D1412F9 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001184 | non-empty Signal ID | SIG-001184 | Signal ID='SIG-001184' |
| primary_id_pattern | N/A | SIG-001184 | no pattern for dataset | SIG-001184 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001184 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001184 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260731 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260731-084456; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001184 | primary id present | SIG-001184 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001184', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001184 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001184 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001184`

## CAND-06004B549E29 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001181 | non-empty Signal ID | SIG-001181 | Signal ID='SIG-001181' |
| primary_id_pattern | N/A | SIG-001181 | no pattern for dataset | SIG-001181 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001181 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001181 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260731 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260731-084456; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001181 | primary id present | SIG-001181 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001181', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-001181 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001181 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001181`
