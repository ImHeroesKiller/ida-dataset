# Integrity Guard Trace

**Generated:** 2026-07-28T06:07:45+00:00

Per-candidate decision chain (evidence only).

## Candidate `CAND-3475745ED4B5`

```text
Candidate CAND-3475745ED4B5
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
  actual=IND-000061
  evidence=Industry ID='IND-000061'
  ↓
primary_id_pattern
  PASS
  actual=IND-000061
  evidence=pattern ^IND- vs 'IND-000061'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-07-28T06:04:47+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260728-BD5387; document=DOC-9D814DA54
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-07-28T06:04:47+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260728-BD5387; document=DOC-9D814DA54
  ↓
completeness_primary
  PASS
  actual=IND-000061
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000061
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000061
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000061
```

## Candidate `CAND-96D7F41016DC`

```text
Candidate CAND-96D7F41016DC
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
  actual=IND-000060
  evidence=Industry ID='IND-000060'
  ↓
primary_id_pattern
  PASS
  actual=IND-000060
  evidence=pattern ^IND- vs 'IND-000060'
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
  actual=0.92 threshold=0.8
  evidence=threshold=0.8; conf=0.92
  ↓
confidence_present
  PASS
  actual=0.92
  evidence=integrity only fails when conf is present and < 0.80
  ↓
provenance_required
  PASS
  actual=ok
  evidence=provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-07-28T06:04:47+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260728-BD5387; document=DOC-9D814DA54
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-07-28T06:04:47+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260728-BD5387; document=DOC-9D814DA54
  ↓
completeness_primary
  PASS
  actual=IND-000060
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000060
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000060
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000060
```
