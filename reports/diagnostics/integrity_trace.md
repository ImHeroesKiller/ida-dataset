# Integrity Guard Trace

**Generated:** 2026-07-21T17:42:05+00:00

Per-candidate decision chain (evidence only).

## Candidate `CAND-51E383BC1A5B`

```text
Candidate CAND-51E383BC1A5B
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
  actual=SIG-000638
  evidence=Signal ID='SIG-000638'
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
  evidence=provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260721-14399C; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-CROSSREF; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000638
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000638
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000638
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000638
```

## Candidate `CAND-60B943872A97`

```text
Candidate CAND-60B943872A97
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
  actual=SIG-000636
  evidence=Signal ID='SIG-000636'
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
  evidence=provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260721-14399C; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-000004; urls=https://docu
  ↓
completeness_primary
  PASS
  actual=SIG-000636
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000636
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000636
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000636
```

## Candidate `CAND-3E1D825DF7D0`

```text
Candidate CAND-3E1D825DF7D0
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
  actual=SIG-000639
  evidence=Signal ID='SIG-000639'
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
  evidence=provenance: source=SRC-000004; document=DOC-D5443F5620D9; mission=MIS-20260721-14399C; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-000004; urls=http://docum
  ↓
completeness_primary
  PASS
  actual=SIG-000639
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000639
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000639
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000639
```

## Candidate `CAND-F7602E0B9057`

```text
Candidate CAND-F7602E0B9057
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
  actual=SIG-000635
  evidence=Signal ID='SIG-000635'
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
  evidence=provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260721-14399C; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-CROSSREF; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000635
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000635
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000635
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000635
```

## Candidate `CAND-9B7A5193E409`

```text
Candidate CAND-9B7A5193E409
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
  actual=SIG-000637
  evidence=Signal ID='SIG-000637'
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
  evidence=provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260721-14399C; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-OPENALEX; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000637
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000637
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000637
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000637
```
