# Validation Trace

**Generated:** 2026-07-11T10:24:16+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-C591A3211145 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000035 | non-empty Signal ID | SIG-000035 | Signal ID='SIG-000035' |
| primary_id_pattern | N/A | SIG-000035 | no pattern for dataset | SIG-000035 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000035 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000035 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260711 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260711-2A6107; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000035 | primary id present | SIG-000035 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000035', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000035 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000035 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000035`

## CAND-E1A9E882A02E · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-C59E093AE6F0`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000039 | non-empty Signal ID | SIG-000039 | Signal ID='SIG-000039' |
| primary_id_pattern | N/A | SIG-000039 | no pattern for dataset | SIG-000039 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000039 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000039 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-C59E093AE6F0; mission=MIS-20260711-2 | optional | present | provenance: source=SRC-000004; document=DOC-C59E093AE6F0; mission=MIS-20260711-2A6107; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000039 | primary id present | SIG-000039 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000039', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000039 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000039 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000039`

## CAND-821C4A7AAAEB · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000038 | non-empty Signal ID | SIG-000038 | Signal ID='SIG-000038' |
| primary_id_pattern | N/A | SIG-000038 | no pattern for dataset | SIG-000038 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000038 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000038 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260711 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260711-2A6107; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000038 | primary id present | SIG-000038 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000038', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000038 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000038 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000038`

## CAND-825DCF302C31 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000036 | non-empty Signal ID | SIG-000036 | Signal ID='SIG-000036' |
| primary_id_pattern | N/A | SIG-000036 | no pattern for dataset | SIG-000036 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000036 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000036 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260711-2 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260711-2A6107; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000036 | primary id present | SIG-000036 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000036', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000036 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000036 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000036`

## CAND-33AB2719B8BC · The biodiversity and ecosystem service contributions and trade-offs of forest restoration approaches

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-C8336B1CF486`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000037 | non-empty Signal ID | SIG-000037 | Signal ID='SIG-000037' |
| primary_id_pattern | N/A | SIG-000037 | no pattern for dataset | SIG-000037 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000037 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000037 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260711 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260711-2A6107; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2022-03-17 | not enforced by integrity_guard | 2022-03-17 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000037 | primary id present | SIG-000037 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000037', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000037 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000037 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000037`
