# Candidate Root Cause

**Generated:** 2026-08-20T05:50:44+00:00
**Session:** `SESSION-20260820-B17DEC`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000751`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260820-B17DEC`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000751': 1, 'duplicate_id:SIG-000753': 1, 'duplicate_id:SIG-000752': 1, 'duplicate_id:SIG-000754': 1, 'duplicate_id:SIG-000755': 1}`
- `candidate CAND-DC5A031DADFE entity_id=SIG-000751 reason=duplicate_id:SIG-000751 conf=0.92`
- `candidate CAND-630BD2E98FD1 entity_id=SIG-000753 reason=duplicate_id:SIG-000753 conf=0.9`
- `candidate CAND-ABC030040C63 entity_id=SIG-000752 reason=duplicate_id:SIG-000752 conf=0.9`
- `candidate CAND-FE89B7912280 entity_id=SIG-000754 reason=duplicate_id:SIG-000754 conf=0.9`
- `candidate CAND-DD36497F708F entity_id=SIG-000755 reason=duplicate_id:SIG-000755 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-DC5A031DADFE | business_signal_library | 0.92 | False | duplicate_id:SIG-000751 | Rejected |
| CAND-630BD2E98FD1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000753 | Rejected |
| CAND-ABC030040C63 | business_signal_library | 0.9 | False | duplicate_id:SIG-000752 | Rejected |
| CAND-FE89B7912280 | business_signal_library | 0.9 | False | duplicate_id:SIG-000754 | Rejected |
| CAND-DD36497F708F | business_signal_library | 0.9 | False | duplicate_id:SIG-000755 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000751` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
