# Validation Trace

**Generated:** 2026-08-09T10:54:41+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-142B9F6713E6 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001712 | non-empty Signal ID | SIG-001712 | Signal ID='SIG-001712' |
| primary_id_pattern | N/A | SIG-001712 | no pattern for dataset | SIG-001712 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001712 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001712 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260809 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260809-ADD3E7; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001712 | primary id present | SIG-001712 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001712', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-001712 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001712 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001712`

## CAND-EEAD220E230C · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001714 | non-empty Signal ID | SIG-001714 | Signal ID='SIG-001714' |
| primary_id_pattern | N/A | SIG-001714 | no pattern for dataset | SIG-001714 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001714 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001714 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260809-A | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260809-ADD3E7; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001714 | primary id present | SIG-001714 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001714', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001714 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001714 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001714`

## CAND-64DAB0DAF43C · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001711 | non-empty Signal ID | SIG-001711 | Signal ID='SIG-001711' |
| primary_id_pattern | N/A | SIG-001711 | no pattern for dataset | SIG-001711 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001711 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001711 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260809-A | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260809-ADD3E7; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001711 | primary id present | SIG-001711 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001711', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-001711 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001711 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001711`

## CAND-6A36195C4C20 · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001710 | non-empty Signal ID | SIG-001710 | Signal ID='SIG-001710' |
| primary_id_pattern | N/A | SIG-001710 | no pattern for dataset | SIG-001710 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001710 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001710 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260809 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260809-ADD3E7; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001710 | primary id present | SIG-001710 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001710', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001710 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001710 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001710`

## CAND-4EC22A8B5198 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-001713 | non-empty Signal ID | SIG-001713 | Signal ID='SIG-001713' |
| primary_id_pattern | N/A | SIG-001713 | no pattern for dataset | SIG-001713 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-001713 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-001713 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260809 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260809-ADD3E7; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-001713 | primary id present | SIG-001713 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-001713', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-001713 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-001713 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-001713`
