# Validation Trace

**Generated:** 2026-08-13T01:08:35+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-FF822FF57AA1 · Information Technology Services

dataset=`industry_library` · confidence=`0.855` · threshold=`0.8` · document=`DOC-AFB055C754E2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000015 | non-empty Industry ID | IND-000015 | Industry ID='IND-000015' |
| primary_id_pattern | PASS | IND-000015 | ^IND- | IND-000015 | pattern ^IND- vs 'IND-000015' |
| duplicate_id_in_batch | PASS | IND-000015 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000015 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.85} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2020; retrieved_date=2026-08-13T01:07:08+00:00; confidence=0.85; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2020; retrieved_date=2026-08-13T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2020; retrieved_date=2026-08-13T01:07:08+00:00; confidence=0.85; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000015 | primary id present | IND-000015 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000015', 'confidence': 0.85} | validate_row ok | duplicate_id:IND-000015 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000015 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000015`

## CAND-7AA61C9E1321 · Banking

dataset=`industry_library` · confidence=`0.855` · threshold=`0.8` · document=`DOC-23B61DA3B184`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000015 | non-empty Industry ID | IND-000015 | Industry ID='IND-000015' |
| primary_id_pattern | PASS | IND-000015 | ^IND- | IND-000015 | pattern ^IND- vs 'IND-000015' |
| duplicate_id_in_batch | PASS | IND-000015 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000015 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.85} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-13T01:07:14+00:00; confidence=0.85; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-13T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-13T01:07:14+00:00; confidence=0.85; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000015 | primary id present | IND-000015 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000015', 'confidence': 0.85} | validate_row ok | duplicate_id:IND-000015 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000015 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000015`

## CAND-930DF863CECD · Cement & Building Materials

dataset=`industry_library` · confidence=`0.855` · threshold=`0.8` · document=`DOC-23B61DA3B184`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000016 | non-empty Industry ID | IND-000016 | Industry ID='IND-000016' |
| primary_id_pattern | PASS | IND-000016 | ^IND- | IND-000016 | pattern ^IND- vs 'IND-000016' |
| duplicate_id_in_batch | PASS | IND-000016 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000016 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.85 | >= 0.8 | 0.85 | threshold=0.8; conf=0.85 |
| confidence_present | PASS | 0.85 | optional numeric confidence in Notes/Data Sources/Confidence | 0.85 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.85} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-13T01:07:14+00:00; confidence=0.85; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-13T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-13T01:07:14+00:00; confidence=0.85; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000016 | primary id present | IND-000016 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000016', 'confidence': 0.85} | validate_row ok | duplicate_id:IND-000016 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000016 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000016`

## CAND-E182B875B84B · Food & Beverage Processing

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-42435589D8A0`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000018 | non-empty Industry ID | IND-000018 | Industry ID='IND-000018' |
| primary_id_pattern | PASS | IND-000018 | ^IND- | IND-000018 | pattern ^IND- vs 'IND-000018' |
| duplicate_id_in_batch | PASS | IND-000018 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000018 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2013; retrieved_date=2026-08-13T01:08:07+00:00; confidence=0.92; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2013; retrieved_date=2026-08-13T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2013; retrieved_date=2026-08-13T01:08:07+00:00; confidence=0.92; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000018 | primary id present | IND-000018 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000018', 'confidence': 0.92} | validate_row ok | duplicate_id:IND-000018 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000018 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000018`

## CAND-87503D97E993 · MSMEs / UMKM

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-8DEAD915EF6F`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000016 | non-empty Industry ID | IND-000016 | Industry ID='IND-000016' |
| primary_id_pattern | PASS | IND-000016 | ^IND- | IND-000016 | pattern ^IND- vs 'IND-000016' |
| duplicate_id_in_batch | PASS | IND-000016 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000016 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-13T01:07:08+00:00; confidence=0.92; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-13T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-13T01:07:08+00:00; confidence=0.92; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000016 | primary id present | IND-000016 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000016', 'confidence': 0.92} | validate_row ok | duplicate_id:IND-000016 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000016 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000016`

## CAND-C47F843D31CF · Cement & Building Materials

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-E96B9B477A4B`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000017 | non-empty Industry ID | IND-000017 | Industry ID='IND-000017' |
| primary_id_pattern | PASS | IND-000017 | ^IND- | IND-000017 | pattern ^IND- vs 'IND-000017' |
| duplicate_id_in_batch | PASS | IND-000017 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000017 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2014; retrieved_date=2026-08-13T01:08:00+00:00; confidence=0.92; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2014; retrieved_date=2026-08-13T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2014; retrieved_date=2026-08-13T01:08:00+00:00; confidence=0.92; version=acquisition-grounde |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000017 | primary id present | IND-000017 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000017', 'confidence': 0.92} | validate_row ok | duplicate_id:IND-000017 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000017 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000017`

## CAND-236285DF4A3F · Banking

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-9C3FE7A510A0`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000015 | non-empty Industry ID | IND-000015 | Industry ID='IND-000015' |
| primary_id_pattern | PASS | IND-000015 | ^IND- | IND-000015 | pattern ^IND- vs 'IND-000015' |
| duplicate_id_in_batch | PASS | IND-000015 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | FAIL | IND-000015 | id not in existing CSV | exists_in_csv | existing_csv_contains=True; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-000004; published_date=; retrieved_date=2026-08-13T01:07:42+00:00; confidence=0.92; version=acquisition-grounded-2.0. |
| provenance_present | PASS | provenance: source=SRC-000004; published_date=; retrieved_date=2026-08-13T01:07: | Notes/Data Sources contain source markers | present | provenance: source=SRC-000004; published_date=; retrieved_date=2026-08-13T01:07:42+00:00; confidence=0.92; version=acquisition-grounded-2.0. |
| freshness | N/A | 2026-08-13 | not enforced by integrity_guard | 2026-08-13 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000015 | primary id present | IND-000015 | primary id completeness |
| integrity_final_validate_row | FAIL | {'Industry ID': 'IND-000015', 'confidence': 0.92} | validate_row ok | duplicate_id:IND-000015 | automation.quality.integrity_guard.validate_row → duplicate_id:IND-000015 |

**Integrity final:** `False` · reason=`duplicate_id:IND-000015`
