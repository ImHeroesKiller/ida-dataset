# Validation Trace

**Generated:** 2026-07-15T22:23:48+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-07B7C916E817 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000284 | non-empty Signal ID | SIG-000284 | Signal ID='SIG-000284' |
| primary_id_pattern | N/A | SIG-000284 | no pattern for dataset | SIG-000284 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000284 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000284 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260715 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260715-926818; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000284 | primary id present | SIG-000284 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000284', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000284 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000284 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000284`

## CAND-04C066C3BA7A · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000282 | non-empty Signal ID | SIG-000282 | Signal ID='SIG-000282' |
| primary_id_pattern | N/A | SIG-000282 | no pattern for dataset | SIG-000282 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000282 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000282 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260715 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260715-926818; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000282 | primary id present | SIG-000282 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000282', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000282 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000282 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000282`

## CAND-F13DFE2C40FF · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000281 | non-empty Signal ID | SIG-000281 | Signal ID='SIG-000281' |
| primary_id_pattern | N/A | SIG-000281 | no pattern for dataset | SIG-000281 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000281 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000281 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260715-9 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260715-926818; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000281 | primary id present | SIG-000281 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000281', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000281 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000281 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000281`

## CAND-878167D9920A · Corporate Governance In Middle East Family Businesses

dataset=`business_signal_library` · confidence=`0.85` · threshold=`0.8` · document=`DOC-27A2235900BA`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000283 | non-empty Signal ID | SIG-000283 | Signal ID='SIG-000283' |
| primary_id_pattern | N/A | SIG-000283 | no pattern for dataset | SIG-000283 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000283 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000283 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000001; document=DOC-27A2235900BA; mission=MIS-20260715-9 | optional | present | provenance: source=SRC-000001; document=DOC-27A2235900BA; mission=MIS-20260715-926818; discovery_provider=DISC-TAVILY; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000283 | primary id present | SIG-000283 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000283', 'confidence': 0.85} | validate_row ok | duplicate_id:SIG-000283 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000283 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000283`

## CAND-A77F3743BE74 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000280 | non-empty Signal ID | SIG-000280 | Signal ID='SIG-000280' |
| primary_id_pattern | N/A | SIG-000280 | no pattern for dataset | SIG-000280 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000280 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000280 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260715 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260715-926818; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000280 | primary id present | SIG-000280 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000280', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000280 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000280 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000280`
