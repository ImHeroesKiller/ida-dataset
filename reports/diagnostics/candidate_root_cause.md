# Candidate Root Cause

**Generated:** 2026-07-20T16:11:44+00:00
**Session:** `SESSION-20260720-608BB8`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000575`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260720-608BB8`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000575': 1, 'duplicate_id:SIG-000579': 1, 'duplicate_id:SIG-000578': 1, 'duplicate_id:SIG-000577': 1, 'duplicate_id:SIG-000576': 1}`
- `candidate CAND-2823278729A2 entity_id=SIG-000575 reason=duplicate_id:SIG-000575 conf=0.9`
- `candidate CAND-33530883E9C0 entity_id=SIG-000579 reason=duplicate_id:SIG-000579 conf=0.92`
- `candidate CAND-64698D8C5A13 entity_id=SIG-000578 reason=duplicate_id:SIG-000578 conf=0.9`
- `candidate CAND-689A475C2BFB entity_id=SIG-000577 reason=duplicate_id:SIG-000577 conf=0.88`
- `candidate CAND-A480B3813A4F entity_id=SIG-000576 reason=duplicate_id:SIG-000576 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-2823278729A2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000575 | Rejected |
| CAND-33530883E9C0 | business_signal_library | 0.92 | False | duplicate_id:SIG-000579 | Rejected |
| CAND-64698D8C5A13 | business_signal_library | 0.9 | False | duplicate_id:SIG-000578 | Rejected |
| CAND-689A475C2BFB | business_signal_library | 0.88 | False | duplicate_id:SIG-000577 | Rejected |
| CAND-A480B3813A4F | business_signal_library | 0.92 | False | duplicate_id:SIG-000576 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000575` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
