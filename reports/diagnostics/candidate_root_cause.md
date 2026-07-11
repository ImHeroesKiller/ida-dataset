# Candidate Root Cause

**Generated:** 2026-07-11T13:10:45+00:00
**Session:** `SESSION-20260711-CF5FA7`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:IND-000054`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **2**
- Integrity blocked: **2**
- Blocked by primary reason: **2**

## What evidence proves it?

- `session_id=SESSION-20260711-CF5FA7`
- `dry_run=False`
- `candidates_analyzed=2`
- `integrity_blocked=2`
- `top_family=duplicate_id count=2`
- `family_histogram={'duplicate_id': 2}`
- `reason_histogram={'duplicate_id:IND-000054': 1, 'duplicate_id:IND-000055': 1}`
- `candidate CAND-A2586EE1B9E4 entity_id=IND-000054 reason=duplicate_id:IND-000054 conf=0.8375`
- `candidate CAND-18CCB68EA40E entity_id=IND-000055 reason=duplicate_id:IND-000055 conf=0.8375`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A2586EE1B9E4 | industry_library | 0.8375 | False | duplicate_id:IND-000054 | Rejected |
| CAND-18CCB68EA40E | industry_library | 0.8375 | False | duplicate_id:IND-000055 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:IND-000054` were satisfied for 2/2 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
