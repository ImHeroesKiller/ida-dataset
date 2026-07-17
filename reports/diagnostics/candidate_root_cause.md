# Candidate Root Cause

**Generated:** 2026-07-17T10:18:22+00:00
**Session:** `SESSION-20260717-AD997B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000369`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260717-AD997B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000369': 1, 'duplicate_id:SIG-000367': 1, 'duplicate_id:SIG-000365': 1, 'duplicate_id:SIG-000368': 1, 'duplicate_id:SIG-000366': 1}`
- `candidate CAND-5F16CEFAE1E1 entity_id=SIG-000369 reason=duplicate_id:SIG-000369 conf=0.92`
- `candidate CAND-7F28F069C400 entity_id=SIG-000367 reason=duplicate_id:SIG-000367 conf=0.88`
- `candidate CAND-97EB7DD92AE0 entity_id=SIG-000365 reason=duplicate_id:SIG-000365 conf=0.9`
- `candidate CAND-22E1C8BBE42B entity_id=SIG-000368 reason=duplicate_id:SIG-000368 conf=0.9`
- `candidate CAND-A8C71ED4AF39 entity_id=SIG-000366 reason=duplicate_id:SIG-000366 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5F16CEFAE1E1 | business_signal_library | 0.92 | False | duplicate_id:SIG-000369 | Rejected |
| CAND-7F28F069C400 | business_signal_library | 0.88 | False | duplicate_id:SIG-000367 | Rejected |
| CAND-97EB7DD92AE0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000365 | Rejected |
| CAND-22E1C8BBE42B | business_signal_library | 0.9 | False | duplicate_id:SIG-000368 | Rejected |
| CAND-A8C71ED4AF39 | business_signal_library | 0.92 | False | duplicate_id:SIG-000366 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000369` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
