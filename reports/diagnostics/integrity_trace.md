# Integrity Guard Trace

**Generated:** 2026-08-13T00:38:59+00:00

Per-candidate decision chain (evidence only).

## Candidate `CAND-FD9FB8F20088`

```text
Candidate CAND-FD9FB8F20088
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
  actual=IND-000011
  evidence=Industry ID='IND-000011'
  ↓
primary_id_pattern
  PASS
  actual=IND-000011
  evidence=pattern ^IND- vs 'IND-000011'
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
  evidence=provenance: source=SRC-000004; published_date=2018-11-01T00:00:00Z; retrieved_date=2026-08-13T00:02:00+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-000004; published_date=2018-11-01T00:00:00Z; retrieved_date=2026-08-13T00:02:00+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document
  ↓
completeness_primary
  PASS
  actual=IND-000011
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000011
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000011
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000011
```

## Candidate `CAND-4D31A7BF92F6`

```text
Candidate CAND-4D31A7BF92F6
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
  actual=IND-000008
  evidence=Industry ID='IND-000008'
  ↓
primary_id_pattern
  PASS
  actual=IND-000008
  evidence=pattern ^IND- vs 'IND-000008'
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
  evidence=provenance: source=SRC-000004; published_date=1997-02-20T00:00:00Z; retrieved_date=2026-08-12T23:58:16+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-000004; published_date=1997-02-20T00:00:00Z; retrieved_date=2026-08-12T23:58:16+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document
  ↓
completeness_primary
  PASS
  actual=IND-000008
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000008
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000008
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000008
```

## Candidate `CAND-E1882A3C114F`

```text
Candidate CAND-E1882A3C114F
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
  actual=IND-000002
  evidence=Industry ID='IND-000002'
  ↓
primary_id_pattern
  PASS
  actual=IND-000002
  evidence=pattern ^IND- vs 'IND-000002'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T23:58:04+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-738AC7BFF
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T23:58:04+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-738AC7BFF
  ↓
completeness_primary
  PASS
  actual=IND-000002
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000002
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000002
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000002
```

## Candidate `CAND-4AF10225EB6B`

```text
Candidate CAND-4AF10225EB6B
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
  actual=IND-000006
  evidence=Industry ID='IND-000006'
  ↓
primary_id_pattern
  PASS
  actual=IND-000006
  evidence=pattern ^IND- vs 'IND-000006'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-206B13589
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-206B13589
  ↓
completeness_primary
  PASS
  actual=IND-000006
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000006
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000006
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000006
```

## Candidate `CAND-6ADD53D8E489`

```text
Candidate CAND-6ADD53D8E489
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
  actual=IND-000010
  evidence=Industry ID='IND-000010'
  ↓
primary_id_pattern
  PASS
  actual=IND-000010
  evidence=pattern ^IND- vs 'IND-000010'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-12T23:58:42+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-E05725A2B
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-12T23:58:42+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-E05725A2B
  ↓
completeness_primary
  PASS
  actual=IND-000010
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000010
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000010
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000010
```

## Candidate `CAND-AB49E874BE64`

```text
Candidate CAND-AB49E874BE64
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
  actual=IND-000012
  evidence=Industry ID='IND-000012'
  ↓
primary_id_pattern
  PASS
  actual=IND-000012
  evidence=pattern ^IND- vs 'IND-000012'
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
  evidence=provenance: source=SRC-000004; published_date=2017-06-01T00:00:00Z; retrieved_date=2026-08-13T00:02:44+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-000004; published_date=2017-06-01T00:00:00Z; retrieved_date=2026-08-13T00:02:44+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document
  ↓
completeness_primary
  PASS
  actual=IND-000012
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000012
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000012
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000012
```

## Candidate `CAND-BA8A78824279`

