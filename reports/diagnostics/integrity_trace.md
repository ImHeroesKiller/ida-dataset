# Integrity Guard Trace

**Generated:** 2026-07-13T19:06:35+00:00

Per-candidate decision chain (evidence only).

## Candidate `CAND-B4BEF09F0359`

```text
Candidate CAND-B4BEF09F0359
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
  actual=SIG-000168
  evidence=Signal ID='SIG-000168'
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
  evidence=provenance: source=SRC-000006; document=DOC-2B7A69D877EE; mission=MIS-20260713-A96542; discovery_provider=DISC-TAVILY; append_only=true; extraction=grounded_text source_ids=SRC-000006; urls=https://ww
  ↓
completeness_primary
  PASS
  actual=SIG-000168
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000168
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000168
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000168
```

## Candidate `CAND-A6284C9FE7DD`

```text
Candidate CAND-A6284C9FE7DD
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
  actual=SIG-000165
  evidence=Signal ID='SIG-000165'
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
  evidence=provenance: source=SRC-CROSSREF; document=DOC-5DFD7BF054D2; mission=MIS-20260713-A96542; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-CROSSREF; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000165
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000165
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000165
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000165
```

## Candidate `CAND-422D3FE54EE2`

```text
Candidate CAND-422D3FE54EE2
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
  actual=SIG-000166
  evidence=Signal ID='SIG-000166'
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
  evidence=provenance: source=SRC-000004; document=DOC-A99E56C64737; mission=MIS-20260713-A96542; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-000004; urls=https://docu
  ↓
completeness_primary
  PASS
  actual=SIG-000166
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000166
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000166
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000166
```

## Candidate `CAND-31E135690274`

```text
Candidate CAND-31E135690274
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
  actual=SIG-000167
  evidence=Signal ID='SIG-000167'
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
  evidence=provenance: source=SRC-OPENALEX; document=DOC-7C7239075702; mission=MIS-20260713-A96542; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-OPENALEX; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000167
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000167
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000167
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000167
```

## Candidate `CAND-57F278088148`

```text
Candidate CAND-57F278088148
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
  actual=SIG-000169
  evidence=Signal ID='SIG-000169'
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
  evidence=provenance: source=SRC-CROSSREF; document=DOC-50B3F3BC8DEB; mission=MIS-20260713-A96542; discovery_provider=connector; append_only=true; extraction=grounded_text source_ids=SRC-CROSSREF; urls=https://
  ↓
completeness_primary
  PASS
  actual=SIG-000169
  evidence=primary id completeness
  ↓
integrity_final_validate_row
  FAIL
  actual=duplicate_id:SIG-000169
  evidence=automation.quality.integrity_guard.validate_row → duplicate_id:SIG-000169
  ↓
Publisher decision: Rejected
  reason=integrity_guard:duplicate_id:SIG-000169
```
