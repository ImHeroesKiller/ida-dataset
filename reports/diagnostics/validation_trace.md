# Validation Trace

**Generated:** 2026-07-15T20:34:42+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-73669B722259 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000277 | non-empty Signal ID | SIG-000277 | Signal ID='SIG-000277' |
| primary_id_pattern | N/A | SIG-000277 | no pattern for dataset | SIG-000277 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000277 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000277 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260715 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260715-53057A; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000277 | primary id present | SIG-000277 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000277', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000277 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000277 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000277`

## CAND-D70296C73563 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000276 | non-empty Signal ID | SIG-000276 | Signal ID='SIG-000276' |
| primary_id_pattern | N/A | SIG-000276 | no pattern for dataset | SIG-000276 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000276 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000276 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260715-5 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260715-53057A; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000276 | primary id present | SIG-000276 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000276', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000276 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000276 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000276`

## CAND-8B5C4E38E467 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000279 | non-empty Signal ID | SIG-000279 | Signal ID='SIG-000279' |
| primary_id_pattern | N/A | SIG-000279 | no pattern for dataset | SIG-000279 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000279 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000279 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260715 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260715-53057A; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000279 | primary id present | SIG-000279 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000279', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000279 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000279 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000279`

## CAND-8F934284A5BD · Corporate Governance In Middle East Family Businesses

dataset=`business_signal_library` · confidence=`0.85` · threshold=`0.8` · document=`DOC-E689A7156EBC`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000278 | non-empty Signal ID | SIG-000278 | Signal ID='SIG-000278' |
| primary_id_pattern | N/A | SIG-000278 | no pattern for dataset | SIG-000278 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000278 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000278 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000001; document=DOC-E689A7156EBC; mission=MIS-20260715-5 | optional | present | provenance: source=SRC-000001; document=DOC-E689A7156EBC; mission=MIS-20260715-53057A; discovery_provider=DISC-TAVILY; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000278 | primary id present | SIG-000278 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000278', 'confidence': 0.85} | validate_row ok | duplicate_id:SIG-000278 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000278 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000278`

## CAND-3840D11A0592 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000275 | non-empty Signal ID | SIG-000275 | Signal ID='SIG-000275' |
| primary_id_pattern | N/A | SIG-000275 | no pattern for dataset | SIG-000275 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000275 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000275 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260715 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260715-53057A; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000275 | primary id present | SIG-000275 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000275', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000275 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000275 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000275`
