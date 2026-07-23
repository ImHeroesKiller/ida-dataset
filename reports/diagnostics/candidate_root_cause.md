# Candidate Root Cause

**Generated:** 2026-07-23T22:23:04+00:00
**Session:** `SESSION-20260723-74FFCD`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000752`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260723-74FFCD`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000752': 1, 'duplicate_id:SIG-000751': 1, 'duplicate_id:SIG-000750': 1, 'duplicate_id:SIG-000753': 1, 'duplicate_id:SIG-000754': 1}`
- `candidate CAND-AC3B74F2B850 entity_id=SIG-000752 reason=duplicate_id:SIG-000752 conf=0.88`
- `candidate CAND-D2A64B10192D entity_id=SIG-000751 reason=duplicate_id:SIG-000751 conf=0.92`
- `candidate CAND-5ABAB050B32B entity_id=SIG-000750 reason=duplicate_id:SIG-000750 conf=0.9`
- `candidate CAND-3328277DE0CF entity_id=SIG-000753 reason=duplicate_id:SIG-000753 conf=0.9`
- `candidate CAND-1CEB4B1790DF entity_id=SIG-000754 reason=duplicate_id:SIG-000754 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-AC3B74F2B850 | business_signal_library | 0.88 | False | duplicate_id:SIG-000752 | Rejected |
| CAND-D2A64B10192D | business_signal_library | 0.92 | False | duplicate_id:SIG-000751 | Rejected |
| CAND-5ABAB050B32B | business_signal_library | 0.9 | False | duplicate_id:SIG-000750 | Rejected |
| CAND-3328277DE0CF | business_signal_library | 0.9 | False | duplicate_id:SIG-000753 | Rejected |
| CAND-1CEB4B1790DF | business_signal_library | 0.92 | False | duplicate_id:SIG-000754 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000752` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
