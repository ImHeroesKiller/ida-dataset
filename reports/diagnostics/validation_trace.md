# Validation Trace

**Generated:** 2026-07-14T22:20:20+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-6A86A762D174 · Their Potential Role in Corporate Governance

dataset=`business_signal_library` · confidence=`0.85` · threshold=`0.8` · document=`DOC-2B7A69D877EE`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000228 | non-empty Signal ID | SIG-000228 | Signal ID='SIG-000228' |
| primary_id_pattern | N/A | SIG-000228 | no pattern for dataset | SIG-000228 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000228 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000228 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000006; document=DOC-2B7A69D877EE; mission=MIS-20260714-D | optional | present | provenance: source=SRC-000006; document=DOC-2B7A69D877EE; mission=MIS-20260714-D70900; discovery_provider=DISC-TAVILY; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000228 | primary id present | SIG-000228 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000228', 'confidence': 0.85} | validate_row ok | duplicate_id:SIG-000228 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000228 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000228`

## CAND-2B893D76402E · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000229 | non-empty Signal ID | SIG-000229 | Signal ID='SIG-000229' |
| primary_id_pattern | N/A | SIG-000229 | no pattern for dataset | SIG-000229 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000229 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000229 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260714 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260714-D70900; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000229 | primary id present | SIG-000229 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000229', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000229 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000229 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000229`

## CAND-9F2FD6E9E5D6 · Corporate Governance Improving Corporate Governance in India- Related ...

dataset=`business_signal_library` · confidence=`0.85` · threshold=`0.8` · document=`DOC-DA23EFA062CA`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000225 | non-empty Signal ID | SIG-000225 | Signal ID='SIG-000225' |
| primary_id_pattern | N/A | SIG-000225 | no pattern for dataset | SIG-000225 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000225 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000225 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-DA23EFA062CA; mission=MIS-20260714-D | optional | present | provenance: source=SRC-000004; document=DOC-DA23EFA062CA; mission=MIS-20260714-D70900; discovery_provider=DISC-TAVILY; append_only=true; ext |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000225 | primary id present | SIG-000225 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000225', 'confidence': 0.85} | validate_row ok | duplicate_id:SIG-000225 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000225 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000225`

## CAND-574B2781AD02 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000227 | non-empty Signal ID | SIG-000227 | Signal ID='SIG-000227' |
| primary_id_pattern | N/A | SIG-000227 | no pattern for dataset | SIG-000227 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000227 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000227 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260714-D | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260714-D70900; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000227 | primary id present | SIG-000227 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000227', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000227 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000227 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000227`

## CAND-213C11B13B85 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000226 | non-empty Signal ID | SIG-000226 | Signal ID='SIG-000226' |
| primary_id_pattern | N/A | SIG-000226 | no pattern for dataset | SIG-000226 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000226 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000226 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260714 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260714-D70900; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000226 | primary id present | SIG-000226 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000226', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000226 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000226 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000226`
