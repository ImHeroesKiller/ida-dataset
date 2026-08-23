# Candidate Root Cause

**Generated:** 2026-08-23T17:40:41+00:00
**Session:** `SESSION-20260823-1D1020`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001147`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260823-1D1020`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001147': 1, 'duplicate_id:SIG-001149': 1, 'duplicate_id:SIG-001148': 1, 'duplicate_id:SIG-001146': 1, 'duplicate_id:SIG-001150': 1}`
- `candidate CAND-8E46FD5D5E16 entity_id=SIG-001147 reason=duplicate_id:SIG-001147 conf=0.9`
- `candidate CAND-C75F1793E67C entity_id=SIG-001149 reason=duplicate_id:SIG-001149 conf=0.9`
- `candidate CAND-527E3D09BEFA entity_id=SIG-001148 reason=duplicate_id:SIG-001148 conf=0.9`
- `candidate CAND-8501B28CE086 entity_id=SIG-001146 reason=duplicate_id:SIG-001146 conf=0.92`
- `candidate CAND-A5D0161F4817 entity_id=SIG-001150 reason=duplicate_id:SIG-001150 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-8E46FD5D5E16 | business_signal_library | 0.9 | False | duplicate_id:SIG-001147 | Rejected |
| CAND-C75F1793E67C | business_signal_library | 0.9 | False | duplicate_id:SIG-001149 | Rejected |
| CAND-527E3D09BEFA | business_signal_library | 0.9 | False | duplicate_id:SIG-001148 | Rejected |
| CAND-8501B28CE086 | business_signal_library | 0.92 | False | duplicate_id:SIG-001146 | Rejected |
| CAND-A5D0161F4817 | business_signal_library | 0.9 | False | duplicate_id:SIG-001150 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001147` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
