# Validation Trace

**Generated:** 2026-07-14T16:43:39+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-8D11029D5BE1 · The biodiversity and ecosystem service contributions and trade-offs of forest restoration approaches

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-C8336B1CF486`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000211 | non-empty Signal ID | SIG-000211 | Signal ID='SIG-000211' |
| primary_id_pattern | N/A | SIG-000211 | no pattern for dataset | SIG-000211 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000211 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000211 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260714 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260714-45D0A0; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2022-03-17 | not enforced by integrity_guard | 2022-03-17 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000211 | primary id present | SIG-000211 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000211', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000211 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000211 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000211`

## CAND-AAC0D0884237 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000214 | non-empty Signal ID | SIG-000214 | Signal ID='SIG-000214' |
| primary_id_pattern | N/A | SIG-000214 | no pattern for dataset | SIG-000214 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000214 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000214 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260714 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260714-45D0A0; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000214 | primary id present | SIG-000214 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000214', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000214 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000214 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000214`

## CAND-58D14B9F4237 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000212 | non-empty Signal ID | SIG-000212 | Signal ID='SIG-000212' |
| primary_id_pattern | N/A | SIG-000212 | no pattern for dataset | SIG-000212 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000212 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000212 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260714-4 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260714-45D0A0; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000212 | primary id present | SIG-000212 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000212', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000212 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000212 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000212`

## CAND-9642D6153AC2 · Corporate Governance of State-Owned Enterprises

dataset=`business_signal_library` · confidence=`0.85` · threshold=`0.8` · document=`DOC-F643783FC006`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000213 | non-empty Signal ID | SIG-000213 | Signal ID='SIG-000213' |
| primary_id_pattern | N/A | SIG-000213 | no pattern for dataset | SIG-000213 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000213 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000213 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-F643783FC006; mission=MIS-20260714-4 | optional | present | provenance: source=SRC-000004; document=DOC-F643783FC006; mission=MIS-20260714-45D0A0; discovery_provider=DISC-TAVILY; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000213 | primary id present | SIG-000213 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000213', 'confidence': 0.85} | validate_row ok | duplicate_id:SIG-000213 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000213 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000213`

## CAND-DB719B453546 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000210 | non-empty Signal ID | SIG-000210 | Signal ID='SIG-000210' |
| primary_id_pattern | N/A | SIG-000210 | no pattern for dataset | SIG-000210 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000210 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000210 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260714 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260714-45D0A0; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000210 | primary id present | SIG-000210 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000210', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000210 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000210 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000210`
