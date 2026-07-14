# Validation Trace

**Generated:** 2026-07-14T15:15:09+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-5683E4B5DD20 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000205 | non-empty Signal ID | SIG-000205 | Signal ID='SIG-000205' |
| primary_id_pattern | N/A | SIG-000205 | no pattern for dataset | SIG-000205 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000205 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000205 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260714 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260714-083117; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000205 | primary id present | SIG-000205 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000205', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000205 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000205 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000205`

## CAND-CB658F2E3CE1 · Library Service Quality and Student Trust A Case Study of the University of Sumatera Utara Library, Indonesia

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-05E7BC8EA754`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000209 | non-empty Signal ID | SIG-000209 | Signal ID='SIG-000209' |
| primary_id_pattern | N/A | SIG-000209 | no pattern for dataset | SIG-000209 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000209 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000209 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-05E7BC8EA754; mission=MIS-20260714 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-05E7BC8EA754; mission=MIS-20260714-083117; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2021 | not enforced by integrity_guard | 2021 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000209 | primary id present | SIG-000209 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000209', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000209 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000209 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000209`

## CAND-EDDAAF85E5FE · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000207 | non-empty Signal ID | SIG-000207 | Signal ID='SIG-000207' |
| primary_id_pattern | N/A | SIG-000207 | no pattern for dataset | SIG-000207 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000207 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000207 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260714 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260714-083117; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000207 | primary id present | SIG-000207 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000207', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000207 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000207 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000207`

## CAND-BA47A0E637CD · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D733F4309CB6`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000208 | non-empty Signal ID | SIG-000208 | Signal ID='SIG-000208' |
| primary_id_pattern | N/A | SIG-000208 | no pattern for dataset | SIG-000208 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000208 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000208 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D733F4309CB6; mission=MIS-20260714-0 | optional | present | provenance: source=SRC-000004; document=DOC-D733F4309CB6; mission=MIS-20260714-083117; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000208 | primary id present | SIG-000208 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000208', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000208 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000208 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000208`

## CAND-E0044C696D3F · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000206 | non-empty Signal ID | SIG-000206 | Signal ID='SIG-000206' |
| primary_id_pattern | N/A | SIG-000206 | no pattern for dataset | SIG-000206 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000206 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000206 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260714-0 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260714-083117; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000206 | primary id present | SIG-000206 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000206', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000206 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000206 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000206`
