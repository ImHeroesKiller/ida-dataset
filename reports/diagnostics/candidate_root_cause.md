# Candidate Root Cause

**Generated:** 2026-08-17T20:42:19+00:00
**Session:** `SESSION-20260817-1536BD`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000485`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260817-1536BD`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000485': 1, 'duplicate_id:SIG-000481': 1, 'duplicate_id:SIG-000482': 1, 'duplicate_id:SIG-000483': 1, 'duplicate_id:SIG-000484': 1}`
- `candidate CAND-4B6170407FBD entity_id=SIG-000485 reason=duplicate_id:SIG-000485 conf=0.9`
- `candidate CAND-EC5CCD433D6C entity_id=SIG-000481 reason=duplicate_id:SIG-000481 conf=0.92`
- `candidate CAND-2C3100FB78C0 entity_id=SIG-000482 reason=duplicate_id:SIG-000482 conf=0.9`
- `candidate CAND-3714327642B7 entity_id=SIG-000483 reason=duplicate_id:SIG-000483 conf=0.9`
- `candidate CAND-0B7F3B61D705 entity_id=SIG-000484 reason=duplicate_id:SIG-000484 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-4B6170407FBD | business_signal_library | 0.9 | False | duplicate_id:SIG-000485 | Rejected |
| CAND-EC5CCD433D6C | business_signal_library | 0.92 | False | duplicate_id:SIG-000481 | Rejected |
| CAND-2C3100FB78C0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000482 | Rejected |
| CAND-3714327642B7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000483 | Rejected |
| CAND-0B7F3B61D705 | business_signal_library | 0.9 | False | duplicate_id:SIG-000484 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000485` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
