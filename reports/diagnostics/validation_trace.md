# Validation Trace

**Generated:** 2026-08-13T00:05:11+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-FD9FB8F20088 · Mining & Quarrying

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-C700CE372035`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000011 | non-empty Industry ID | IND-000011 | Industry ID='IND-000011' |
| primary_id_pattern | PASS | IND-000011 | ^IND- | IND-000011 | pattern ^IND- vs 'IND-000011' |
| duplicate_id_in_batch | PASS | IND-000011 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000011 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-000004; published_date=2018-11-01T00:00:00Z; retrieved_date=2026-08-13T00:02:00+00:00; confidence=0.92; version=acqui |
| provenance_present | PASS | provenance: source=SRC-000004; published_date=2018-11-01T00:00:00Z; retrieved_da | Notes/Data Sources contain source markers | present | provenance: source=SRC-000004; published_date=2018-11-01T00:00:00Z; retrieved_date=2026-08-13T00:02:00+00:00; confidence=0.92; version=acqui |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000011 | primary id present | IND-000011 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000011', 'confidence': 0.92} | validate_row ok | duplicate_id:IND-000011 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000011 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000011`

## CAND-4D31A7BF92F6 · Banking

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-537579D22309`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000008 | non-empty Industry ID | IND-000008 | Industry ID='IND-000008' |
| primary_id_pattern | PASS | IND-000008 | ^IND- | IND-000008 | pattern ^IND- vs 'IND-000008' |
| duplicate_id_in_batch | PASS | IND-000008 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000008 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-000004; published_date=1997-02-20T00:00:00Z; retrieved_date=2026-08-12T23:58:16+00:00; confidence=0.92; version=acqui |
| provenance_present | PASS | provenance: source=SRC-000004; published_date=1997-02-20T00:00:00Z; retrieved_da | Notes/Data Sources contain source markers | present | provenance: source=SRC-000004; published_date=1997-02-20T00:00:00Z; retrieved_date=2026-08-12T23:58:16+00:00; confidence=0.92; version=acqui |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000008 | primary id present | IND-000008 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000008', 'confidence': 0.92} | validate_row ok | duplicate_id:IND-000008 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000008 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000008`

## CAND-E1882A3C114F · Manufacturing

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-738AC7BFF092`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000002 | non-empty Industry ID | IND-000002 | Industry ID='IND-000002' |
| primary_id_pattern | PASS | IND-000002 | ^IND- | IND-000002 | pattern ^IND- vs 'IND-000002' |
| duplicate_id_in_batch | PASS | IND-000002 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000002 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T23:58:04+00:00; confidence=0.92; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T23:58:04+00:00; confidence=0.92; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000002 | primary id present | IND-000002 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000002', 'confidence': 0.92} | validate_row ok | duplicate_id:IND-000002 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000002 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000002`

## CAND-4AF10225EB6B · Water & Sanitation Utilities

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-206B13589D61`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000006 | non-empty Industry ID | IND-000006 | Industry ID='IND-000006' |
| primary_id_pattern | PASS | IND-000006 | ^IND- | IND-000006 | pattern ^IND- vs 'IND-000006' |
| duplicate_id_in_batch | PASS | IND-000006 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000006 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.92; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.92; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000006 | primary id present | IND-000006 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000006', 'confidence': 0.92} | validate_row ok | duplicate_id:IND-000006 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000006 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000006`

## CAND-6ADD53D8E489 · Tourism & Travel Services

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-E05725A2B141`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000010 | non-empty Industry ID | IND-000010 | Industry ID='IND-000010' |
| primary_id_pattern | PASS | IND-000010 | ^IND- | IND-000010 | pattern ^IND- vs 'IND-000010' |
| duplicate_id_in_batch | PASS | IND-000010 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000010 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-12T23:58:42+00:00; confidence=0.92; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-12T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-12T23:58:42+00:00; confidence=0.92; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000010 | primary id present | IND-000010 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000010', 'confidence': 0.92} | validate_row ok | duplicate_id:IND-000010 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000010 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000010`

## CAND-AB49E874BE64 · Insurance

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-9414CC3EF4C2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000012 | non-empty Industry ID | IND-000012 | Industry ID='IND-000012' |
| primary_id_pattern | PASS | IND-000012 | ^IND- | IND-000012 | pattern ^IND- vs 'IND-000012' |
| duplicate_id_in_batch | PASS | IND-000012 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000012 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-000004; published_date=2017-06-01T00:00:00Z; retrieved_date=2026-08-13T00:02:44+00:00; confidence=0.92; version=acqui |
| provenance_present | PASS | provenance: source=SRC-000004; published_date=2017-06-01T00:00:00Z; retrieved_da | Notes/Data Sources contain source markers | present | provenance: source=SRC-000004; published_date=2017-06-01T00:00:00Z; retrieved_date=2026-08-13T00:02:44+00:00; confidence=0.92; version=acqui |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000012 | primary id present | IND-000012 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000012', 'confidence': 0.92} | validate_row ok | duplicate_id:IND-000012 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000012 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000012`

