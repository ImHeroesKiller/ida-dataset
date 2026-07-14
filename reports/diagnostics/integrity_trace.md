# Integrity Guard Trace

**Generated:** 2026-07-14T05:54:46+00:00

Per-candidate decision chain (evidence only).

## Candidate `CAND-86B273EBAE9C`

```text
Candidate CAND-86B273EBAE9C
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
  actual=SIG-000186
  evidence=Signal ID='SIG-000186'
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
  evidence=provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260714-E9DA36; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-OPENALEX; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000186
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000186
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000186
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000186
```

## Candidate `CAND-4CFAB16F2AD4`

```text
Candidate CAND-4CFAB16F2AD4
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
  actual=SIG-000185
  evidence=Signal ID='SIG-000185'
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
  evidence=provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260714-E9DA36; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-CROSSREF; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000185
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000185
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000185
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000185
```

## Candidate `CAND-E6CDA3484A99`

```text
Candidate CAND-E6CDA3484A99
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
  actual=SIG-000188
  evidence=Signal ID='SIG-000188'
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
  actual=0.85 threshold=0.8
  evidence=threshold=0.8; conf=0.85
  ↓
confidence_present
  PASS
  actual=0.85
  evidence=integrity only fails when conf is present and < 0.80
  ↓
provenance_present
  PASS
  actual=present
  evidence=provenance: source=SRC-000006; document=DOC-8E65A51B4E13; mission=MIS-20260714-E9DA36; discovery_provider=DISC-TAVILY; append_only=true; extraction=grounded_text source_ids=SRC-000006; urls=https://ww
  ↓
completeness_primary
  PASS
  actual=SIG-000188
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000188
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000188
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000188
```

## Candidate `CAND-03366690A3AA`

```text
Candidate CAND-03366690A3AA
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
  actual=SIG-000187
  evidence=Signal ID='SIG-000187'
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
  evidence=provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260714-E9DA36; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-000004; urls=https://docu
  ↓
completeness_primary
  PASS
  actual=SIG-000187
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000187
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000187
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000187
```

## Candidate `CAND-78B3E8ED13A7`

```text
Candidate CAND-78B3E8ED13A7
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
  actual=SIG-000189
  evidence=Signal ID='SIG-000189'
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
  evidence=provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260714-E9DA36; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-CROSSREF; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000189
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000189
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000189
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000189
```
