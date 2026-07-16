# Candidate Root Cause

**Generated:** 2026-07-16T11:58:48+00:00
**Session:** `SESSION-20260716-737E5C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000313`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260716-737E5C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000313': 1, 'duplicate_id:SIG-000311': 1, 'duplicate_id:SIG-000312': 1, 'duplicate_id:SIG-000314': 1, 'duplicate_id:SIG-000310': 1}`
- `candidate CAND-3CC545F0F6C2 entity_id=SIG-000313 reason=duplicate_id:SIG-000313 conf=0.9`
- `candidate CAND-0CF45BC9F2D1 entity_id=SIG-000311 reason=duplicate_id:SIG-000311 conf=0.92`
- `candidate CAND-CE0FE9D61E92 entity_id=SIG-000312 reason=duplicate_id:SIG-000312 conf=0.88`
- `candidate CAND-C8C108A10DFC entity_id=SIG-000314 reason=duplicate_id:SIG-000314 conf=0.92`
- `candidate CAND-75A54B12B9CC entity_id=SIG-000310 reason=duplicate_id:SIG-000310 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-3CC545F0F6C2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000313 | Rejected |
| CAND-0CF45BC9F2D1 | business_signal_library | 0.92 | False | duplicate_id:SIG-000311 | Rejected |
| CAND-CE0FE9D61E92 | business_signal_library | 0.88 | False | duplicate_id:SIG-000312 | Rejected |
| CAND-C8C108A10DFC | business_signal_library | 0.92 | False | duplicate_id:SIG-000314 | Rejected |
| CAND-75A54B12B9CC | business_signal_library | 0.9 | False | duplicate_id:SIG-000310 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000313` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
