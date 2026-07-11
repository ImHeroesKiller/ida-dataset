# Integrity Guard Trace

**Generated:** 2026-07-11T14:18:19+00:00

Per-candidate decision chain (evidence only).

## Candidate `CAND-1CAE1B4D1FB3`

```text
Candidate CAND-1CAE1B4D1FB3
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
  PASS
  actual=new_id
  evidence=existing_csv_contains=False; dataset_path=industry_library.csv
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
  evidence=provenance: source=SRC-CROSSREF; published_date=1998; retrieved_date=2026-07-11T14:15:45+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260711-E0F5D5; document=DOC-895A2B279
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=1998; retrieved_date=2026-07-11T14:15:45+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260711-E0F5D5; document=DOC-895A2B279
  ↓
completeness_primary
  PASS
  actual=IND-000056
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  PASS
  actual=ok
  evidence=automation.quality.integrity_guard.validate_row → ok
  ↓
Publisher decision: Skipped
  reason=session_dry_run_true — publisher did not append
```

## Candidate `CAND-68DBCF40956E`

```text
Candidate CAND-68DBCF40956E
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
  PASS
  actual=new_id
  evidence=existing_csv_contains=False; dataset_path=industry_library.csv
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2013; retrieved_date=2026-07-11T14:15:42+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260711-E0F5D5; document=DOC-9C403F1BA
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2013; retrieved_date=2026-07-11T14:15:42+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260711-E0F5D5; document=DOC-9C403F1BA
  ↓
completeness_primary
  PASS
  actual=IND-000056
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  PASS
  actual=ok
  evidence=automation.quality.integrity_guard.validate_row → ok
  ↓
Publisher decision: Skipped
  reason=session_dry_run_true — publisher did not append
```

## Candidate `CAND-B707E7081EA3`

```text
Candidate CAND-B707E7081EA3
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
  PASS
  actual=new_id
  evidence=existing_csv_contains=False; dataset_path=industry_library.csv
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
  evidence=provenance: source=SRC-OPENALEX; published_date=2023-07-29; retrieved_date=2026-07-11T14:15:38+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260711-E0F5D5; document=DOC-66C
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-OPENALEX; published_date=2023-07-29; retrieved_date=2026-07-11T14:15:38+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260711-E0F5D5; document=DOC-66C
  ↓
completeness_primary
  PASS
  actual=IND-000056
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  PASS
  actual=ok
  evidence=automation.quality.integrity_guard.validate_row → ok
  ↓
Publisher decision: Skipped
  reason=session_dry_run_true — publisher did not append
```
