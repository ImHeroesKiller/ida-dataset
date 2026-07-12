# Validation Trace

**Generated:** 2026-07-12T07:33:56+00:00

Every Integrity Guard rule evaluated (observe-only mirror).

## CAND-A9BDDA0A288F · Green Industry

dataset=`industry_library` · confidence=`0.8375` · threshold=`0.8` · document=`DOC-873B79CA48AE`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000059 | non-empty Industry ID | IND-000059 | Industry ID='IND-000059' |
| primary_id_pattern | PASS | IND-000059 | ^IND- | IND-000059 | pattern ^IND- vs 'IND-000059' |
| duplicate_id_in_batch | PASS | IND-000059 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | PASS | IND-000059 | id not in existing CSV | new_id | existing_csv_contains=False; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.84 | >= 0.8 | 0.84 | threshold=0.8; conf=0.84 |
| confidence_present | PASS | 0.84 | optional numeric confidence in Notes/Data Sources/Confidence | 0.84 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.84} | SRC-/source text OR conf present | ok | provenance: source=SRC-000007; published_date=; retrieved_date=2026-07-12T07:32:35+00:00; confidence=0.84; version=acquisition-grounded-2.0. |
| provenance_present | PASS | provenance: source=SRC-000007; published_date=; retrieved_date=2026-07-12T07:32: | Notes/Data Sources contain source markers | present | provenance: source=SRC-000007; published_date=; retrieved_date=2026-07-12T07:32:35+00:00; confidence=0.84; version=acquisition-grounded-2.0. |
| freshness | N/A | 2026-07-12 | not enforced by integrity_guard | 2026-07-12 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000059 | primary id present | IND-000059 | primary id completeness |
| integrity_final_validate_row | PASS | {'Industry ID': 'IND-000059', 'confidence': 0.84} | validate_row ok | ok | automation.quality.integrity_guard.validate_row → ok |

**Integrity final:** `True` · reason=`ok`

## CAND-7032256FDB1F · Nickel Downstream Industry

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-895A2B2798DA`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000058 | non-empty Industry ID | IND-000058 | Industry ID='IND-000058' |
| primary_id_pattern | PASS | IND-000058 | ^IND- | IND-000058 | pattern ^IND- vs 'IND-000058' |
| duplicate_id_in_batch | PASS | IND-000058 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | PASS | IND-000058 | id not in existing CSV | new_id | existing_csv_contains=False; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=1998; retrieved_date=2026-07-12T07:31:28+00:00; confidence=0.92; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=1998; retrieved_date=2026-07-12T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=1998; retrieved_date=2026-07-12T07:31:28+00:00; confidence=0.92; version=acquisition-grounde |
| freshness | N/A | 2026-07-12 | not enforced by integrity_guard | 2026-07-12 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000058 | primary id present | IND-000058 | primary id completeness |
| integrity_final_validate_row | PASS | {'Industry ID': 'IND-000058', 'confidence': 0.92} | validate_row ok | ok | automation.quality.integrity_guard.validate_row → ok |

**Integrity final:** `True` · reason=`ok`

## CAND-D898D6A1DF9D · Shared Services Centers

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-9C403F1BA3C2`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000058 | non-empty Industry ID | IND-000058 | Industry ID='IND-000058' |
| primary_id_pattern | PASS | IND-000058 | ^IND- | IND-000058 | pattern ^IND- vs 'IND-000058' |
| duplicate_id_in_batch | PASS | IND-000058 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | PASS | IND-000058 | id not in existing CSV | new_id | existing_csv_contains=False; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-CROSSREF; published_date=2013; retrieved_date=2026-07-12T07:31:20+00:00; confidence=0.92; version=acquisition-grounde |
| provenance_present | PASS | provenance: source=SRC-CROSSREF; published_date=2013; retrieved_date=2026-07-12T | Notes/Data Sources contain source markers | present | provenance: source=SRC-CROSSREF; published_date=2013; retrieved_date=2026-07-12T07:31:20+00:00; confidence=0.92; version=acquisition-grounde |
| freshness | N/A | 2026-07-12 | not enforced by integrity_guard | 2026-07-12 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000058 | primary id present | IND-000058 | primary id completeness |
| integrity_final_validate_row | PASS | {'Industry ID': 'IND-000058', 'confidence': 0.92} | validate_row ok | ok | automation.quality.integrity_guard.validate_row → ok |

**Integrity final:** `True` · reason=`ok`

## CAND-A4F2A2B3D784 · MSMEs / UMKM

dataset=`industry_library` · confidence=`0.92` · threshold=`0.8` · document=`DOC-66CDFCAF91C7`

| Rule Name | PASS/FAIL | Input | Expected | Actual | Evidence |
| --- | --- | --- | --- | --- | --- |
| dataset_csv_exists | PASS | — | — | industry_library.csv | CSV present |
| payload_present | PASS | — | — | — | payload fields=32 |
| schema_indexed_dataset | PASS | industry_library | Industry ID | Industry ID | ID field mapped: Industry ID |
| primary_id_present | PASS | IND-000058 | non-empty Industry ID | IND-000058 | Industry ID='IND-000058' |
| primary_id_pattern | PASS | IND-000058 | ^IND- | IND-000058 | pattern ^IND- vs 'IND-000058' |
| duplicate_id_in_batch | PASS | IND-000058 | id not already in this batch | unique_in_batch | batch_ids_contains=False |
| duplicate_id_existing_dataset | PASS | IND-000058 | id not in existing CSV | new_id | existing_csv_contains=False; dataset_path=industry_library.csv |
| confidence_threshold | PASS | 0.92 | >= 0.8 | 0.92 | threshold=0.8; conf=0.92 |
| confidence_present | PASS | 0.92 | optional numeric confidence in Notes/Data Sources/Confidence | 0.92 | integrity only fails when conf is present and < 0.80 |
| relationship_fk | N/A | industry_library | no FK rules for this dataset | n/a | integrity_guard has no FK branch for this stem |
| provenance_required | PASS | {'has_source_marker': True, 'confidence': 0.92} | SRC-/source text OR conf present | ok | provenance: source=SRC-OPENALEX; published_date=2023-07-29; retrieved_date=2026-07-12T07:31:14+00:00; confidence=0.92; version=acquisition-g |
| provenance_present | PASS | provenance: source=SRC-OPENALEX; published_date=2023-07-29; retrieved_date=2026- | Notes/Data Sources contain source markers | present | provenance: source=SRC-OPENALEX; published_date=2023-07-29; retrieved_date=2026-07-12T07:31:14+00:00; confidence=0.92; version=acquisition-g |
| freshness | N/A | 2026-07-12 | not enforced by integrity_guard | 2026-07-12 | integrity_guard has no freshness rule |
| completeness_primary | PASS | IND-000058 | primary id present | IND-000058 | primary id completeness |
| integrity_final_validate_row | PASS | {'Industry ID': 'IND-000058', 'confidence': 0.92} | validate_row ok | ok | automation.quality.integrity_guard.validate_row → ok |

**Integrity final:** `True` · reason=`ok`
