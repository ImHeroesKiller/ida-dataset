# Validation Trace

**Generated:** 2026-08-08T13:09:25+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-B9312C706295 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001617 | non-empty Signal ID | SIG-001617 | Signal ID='SIG-001617' |
| primary_id_pattern | N/A | SIG-001617 | no pattern for dataset | SIG-001617 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001617 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001617 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260808 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260808-C0CF57; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001617 | primary id present | SIG-001617 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001617', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-001617 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001617 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001617`

## CAND-A746275E5DDD · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001618 | non-empty Signal ID | SIG-001618 | Signal ID='SIG-001618' |
| primary_id_pattern | N/A | SIG-001618 | no pattern for dataset | SIG-001618 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001618 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001618 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260808 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260808-C0CF57; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001618 | primary id present | SIG-001618 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001618', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001618 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001618 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001618`

## CAND-CE0F2F664786 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001616 | non-empty Signal ID | SIG-001616 | Signal ID='SIG-001616' |
| primary_id_pattern | N/A | SIG-001616 | no pattern for dataset | SIG-001616 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001616 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001616 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260808-C | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260808-C0CF57; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001616 | primary id present | SIG-001616 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001616', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001616 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001616 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001616`

## CAND-62BCE049BFEC · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001615 | non-empty Signal ID | SIG-001615 | Signal ID='SIG-001615' |
| primary_id_pattern | N/A | SIG-001615 | no pattern for dataset | SIG-001615 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001615 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001615 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260808 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260808-C0CF57; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001615 | primary id present | SIG-001615 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001615', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001615 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001615 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001615`

## CAND-9F52E6140531 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001619 | non-empty Signal ID | SIG-001619 | Signal ID='SIG-001619' |
| primary_id_pattern | N/A | SIG-001619 | no pattern for dataset | SIG-001619 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001619 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001619 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260808-C | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260808-C0CF57; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001619 | primary id present | SIG-001619 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001619', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001619 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001619 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001619`
