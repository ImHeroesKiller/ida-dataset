# Candidate Root Cause

**Generated:** 2026-07-21T19:45:19+00:00
**Session:** `SESSION-20260721-768F7D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000641`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260721-768F7D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000641': 1, 'duplicate_id:SIG-000643': 1, 'duplicate_id:SIG-000644': 1, 'duplicate_id:SIG-000640': 1, 'duplicate_id:SIG-000642': 1}`
- `candidate CAND-21FC01625C5B entity_id=SIG-000641 reason=duplicate_id:SIG-000641 conf=0.92`
- `candidate CAND-0CD42E9AE8A9 entity_id=SIG-000643 reason=duplicate_id:SIG-000643 conf=0.9`
- `candidate CAND-92E89AD8E575 entity_id=SIG-000644 reason=duplicate_id:SIG-000644 conf=0.92`
- `candidate CAND-1BB372928C74 entity_id=SIG-000640 reason=duplicate_id:SIG-000640 conf=0.9`
- `candidate CAND-F48E9EFFBAA4 entity_id=SIG-000642 reason=duplicate_id:SIG-000642 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-21FC01625C5B | business_signal_library | 0.92 | False | duplicate_id:SIG-000641 | Rejected |
| CAND-0CD42E9AE8A9 | business_signal_library | 0.9 | False | duplicate_id:SIG-000643 | Rejected |
| CAND-92E89AD8E575 | business_signal_library | 0.92 | False | duplicate_id:SIG-000644 | Rejected |
| CAND-1BB372928C74 | business_signal_library | 0.9 | False | duplicate_id:SIG-000640 | Rejected |
| CAND-F48E9EFFBAA4 | business_signal_library | 0.88 | False | duplicate_id:SIG-000642 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000641` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