## CAND-BA8A78824279 · Real Estate

dataset=`industry_library` · confidence=`0.855` · threshold=`0.8` · document=`DOC-738AC7BFF092`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000005 | non-empty Industry ID | IND-000005 | Industry ID='IND-000005' |
| primary_id_pattern | PASS | IND-000005 | ^IND- | IND-000005 | pattern ^IND- vs 'IND-000005' |
| duplicate_id_in_batch | PASS | IND-000005 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000005 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.85} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T23:58:04+00:00; confidence=0.85; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T23:58:04+00:00; confidence=0.85; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000005 | primary id present | IND-000005 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000005', 'confidence': 0.85} | validate_row ok | duplicate_id:IND-000005 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000005 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000005`

## CAND-61FC37838342 · Transportation & Logistics

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-59B8A447D964`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000011 | non-empty Industry ID | IND-000011 | Industry ID='IND-000011' |
| primary_id_pattern | PASS | IND-000011 | ^IND- | IND-000011 | pattern ^IND- vs 'IND-000011' |
| duplicate_id_in_batch | PASS | IND-000011 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000011 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2024; retrieved_date=2026-08-13T00:01:53+00:00; confidence=0.92; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2024; retrieved_date=2026-08-13T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2024; retrieved_date=2026-08-13T00:01:53+00:00; confidence=0.92; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000011 | primary id present | IND-000011 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000011', 'confidence': 0.92} | validate_row ok | duplicate_id:IND-000011 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000011 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000011`

## CAND-7DDE5E598B3B · Cement & Building Materials

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-C70A332231EE`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000010 | non-empty Industry ID | IND-000010 | Industry ID='IND-000010' |
| primary_id_pattern | PASS | IND-000010 | ^IND- | IND-000010 | pattern ^IND- vs 'IND-000010' |
| duplicate_id_in_batch | PASS | IND-000010 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000010 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-000004; published_date=1988-07-01T00:00:00Z; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.92; version=acqui |
| provenance_present | PASS | provenance: source=SRC-000004; published_date=1988-07-01T00:00:00Z; retrieved_da | Notes/Data Sources contain source markers | present | provenance: source=SRC-000004; published_date=1988-07-01T00:00:00Z; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.92; version=acqui |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000010 | primary id present | IND-000010 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000010', 'confidence': 0.92} | validate_row ok | duplicate_id:IND-000010 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000010 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000010`

## CAND-198A3C192524 · Chemicals

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-E6234DE5D9AA`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000014 | non-empty Industry ID | IND-000014 | Industry ID='IND-000014' |
| primary_id_pattern | PASS | IND-000014 | ^IND- | IND-000014 | pattern ^IND- vs 'IND-000014' |
| duplicate_id_in_batch | PASS | IND-000014 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000014 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2021; retrieved_date=2026-08-13T00:02:44+00:00; confidence=0.92; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2021; retrieved_date=2026-08-13T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2021; retrieved_date=2026-08-13T00:02:44+00:00; confidence=0.92; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000014 | primary id present | IND-000014 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000014', 'confidence': 0.92} | validate_row ok | duplicate_id:IND-000014 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000014 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000014`

## CAND-64F739498BDB · Oil & Gas

dataset=`industry_library` · confidence=`0.855` · threshold=`0.8` · document=`DOC-E05725A2B141`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000007 | non-empty Industry ID | IND-000007 | Industry ID='IND-000007' |
| primary_id_pattern | PASS | IND-000007 | ^IND- | IND-000007 | pattern ^IND- vs 'IND-000007' |
| duplicate_id_in_batch | PASS | IND-000007 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000007 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.85} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-12T23:58:42+00:00; confidence=0.85; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-12T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-12T23:58:42+00:00; confidence=0.85; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000007 | primary id present | IND-000007 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000007', 'confidence': 0.85} | validate_row ok | duplicate_id:IND-000007 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000007 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000007`

## CAND-14C0396A9DC4 · Telecommunications

dataset=`industry_library` · confidence=`0.855` · threshold=`0.8` · document=`DOC-206B13589D61`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000005 | non-empty Industry ID | IND-000005 | Industry ID='IND-000005' |
| primary_id_pattern | PASS | IND-000005 | ^IND- | IND-000005 | pattern ^IND- vs 'IND-000005' |
| duplicate_id_in_batch | PASS | IND-000005 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000005 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.85} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.85; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.85; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000005 | primary id present | IND-000005 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000005', 'confidence': 0.85} | validate_row ok | duplicate_id:IND-000005 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000005 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000005`

## CAND-8E0287DD32BE · Digital Economy

