# Validation Trace

**Generated:** 2026-07-13T07:16:09+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-AD44BECE8865 · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000146 | non-empty Signal ID | SIG-000146 | Signal ID='SIG-000146' |
| primary_id_pattern | N/A | SIG-000146 | no pattern for dataset | SIG-000146 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000146 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000146 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260713-4 | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260713-44F611; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000146 | primary id present | SIG-000146 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000146', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000146 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000146 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000146`

## CAND-C62A2DF0F626 · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000147 | non-empty Signal ID | SIG-000147 | Signal ID='SIG-000147' |
| primary_id_pattern | N/A | SIG-000147 | no pattern for dataset | SIG-000147 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000147 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000147 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260713 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260713-44F611; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000147 | primary id present | SIG-000147 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000147', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000147 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000147 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000147`

## CAND-C62BD33D6670 · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000145 | non-empty Signal ID | SIG-000145 | Signal ID='SIG-000145' |
| primary_id_pattern | N/A | SIG-000145 | no pattern for dataset | SIG-000145 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000145 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000145 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260713 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260713-44F611; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000145 | primary id present | SIG-000145 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000145', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000145 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000145 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000145`

## CAND-FDC7B3642121 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-2430A598BF3B`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000149 | non-empty Signal ID | SIG-000149 | Signal ID='SIG-000149' |
| primary_id_pattern | N/A | SIG-000149 | no pattern for dataset | SIG-000149 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000149 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000149 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260713-4 | optional | present | provenance: source=SRC-000004; document=DOC-2430A598BF3B; mission=MIS-20260713-44F611; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000149 | primary id present | SIG-000149 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000149', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000149 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000149 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000149`

## CAND-73BB26E893A8 · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000148 | non-empty Signal ID | SIG-000148 | Signal ID='SIG-000148' |
| primary_id_pattern | N/A | SIG-000148 | no pattern for dataset | SIG-000148 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000148 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000148 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260713 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260713-44F611; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000148 | primary id present | SIG-000148 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000148', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000148 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000148 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000148`