```text
Candidate CAND-BA8A78824279
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
  actual=IND-000005
  evidence=Industry ID='IND-000005'
  ↓
primary_id_pattern
  PASS
  actual=IND-000005
  evidence=pattern ^IND- vs 'IND-000005'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T23:58:04+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-738AC7BFF
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T23:58:04+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-738AC7BFF
  ↓
completeness_primary
  PASS
  actual=IND-000005
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000005
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000005
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000005
```

## Candidate `CAND-61FC37838342`

```text
Candidate CAND-61FC37838342
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
  actual=IND-000011
  evidence=Industry ID='IND-000011'
  ↓
primary_id_pattern
  PASS
  actual=IND-000011
  evidence=pattern ^IND- vs 'IND-000011'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2024; retrieved_date=2026-08-13T00:01:53+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-59B8A447D
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2024; retrieved_date=2026-08-13T00:01:53+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-59B8A447D
  ↓
completeness_primary
  PASS
  actual=IND-000011
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000011
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000011
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000011
```

## Candidate `CAND-7DDE5E598B3B`

```text
Candidate CAND-7DDE5E598B3B
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
  actual=IND-000010
  evidence=Industry ID='IND-000010'
  ↓
primary_id_pattern
  PASS
  actual=IND-000010
  evidence=pattern ^IND- vs 'IND-000010'
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
  evidence=provenance: source=SRC-000004; published_date=1988-07-01T00:00:00Z; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-000004; published_date=1988-07-01T00:00:00Z; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document
  ↓
completeness_primary
  PASS
  actual=IND-000010
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000010
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000010
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000010
```

## Candidate `CAND-198A3C192524`

```text
Candidate CAND-198A3C192524
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
  actual=IND-000014
  evidence=Industry ID='IND-000014'
  ↓
primary_id_pattern
  PASS
  actual=IND-000014
  evidence=pattern ^IND- vs 'IND-000014'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2021; retrieved_date=2026-08-13T00:02:44+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-E6234DE5D
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2021; retrieved_date=2026-08-13T00:02:44+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-E6234DE5D
  ↓
completeness_primary
  PASS
  actual=IND-000014
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000014
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000014
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000014
```

## Candidate `CAND-64F739498BDB`

```text
Candidate CAND-64F739498BDB
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
  actual=IND-000007
  evidence=Industry ID='IND-000007'
  ↓
primary_id_pattern
  PASS
  actual=IND-000007
  evidence=pattern ^IND- vs 'IND-000007'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-12T23:58:42+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-E05725A2B
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-12T23:58:42+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-E05725A2B
  ↓
completeness_primary
  PASS
  actual=IND-000007
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000007
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000007
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000007
```

## Candidate `CAND-14C0396A9DC4`

```text
Candidate CAND-14C0396A9DC4
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
  actual=IND-000005
  evidence=Industry ID='IND-000005'
  ↓
primary_id_pattern
  PASS
  actual=IND-000005
  evidence=pattern ^IND- vs 'IND-000005'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-206B13589
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-206B13589
  ↓
completeness_primary
  PASS
  actual=IND-000005
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000005
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000005
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000005
```

## Candidate `CAND-8E0287DD32BE`

```text
Candidate CAND-8E0287DD32BE
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
  actual=IND-000006
  evidence=Industry ID='IND-000006'
  ↓
primary_id_pattern
  PASS
  actual=IND-000006
  evidence=pattern ^IND- vs 'IND-000006'
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
  actual=0.87 threshold=0.8
  evidence=threshold=0.8; conf=0.87
  ↓
confidence_present
  PASS
  actual=0.87
  evidence=integrity only fails when conf is present and < 0.80
  ↓
provenance_required
  PASS
  actual=ok
  evidence=provenance: source=SRC-000004; published_date=1997-02-20T00:00:00Z; retrieved_date=2026-08-12T23:58:16+00:00; confidence=0.87; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-000004; published_date=1997-02-20T00:00:00Z; retrieved_date=2026-08-12T23:58:16+00:00; confidence=0.87; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document
  ↓
completeness_primary
  PASS
  actual=IND-000006
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000006
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000006
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000006
```

## Candidate `CAND-AB5E38F39855`