dataset=`industry_library` · confidence=`0.874` · threshold=`0.8` · document=`DOC-537579D22309`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000006 | non-empty Industry ID | IND-000006 | Industry ID='IND-000006' |
| primary_id_pattern | PASS | IND-000006 | ^IND- | IND-000006 | pattern ^IND- vs 'IND-000006' |
| duplicate_id_in_batch | PASS | IND-000006 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000006 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.87 | >= 0.8 | 0.87 | threshold=0.8; conf=0.87 |
| confidence_present | PASS | 0.87 | optional numeric confidence in Notes/Data Sources/Confidence | 0.87 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.87} | SRC-/source text OR conf present | ok | provenance: source=SRC-000004; published_date=1997-02-20T00:00:00Z; retrieved_date=2026-08-12T23:58:16+00:00; confidence=0.87; version=acqui |
| provenance_present | PASS | provenance: source=SRC-000004; published_date=1997-02-20T00:00:00Z; retrieved_da | Notes/Data Sources contain source markers | present | provenance: source=SRC-000004; published_date=1997-02-20T00:00:00Z; retrieved_date=2026-08-12T23:58:16+00:00; confidence=0.87; version=acqui |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000006 | primary id present | IND-000006 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000006', 'confidence': 0.87} | validate_row ok | duplicate_id:IND-000006 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000006 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000006`

## CAND-C0DEF0FB996B · Palm Oil & Plantations

dataset=`industry_library` · confidence=`0.855` · threshold=`0.8` · document=`DOC-E05725A2B141`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000008 | non-empty Industry ID | IND-000008 | Industry ID='IND-000008' |
| primary_id_pattern | PASS | IND-000008 | ^IND- | IND-000008 | pattern ^IND- vs 'IND-000008' |
| duplicate_id_in_batch | PASS | IND-000008 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000008 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.85} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-12T23:58:42+00:00; confidence=0.85; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-12T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-12T23:58:42+00:00; confidence=0.85; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000008 | primary id present | IND-000008 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000008', 'confidence': 0.85} | validate_row ok | duplicate_id:IND-000008 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000008 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000008`

## CAND-6ACEF72974C4 · Education Services

dataset=`industry_library` · confidence=`0.874` · threshold=`0.8` · document=`DOC-537579D22309`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000009 | non-empty Industry ID | IND-000009 | Industry ID='IND-000009' |
| primary_id_pattern | PASS | IND-000009 | ^IND- | IND-000009 | pattern ^IND- vs 'IND-000009' |
| duplicate_id_in_batch | PASS | IND-000009 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000009 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.87 | >= 0.8 | 0.87 | threshold=0.8; conf=0.87 |
| confidence_present | PASS | 0.87 | optional numeric confidence in Notes/Data Sources/Confidence | 0.87 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.87} | SRC-/source text OR conf present | ok | provenance: source=SRC-000004; published_date=1997-02-20T00:00:00Z; retrieved_date=2026-08-12T23:58:16+00:00; confidence=0.87; version=acqui |
| provenance_present | PASS | provenance: source=SRC-000004; published_date=1997-02-20T00:00:00Z; retrieved_da | Notes/Data Sources contain source markers | present | provenance: source=SRC-000004; published_date=1997-02-20T00:00:00Z; retrieved_date=2026-08-12T23:58:16+00:00; confidence=0.87; version=acqui |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000009 | primary id present | IND-000009 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000009', 'confidence': 0.87} | validate_row ok | duplicate_id:IND-000009 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000009 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000009`

## CAND-59B49A1A8F1F · Agriculture

dataset=`industry_library` · confidence=`0.874` · threshold=`0.8` · document=`DOC-537579D22309`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000007 | non-empty Industry ID | IND-000007 | Industry ID='IND-000007' |
| primary_id_pattern | PASS | IND-000007 | ^IND- | IND-000007 | pattern ^IND- vs 'IND-000007' |
| duplicate_id_in_batch | PASS | IND-000007 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000007 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.87 | >= 0.8 | 0.87 | threshold=0.8; conf=0.87 |
| confidence_present | PASS | 0.87 | optional numeric confidence in Notes/Data Sources/Confidence | 0.87 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.87} | SRC-/source text OR conf present | ok | provenance: source=SRC-000004; published_date=1997-02-20T00:00:00Z; retrieved_date=2026-08-12T23:58:16+00:00; confidence=0.87; version=acqui |
| provenance_present | PASS | provenance: source=SRC-000004; published_date=1997-02-20T00:00:00Z; retrieved_da | Notes/Data Sources contain source markers | present | provenance: source=SRC-000004; published_date=1997-02-20T00:00:00Z; retrieved_date=2026-08-12T23:58:16+00:00; confidence=0.87; version=acqui |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000007 | primary id present | IND-000007 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000007', 'confidence': 0.87} | validate_row ok | duplicate_id:IND-000007 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000007 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000007`

