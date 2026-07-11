# Validation Trace

**Generated:** 2026-07-11T11:49:33+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-6311DFB6B180 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000043 | non-empty Signal ID | SIG-000043 | Signal ID='SIG-000043' |
| primary_id_pattern | N/A | SIG-000043 | no pattern for dataset | SIG-000043 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000043 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000043 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260711 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260711-9A55F5; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000043 | primary id present | SIG-000043 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000043', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000043 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000043 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000043`

## CAND-B8DEAB4C7490 · The biodiversity and ecosystem service contributions and trade-offs of forest restoration approaches

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-C8336B1CF486`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000042 | non-empty Signal ID | SIG-000042 | Signal ID='SIG-000042' |
| primary_id_pattern | N/A | SIG-000042 | no pattern for dataset | SIG-000042 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000042 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000042 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260711 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260711-9A55F5; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2022-03-17 | not enforced by integrity_guard | 2022-03-17 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000042 | primary id present | SIG-000042 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000042', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000042 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000042 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000042`

## CAND-BADF000AB75B · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000040 | non-empty Signal ID | SIG-000040 | Signal ID='SIG-000040' |
| primary_id_pattern | N/A | SIG-000040 | no pattern for dataset | SIG-000040 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000040 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000040 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260711 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260711-9A55F5; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000040 | primary id present | SIG-000040 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000040', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000040 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000040 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000040`

## CAND-5B59CD29ABBA · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-2430A598BF3B`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000044 | non-empty Signal ID | SIG-000044 | Signal ID='SIG-000044' |
| primary_id_pattern | N/A | SIG-000044 | no pattern for dataset | SIG-000044 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000044 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000044 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260711-9 | optional | present | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260711-9A55F5; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000044 | primary id present | SIG-000044 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000044', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000044 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000044 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000044`

## CAND-B76D41661BD0 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000041 | non-empty Signal ID | SIG-000041 | Signal ID='SIG-000041' |
| primary_id_pattern | N/A | SIG-000041 | no pattern for dataset | SIG-000041 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000041 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000041 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260711-9 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260711-9A55F5; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000041 | primary id present | SIG-000041 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000041', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000041 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000041 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000041`
