# Candidate Root Cause

**Generated:** 2026-07-19T10:57:00+00:00
**Session:** `SESSION-20260719-4DC64F`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000495`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260719-4DC64F`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000495': 1, 'duplicate_id:SIG-000499': 1, 'duplicate_id:SIG-000497': 1, 'duplicate_id:SIG-000498': 1, 'duplicate_id:SIG-000496': 1}`
- `candidate CAND-9161EBFF50F6 entity_id=SIG-000495 reason=duplicate_id:SIG-000495 conf=0.9`
- `candidate CAND-AE663F01AF36 entity_id=SIG-000499 reason=duplicate_id:SIG-000499 conf=0.92`
- `candidate CAND-6F4FEF380A18 entity_id=SIG-000497 reason=duplicate_id:SIG-000497 conf=0.88`
- `candidate CAND-7D8B10FD604A entity_id=SIG-000498 reason=duplicate_id:SIG-000498 conf=0.9`
- `candidate CAND-326718AE0364 entity_id=SIG-000496 reason=duplicate_id:SIG-000496 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-9161EBFF50F6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000495 | Rejected |
| CAND-AE663F01AF36 | business_signal_library | 0.92 | False | duplicate_id:SIG-000499 | Rejected |
| CAND-6F4FEF380A18 | business_signal_library | 0.88 | False | duplicate_id:SIG-000497 | Rejected |
| CAND-7D8B10FD604A | business_signal_library | 0.9 | False | duplicate_id:SIG-000498 | Rejected |
| CAND-326718AE0364 | business_signal_library | 0.92 | False | duplicate_id:SIG-000496 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000495` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