## CAND-8B66153B6B79 · Mining & Quarrying

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-F517B91263BF`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000013 | non-empty Industry ID | IND-000013 | Industry ID='IND-000013' |
| primary_id_pattern | PASS | IND-000013 | ^IND- | IND-000013 | pattern ^IND- vs 'IND-000013' |
| duplicate_id_in_batch | PASS | IND-000013 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000013 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-13T00:02:01+00:00; confidence=0.92; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-13T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-13T00:02:01+00:00; confidence=0.92; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000013 | primary id present | IND-000013 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000013', 'confidence': 0.92} | validate_row ok | duplicate_id:IND-000013 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000013 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000013`

## CAND-EFE423B30DA3 · Ports & Terminals

dataset=`industry_library` · confidence=`0.855` · threshold=`0.8` · document=`DOC-738AC7BFF092`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000004 | non-empty Industry ID | IND-000004 | Industry ID='IND-000004' |
| primary_id_pattern | PASS | IND-000004 | ^IND- | IND-000004 | pattern ^IND- vs 'IND-000004' |
| duplicate_id_in_batch | PASS | IND-000004 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000004 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.85} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T23:58:04+00:00; confidence=0.85; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T23:58:04+00:00; confidence=0.85; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000004 | primary id present | IND-000004 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000004', 'confidence': 0.85} | validate_row ok | duplicate_id:IND-000004 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000004 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000004`

## CAND-A794C3DE0ED1 · Artificial Intelligence Services

dataset=`industry_library` · confidence=`0.855` · threshold=`0.8` · document=`DOC-206B13589D61`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000002 | non-empty Industry ID | IND-000002 | Industry ID='IND-000002' |
| primary_id_pattern | PASS | IND-000002 | ^IND- | IND-000002 | pattern ^IND- vs 'IND-000002' |
| duplicate_id_in_batch | PASS | IND-000002 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000002 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.85} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.85; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.85; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000002 | primary id present | IND-000002 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000002', 'confidence': 0.85} | validate_row ok | duplicate_id:IND-000002 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000002 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000002`

## CAND-924C6F41A07B · Information Technology Services

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-206B13589D61`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000004 | non-empty Industry ID | IND-000004 | Industry ID='IND-000004' |
| primary_id_pattern | PASS | IND-000004 | ^IND- | IND-000004 | pattern ^IND- vs 'IND-000004' |
| duplicate_id_in_batch | PASS | IND-000004 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000004 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.92; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.92; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000004 | primary id present | IND-000004 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000004', 'confidence': 0.92} | validate_row ok | duplicate_id:IND-000004 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000004 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000004`

## CAND-29E5FA722096 · Media & Entertainment

dataset=`industry_library` · confidence=`0.855` · threshold=`0.8` · document=`DOC-738AC7BFF092`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000003 | non-empty Industry ID | IND-000003 | Industry ID='IND-000003' |
| primary_id_pattern | PASS | IND-000003 | ^IND- | IND-000003 | pattern ^IND- vs 'IND-000003' |
| duplicate_id_in_batch | PASS | IND-000003 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000003 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.85} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T23:58:04+00:00; confidence=0.85; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T23:58:04+00:00; confidence=0.85; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000003 | primary id present | IND-000003 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000003', 'confidence': 0.85} | validate_row ok | duplicate_id:IND-000003 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000003 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000003`

## CAND-4D7BD598AB16 · Automotive

dataset=`industry_library` · confidence=`0.855` · threshold=`0.8` · document=`DOC-738AC7BFF092`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000001 | non-empty Industry ID | IND-000001 | Industry ID='IND-000001' |
| primary_id_pattern | PASS | IND-000001 | ^IND- | IND-000001 | pattern ^IND- vs 'IND-000001' |
| duplicate_id_in_batch | PASS | IND-000001 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000001 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.85} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T23:58:04+00:00; confidence=0.85; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T23:58:04+00:00; confidence=0.85; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000001 | primary id present | IND-000001 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000001', 'confidence': 0.85} | validate_row ok | duplicate_id:IND-000001 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000001 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000001`

## CAND-21EFE6035AB9 · Cybersecurity Industry

dataset=`industry_library` · confidence=`0.855` · threshold=`0.8` · document=`DOC-206B13589D61`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000003 | non-empty Industry ID | IND-000003 | Industry ID='IND-000003' |
| primary_id_pattern | PASS | IND-000003 | ^IND- | IND-000003 | pattern ^IND- vs 'IND-000003' |
| duplicate_id_in_batch | PASS | IND-000003 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000003 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.85} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.85; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.85; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000003 | primary id present | IND-000003 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000003', 'confidence': 0.85} | validate_row ok | duplicate_id:IND-000003 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000003 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000003`

