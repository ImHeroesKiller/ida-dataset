# Validation Trace

**Generated:** 2026-07-18T16:21:39+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-D131CB4FFAB0 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000445 | non-empty Signal ID | SIG-000445 | Signal ID='SIG-000445' |
| primary_id_pattern | N/A | SIG-000445 | no pattern for dataset | SIG-000445 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000445 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000445 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260718 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260718-917199; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000445 | primary id present | SIG-000445 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000445', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000445 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000445 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000445`

## CAND-F7A5D2B8A3B1 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-3ED7FE5F0429`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000446 | non-empty Signal ID | SIG-000446 | Signal ID='SIG-000446' |
| primary_id_pattern | N/A | SIG-000446 | no pattern for dataset | SIG-000446 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000446 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000446 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-3ED7FE5F0429; mission=MIS-20260718-9 | optional | present | provenance: source=SRC-000004; document=DOC-3ED7FE5F0429; mission=MIS-20260718-917199; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000446 | primary id present | SIG-000446 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000446', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000446 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000446 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000446`

## CAND-0C71BF1FC76C · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-C59E093AE6F0`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000449 | non-empty Signal ID | SIG-000449 | Signal ID='SIG-000449' |
| primary_id_pattern | N/A | SIG-000449 | no pattern for dataset | SIG-000449 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000449 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000449 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-C59E093AE6F0; mission=MIS-20260718-9 | optional | present | provenance: source=SRC-000004; document=DOC-C59E093AE6F0; mission=MIS-20260718-917199; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000449 | primary id present | SIG-000449 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000449', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000449 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000449 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000449`

## CAND-3D8866CD9B0D · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000448 | non-empty Signal ID | SIG-000448 | Signal ID='SIG-000448' |
| primary_id_pattern | N/A | SIG-000448 | no pattern for dataset | SIG-000448 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000448 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000448 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260718 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260718-917199; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000448 | primary id present | SIG-000448 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000448', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000448 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000448 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000448`

## CAND-48CA4C5065BC · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000447 | non-empty Signal ID | SIG-000447 | Signal ID='SIG-000447' |
| primary_id_pattern | N/A | SIG-000447 | no pattern for dataset | SIG-000447 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000447 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000447 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260718 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260718-917199; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000447 | primary id present | SIG-000447 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000447', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000447 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000447 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000447`
