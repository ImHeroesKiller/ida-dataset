# Validation Trace

**Generated:** 2026-08-07T06:00:03+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-3BEFA05AFD89 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001488 | non-empty Signal ID | SIG-001488 | Signal ID='SIG-001488' |
| primary_id_pattern | N/A | SIG-001488 | no pattern for dataset | SIG-001488 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001488 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001488 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260807 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260807-8E681C; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001488 | primary id present | SIG-001488 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001488', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001488 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001488 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001488`

## CAND-BA250567348B · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001486 | non-empty Signal ID | SIG-001486 | Signal ID='SIG-001486' |
| primary_id_pattern | N/A | SIG-001486 | no pattern for dataset | SIG-001486 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001486 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001486 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260807-8 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260807-8E681C; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001486 | primary id present | SIG-001486 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001486', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001486 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001486 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001486`

## CAND-A1BB6AD11B32 · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001485 | non-empty Signal ID | SIG-001485 | Signal ID='SIG-001485' |
| primary_id_pattern | N/A | SIG-001485 | no pattern for dataset | SIG-001485 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001485 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001485 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260807 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260807-8E681C; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001485 | primary id present | SIG-001485 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001485', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001485 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001485 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001485`

## CAND-099D9DF66EDC · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001487 | non-empty Signal ID | SIG-001487 | Signal ID='SIG-001487' |
| primary_id_pattern | N/A | SIG-001487 | no pattern for dataset | SIG-001487 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001487 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001487 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260807 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260807-8E681C; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001487 | primary id present | SIG-001487 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001487', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-001487 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001487 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001487`

## CAND-47AD6A9B5F03 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-C59E093AE6F0`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001489 | non-empty Signal ID | SIG-001489 | Signal ID='SIG-001489' |
| primary_id_pattern | N/A | SIG-001489 | no pattern for dataset | SIG-001489 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001489 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001489 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-C59E093AE6F0; mission=MIS-20260807-8 | optional | present | provenance: source=SRC-000004; document=DOC-C59E093AE6F0; mission=MIS-20260807-8E681C; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001489 | primary id present | SIG-001489 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001489', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001489 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001489 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001489`
