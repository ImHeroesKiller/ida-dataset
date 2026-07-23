# Validation Trace

**Generated:** 2026-07-23T18:33:22+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-250C74F2EEBB · World Bank document

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-A99E56C64737`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000741 | non-empty Signal ID | SIG-000741 | Signal ID='SIG-000741' |
| primary_id_pattern | N/A | SIG-000741 | no pattern for dataset | SIG-000741 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000741 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000741 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260723-A | optional | present | provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260723-A2B893; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | — | not enforced by integrity_guard | (none) | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000741 | primary id present | SIG-000741 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000741', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000741 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000741 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000741`

## CAND-D6678FE6776D · The Influence of Service Quality on Library Users at Padang State Polytechnic

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-5DFD7BF054D2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000740 | non-empty Signal ID | SIG-000740 | Signal ID='SIG-000740' |
| primary_id_pattern | N/A | SIG-000740 | no pattern for dataset | SIG-000740 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000740 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000740 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260723 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260723-A2B893; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000740 | primary id present | SIG-000740 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000740', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000740 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000740 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000740`

## CAND-825E598F936A · New normal and library services in Indonesia: a case study of university libraries

dataset=`business_signal_library` · confidence=`0.88` · threshold=`0.8` · document=`DOC-7C7239075702`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000742 | non-empty Signal ID | SIG-000742 | Signal ID='SIG-000742' |
| primary_id_pattern | N/A | SIG-000742 | no pattern for dataset | SIG-000742 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000742 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000742 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.88 | >= 0.8 | 0.88 | threshold=0.8; conf=0.88 |
| confidence_present | PASS | 0.88 | optional numeric confidence in Notes/Data Sources/Confidence | 0.88 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260723 | optional | present | provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260723-A2B893; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2020-10-28 | not enforced by integrity_guard | 2020-10-28 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000742 | primary id present | SIG-000742 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000742', 'confidence': 0.88} | validate_row ok | duplicate_id:SIG-000742 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000742 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000742`

## CAND-8D478EAD28B6 · Indonesia - Library Development Project

dataset=`business_signal_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-D5443F5620D9`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000744 | non-empty Signal ID | SIG-000744 | Signal ID='SIG-000744' |
| primary_id_pattern | N/A | SIG-000744 | no pattern for dataset | SIG-000744 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000744 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000744 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260723-A | optional | present | provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260723-A2B893; discovery_provider=connector; append_only=true; extra |
| freshness | N/A | 2001-05-07T00:00:00Z | not enforced by integrity_guard | 2001-05-07T00:00:00Z | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000744 | primary id present | SIG-000744 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000744', 'confidence': 0.92} | validate_row ok | duplicate_id:SIG-000744 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000744 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000744`

## CAND-C1F9121CCB1E · Development of the Siak Library and Archives Service (2004-2022)

dataset=`business_signal_library` · confidence=`0.9` · threshold=`0.8` · document=`DOC-50B3F3BC8DEB`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | business_signal_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=14 |
| schema_indexed_dataset | PASS | business_signal_library | Signal ID | Signal ID | ID field mapped: Signal ID |
| primary_id_present | PASS | SIG-000743 | non-empty Signal ID | SIG-000743 | Signal ID='SIG-000743' |
| primary_id_pattern | N/A | SIG-000743 | no pattern for dataset | SIG-000743 | ID_PATTERNS has no entry |
| duplicate_id_in_batch | PASS | SIG-000743 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | SIG-000743 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=business_signal_library.csv |
| confidence_threshold | PASS | 0.9 | >= 0.8 | 0.9 | threshold=0.8; conf=0.9 |
| confidence_present | PASS | 0.9 | optional numeric confidence in Notes/Data Sources/Confidence | 0.9 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | business_signal_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | N/A | — | — | — | dataset business_signal_library not in provenance-required set |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260723 | optional | present | provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260723-A2B893; discovery_provider=connector; append_only=true; ext |
| freshness | N/A | 2024 | not enforced by integrity_guard | 2024 | integrity_guard has no freshness rule |
| completeness_primary | PASS | SIG-000743 | primary id present | SIG-000743 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Signal ID': 'SIG-000743', 'confidence': 0.9} | validate_row ok | duplicate_id:SIG-000743 | automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000743 |

**Integrity final:** `False` · reason=`duplicate_id:SIG-000743`
