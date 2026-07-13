# Integrity Guard Trace

**Generated:** 2026-07-13T16:55:52+00:00

Per-candidate decision chain (evidence only).

## Candidate `CAND-DF3B643DC4FC`

```text
Candidate CAND-DF3B643DC4FC
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
  actual=IND-000059
  evidence=Industry ID='IND-000059'
  ↓
primary_id_pattern
  PASS
  actual=IND-000059
  evidence=pattern ^IND- vs 'IND-000059'
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
  actual=0.84 threshold=0.8
  evidence=threshold=0.8; conf=0.84
  ↓
confidence_present
  PASS
  actual=0.84
  evidence=integrity only fails when conf is present and < 0.80
  ↓
provenance_required
  PASS
  actual=ok
  evidence=provenance: source=SRC-000007; published_date=; retrieved_date=2026-07-13T16:54:09+00:00; confidence=0.84; version=acquisition-grounded-2.0.0; mission=MIS-20260713-0C2CB5; document=DOC-648623E72C93; e
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-000007; published_date=; retrieved_date=2026-07-13T16:54:09+00:00; confidence=0.84; version=acquisition-grounded-2.0.0; mission=MIS-20260713-0C2CB5; document=DOC-648623E72C93; e
  ↓
completeness_primary
  PASS
  actual=IND-000059
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000059
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000059
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000059
```
