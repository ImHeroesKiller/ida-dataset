# Candidate Root Cause

**Generated:** 2026-07-28T06:07:45+00:00
**Session:** `SESSION-20260728-71899B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:IND-000061`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **2**
- Integrity blocked: **2**
- Blocked by primary reason: **2**

## What evidence proves it?

- `session_id=SESSION-20260728-71899B`
- `dry_run=False`
- `candidates_analyzed=2`
- `integrity_blocked=2`
- `top_family=duplicate_id count=2`
- `family_histogram={'duplicate_id': 2}`
- `reason_histogram={'duplicate_id:IND-000061': 1, 'duplicate_id:IND-000060': 1}`
- `candidate CAND-3475745ED4B5 entity_id=IND-000061 reason=duplicate_id:IND-000061 conf=0.855`
- `candidate CAND-96D7F41016DC entity_id=IND-000060 reason=duplicate_id:IND-000060 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-3475745ED4B5 | industry_library | 0.855 | False | duplicate_id:IND-000061 | Rejected |
| CAND-96D7F41016DC | industry_library | 0.92 | False | duplicate_id:IND-000060 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:IND-000061` were satisfied for 2/2 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