```text
Candidate CAND-AB5E38F39855
  ↓
dataset_csv_exists
  PASS
  actual=business_signal_library.csv
  evidence=CSV present
  ↓
payload_present
  PASS
  evidence=payload fields=14
  ↓
schema_indexed_dataset
  PASS
  actual=Signal ID
  evidence=ID field mapped: Signal ID
  ↓
primary_id_present
  PASS
  actual=SIG-000015
  evidence=Signal ID='SIG-000015'
  ↓
duplicate_id_in_batch
  PASS
  actual=unique_in_batch
  evidence=batch_ids_contains=False
  ↓
duplicate_id_existing_dataset
  PASS
  actual=new_id
  evidence=existing_csv_contains=False; dataset_path=business_signal_library.csv
  ↓
confidence_threshold
  PASS
  actual=0.9 threshold=0.8
  evidence=threshold=0.8; conf=0.9
  ↓
confidence_present
  PASS
  actual=0.9
  evidence=integrity only fails when conf is present and < 0.80
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; document=DOC-030B58207BDD; mission=MIS-20260710-8E1602; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-CROSSREF; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000015
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  PASS
  actual=ok
  evidence=automation.quality.integrity_guard.validate_row → ok
  ↓
Publisher decision: Queued
  reason=publish_status=unknown
```

## Candidate `CAND-C0DEF0FB996B`

```text
Candidate CAND-C0DEF0FB996B
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
  actual=IND-000008
  evidence=Industry ID='IND-000008'
  ↓
primary_id_pattern
  PASS
  actual=IND-000008
  evidence=pattern ^IND- vs 'IND-000008'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-12T23:58:42+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-E05725A2B
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-12T23:58:42+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-E05725A2B
  ↓
completeness_primary
  PASS
  actual=IND-000008
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000008
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000008
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000008
```

## Candidate `CAND-95C824E2F514`

```text
Candidate CAND-95C824E2F514
  ↓
dataset_csv_exists
  PASS
  actual=business_signal_library.csv
  evidence=CSV present
  ↓
payload_present
  PASS
  evidence=payload fields=14
  ↓
schema_indexed_dataset
  PASS
  actual=Signal ID
  evidence=ID field mapped: Signal ID
  ↓
primary_id_present
  PASS
  actual=SIG-000013
  evidence=Signal ID='SIG-000013'
  ↓
duplicate_id_in_batch
  PASS
  actual=unique_in_batch
  evidence=batch_ids_contains=False
  ↓
duplicate_id_existing_dataset
  PASS
  actual=new_id
  evidence=existing_csv_contains=False; dataset_path=business_signal_library.csv
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
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-000004; document=DOC-1C7ABF5820D1; mission=MIS-20260710-8E1602; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-000004; urls=https://docu
  ↓
completeness_primary
  PASS
  actual=SIG-000013
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  PASS
  actual=ok
  evidence=automation.quality.integrity_guard.validate_row → ok
  ↓
Publisher decision: Queued
  reason=publish_status=unknown
```

## Candidate `CAND-7528E4183942`

```text
Candidate CAND-7528E4183942
  ↓
dataset_csv_exists
  PASS
  actual=business_signal_library.csv
  evidence=CSV present
  ↓
payload_present
  PASS
  evidence=payload fields=14
  ↓
schema_indexed_dataset
  PASS
  actual=Signal ID
  evidence=ID field mapped: Signal ID
  ↓
primary_id_present
  PASS
  actual=SIG-000025
  evidence=Signal ID='SIG-000025'
  ↓
duplicate_id_in_batch
  PASS
  actual=unique_in_batch
  evidence=batch_ids_contains=False
  ↓
duplicate_id_existing_dataset
  PASS
  actual=new_id
  evidence=existing_csv_contains=False; dataset_path=business_signal_library.csv
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
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-000004; document=DOC-1C7ABF5820D1; mission=MIS-20260711-1B1B1E; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-000004; urls=https://docu
  ↓
completeness_primary
  PASS
  actual=SIG-000025
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  PASS
  actual=ok
  evidence=automation.quality.integrity_guard.validate_row → ok
  ↓
Publisher decision: Queued
  reason=publish_status=unknown
```

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
  PASS
  actual=ok
  evidence=automation.quality.integrity_guard.validate_row → ok
  ↓
