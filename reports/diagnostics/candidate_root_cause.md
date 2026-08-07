# Candidate Root Cause

**Generated:** 2026-08-07T13:24:53+00:00
**Session:** `SESSION-20260807-E88D04`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001514`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260807-E88D04`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001514': 1, 'duplicate_id:SIG-001510': 1, 'duplicate_id:SIG-001511': 1, 'duplicate_id:SIG-001512': 1, 'duplicate_id:SIG-001513': 1}`
- `candidate CAND-F6D2E98D074F entity_id=SIG-001514 reason=duplicate_id:SIG-001514 conf=0.92`
- `candidate CAND-488D7039FD3C entity_id=SIG-001510 reason=duplicate_id:SIG-001510 conf=0.9`
- `candidate CAND-84B06D4CBE68 entity_id=SIG-001511 reason=duplicate_id:SIG-001511 conf=0.92`
- `candidate CAND-53BCAAA920C2 entity_id=SIG-001512 reason=duplicate_id:SIG-001512 conf=0.88`
- `candidate CAND-0B3AD52B11BB entity_id=SIG-001513 reason=duplicate_id:SIG-001513 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F6D2E98D074F | business_signal_library | 0.92 | False | duplicate_id:SIG-001514 | Rejected |
| CAND-488D7039FD3C | business_signal_library | 0.9 | False | duplicate_id:SIG-001510 | Rejected |
| CAND-84B06D4CBE68 | business_signal_library | 0.92 | False | duplicate_id:SIG-001511 | Rejected |
| CAND-53BCAAA920C2 | business_signal_library | 0.88 | False | duplicate_id:SIG-001512 | Rejected |
| CAND-0B3AD52B11BB | business_signal_library | 0.9 | False | duplicate_id:SIG-001513 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001514` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
