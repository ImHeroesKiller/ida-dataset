# Candidate Root Cause

**Generated:** 2026-07-19T21:13:52+00:00
**Session:** `SESSION-20260719-361F3D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000530`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260719-361F3D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000530': 1, 'duplicate_id:SIG-000532': 1, 'duplicate_id:SIG-000534': 1, 'duplicate_id:SIG-000531': 1, 'duplicate_id:SIG-000533': 1}`
- `candidate CAND-A344B2CC5EB6 entity_id=SIG-000530 reason=duplicate_id:SIG-000530 conf=0.9`
- `candidate CAND-EBCA028727E9 entity_id=SIG-000532 reason=duplicate_id:SIG-000532 conf=0.88`
- `candidate CAND-EDEDDA367BE1 entity_id=SIG-000534 reason=duplicate_id:SIG-000534 conf=0.92`
- `candidate CAND-911AD49400EC entity_id=SIG-000531 reason=duplicate_id:SIG-000531 conf=0.92`
- `candidate CAND-245023F27102 entity_id=SIG-000533 reason=duplicate_id:SIG-000533 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A344B2CC5EB6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000530 | Rejected |
| CAND-EBCA028727E9 | business_signal_library | 0.88 | False | duplicate_id:SIG-000532 | Rejected |
| CAND-EDEDDA367BE1 | business_signal_library | 0.92 | False | duplicate_id:SIG-000534 | Rejected |
| CAND-911AD49400EC | business_signal_library | 0.92 | False | duplicate_id:SIG-000531 | Rejected |
| CAND-245023F27102 | business_signal_library | 0.9 | False | duplicate_id:SIG-000533 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000530` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
