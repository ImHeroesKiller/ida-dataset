# Integrity Guard Trace

**Generated:** 2026-08-17T11:42:05+00:00

Per-candidate decision chain (evidence only).

## Candidate `CAND-6C16C3789B2E`

```text
Candidate CAND-6C16C3789B2E
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
  actual=SIG-000439
  evidence=Signal ID='SIG-000439'
  ↓
duplicate_id_in_batch
  PASS
  actual=unique_in_batch
  evidence=batch_ids_contains=False
  ↓
duplicate_id_existing_dataset
  FAIL
  actual=exists_in_csv
  evidence=existing_csv_contains=True; dataset_path=business_signal_library.csv
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
  evidence=provenance: source=SRC-CROSSREF; document=DOC-8DEAD915EF6F; mission=MIS-20260817-4F5AFB; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-CROSSREF; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000439
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000439
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000439
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000439
```

## Candidate `CAND-72A4D9CCBCF7`

```text
Candidate CAND-72A4D9CCBCF7
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
  actual=SIG-000436
  evidence=Signal ID='SIG-000436'
  ↓
duplicate_id_in_batch
  PASS
  actual=unique_in_batch
  evidence=batch_ids_contains=False
  ↓
duplicate_id_existing_dataset
  FAIL
  actual=exists_in_csv
  evidence=existing_csv_contains=True; dataset_path=business_signal_library.csv
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
  evidence=provenance: source=SRC-000004; document=DOC-9C3FE7A510A0; mission=MIS-20260817-4F5AFB; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-000004; urls=https://docu
  ↓
completeness_primary
  PASS
  actual=SIG-000436
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000436
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000436
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000436
```

## Candidate `CAND-8FFC01A632B7`

```text
Candidate CAND-8FFC01A632B7
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
  actual=SIG-000440
  evidence=Signal ID='SIG-000440'
  ↓
duplicate_id_in_batch
  PASS
  actual=unique_in_batch
  evidence=batch_ids_contains=False
  ↓
duplicate_id_existing_dataset
  FAIL
  actual=exists_in_csv
  evidence=existing_csv_contains=True; dataset_path=business_signal_library.csv
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
  evidence=provenance: source=SRC-CROSSREF; document=DOC-23B61DA3B184; mission=MIS-20260817-4F5AFB; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-CROSSREF; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000440
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000440
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000440
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000440
```

## Candidate `CAND-D40B2465B054`

```text
Candidate CAND-D40B2465B054
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
  actual=SIG-000437
  evidence=Signal ID='SIG-000437'
  ↓
duplicate_id_in_batch
  PASS
  actual=unique_in_batch
  evidence=batch_ids_contains=False
  ↓
duplicate_id_existing_dataset
  FAIL
  actual=exists_in_csv
  evidence=existing_csv_contains=True; dataset_path=business_signal_library.csv
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
  evidence=provenance: source=SRC-CROSSREF; document=DOC-9CF2639B264C; mission=MIS-20260817-4F5AFB; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-CROSSREF; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000437
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000437
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000437
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000437
```

## Candidate `CAND-8183A61CB729`

```text
Candidate CAND-8183A61CB729
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
  actual=SIG-000438
  evidence=Signal ID='SIG-000438'
  ↓
duplicate_id_in_batch
  PASS
  actual=unique_in_batch
  evidence=batch_ids_contains=False
  ↓
duplicate_id_existing_dataset
  FAIL
  actual=exists_in_csv
  evidence=existing_csv_contains=True; dataset_path=business_signal_library.csv
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
  evidence=provenance: source=SRC-CROSSREF; document=DOC-AFB055C754E2; mission=MIS-20260817-4F5AFB; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-CROSSREF; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000438
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000438
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000438
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000438
```
