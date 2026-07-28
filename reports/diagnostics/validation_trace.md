# Validation Trace

**Generated:** 2026-07-28T08:54:08+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-16C79C3441C4 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000986 | non-empty Signal ID | SIG-000986 | Signal ID='SIG-000986' |
| primary_id_pattern | N/A | SIG-000986 | no pattern for dataset | SIG-000986 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000986 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000986 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260728-8 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260728-8E842D; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000986 | primary id present | SIG-000986 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000986', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000986 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000986 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000986`

## CAND-D9513A2DF8F1 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000989 | non-empty Signal ID | SIG-000989 | Signal ID='SIG-000989' |
| primary_id_pattern | N/A | SIG-000989 | no pattern for dataset | SIG-000989 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000989 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000989 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260728 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260728-8E842D; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000989 | primary id present | SIG-000989 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000989', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000989 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000989 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000989`

## CAND-3C186A705BA5 · Exploring the influence of regional economic pillars on library service equity in Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-A0E1922823F9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000985 | non-empty Signal ID | SIG-000985 | Signal ID='SIG-000985' |
| primary_id_pattern | N/A | SIG-000985 | no pattern for dataset | SIG-000985 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000985 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000985 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260728 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-A0E1922823F9; mission=MIS-20260728-8E842D; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000985 | primary id present | SIG-000985 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000985', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000985 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000985 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000985`

## CAND-0A934A15B204 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000987 | non-empty Signal ID | SIG-000987 | Signal ID='SIG-000987' |
| primary_id_pattern | N/A | SIG-000987 | no pattern for dataset | SIG-000987 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000987 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000987 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260728 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260728-8E842D; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000987 | primary id present | SIG-000987 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000987', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000987 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000987 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000987`

## CAND-1FCBC54D3AB4 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000988 | non-empty Signal ID | SIG-000988 | Signal ID='SIG-000988' |
| primary_id_pattern | N/A | SIG-000988 | no pattern for dataset | SIG-000988 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000988 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000988 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260728-8 | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260728-8E842D; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000988 | primary id present | SIG-000988 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000988', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000988 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000988 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000988`
