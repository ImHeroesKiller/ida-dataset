# Validation Trace

**Generated:** 2026-07-22T07:53:32+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-0D9BC5BA4A17 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000667 | non-empty Signal ID | SIG-000667 | Signal ID='SIG-000667' |
| primary_id_pattern | N/A | SIG-000667 | no pattern for dataset | SIG-000667 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000667 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000667 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260722 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260722-B41A9F; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000667 | primary id present | SIG-000667 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000667', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000667 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000667 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000667`

## CAND-1704E2993E48 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000666 | non-empty Signal ID | SIG-000666 | Signal ID='SIG-000666' |
| primary_id_pattern | N/A | SIG-000666 | no pattern for dataset | SIG-000666 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000666 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000666 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260722-B | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260722-B41A9F; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000666 | primary id present | SIG-000666 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000666', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000666 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000666 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000666`

## CAND-A47DAF18B917 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000668 | non-empty Signal ID | SIG-000668 | Signal ID='SIG-000668' |
| primary_id_pattern | N/A | SIG-000668 | no pattern for dataset | SIG-000668 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000668 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000668 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260722 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260722-B41A9F; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000668 | primary id present | SIG-000668 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000668', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000668 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000668 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000668`

## CAND-24EB6CFB982D · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000669 | non-empty Signal ID | SIG-000669 | Signal ID='SIG-000669' |
| primary_id_pattern | N/A | SIG-000669 | no pattern for dataset | SIG-000669 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000669 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000669 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260722-B | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260722-B41A9F; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000669 | primary id present | SIG-000669 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000669', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000669 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000669 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000669`

## CAND-F6B93D60A3A9 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000665 | non-empty Signal ID | SIG-000665 | Signal ID='SIG-000665' |
| primary_id_pattern | N/A | SIG-000665 | no pattern for dataset | SIG-000665 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000665 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000665 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260722 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260722-B41A9F; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000665 | primary id present | SIG-000665 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000665', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000665 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000665 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000665`
