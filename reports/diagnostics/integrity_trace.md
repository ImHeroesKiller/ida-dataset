# Integrity Guard Trace

**Generated:** 2026-08-16T18:45:37+00:00

Per-candidate decision chain (evidence only).

## Candidate `CAND-5BB36E9B897A`

```text
Candidate CAND-5BB36E9B897A
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
  actual=SIG-000365
  evidence=Signal ID='SIG-000365'
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
  evidence=provenance: source=SRC-CROSSREF; document=DOC-23B61DA3B184; mission=MIS-20260816-953669; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-CROSSREF; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000365
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000365
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000365
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000365
```

## Candidate `CAND-D383A5022E66`

```text
Candidate CAND-D383A5022E66
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
  actual=SIG-000362
  evidence=Signal ID='SIG-000362'
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
  evidence=provenance: source=SRC-CROSSREF; document=DOC-9CF2639B264C; mission=MIS-20260816-953669; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-CROSSREF; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000362
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000362
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000362
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000362
```

## Candidate `CAND-F9DBF09376D3`

```text
Candidate CAND-F9DBF09376D3
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
  actual=SIG-000363
  evidence=Signal ID='SIG-000363'
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
  evidence=provenance: source=SRC-CROSSREF; document=DOC-AFB055C754E2; mission=MIS-20260816-953669; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-CROSSREF; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000363
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000363
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000363
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000363
```

## Candidate `CAND-29910E5FDBDF`

```text
Candidate CAND-29910E5FDBDF
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
  actual=SIG-000364
  evidence=Signal ID='SIG-000364'
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
  evidence=provenance: source=SRC-CROSSREF; document=DOC-8DEAD915EF6F; mission=MIS-20260816-953669; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-CROSSREF; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000364
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000364
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000364
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000364
```

## Candidate `CAND-228F9051A01C`

```text
Candidate CAND-228F9051A01C
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
  actual=SIG-000361
  evidence=Signal ID='SIG-000361'
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
  evidence=provenance: source=SRC-000004; document=DOC-9C3FE7A510A0; mission=MIS-20260816-953669; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-000004; urls=https://docu
  ↓
completeness_primary
  PASS
  actual=SIG-000361
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000361
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000361
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000361
```