Publisher decision: Queued
  reason=publish_status=unknown
```

## Candidate `CAND-6ACEF72974C4`

```text
Candidate CAND-6ACEF72974C4
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
  actual=IND-000009
  evidence=Industry ID='IND-000009'
  ↓
primary_id_pattern
  PASS
  actual=IND-000009
  evidence=pattern ^IND- vs 'IND-000009'
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
  actual=0.87 threshold=0.8
  evidence=threshold=0.8; conf=0.87
  ↓
confidence_present
  PASS
  actual=0.87
  evidence=integrity only fails when conf is present and < 0.80
  ↓
provenance_required
  PASS
  actual=ok
  evidence=provenance: source=SRC-000004; published_date=1997-02-20T00:00:00Z; retrieved_date=2026-08-12T23:58:16+00:00; confidence=0.87; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-000004; published_date=1997-02-20T00:00:00Z; retrieved_date=2026-08-12T23:58:16+00:00; confidence=0.87; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document
  ↓
completeness_primary
  PASS
  actual=IND-000009
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000009
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000009
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000009
```

## Candidate `CAND-59B49A1A8F1F`

```text
Candidate CAND-59B49A1A8F1F
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
  actual=IND-000007
  evidence=Industry ID='IND-000007'
  ↓
primary_id_pattern
  PASS
  actual=IND-000007
  evidence=pattern ^IND- vs 'IND-000007'
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
  actual=0.87 threshold=0.8
  evidence=threshold=0.8; conf=0.87
  ↓
confidence_present
  PASS
  actual=0.87
  evidence=integrity only fails when conf is present and < 0.80
  ↓
provenance_required
  PASS
  actual=ok
  evidence=provenance: source=SRC-000004; published_date=1997-02-20T00:00:00Z; retrieved_date=2026-08-12T23:58:16+00:00; confidence=0.87; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-000004; published_date=1997-02-20T00:00:00Z; retrieved_date=2026-08-12T23:58:16+00:00; confidence=0.87; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document
  ↓
completeness_primary
  PASS
  actual=IND-000007
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000007
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000007
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000007
```

## Candidate `CAND-8B66153B6B79`

```text
Candidate CAND-8B66153B6B79
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
  actual=IND-000013
  evidence=Industry ID='IND-000013'
  ↓
primary_id_pattern
  PASS
  actual=IND-000013
  evidence=pattern ^IND- vs 'IND-000013'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-13T00:02:01+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-F517B9126
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-13T00:02:01+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-F517B9126
  ↓
completeness_primary
  PASS
  actual=IND-000013
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000013
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000013
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000013
```

## Candidate `CAND-EFE423B30DA3`

```text
Candidate CAND-EFE423B30DA3
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
  actual=IND-000004
  evidence=Industry ID='IND-000004'
  ↓
primary_id_pattern
  PASS
  actual=IND-000004
  evidence=pattern ^IND- vs 'IND-000004'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T23:58:04+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-738AC7BFF
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T23:58:04+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-738AC7BFF
  ↓
completeness_primary
  PASS
  actual=IND-000004
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000004
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000004
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000004
```

## Candidate `CAND-94B9A207CDEE`

```text
Candidate CAND-94B9A207CDEE
  ↓
dataset_csv_exists
  PASS
  actual=business_signal_library.csv
  evidence=CSV present
  ↓
payload_present
  PASS
  evidence=payload fields=14
  ↓
schema_indexed_dataset
  PASS
  actual=Signal ID
  evidence=ID field mapped: Signal ID
  ↓
primary_id_present
  PASS
  actual=SIG-000014
  evidence=Signal ID='SIG-000014'
  ↓
