# Candidate Root Cause

**Generated:** 2026-08-17T03:15:48+00:00
**Session:** `SESSION-20260817-368724`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000396`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260817-368724`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000396': 1, 'duplicate_id:SIG-000397': 1, 'duplicate_id:SIG-000398': 1, 'duplicate_id:SIG-000399': 1, 'duplicate_id:SIG-000400': 1}`
- `candidate CAND-E642B5DFDBD9 entity_id=SIG-000396 reason=duplicate_id:SIG-000396 conf=0.92`
- `candidate CAND-4B4565D37014 entity_id=SIG-000397 reason=duplicate_id:SIG-000397 conf=0.9`
- `candidate CAND-08FFDD049E73 entity_id=SIG-000398 reason=duplicate_id:SIG-000398 conf=0.9`
- `candidate CAND-ED14380CCF06 entity_id=SIG-000399 reason=duplicate_id:SIG-000399 conf=0.9`
- `candidate CAND-222F894251F3 entity_id=SIG-000400 reason=duplicate_id:SIG-000400 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-E642B5DFDBD9 | business_signal_library | 0.92 | False | duplicate_id:SIG-000396 | Rejected |
| CAND-4B4565D37014 | business_signal_library | 0.9 | False | duplicate_id:SIG-000397 | Rejected |
| CAND-08FFDD049E73 | business_signal_library | 0.9 | False | duplicate_id:SIG-000398 | Rejected |
| CAND-ED14380CCF06 | business_signal_library | 0.9 | False | duplicate_id:SIG-000399 | Rejected |
| CAND-222F894251F3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000400 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000396` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
