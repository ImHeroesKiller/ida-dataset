# Integrity Guard Trace

**Generated:** 2026-07-11T18:00:48+00:00

Per-candidate decision chain (evidence only).

## Candidate `CAND-E9B6307893CE`

```text
Candidate CAND-E9B6307893CE
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
  actual=IND-000056
  evidence=Industry ID='IND-000056'
  ↓
primary_id_pattern
  PASS
  actual=IND-000056
  evidence=pattern ^IND- vs 'IND-000056'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=1998; retrieved_date=2026-07-11T17:54:39+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260711-CF302E; document=DOC-895A2B279
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=1998; retrieved_date=2026-07-11T17:54:39+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260711-CF302E; document=DOC-895A2B279
  ↓
completeness_primary
  PASS
  actual=IND-000056
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000056
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000056
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000056
```

## Candidate `CAND-D5FB552C5669`

```text
Candidate CAND-D5FB552C5669
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
  actual=IND-000057
  evidence=Industry ID='IND-000057'
  ↓
primary_id_pattern
  PASS
  actual=IND-000057
  evidence=pattern ^IND- vs 'IND-000057'
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
  evidence=provenance: source=SRC-OPENALEX; published_date=; retrieved_date=2026-07-11T17:56:31+00:00; confidence=0.84; version=acquisition-grounded-2.0.0; mission=MIS-20260711-CF302E; document=DOC-170DB7E26EB9;
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-OPENALEX; published_date=; retrieved_date=2026-07-11T17:56:31+00:00; confidence=0.84; version=acquisition-grounded-2.0.0; mission=MIS-20260711-CF302E; document=DOC-170DB7E26EB9;
  ↓
completeness_primary
  PASS
  actual=IND-000057
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000057
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000057
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000057
```

## Candidate `CAND-5D05664CF73E`

```text
Candidate CAND-5D05664CF73E
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
  actual=IND-000056
  evidence=Industry ID='IND-000056'
  ↓
primary_id_pattern
  PASS
  actual=IND-000056
  evidence=pattern ^IND- vs 'IND-000056'
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
  evidence=provenance: source=SRC-OPENALEX; published_date=2020-03-31; retrieved_date=2026-07-11T17:53:23+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260711-CF302E; document=DOC-F4E
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-OPENALEX; published_date=2020-03-31; retrieved_date=2026-07-11T17:53:23+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260711-CF302E; document=DOC-F4E
  ↓
completeness_primary
  PASS
  actual=IND-000056
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000056
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000056
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000056
```
