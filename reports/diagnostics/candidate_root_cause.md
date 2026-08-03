# Candidate Root Cause

**Generated:** 2026-08-03T10:15:23+00:00
**Session:** `SESSION-20260803-05BC68`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001311`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260803-05BC68`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001311': 1, 'duplicate_id:SIG-001313': 1, 'duplicate_id:SIG-001312': 1, 'duplicate_id:SIG-001314': 1, 'duplicate_id:SIG-001310': 1}`
- `candidate CAND-EF208AC7C929 entity_id=SIG-001311 reason=duplicate_id:SIG-001311 conf=0.92`
- `candidate CAND-46FC665B8104 entity_id=SIG-001313 reason=duplicate_id:SIG-001313 conf=0.9`
- `candidate CAND-5669F501D1D0 entity_id=SIG-001312 reason=duplicate_id:SIG-001312 conf=0.88`
- `candidate CAND-C77440FF296A entity_id=SIG-001314 reason=duplicate_id:SIG-001314 conf=0.92`
- `candidate CAND-92A62C2A4D07 entity_id=SIG-001310 reason=duplicate_id:SIG-001310 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-EF208AC7C929 | business_signal_library | 0.92 | False | duplicate_id:SIG-001311 | Rejected |
| CAND-46FC665B8104 | business_signal_library | 0.9 | False | duplicate_id:SIG-001313 | Rejected |
| CAND-5669F501D1D0 | business_signal_library | 0.88 | False | duplicate_id:SIG-001312 | Rejected |
| CAND-C77440FF296A | business_signal_library | 0.92 | False | duplicate_id:SIG-001314 | Rejected |
| CAND-92A62C2A4D07 | business_signal_library | 0.9 | False | duplicate_id:SIG-001310 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001311` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