duplicate_id_in_batch
  PASS
  actual=unique_in_batch
  evidence=batch_ids_contains=False
  ↓
duplicate_id_existing_dataset
  PASS
  actual=new_id
  evidence=existing_csv_contains=False; dataset_path=business_signal_library.csv
  ↓
confidence_threshold
  PASS
  actual=0.88 threshold=0.8
  evidence=threshold=0.8; conf=0.88
  ↓
confidence_present
  PASS
  actual=0.88
  evidence=integrity only fails when conf is present and < 0.80
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-OPENALEX; document=DOC-BC12979C0BEE; mission=MIS-20260710-8E1602; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-OPENALEX; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000014
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  PASS
  actual=ok
  evidence=automation.quality.integrity_guard.validate_row → ok
  ↓
Publisher decision: Queued
  reason=publish_status=unknown
```

## Candidate `CAND-D03DE2F0A439`

```text
Candidate CAND-D03DE2F0A439
  ↓
dataset_csv_exists
  PASS
  actual=business_signal_library.csv
  evidence=CSV present
  ↓
payload_present
  PASS
  evidence=payload fields=14
  ↓
schema_indexed_dataset
  PASS
  actual=Signal ID
  evidence=ID field mapped: Signal ID
  ↓
primary_id_present
  PASS
  actual=SIG-000027
  evidence=Signal ID='SIG-000027'
  ↓
duplicate_id_in_batch
  PASS
  actual=unique_in_batch
  evidence=batch_ids_contains=False
  ↓
duplicate_id_existing_dataset
  PASS
  actual=new_id
  evidence=existing_csv_contains=False; dataset_path=business_signal_library.csv
  ↓
confidence_threshold
  PASS
  actual=0.9 threshold=0.8
  evidence=threshold=0.8; conf=0.9
  ↓
confidence_present
  PASS
  actual=0.9
  evidence=integrity only fails when conf is present and < 0.80
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; document=DOC-030B58207BDD; mission=MIS-20260711-1B1B1E; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-CROSSREF; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000027
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  PASS
  actual=ok
  evidence=automation.quality.integrity_guard.validate_row → ok
  ↓
Publisher decision: Queued
  reason=publish_status=unknown
```

## Candidate `CAND-A794C3DE0ED1`

```text
Candidate CAND-A794C3DE0ED1
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
  actual=IND-000002
  evidence=Industry ID='IND-000002'
  ↓
primary_id_pattern
  PASS
  actual=IND-000002
  evidence=pattern ^IND- vs 'IND-000002'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-206B13589
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-206B13589
  ↓
completeness_primary
  PASS
  actual=IND-000002
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000002
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000002
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000002
```

## Candidate `CAND-924C6F41A07B`

```text
Candidate CAND-924C6F41A07B
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
  actual=IND-000004
  evidence=Industry ID='IND-000004'
  ↓
primary_id_pattern
  PASS
  actual=IND-000004
  evidence=pattern ^IND- vs 'IND-000004'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-206B13589
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-206B13589
  ↓
completeness_primary
  PASS
  actual=IND-000004
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000004
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000004
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000004
```

## Candidate `CAND-29E5FA722096`

```text
Candidate CAND-29E5FA722096
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
  actual=IND-000003
  evidence=Industry ID='IND-000003'
  ↓
primary_id_pattern
  PASS
  actual=IND-000003
  evidence=pattern ^IND- vs 'IND-000003'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T23:58:04+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-738AC7BFF
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T23:58:04+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-738AC7BFF
  ↓
completeness_primary
  PASS
  actual=IND-000003
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000003
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000003
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000003
```

## Candidate `CAND-4D7BD598AB16`

```text
Candidate CAND-4D7BD598AB16
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
  actual=IND-000001
  evidence=Industry ID='IND-000001'
  ↓
primary_id_pattern
  PASS
  actual=IND-000001
  evidence=pattern ^IND- vs 'IND-000001'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T23:58:04+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-738AC7BFF
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2026; retrieved_date=2026-08-12T23:58:04+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-738AC7BFF
  ↓
