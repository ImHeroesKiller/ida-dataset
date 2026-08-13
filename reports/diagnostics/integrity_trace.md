# Integrity Guard Trace

**Generated:** 2026-08-13T02:17:58+00:00

Per-candidate decision chain (evidence only).

## Candidate `CAND-76D8F951A184`

```text
Candidate CAND-76D8F951A184
  ↓
dataset_csv_exists
  PASS
  actual=industry_library.csv
  evidence=CSV present
  ↓
payload_present
  PASS
  evidence=payload fields=32
  ↓
schema_indexed_dataset
  PASS
  actual=Industry ID
  evidence=ID field mapped: Industry ID
  ↓
primary_id_present
  PASS
  actual=IND-000019
  evidence=Industry ID='IND-000019'
  ↓
primary_id_pattern
  PASS
  actual=IND-000019
  evidence=pattern ^IND- vs 'IND-000019'
  ↓
duplicate_id_in_batch
  PASS
  actual=unique_in_batch
  evidence=batch_ids_contains=False
  ↓
duplicate_id_existing_dataset
  FAIL
  actual=exists_in_csv
  evidence=existing_csv_contains=True; dataset_path=industry_library.csv
  ↓
confidence_threshold
  PASS
  actual=0.85 threshold=0.8
  evidence=threshold=0.8; conf=0.85
  ↓
confidence_present
  PASS
  actual=0.85
  evidence=integrity only fails when conf is present and < 0.80
  ↓
provenance_required
  PASS
  actual=ok
  evidence=provenance: source=SRC-CROSSREF; published_date=2020; retrieved_date=2026-08-13T02:16:31+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260813-3FFF19; document=DOC-AFB055C75
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2020; retrieved_date=2026-08-13T02:16:31+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260813-3FFF19; document=DOC-AFB055C75
  ↓
completeness_primary
  PASS
  actual=IND-000019
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000019
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000019
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000019
```
