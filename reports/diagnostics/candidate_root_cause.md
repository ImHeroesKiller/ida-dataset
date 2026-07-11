# Candidate Root Cause

**Generated:** 2026-07-11T18:00:48+00:00
**Session:** `SESSION-20260711-41DBF5`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:IND-000056`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **3**
- Integrity blocked: **3**
- Blocked by primary reason: **3**

## What evidence proves it?

- `session_id=SESSION-20260711-41DBF5`
- `dry_run=False`
- `candidates_analyzed=3`
- `integrity_blocked=3`
- `top_family=duplicate_id count=3`
- `family_histogram={'duplicate_id': 3}`
- `reason_histogram={'duplicate_id:IND-000056': 2, 'duplicate_id:IND-000057': 1}`
- `candidate CAND-E9B6307893CE entity_id=IND-000056 reason=duplicate_id:IND-000056 conf=0.92`
- `candidate CAND-D5FB552C5669 entity_id=IND-000057 reason=duplicate_id:IND-000057 conf=0.8375`
- `candidate CAND-5D05664CF73E entity_id=IND-000056 reason=duplicate_id:IND-000056 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-E9B6307893CE | industry_library | 0.92 | False | duplicate_id:IND-000056 | Rejected |
| CAND-D5FB552C5669 | industry_library | 0.8375 | False | duplicate_id:IND-000057 | Rejected |
| CAND-5D05664CF73E | industry_library | 0.92 | False | duplicate_id:IND-000056 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:IND-000056` were satisfied for 3/3 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
