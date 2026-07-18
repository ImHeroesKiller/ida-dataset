# Validation Trace

**Generated:** 2026-07-18T02:55:46+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-DB4D2A6237B1 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-2430A598BF3B`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000414 | non-empty Signal ID | SIG-000414 | Signal ID='SIG-000414' |
| primary_id_pattern | N/A | SIG-000414 | no pattern for dataset | SIG-000414 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000414 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000414 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260718-F | optional | present | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260718-F35FC1; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000414 | primary id present | SIG-000414 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000414', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000414 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000414 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000414`

## CAND-ABD3CF26FE51 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000411 | non-empty Signal ID | SIG-000411 | Signal ID='SIG-000411' |
| primary_id_pattern | N/A | SIG-000411 | no pattern for dataset | SIG-000411 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000411 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000411 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260718-F | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260718-F35FC1; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000411 | primary id present | SIG-000411 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000411', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000411 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000411 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000411`

## CAND-3BC014FA05DB · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000410 | non-empty Signal ID | SIG-000410 | Signal ID='SIG-000410' |
| primary_id_pattern | N/A | SIG-000410 | no pattern for dataset | SIG-000410 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000410 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000410 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260718 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260718-F35FC1; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000410 | primary id present | SIG-000410 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000410', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000410 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000410 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000410`

## CAND-62C6AD0BF6E5 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000413 | non-empty Signal ID | SIG-000413 | Signal ID='SIG-000413' |
| primary_id_pattern | N/A | SIG-000413 | no pattern for dataset | SIG-000413 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000413 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000413 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260718 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260718-F35FC1; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000413 | primary id present | SIG-000413 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000413', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000413 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000413 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000413`

## CAND-A30EA4659347 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000412 | non-empty Signal ID | SIG-000412 | Signal ID='SIG-000412' |
| primary_id_pattern | N/A | SIG-000412 | no pattern for dataset | SIG-000412 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000412 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000412 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260718 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260718-F35FC1; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000412 | primary id present | SIG-000412 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000412', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000412 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000412 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000412`
