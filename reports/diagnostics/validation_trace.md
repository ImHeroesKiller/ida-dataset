# Validation Trace

**Generated:** 2026-07-17T00:27:59+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-47412DE29FD3 · The biodiversity and ecosystem service contributions and trade-offs of forest restoration approaches

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-C8336B1CF486`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000346 | non-empty Signal ID | SIG-000346 | Signal ID='SIG-000346' |
| primary_id_pattern | N/A | SIG-000346 | no pattern for dataset | SIG-000346 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000346 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000346 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260717 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260717-F493F6; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2022-03-17 | not enforced by integrity_guard | 2022-03-17 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000346 | primary id present | SIG-000346 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000346', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000346 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000346 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000346`

## CAND-BCAF37C2A947 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000347 | non-empty Signal ID | SIG-000347 | Signal ID='SIG-000347' |
| primary_id_pattern | N/A | SIG-000347 | no pattern for dataset | SIG-000347 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000347 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000347 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260717-F | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260717-F493F6; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000347 | primary id present | SIG-000347 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000347', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000347 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000347 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000347`

## CAND-88C287BA2ED0 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000345 | non-empty Signal ID | SIG-000345 | Signal ID='SIG-000345' |
| primary_id_pattern | N/A | SIG-000345 | no pattern for dataset | SIG-000345 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000345 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000345 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260717 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260717-F493F6; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000345 | primary id present | SIG-000345 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000345', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000345 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000345 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000345`

## CAND-EB3B100437CC · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000348 | non-empty Signal ID | SIG-000348 | Signal ID='SIG-000348' |
| primary_id_pattern | N/A | SIG-000348 | no pattern for dataset | SIG-000348 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000348 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000348 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260717 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260717-F493F6; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000348 | primary id present | SIG-000348 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000348', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000348 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000348 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000348`

## CAND-B5358284CBE7 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000349 | non-empty Signal ID | SIG-000349 | Signal ID='SIG-000349' |
| primary_id_pattern | N/A | SIG-000349 | no pattern for dataset | SIG-000349 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000349 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000349 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260717 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260717-F493F6; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000349 | primary id present | SIG-000349 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000349', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000349 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000349 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000349`
