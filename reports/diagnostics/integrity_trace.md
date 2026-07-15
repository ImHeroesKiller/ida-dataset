# Integrity Guard Trace

**Generated:** 2026-07-15T05:56:25+00:00

Per-candidate decision chain (evidence only).

## Candidate `CAND-ED2E6F2683D9`

```text
Candidate CAND-ED2E6F2683D9
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
  actual=SIG-000241
  evidence=Signal ID='SIG-000241'
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
  evidence=provenance: source=SRC-OPENALEX; document=DOC-C8336B1CF486; mission=MIS-20260715-EF13DC; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-OPENALEX; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000241
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000241
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000241
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000241
```

## Candidate `CAND-5E0BC5BBDE48`

```text
Candidate CAND-5E0BC5BBDE48
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
  actual=SIG-000240
  evidence=Signal ID='SIG-000240'
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
  evidence=provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260715-EF13DC; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-CROSSREF; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000240
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000240
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000240
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000240
```

## Candidate `CAND-F0E234340EAA`

```text
Candidate CAND-F0E234340EAA
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
  actual=SIG-000242
  evidence=Signal ID='SIG-000242'
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
  evidence=provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260715-EF13DC; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-000004; urls=https://docu
  ↓
completeness_primary
  PASS
  actual=SIG-000242
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000242
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000242
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000242
```

## Candidate `CAND-E4D897A4A916`

```text
Candidate CAND-E4D897A4A916
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
  actual=SIG-000243
  evidence=Signal ID='SIG-000243'
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
  evidence=provenance: source=SRC-000001; document=DOC-E689A7156EBC; mission=MIS-20260715-EF13DC; discovery_provider=DISC-TAVILY; append_only=true; extraction=grounded_text source_ids=SRC-000001; urls=https://au
  ↓
completeness_primary
  PASS
  actual=SIG-000243
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000243
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000243
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000243
```

## Candidate `CAND-821AE26795AA`

```text
Candidate CAND-821AE26795AA
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
  actual=SIG-000244
  evidence=Signal ID='SIG-000244'
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
  evidence=provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260715-EF13DC; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-CROSSREF; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000244
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000244
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000244
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000244
```
