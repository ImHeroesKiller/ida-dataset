# Validation Trace

**Generated:** 2026-07-15T16:46:49+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-5DD7F6DF2E0D · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000269 | non-empty Signal ID | SIG-000269 | Signal ID='SIG-000269' |
| primary_id_pattern | N/A | SIG-000269 | no pattern for dataset | SIG-000269 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000269 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000269 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260715 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260715-E8F03F; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000269 | primary id present | SIG-000269 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000269', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000269 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000269 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000269`

## CAND-21FE4F267D77 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000265 | non-empty Signal ID | SIG-000265 | Signal ID='SIG-000265' |
| primary_id_pattern | N/A | SIG-000265 | no pattern for dataset | SIG-000265 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000265 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000265 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260715 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260715-E8F03F; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000265 | primary id present | SIG-000265 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000265', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000265 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000265 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000265`

## CAND-48E88C855434 · The biodiversity and ecosystem service contributions and trade-offs of forest restoration approaches

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-C8336B1CF486`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000266 | non-empty Signal ID | SIG-000266 | Signal ID='SIG-000266' |
| primary_id_pattern | N/A | SIG-000266 | no pattern for dataset | SIG-000266 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000266 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000266 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260715 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260715-E8F03F; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2022-03-17 | not enforced by integrity_guard | 2022-03-17 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000266 | primary id present | SIG-000266 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000266', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000266 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000266 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000266`

## CAND-3701ED8B8DE9 · Corporate Governance In Middle East Family Businesses

dataset=`business_signal_library` · confidence=`0.85` · threshold=`0.8` · document=`DOC-E689A7156EBC`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000268 | non-empty Signal ID | SIG-000268 | Signal ID='SIG-000268' |
| primary_id_pattern | N/A | SIG-000268 | no pattern for dataset | SIG-000268 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000268 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000268 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000001; document=DOC-E689A7156EBC; mission=MIS-20260715-E | optional | present | provenance: source=SRC-000001; document=DOC-E689A7156EBC; mission=MIS-20260715-E8F03F; discovery_provider=DISC-TAVILY; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000268 | primary id present | SIG-000268 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000268', 'confidence': 0.85} | validate_row ok | duplicate_id:SIG-000268 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000268 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000268`

## CAND-889942AB4A28 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000267 | non-empty Signal ID | SIG-000267 | Signal ID='SIG-000267' |
| primary_id_pattern | N/A | SIG-000267 | no pattern for dataset | SIG-000267 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000267 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000267 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260715-E | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260715-E8F03F; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000267 | primary id present | SIG-000267 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000267', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000267 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000267 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000267`
