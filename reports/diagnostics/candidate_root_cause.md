# Candidate Root Cause

**Generated:** 2026-07-12T18:23:54+00:00
**Session:** `SESSION-20260712-B8F796`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:IND-000058`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **1**
- Integrity blocked: **1**
- Blocked by primary reason: **1**

## What evidence proves it?

- `session_id=SESSION-20260712-B8F796`
- `dry_run=False`
- `candidates_analyzed=1`
- `integrity_blocked=1`
- `top_family=duplicate_id count=1`
- `family_histogram={'duplicate_id': 1}`
- `reason_histogram={'duplicate_id:IND-000058': 1}`
- `candidate CAND-0D1D5D7F7FD4 entity_id=IND-000058 reason=duplicate_id:IND-000058 conf=0.8375`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-0D1D5D7F7FD4 | industry_library | 0.8375 | False | duplicate_id:IND-000058 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:IND-000058` were satisfied for 1/1 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
