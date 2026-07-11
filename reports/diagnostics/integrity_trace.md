# Integrity Guard Trace

**Generated:** 2026-07-11T13:10:45+00:00

Per-candidate decision chain (evidence only).

## Candidate `CAND-A2586EE1B9E4`

```text
Candidate CAND-A2586EE1B9E4
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
  actual=IND-000054
  evidence=Industry ID='IND-000054'
  ↓
primary_id_pattern
  PASS
  actual=IND-000054
  evidence=pattern ^IND- vs 'IND-000054'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=; retrieved_date=2026-07-11T12:49:26+00:00; confidence=0.84; version=acquisition-grounded-2.0.0; mission=MIS-20260711-A36688; document=DOC-C325082A3272;
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=; retrieved_date=2026-07-11T12:49:26+00:00; confidence=0.84; version=acquisition-grounded-2.0.0; mission=MIS-20260711-A36688; document=DOC-C325082A3272;
  ↓
completeness_primary
  PASS
  actual=IND-000054
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000054
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000054
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000054
```

## Candidate `CAND-18CCB68EA40E`

```text
Candidate CAND-18CCB68EA40E
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
  actual=IND-000055
  evidence=Industry ID='IND-000055'
  ↓
primary_id_pattern
  PASS
  actual=IND-000055
  evidence=pattern ^IND- vs 'IND-000055'
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
  evidence=provenance: source=SRC-CISA; published_date=; retrieved_date=2026-07-11T13:07:20+00:00; confidence=0.84; version=acquisition-grounded-2.0.0; mission=MIS-20260711-A36688; document=DOC-DED8E51BC76A; ent
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CISA; published_date=; retrieved_date=2026-07-11T13:07:20+00:00; confidence=0.84; version=acquisition-grounded-2.0.0; mission=MIS-20260711-A36688; document=DOC-DED8E51BC76A; ent
  ↓
completeness_primary
  PASS
  actual=IND-000055
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000055
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000055
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000055
```
