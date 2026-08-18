# Candidate Root Cause

**Generated:** 2026-08-18T15:47:54+00:00
**Session:** `SESSION-20260818-255187`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000571`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260818-255187`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000571': 1, 'duplicate_id:SIG-000573': 1, 'duplicate_id:SIG-000575': 1, 'duplicate_id:SIG-000572': 1, 'duplicate_id:SIG-000574': 1}`
- `candidate CAND-C6F575E9A0A6 entity_id=SIG-000571 reason=duplicate_id:SIG-000571 conf=0.92`
- `candidate CAND-B7455420B168 entity_id=SIG-000573 reason=duplicate_id:SIG-000573 conf=0.9`
- `candidate CAND-C464AA2E8F77 entity_id=SIG-000575 reason=duplicate_id:SIG-000575 conf=0.9`
- `candidate CAND-6269C45932F3 entity_id=SIG-000572 reason=duplicate_id:SIG-000572 conf=0.9`
- `candidate CAND-196266447F70 entity_id=SIG-000574 reason=duplicate_id:SIG-000574 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-C6F575E9A0A6 | business_signal_library | 0.92 | False | duplicate_id:SIG-000571 | Rejected |
| CAND-B7455420B168 | business_signal_library | 0.9 | False | duplicate_id:SIG-000573 | Rejected |
| CAND-C464AA2E8F77 | business_signal_library | 0.9 | False | duplicate_id:SIG-000575 | Rejected |
| CAND-6269C45932F3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000572 | Rejected |
| CAND-196266447F70 | business_signal_library | 0.9 | False | duplicate_id:SIG-000574 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000571` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
