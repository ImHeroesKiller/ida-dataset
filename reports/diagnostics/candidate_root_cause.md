# Candidate Root Cause

**Generated:** 2026-08-13T01:08:35+00:00
**Session:** `SESSION-20260813-D1D658`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:IND-000015`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **7**
- Integrity blocked: **7**
- Blocked by primary reason: **7**

## What evidence proves it?

- `session_id=SESSION-20260813-D1D658`
- `dry_run=False`
- `candidates_analyzed=7`
- `integrity_blocked=7`
- `top_family=duplicate_id count=7`
- `family_histogram={'duplicate_id': 7}`
- `reason_histogram={'duplicate_id:IND-000015': 3, 'duplicate_id:IND-000016': 2, 'duplicate_id:IND-000018': 1, 'duplicate_id:IND-000017': 1}`
- `candidate CAND-FF822FF57AA1 entity_id=IND-000015 reason=duplicate_id:IND-000015 conf=0.855`
- `candidate CAND-7AA61C9E1321 entity_id=IND-000015 reason=duplicate_id:IND-000015 conf=0.855`
- `candidate CAND-930DF863CECD entity_id=IND-000016 reason=duplicate_id:IND-000016 conf=0.855`
- `candidate CAND-E182B875B84B entity_id=IND-000018 reason=duplicate_id:IND-000018 conf=0.92`
- `candidate CAND-87503D97E993 entity_id=IND-000016 reason=duplicate_id:IND-000016 conf=0.92`
- `candidate CAND-C47F843D31CF entity_id=IND-000017 reason=duplicate_id:IND-000017 conf=0.92`
- `candidate CAND-236285DF4A3F entity_id=IND-000015 reason=duplicate_id:IND-000015 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-FF822FF57AA1 | industry_library | 0.855 | False | duplicate_id:IND-000015 | Rejected |
| CAND-7AA61C9E1321 | industry_library | 0.855 | False | duplicate_id:IND-000015 | Rejected |
| CAND-930DF863CECD | industry_library | 0.855 | False | duplicate_id:IND-000016 | Rejected |
| CAND-E182B875B84B | industry_library | 0.92 | False | duplicate_id:IND-000018 | Rejected |
| CAND-87503D97E993 | industry_library | 0.92 | False | duplicate_id:IND-000016 | Rejected |
| CAND-C47F843D31CF | industry_library | 0.92 | False | duplicate_id:IND-000017 | Rejected |
| CAND-236285DF4A3F | industry_library | 0.92 | False | duplicate_id:IND-000015 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:IND-000015` were satisfied for 7/7 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
