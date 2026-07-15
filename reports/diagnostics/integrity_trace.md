# Integrity Guard Trace

**Generated:** 2026-07-15T08:38:40+00:00

Per-candidate decision chain (evidence only).

## Candidate `CAND-C910394F4891`

```text
Candidate CAND-C910394F4891
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
  actual=SIG-000246
  evidence=Signal ID='SIG-000246'
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
  evidence=provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260715-56572E; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-OPENALEX; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000246
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000246
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000246
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000246
```

## Candidate `CAND-61DAF7743C34`

```text
Candidate CAND-61DAF7743C34
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
  actual=SIG-000245
  evidence=Signal ID='SIG-000245'
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
  evidence=provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260715-56572E; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-CROSSREF; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000245
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000245
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000245
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000245
```

## Candidate `CAND-CC090052C882`

```text
Candidate CAND-CC090052C882
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
  actual=SIG-000248
  evidence=Signal ID='SIG-000248'
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
  evidence=provenance: source=SRC-000001; document=DOC-27A2235900BA; mission=MIS-20260715-56572E; discovery_provider=DISC-TAVILY; append_only=true; extraction=grounded_text source_ids=SRC-000001; urls=https://au
  ↓
completeness_primary
  PASS
  actual=SIG-000248
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000248
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000248
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000248
```

## Candidate `CAND-A14DAF94C302`

```text
Candidate CAND-A14DAF94C302
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
  actual=SIG-000249
  evidence=Signal ID='SIG-000249'
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
  evidence=provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260715-56572E; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-CROSSREF; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000249
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000249
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000249
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000249
```

## Candidate `CAND-41373EEF499D`

```text
Candidate CAND-41373EEF499D
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
  actual=SIG-000247
  evidence=Signal ID='SIG-000247'
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
  evidence=provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260715-56572E; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-000004; urls=https://docu
  ↓
completeness_primary
  PASS
  actual=SIG-000247
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000247
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000247
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000247
```