## CAND-9DFB1CD280F2 · Manufacturing

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-ACDDB05BD4EA`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000001 | non-empty Industry ID | IND-000001 | Industry ID='IND-000001' |
| primary_id_pattern | PASS | IND-000001 | ^IND- | IND-000001 | pattern ^IND- vs 'IND-000001' |
| duplicate_id_in_batch | PASS | IND-000001 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000001 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2022; retrieved_date=2026-08-12T23:58:16+00:00; confidence=0.92; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2022; retrieved_date=2026-08-12T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2022; retrieved_date=2026-08-12T23:58:16+00:00; confidence=0.92; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000001 | primary id present | IND-000001 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000001', 'confidence': 0.92} | validate_row ok | duplicate_id:IND-000001 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000001 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000001`

## CAND-933FD0411EAD · Ports & Terminals

dataset=`industry_library` · confidence=`0.855` · threshold=`0.8` · document=`DOC-E05725A2B141`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000009 | non-empty Industry ID | IND-000009 | Industry ID='IND-000009' |
| primary_id_pattern | PASS | IND-000009 | ^IND- | IND-000009 | pattern ^IND- vs 'IND-000009' |
| duplicate_id_in_batch | PASS | IND-000009 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000009 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.85} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-12T23:58:42+00:00; confidence=0.85; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-12T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-12T23:58:42+00:00; confidence=0.85; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000009 | primary id present | IND-000009 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000009', 'confidence': 0.85} | validate_row ok | duplicate_id:IND-000009 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000009 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000009`

## CAND-6A30FDEFF5EF · Media & Entertainment

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-F517B91263BF`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000012 | non-empty Industry ID | IND-000012 | Industry ID='IND-000012' |
| primary_id_pattern | PASS | IND-000012 | ^IND- | IND-000012 | pattern ^IND- vs 'IND-000012' |
| duplicate_id_in_batch | PASS | IND-000012 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000012 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-13T00:02:01+00:00; confidence=0.92; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-13T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-13T00:02:01+00:00; confidence=0.92; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000012 | primary id present | IND-000012 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000012', 'confidence': 0.92} | validate_row ok | duplicate_id:IND-000012 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000012 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000012`

## CAND-80C2AC135F36 · Creative Economy

dataset=`industry_library` · confidence=`0.836` · threshold=`0.8` · document=`DOC-0955E1D00852`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000009 | non-empty Industry ID | IND-000009 | Industry ID='IND-000009' |
| primary_id_pattern | PASS | IND-000009 | ^IND- | IND-000009 | pattern ^IND- vs 'IND-000009' |
| duplicate_id_in_batch | PASS | IND-000009 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000009 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.84 | >= 0.8 | 0.84 | threshold=0.8; conf=0.84 |
| confidence_present | PASS | 0.84 | optional numeric confidence in Notes/Data Sources/Confidence | 0.84 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.84} | SRC-/source text OR conf present | ok | provenance: source=SRC-OPENALEX; published_date=2012-12-01; retrieved_date=2026-08-13T00:02:50+00:00; confidence=0.84; version=acquisition-g |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; published_date=2012-12-01; retrieved_date=2026- | Notes/Data Sources contain source markers | present | provenance: source=SRC-OPENALEX; published_date=2012-12-01; retrieved_date=2026-08-13T00:02:50+00:00; confidence=0.84; version=acquisition-g |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000009 | primary id present | IND-000009 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000009', 'confidence': 0.84} | validate_row ok | duplicate_id:IND-000009 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000009 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000009`

## CAND-DB2E39200CB1 · Ports & Terminals

dataset=`industry_library` · confidence=`0.8075` · threshold=`0.8` · document=`DOC-4797FB998A54`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000013 | non-empty Industry ID | IND-000013 | Industry ID='IND-000013' |
| primary_id_pattern | PASS | IND-000013 | ^IND- | IND-000013 | pattern ^IND- vs 'IND-000013' |
| duplicate_id_in_batch | PASS | IND-000013 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000013 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.81 | >= 0.8 | 0.81 | threshold=0.8; conf=0.81 |
| confidence_present | PASS | 0.81 | optional numeric confidence in Notes/Data Sources/Confidence | 0.81 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.81} | SRC-/source text OR conf present | ok | provenance: source=SRC-000001; published_date=; retrieved_date=2026-08-13T00:03:44+00:00; confidence=0.81; version=acquisition-grounded-2.0. |
| provenance_present | PASS | provenance: source=SRC-000001; published_date=; retrieved_date=2026-08-13T00:03: | Notes/Data Sources contain source markers | present | provenance: source=SRC-000001; published_date=; retrieved_date=2026-08-13T00:03:44+00:00; confidence=0.81; version=acquisition-grounded-2.0. |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000013 | primary id present | IND-000013 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000013', 'confidence': 0.81} | validate_row ok | duplicate_id:IND-000013 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000013 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000013`

## CAND-8FB7605FB916 · Palm Oil & Plantations

