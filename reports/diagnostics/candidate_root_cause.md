# Candidate Root Cause

**Generated:** 2026-08-13T02:17:58+00:00
**Session:** `SESSION-20260813-F331BD`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:IND-000019`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **1**
- Integrity blocked: **1**
- Blocked by primary reason: **1**

## What evidence proves it?

- `session_id=SESSION-20260813-F331BD`
- `dry_run=False`
- `candidates_analyzed=1`
- `integrity_blocked=1`
- `top_family=duplicate_id count=1`
- `family_histogram={'duplicate_id': 1}`
- `reason_histogram={'duplicate_id:IND-000019': 1}`
- `candidate CAND-76D8F951A184 entity_id=IND-000019 reason=duplicate_id:IND-000019 conf=0.855`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-76D8F951A184 | industry_library | 0.855 | False | duplicate_id:IND-000019 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:IND-000019` were satisfied for 1/1 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
