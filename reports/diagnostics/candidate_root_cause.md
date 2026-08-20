# Candidate Root Cause

**Generated:** 2026-08-20T03:16:14+00:00
**Session:** `SESSION-20260820-19BE20`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000736`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260820-19BE20`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000736': 1, 'duplicate_id:SIG-000739': 1, 'duplicate_id:SIG-000737': 1, 'duplicate_id:SIG-000740': 1, 'duplicate_id:SIG-000738': 1}`
- `candidate CAND-FA0A020E8294 entity_id=SIG-000736 reason=duplicate_id:SIG-000736 conf=0.92`
- `candidate CAND-33740053A32F entity_id=SIG-000739 reason=duplicate_id:SIG-000739 conf=0.9`
- `candidate CAND-6B0441FF7529 entity_id=SIG-000737 reason=duplicate_id:SIG-000737 conf=0.9`
- `candidate CAND-4533D1BD0FD7 entity_id=SIG-000740 reason=duplicate_id:SIG-000740 conf=0.9`
- `candidate CAND-20FBD0C1804C entity_id=SIG-000738 reason=duplicate_id:SIG-000738 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-FA0A020E8294 | business_signal_library | 0.92 | False | duplicate_id:SIG-000736 | Rejected |
| CAND-33740053A32F | business_signal_library | 0.9 | False | duplicate_id:SIG-000739 | Rejected |
| CAND-6B0441FF7529 | business_signal_library | 0.9 | False | duplicate_id:SIG-000737 | Rejected |
| CAND-4533D1BD0FD7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000740 | Rejected |
| CAND-20FBD0C1804C | business_signal_library | 0.9 | False | duplicate_id:SIG-000738 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000736` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