dataset=`industry_library` · confidence=`0.836` · threshold=`0.8` · document=`DOC-021A8A9B5C4E`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000010 | non-empty Industry ID | IND-000010 | Industry ID='IND-000010' |
| primary_id_pattern | PASS | IND-000010 | ^IND- | IND-000010 | pattern ^IND- vs 'IND-000010' |
| duplicate_id_in_batch | PASS | IND-000010 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000010 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.84 | >= 0.8 | 0.84 | threshold=0.8; conf=0.84 |
| confidence_present | PASS | 0.84 | optional numeric confidence in Notes/Data Sources/Confidence | 0.84 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.84} | SRC-/source text OR conf present | ok | provenance: source=SRC-OPENALEX; published_date=2014-04-03; retrieved_date=2026-08-13T00:03:45+00:00; confidence=0.84; version=acquisition-g |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; published_date=2014-04-03; retrieved_date=2026- | Notes/Data Sources contain source markers | present | provenance: source=SRC-OPENALEX; published_date=2014-04-03; retrieved_date=2026-08-13T00:03:45+00:00; confidence=0.84; version=acquisition-g |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000010 | primary id present | IND-000010 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000010', 'confidence': 0.84} | validate_row ok | duplicate_id:IND-000010 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000010 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000010`

## CAND-7AFBC514D015 · Agriculture

dataset=`industry_library` · confidence=`0.8075` · threshold=`0.8` · document=`DOC-7A131D726BF1`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000011 | non-empty Industry ID | IND-000011 | Industry ID='IND-000011' |
| primary_id_pattern | PASS | IND-000011 | ^IND- | IND-000011 | pattern ^IND- vs 'IND-000011' |
| duplicate_id_in_batch | PASS | IND-000011 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000011 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.81 | >= 0.8 | 0.81 | threshold=0.8; conf=0.81 |
| confidence_present | PASS | 0.81 | optional numeric confidence in Notes/Data Sources/Confidence | 0.81 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.81} | SRC-/source text OR conf present | ok | provenance: source=SRC-000001; published_date=; retrieved_date=2026-08-13T00:03:43+00:00; confidence=0.81; version=acquisition-grounded-2.0. |
| provenance_present | PASS | provenance: source=SRC-000001; published_date=; retrieved_date=2026-08-13T00:03: | Notes/Data Sources contain source markers | present | provenance: source=SRC-000001; published_date=; retrieved_date=2026-08-13T00:03:43+00:00; confidence=0.81; version=acquisition-grounded-2.0. |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000011 | primary id present | IND-000011 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000011', 'confidence': 0.81} | validate_row ok | duplicate_id:IND-000011 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000011 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000011`

## CAND-4055AA2F2F4E · Mining & Quarrying

dataset=`industry_library` · confidence=`0.836` · threshold=`0.8` · document=`DOC-7EA36A8AE842`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000005 | non-empty Industry ID | IND-000005 | Industry ID='IND-000005' |
| primary_id_pattern | PASS | IND-000005 | ^IND- | IND-000005 | pattern ^IND- vs 'IND-000005' |
| duplicate_id_in_batch | PASS | IND-000005 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000005 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.84 | >= 0.8 | 0.84 | threshold=0.8; conf=0.84 |
| confidence_present | PASS | 0.84 | optional numeric confidence in Notes/Data Sources/Confidence | 0.84 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.84} | SRC-/source text OR conf present | ok | provenance: source=SRC-OPENALEX; published_date=2020-05-23; retrieved_date=2026-08-12T23:58:36+00:00; confidence=0.84; version=acquisition-g |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; published_date=2020-05-23; retrieved_date=2026- | Notes/Data Sources contain source markers | present | provenance: source=SRC-OPENALEX; published_date=2020-05-23; retrieved_date=2026-08-12T23:58:36+00:00; confidence=0.84; version=acquisition-g |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000005 | primary id present | IND-000005 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000005', 'confidence': 0.84} | validate_row ok | duplicate_id:IND-000005 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000005 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000005`

## CAND-5D1B69EBA921 · Education Services

dataset=`industry_library` · confidence=`0.836` · threshold=`0.8` · document=`DOC-7EA36A8AE842`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000003 | non-empty Industry ID | IND-000003 | Industry ID='IND-000003' |
| primary_id_pattern | PASS | IND-000003 | ^IND- | IND-000003 | pattern ^IND- vs 'IND-000003' |
| duplicate_id_in_batch | PASS | IND-000003 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000003 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.84 | >= 0.8 | 0.84 | threshold=0.8; conf=0.84 |
| confidence_present | PASS | 0.84 | optional numeric confidence in Notes/Data Sources/Confidence | 0.84 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.84} | SRC-/source text OR conf present | ok | provenance: source=SRC-OPENALEX; published_date=2020-05-23; retrieved_date=2026-08-12T23:58:36+00:00; confidence=0.84; version=acquisition-g |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; published_date=2020-05-23; retrieved_date=2026- | Notes/Data Sources contain source markers | present | provenance: source=SRC-OPENALEX; published_date=2020-05-23; retrieved_date=2026-08-12T23:58:36+00:00; confidence=0.84; version=acquisition-g |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000003 | primary id present | IND-000003 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000003', 'confidence': 0.84} | validate_row ok | duplicate_id:IND-000003 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000003 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000003`

