# Candidate Root Cause

**Generated:** 2026-07-20T22:19:43+00:00
**Session:** `SESSION-20260720-AB8670`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000593`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260720-AB8670`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000593': 1, 'duplicate_id:SIG-000591': 1, 'duplicate_id:SIG-000592': 1, 'duplicate_id:SIG-000590': 1, 'duplicate_id:SIG-000594': 1}`
- `candidate CAND-AF1AEB685C3E entity_id=SIG-000593 reason=duplicate_id:SIG-000593 conf=0.92`
- `candidate CAND-558E0CECD07B entity_id=SIG-000591 reason=duplicate_id:SIG-000591 conf=0.92`
- `candidate CAND-9621CD684E8A entity_id=SIG-000592 reason=duplicate_id:SIG-000592 conf=0.9`
- `candidate CAND-688028FB7544 entity_id=SIG-000590 reason=duplicate_id:SIG-000590 conf=0.9`
- `candidate CAND-FF309FD27CB4 entity_id=SIG-000594 reason=duplicate_id:SIG-000594 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-AF1AEB685C3E | business_signal_library | 0.92 | False | duplicate_id:SIG-000593 | Rejected |
| CAND-558E0CECD07B | business_signal_library | 0.92 | False | duplicate_id:SIG-000591 | Rejected |
| CAND-9621CD684E8A | business_signal_library | 0.9 | False | duplicate_id:SIG-000592 | Rejected |
| CAND-688028FB7544 | business_signal_library | 0.9 | False | duplicate_id:SIG-000590 | Rejected |
| CAND-FF309FD27CB4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000594 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000593` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