completeness_primary
  PASS
  actual=IND-000001
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000001
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000001
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000001
```

## Candidate `CAND-21EFE6035AB9`

```text
Candidate CAND-21EFE6035AB9
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
  actual=IND-000003
  evidence=Industry ID='IND-000003'
  ↓
primary_id_pattern
  PASS
  actual=IND-000003
  evidence=pattern ^IND- vs 'IND-000003'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-206B13589
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2023; retrieved_date=2026-08-12T23:58:30+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-206B13589
  ↓
completeness_primary
  PASS
  actual=IND-000003
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000003
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000003
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000003
```

## Candidate `CAND-9DFB1CD280F2`

```text
Candidate CAND-9DFB1CD280F2
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
  actual=IND-000001
  evidence=Industry ID='IND-000001'
  ↓
primary_id_pattern
  PASS
  actual=IND-000001
  evidence=pattern ^IND- vs 'IND-000001'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2022; retrieved_date=2026-08-12T23:58:16+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-ACDDB05BD
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2022; retrieved_date=2026-08-12T23:58:16+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-ACDDB05BD
  ↓
completeness_primary
  PASS
  actual=IND-000001
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000001
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000001
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000001
```

## Candidate `CAND-933FD0411EAD`

```text
Candidate CAND-933FD0411EAD
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
  actual=IND-000009
  evidence=Industry ID='IND-000009'
  ↓
primary_id_pattern
  PASS
  actual=IND-000009
  evidence=pattern ^IND- vs 'IND-000009'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-12T23:58:42+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-E05725A2B
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-12T23:58:42+00:00; confidence=0.85; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-E05725A2B
  ↓
completeness_primary
  PASS
  actual=IND-000009
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000009
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000009
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000009
```

## Candidate `CAND-F04B1DEAECD0`

```text
Candidate CAND-F04B1DEAECD0
  ↓
dataset_csv_exists
  PASS
  actual=business_signal_library.csv
  evidence=CSV present
  ↓
payload_present
  PASS
  evidence=payload fields=14
  ↓
schema_indexed_dataset
  PASS
  actual=Signal ID
  evidence=ID field mapped: Signal ID
  ↓
primary_id_present
  PASS
  actual=SIG-000026
  evidence=Signal ID='SIG-000026'
  ↓
duplicate_id_in_batch
  PASS
  actual=unique_in_batch
  evidence=batch_ids_contains=False
  ↓
duplicate_id_existing_dataset
  PASS
  actual=new_id
  evidence=existing_csv_contains=False; dataset_path=business_signal_library.csv
  ↓
confidence_threshold
  PASS
  actual=0.88 threshold=0.8
  evidence=threshold=0.8; conf=0.88
  ↓
confidence_present
  PASS
  actual=0.88
  evidence=integrity only fails when conf is present and < 0.80
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-OPENALEX; document=DOC-BC12979C0BEE; mission=MIS-20260711-1B1B1E; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-OPENALEX; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000026
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  PASS
  actual=ok
  evidence=automation.quality.integrity_guard.validate_row → ok
  ↓
Publisher decision: Queued
  reason=publish_status=unknown
```

## Candidate `CAND-6A30FDEFF5EF`

```text
Candidate CAND-6A30FDEFF5EF
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
  actual=IND-000012
  evidence=Industry ID='IND-000012'
  ↓
primary_id_pattern
  PASS
  actual=IND-000012
  evidence=pattern ^IND- vs 'IND-000012'
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
  evidence=provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-13T00:02:01+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-F517B9126
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-CROSSREF; published_date=2025; retrieved_date=2026-08-13T00:02:01+00:00; confidence=0.92; version=acquisition-grounded-2.0.0; mission=MIS-20260812-BB1FF2; document=DOC-F517B9126
  ↓
completeness_primary
  PASS
  actual=IND-000012
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:IND-000012
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:IND-000012
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:IND-000012
```