## CAND-02826646AA38 · Transportation & Logistics

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-7EA36A8AE842`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000006 | non-empty Industry ID | IND-000006 | Industry ID='IND-000006' |
| primary_id_pattern | PASS | IND-000006 | ^IND- | IND-000006 | pattern ^IND- vs 'IND-000006' |
| duplicate_id_in_batch | PASS | IND-000006 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000006 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-OPENALEX; published_date=2020-05-23; retrieved_date=2026-08-12T23:58:36+00:00; confidence=0.92; version=acquisition-g |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; published_date=2020-05-23; retrieved_date=2026- | Notes/Data Sources contain source markers | present | provenance: source=SRC-OPENALEX; published_date=2020-05-23; retrieved_date=2026-08-12T23:58:36+00:00; confidence=0.92; version=acquisition-g |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000006 | primary id present | IND-000006 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000006', 'confidence': 0.92} | validate_row ok | duplicate_id:IND-000006 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000006 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000006`

## CAND-6E7840687EAE · Tourism & Travel Services

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-7A53E6CD2239`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000001 | non-empty Industry ID | IND-000001 | Industry ID='IND-000001' |
| primary_id_pattern | PASS | IND-000001 | ^IND- | IND-000001 | pattern ^IND- vs 'IND-000001' |
| duplicate_id_in_batch | PASS | IND-000001 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000001 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-OPENALEX; published_date=2019-09-18; retrieved_date=2026-08-12T23:58:11+00:00; confidence=0.92; version=acquisition-g |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; published_date=2019-09-18; retrieved_date=2026- | Notes/Data Sources contain source markers | present | provenance: source=SRC-OPENALEX; published_date=2019-09-18; retrieved_date=2026-08-12T23:58:11+00:00; confidence=0.92; version=acquisition-g |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000001 | primary id present | IND-000001 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000001', 'confidence': 0.92} | validate_row ok | duplicate_id:IND-000001 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000001 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000001`

## CAND-7E3C4B387591 · Water & Sanitation Utilities

dataset=`industry_library` · confidence=`0.836` · threshold=`0.8` · document=`DOC-7EA36A8AE842`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000007 | non-empty Industry ID | IND-000007 | Industry ID='IND-000007' |
| primary_id_pattern | PASS | IND-000007 | ^IND- | IND-000007 | pattern ^IND- vs 'IND-000007' |
| duplicate_id_in_batch | PASS | IND-000007 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000007 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.84 | >= 0.8 | 0.84 | threshold=0.8; conf=0.84 |
| confidence_present | PASS | 0.84 | optional numeric confidence in Notes/Data Sources/Confidence | 0.84 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.84} | SRC-/source text OR conf present | ok | provenance: source=SRC-OPENALEX; published_date=2020-05-23; retrieved_date=2026-08-12T23:58:36+00:00; confidence=0.84; version=acquisition-g |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; published_date=2020-05-23; retrieved_date=2026- | Notes/Data Sources contain source markers | present | provenance: source=SRC-OPENALEX; published_date=2020-05-23; retrieved_date=2026-08-12T23:58:36+00:00; confidence=0.84; version=acquisition-g |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000007 | primary id present | IND-000007 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000007', 'confidence': 0.84} | validate_row ok | duplicate_id:IND-000007 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000007 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000007`

## CAND-91FFA6E6591A · Media & Entertainment

dataset=`industry_library` · confidence=`0.8075` · threshold=`0.8` · document=`DOC-8903E78503B7`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000014 | non-empty Industry ID | IND-000014 | Industry ID='IND-000014' |
| primary_id_pattern | PASS | IND-000014 | ^IND- | IND-000014 | pattern ^IND- vs 'IND-000014' |
| duplicate_id_in_batch | PASS | IND-000014 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000014 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.81 | >= 0.8 | 0.81 | threshold=0.8; conf=0.81 |
| confidence_present | PASS | 0.81 | optional numeric confidence in Notes/Data Sources/Confidence | 0.81 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.81} | SRC-/source text OR conf present | ok | provenance: source=SRC-000001; published_date=; retrieved_date=2026-08-13T00:03:44+00:00; confidence=0.81; version=acquisition-grounded-2.0. |
| provenance_present | PASS | provenance: source=SRC-000001; published_date=; retrieved_date=2026-08-13T00:03: | Notes/Data Sources contain source markers | present | provenance: source=SRC-000001; published_date=; retrieved_date=2026-08-13T00:03:44+00:00; confidence=0.81; version=acquisition-grounded-2.0. |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000014 | primary id present | IND-000014 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000014', 'confidence': 0.81} | validate_row ok | duplicate_id:IND-000014 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000014 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000014`

