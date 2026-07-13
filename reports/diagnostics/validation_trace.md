# Validation Trace

**Generated:** 2026-07-13T10:49:35+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-4760F5ECD2A7 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000157 | non-empty Signal ID | SIG-000157 | Signal ID='SIG-000157' |
| primary_id_pattern | N/A | SIG-000157 | no pattern for dataset | SIG-000157 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000157 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000157 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260713 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260713-C8594D; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000157 | primary id present | SIG-000157 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000157', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000157 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000157 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000157`

## CAND-51F8478D42C8 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000155 | non-empty Signal ID | SIG-000155 | Signal ID='SIG-000155' |
| primary_id_pattern | N/A | SIG-000155 | no pattern for dataset | SIG-000155 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000155 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000155 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260713 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260713-C8594D; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000155 | primary id present | SIG-000155 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000155', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000155 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000155 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000155`

## CAND-EA06333A2083 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000158 | non-empty Signal ID | SIG-000158 | Signal ID='SIG-000158' |
| primary_id_pattern | N/A | SIG-000158 | no pattern for dataset | SIG-000158 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000158 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000158 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260713 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260713-C8594D; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000158 | primary id present | SIG-000158 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000158', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000158 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000158 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000158`

## CAND-3862E05B462B · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D733F4309CB6`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000159 | non-empty Signal ID | SIG-000159 | Signal ID='SIG-000159' |
| primary_id_pattern | N/A | SIG-000159 | no pattern for dataset | SIG-000159 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000159 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000159 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D733F4309CB6; mission=MIS-20260713-C | optional | present | provenance: source=SRC-000004; document=DOC-D733F4309CB6; mission=MIS-20260713-C8594D; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000159 | primary id present | SIG-000159 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000159', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000159 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000159 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000159`

## CAND-97C42C3C1DBD · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000156 | non-empty Signal ID | SIG-000156 | Signal ID='SIG-000156' |
| primary_id_pattern | N/A | SIG-000156 | no pattern for dataset | SIG-000156 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000156 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000156 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260713-C | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260713-C8594D; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000156 | primary id present | SIG-000156 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000156', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000156 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000156 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000156`
