# Validation Trace

**Generated:** 2026-07-17T17:34:11+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-EDC748B87239 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000387 | non-empty Signal ID | SIG-000387 | Signal ID='SIG-000387' |
| primary_id_pattern | N/A | SIG-000387 | no pattern for dataset | SIG-000387 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000387 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000387 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260717 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260717-86B4AE; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000387 | primary id present | SIG-000387 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000387', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000387 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000387 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000387`

## CAND-9A012B9E46C4 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000385 | non-empty Signal ID | SIG-000385 | Signal ID='SIG-000385' |
| primary_id_pattern | N/A | SIG-000385 | no pattern for dataset | SIG-000385 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000385 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000385 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260717 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260717-86B4AE; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000385 | primary id present | SIG-000385 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000385', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000385 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000385 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000385`

## CAND-2DEB20E9B147 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000386 | non-empty Signal ID | SIG-000386 | Signal ID='SIG-000386' |
| primary_id_pattern | N/A | SIG-000386 | no pattern for dataset | SIG-000386 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000386 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000386 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260717-8 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260717-86B4AE; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000386 | primary id present | SIG-000386 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000386', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000386 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000386 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000386`

## CAND-4ADF466CED68 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D733F4309CB6`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000389 | non-empty Signal ID | SIG-000389 | Signal ID='SIG-000389' |
| primary_id_pattern | N/A | SIG-000389 | no pattern for dataset | SIG-000389 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000389 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000389 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D733F4309CB6; mission=MIS-20260717-8 | optional | present | provenance: source=SRC-000004; document=DOC-D733F4309CB6; mission=MIS-20260717-86B4AE; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000389 | primary id present | SIG-000389 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000389', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000389 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000389 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000389`

## CAND-5F1E3DC05B02 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000388 | non-empty Signal ID | SIG-000388 | Signal ID='SIG-000388' |
| primary_id_pattern | N/A | SIG-000388 | no pattern for dataset | SIG-000388 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000388 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000388 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260717 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260717-86B4AE; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000388 | primary id present | SIG-000388 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000388', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000388 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000388 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000388`