## CAND-DF3529FA1AA8 · Healthcare Services

dataset=`industry_library` · confidence=`0.8075` · threshold=`0.8` · document=`DOC-8D8AB77BAAB8`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000012 | non-empty Industry ID | IND-000012 | Industry ID='IND-000012' |
| primary_id_pattern | PASS | IND-000012 | ^IND- | IND-000012 | pattern ^IND- vs 'IND-000012' |
| duplicate_id_in_batch | PASS | IND-000012 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000012 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.81 | >= 0.8 | 0.81 | threshold=0.8; conf=0.81 |
| confidence_present | PASS | 0.81 | optional numeric confidence in Notes/Data Sources/Confidence | 0.81 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.81} | SRC-/source text OR conf present | ok | provenance: source=SRC-000001; published_date=; retrieved_date=2026-08-13T00:03:43+00:00; confidence=0.81; version=acquisition-grounded-2.0. |
| provenance_present | PASS | provenance: source=SRC-000001; published_date=; retrieved_date=2026-08-13T00:03: | Notes/Data Sources contain source markers | present | provenance: source=SRC-000001; published_date=; retrieved_date=2026-08-13T00:03:43+00:00; confidence=0.81; version=acquisition-grounded-2.0. |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000012 | primary id present | IND-000012 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000012', 'confidence': 0.81} | validate_row ok | duplicate_id:IND-000012 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000012 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000012`

## CAND-8270A7788088 · Waste Management & Environmental Services

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-EBE5AD43307D`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000002 | non-empty Industry ID | IND-000002 | Industry ID='IND-000002' |
| primary_id_pattern | PASS | IND-000002 | ^IND- | IND-000002 | pattern ^IND- vs 'IND-000002' |
| duplicate_id_in_batch | PASS | IND-000002 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000002 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-OPENALEX; published_date=2022-11-22; retrieved_date=2026-08-12T23:58:24+00:00; confidence=0.92; version=acquisition-g |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; published_date=2022-11-22; retrieved_date=2026- | Notes/Data Sources contain source markers | present | provenance: source=SRC-OPENALEX; published_date=2022-11-22; retrieved_date=2026-08-12T23:58:24+00:00; confidence=0.92; version=acquisition-g |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000002 | primary id present | IND-000002 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000002', 'confidence': 0.92} | validate_row ok | duplicate_id:IND-000002 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000002 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000002`

## CAND-31BF7E48BB67 · Maritime & Shipping

dataset=`industry_library` · confidence=`0.836` · threshold=`0.8` · document=`DOC-7EA36A8AE842`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000004 | non-empty Industry ID | IND-000004 | Industry ID='IND-000004' |
| primary_id_pattern | PASS | IND-000004 | ^IND- | IND-000004 | pattern ^IND- vs 'IND-000004' |
| duplicate_id_in_batch | PASS | IND-000004 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000004 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.84 | >= 0.8 | 0.84 | threshold=0.8; conf=0.84 |
| confidence_present | PASS | 0.84 | optional numeric confidence in Notes/Data Sources/Confidence | 0.84 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.84} | SRC-/source text OR conf present | ok | provenance: source=SRC-OPENALEX; published_date=2020-05-23; retrieved_date=2026-08-12T23:58:36+00:00; confidence=0.84; version=acquisition-g |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; published_date=2020-05-23; retrieved_date=2026- | Notes/Data Sources contain source markers | present | provenance: source=SRC-OPENALEX; published_date=2020-05-23; retrieved_date=2026-08-12T23:58:36+00:00; confidence=0.84; version=acquisition-g |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000004 | primary id present | IND-000004 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000004', 'confidence': 0.84} | validate_row ok | duplicate_id:IND-000004 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000004 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000004`

## CAND-2D17B6521F4F · Textiles & Apparel

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-1D57F420AD4F`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000008 | non-empty Industry ID | IND-000008 | Industry ID='IND-000008' |
| primary_id_pattern | PASS | IND-000008 | ^IND- | IND-000008 | pattern ^IND- vs 'IND-000008' |
| duplicate_id_in_batch | PASS | IND-000008 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000008 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-OPENALEX; published_date=2019-09-27; retrieved_date=2026-08-13T00:02:09+00:00; confidence=0.92; version=acquisition-g |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; published_date=2019-09-27; retrieved_date=2026- | Notes/Data Sources contain source markers | present | provenance: source=SRC-OPENALEX; published_date=2019-09-27; retrieved_date=2026-08-13T00:02:09+00:00; confidence=0.92; version=acquisition-g |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000008 | primary id present | IND-000008 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000008', 'confidence': 0.92} | validate_row ok | duplicate_id:IND-000008 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000008 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000008`
