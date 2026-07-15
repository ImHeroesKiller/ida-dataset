# Validation Trace

**Generated:** 2026-07-15T08:38:40+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-C910394F4891 · The biodiversity and ecosystem service contributions and trade-offs of forest restoration approaches

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-C8336B1CF486`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000246 | non-empty Signal ID | SIG-000246 | Signal ID='SIG-000246' |
| primary_id_pattern | N/A | SIG-000246 | no pattern for dataset | SIG-000246 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000246 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000246 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260715 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260715-56572E; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2022-03-17 | not enforced by integrity_guard | 2022-03-17 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000246 | primary id present | SIG-000246 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000246', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000246 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000246 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000246`

## CAND-61DAF7743C34 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000245 | non-empty Signal ID | SIG-000245 | Signal ID='SIG-000245' |
| primary_id_pattern | N/A | SIG-000245 | no pattern for dataset | SIG-000245 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000245 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000245 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260715 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260715-56572E; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000245 | primary id present | SIG-000245 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000245', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000245 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000245 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000245`

## CAND-CC090052C882 · Corporate Governance In Middle East Family Businesses

dataset=`business_signal_library` · confidence=`0.85` · threshold=`0.8` · document=`DOC-27A2235900BA`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000248 | non-empty Signal ID | SIG-000248 | Signal ID='SIG-000248' |
| primary_id_pattern | N/A | SIG-000248 | no pattern for dataset | SIG-000248 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000248 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000248 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000001; document=DOC-27A2235900BA; mission=MIS-20260715-5 | optional | present | provenance: source=SRC-000001; document=DOC-27A2235900BA; mission=MIS-20260715-56572E; discovery_provider=DISC-TAVILY; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000248 | primary id present | SIG-000248 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000248', 'confidence': 0.85} | validate_row ok | duplicate_id:SIG-000248 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000248 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000248`

## CAND-A14DAF94C302 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000249 | non-empty Signal ID | SIG-000249 | Signal ID='SIG-000249' |
| primary_id_pattern | N/A | SIG-000249 | no pattern for dataset | SIG-000249 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000249 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000249 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260715 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260715-56572E; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000249 | primary id present | SIG-000249 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000249', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000249 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000249 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000249`

## CAND-41373EEF499D · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000247 | non-empty Signal ID | SIG-000247 | Signal ID='SIG-000247' |
| primary_id_pattern | N/A | SIG-000247 | no pattern for dataset | SIG-000247 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000247 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000247 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260715-5 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260715-56572E; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000247 | primary id present | SIG-000247 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000247', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000247 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000247 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000247`
