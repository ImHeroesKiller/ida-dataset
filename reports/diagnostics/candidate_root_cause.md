# Candidate Root Cause

**Generated:** 2026-07-16T00:20:44+00:00
**Session:** `SESSION-20260716-115B52`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000286`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260716-115B52`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000286': 1, 'duplicate_id:SIG-000285': 1, 'duplicate_id:SIG-000288': 1, 'duplicate_id:SIG-000289': 1, 'duplicate_id:SIG-000287': 1}`
- `candidate CAND-50FA56B887D1 entity_id=SIG-000286 reason=duplicate_id:SIG-000286 conf=0.92`
- `candidate CAND-62B46CE97856 entity_id=SIG-000285 reason=duplicate_id:SIG-000285 conf=0.9`
- `candidate CAND-7253D37782F3 entity_id=SIG-000288 reason=duplicate_id:SIG-000288 conf=0.85`
- `candidate CAND-A8355028B270 entity_id=SIG-000289 reason=duplicate_id:SIG-000289 conf=0.9`
- `candidate CAND-0BE551E19876 entity_id=SIG-000287 reason=duplicate_id:SIG-000287 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-50FA56B887D1 | business_signal_library | 0.92 | False | duplicate_id:SIG-000286 | Rejected |
| CAND-62B46CE97856 | business_signal_library | 0.9 | False | duplicate_id:SIG-000285 | Rejected |
| CAND-7253D37782F3 | business_signal_library | 0.85 | False | duplicate_id:SIG-000288 | Rejected |
| CAND-A8355028B270 | business_signal_library | 0.9 | False | duplicate_id:SIG-000289 | Rejected |
| CAND-0BE551E19876 | business_signal_library | 0.88 | False | duplicate_id:SIG-000287 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000286` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
