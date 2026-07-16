# Candidate Root Cause

**Generated:** 2026-07-16T19:34:50+00:00
**Session:** `SESSION-20260716-6824A3`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000332`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260716-6824A3`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000332': 1, 'duplicate_id:SIG-000333': 1, 'duplicate_id:SIG-000331': 1, 'duplicate_id:SIG-000334': 1, 'duplicate_id:SIG-000330': 1}`
- `candidate CAND-138A8AEA4DE4 entity_id=SIG-000332 reason=duplicate_id:SIG-000332 conf=0.92`
- `candidate CAND-5A0BE092C477 entity_id=SIG-000333 reason=duplicate_id:SIG-000333 conf=0.9`
- `candidate CAND-521046BA38E1 entity_id=SIG-000331 reason=duplicate_id:SIG-000331 conf=0.88`
- `candidate CAND-C9B3911E5D0D entity_id=SIG-000334 reason=duplicate_id:SIG-000334 conf=0.88`
- `candidate CAND-9FC2F7183EF8 entity_id=SIG-000330 reason=duplicate_id:SIG-000330 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-138A8AEA4DE4 | business_signal_library | 0.92 | False | duplicate_id:SIG-000332 | Rejected |
| CAND-5A0BE092C477 | business_signal_library | 0.9 | False | duplicate_id:SIG-000333 | Rejected |
| CAND-521046BA38E1 | business_signal_library | 0.88 | False | duplicate_id:SIG-000331 | Rejected |
| CAND-C9B3911E5D0D | business_signal_library | 0.88 | False | duplicate_id:SIG-000334 | Rejected |
| CAND-9FC2F7183EF8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000330 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000332` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
