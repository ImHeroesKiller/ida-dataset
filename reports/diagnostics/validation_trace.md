# Validation Trace

**Generated:** 2026-07-19T14:05:58+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-A476E3F9EE84 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000505 | non-empty Signal ID | SIG-000505 | Signal ID='SIG-000505' |
| primary_id_pattern | N/A | SIG-000505 | no pattern for dataset | SIG-000505 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000505 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000505 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260719 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260719-6A8A74; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000505 | primary id present | SIG-000505 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000505', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000505 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000505 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000505`

## CAND-AF16021D6EDA · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000506 | non-empty Signal ID | SIG-000506 | Signal ID='SIG-000506' |
| primary_id_pattern | N/A | SIG-000506 | no pattern for dataset | SIG-000506 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000506 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000506 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260719-6 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260719-6A8A74; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000506 | primary id present | SIG-000506 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000506', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000506 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000506 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000506`

## CAND-F83063C02249 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000508 | non-empty Signal ID | SIG-000508 | Signal ID='SIG-000508' |
| primary_id_pattern | N/A | SIG-000508 | no pattern for dataset | SIG-000508 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000508 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000508 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260719 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260719-6A8A74; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000508 | primary id present | SIG-000508 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000508', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000508 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000508 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000508`

## CAND-953F121DE47F · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-C59E093AE6F0`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000509 | non-empty Signal ID | SIG-000509 | Signal ID='SIG-000509' |
| primary_id_pattern | N/A | SIG-000509 | no pattern for dataset | SIG-000509 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000509 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000509 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-C59E093AE6F0; mission=MIS-20260719-6 | optional | present | provenance: source=SRC-000004; document=DOC-C59E093AE6F0; mission=MIS-20260719-6A8A74; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000509 | primary id present | SIG-000509 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000509', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000509 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000509 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000509`

## CAND-2BD17A0F64E3 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000507 | non-empty Signal ID | SIG-000507 | Signal ID='SIG-000507' |
| primary_id_pattern | N/A | SIG-000507 | no pattern for dataset | SIG-000507 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000507 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000507 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260719 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260719-6A8A74; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000507 | primary id present | SIG-000507 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000507', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000507 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000507 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000507`
