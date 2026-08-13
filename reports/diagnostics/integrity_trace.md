# Integrity Guard Trace

**Generated:** 2026-08-13T01:08:35+00:00

Per-candidate decision chain (evidence only).

## Candidate `CAND-FF822FF57AA1`

```text
Candidate CAND-FF822FF57AA1
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
  actual=IND-000015
  evidence=Industry ID='IND-000015'
  ↓
primary_id_pattern
  PASS
  actual=IND-000015
  evidence=pattern ^IND- vs 'IND-000015'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2020; retrieved_date=2026-08-13T01:07:08+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260813-E95C7C; document=DOC-AFB055C75
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2020; retrieved_date=2026-08-13T01:07:08+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260813-E95C7C; document=DOC-AFB055C75
  ↓
completeness_primary
  PASS
  actual=IND-000015
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000015
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000015
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000015
```

## Candidate `CAND-7AA61C9E1321`

```text
Candidate CAND-7AA61C9E1321
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
  actual=IND-000015
  evidence=Industry ID='IND-000015'
  ↓
primary_id_pattern
  PASS
  actual=IND-000015
  evidence=pattern ^IND- vs 'IND-000015'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-13T01:07:14+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260813-E95C7C; document=DOC-23B61DA3B
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-13T01:07:14+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260813-E95C7C; document=DOC-23B61DA3B
  ↓
completeness_primary
  PASS
  actual=IND-000015
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000015
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000015
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000015
```

## Candidate `CAND-930DF863CECD`

```text
Candidate CAND-930DF863CECD
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
  actual=IND-000016
  evidence=Industry ID='IND-000016'
  ↓
primary_id_pattern
  PASS
  actual=IND-000016
  evidence=pattern ^IND- vs 'IND-000016'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-13T01:07:14+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260813-E95C7C; document=DOC-23B61DA3B
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-13T01:07:14+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260813-E95C7C; document=DOC-23B61DA3B
  ↓
completeness_primary
  PASS
  actual=IND-000016
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000016
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000016
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000016
```

## Candidate `CAND-E182B875B84B`

```text
Candidate CAND-E182B875B84B
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
  actual=IND-000018
  evidence=Industry ID='IND-000018'
  ↓
primary_id_pattern
  PASS
  actual=IND-000018
  evidence=pattern ^IND- vs 'IND-000018'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2013; retrieved_date=2026-08-13T01:08:07+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260813-E95C7C; document=DOC-42435589D
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2013; retrieved_date=2026-08-13T01:08:07+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260813-E95C7C; document=DOC-42435589D
  ↓
completeness_primary
  PASS
  actual=IND-000018
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000018
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000018
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000018
```

## Candidate `CAND-87503D97E993`

```text
Candidate CAND-87503D97E993
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
  actual=IND-000016
  evidence=Industry ID='IND-000016'
  ↓
primary_id_pattern
  PASS
  actual=IND-000016
  evidence=pattern ^IND- vs 'IND-000016'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-13T01:07:08+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260813-E95C7C; document=DOC-8DEAD915E
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-13T01:07:08+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260813-E95C7C; document=DOC-8DEAD915E
  ↓
completeness_primary
  PASS
  actual=IND-000016
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000016
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000016
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000016
```

## Candidate `CAND-C47F843D31CF`

```text
Candidate CAND-C47F843D31CF
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
  actual=IND-000017
  evidence=Industry ID='IND-000017'
  ↓
primary_id_pattern
  PASS
  actual=IND-000017
  evidence=pattern ^IND- vs 'IND-000017'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2014; retrieved_date=2026-08-13T01:08:00+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260813-E95C7C; document=DOC-E96B9B477
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2014; retrieved_date=2026-08-13T01:08:00+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260813-E95C7C; document=DOC-E96B9B477
  ↓
completeness_primary
  PASS
  actual=IND-000017
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000017
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000017
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000017
```

## Candidate `CAND-236285DF4A3F`

```text
Candidate CAND-236285DF4A3F
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
  actual=IND-000015
  evidence=Industry ID='IND-000015'
  ↓
primary_id_pattern
  PASS
  actual=IND-000015
  evidence=pattern ^IND- vs 'IND-000015'
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
  evidence=provenance: source=SRC-000004; published_date=; retrieved_date=2026-08-13T01:07:42+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260813-E95C7C; document=DOC-9C3FE7A510A0; e
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-000004; published_date=; retrieved_date=2026-08-13T01:07:42+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260813-E95C7C; document=DOC-9C3FE7A510A0; e
  ↓
completeness_primary
  PASS
  actual=IND-000015
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000015
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000015
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000015
```
