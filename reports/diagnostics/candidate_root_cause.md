# Candidate Root Cause

**Generated:** 2026-08-14T05:03:43+00:00
**Session:** `SESSION-20260814-C295B0`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000081`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260814-C295B0`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000081': 1, 'duplicate_id:SIG-000082': 1, 'duplicate_id:SIG-000084': 1, 'duplicate_id:SIG-000083': 1, 'duplicate_id:SIG-000085': 1}`
- `candidate CAND-DA4A8D53B71F entity_id=SIG-000081 reason=duplicate_id:SIG-000081 conf=0.92`
- `candidate CAND-797FCFC50EF9 entity_id=SIG-000082 reason=duplicate_id:SIG-000082 conf=0.9`
- `candidate CAND-95A33A1CE533 entity_id=SIG-000084 reason=duplicate_id:SIG-000084 conf=0.9`
- `candidate CAND-BB953CE16DAD entity_id=SIG-000083 reason=duplicate_id:SIG-000083 conf=0.9`
- `candidate CAND-ACCFA3487FC6 entity_id=SIG-000085 reason=duplicate_id:SIG-000085 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-DA4A8D53B71F | business_signal_library | 0.92 | False | duplicate_id:SIG-000081 | Rejected |
| CAND-797FCFC50EF9 | business_signal_library | 0.9 | False | duplicate_id:SIG-000082 | Rejected |
| CAND-95A33A1CE533 | business_signal_library | 0.9 | False | duplicate_id:SIG-000084 | Rejected |
| CAND-BB953CE16DAD | business_signal_library | 0.9 | False | duplicate_id:SIG-000083 | Rejected |
| CAND-ACCFA3487FC6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000085 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000081` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
