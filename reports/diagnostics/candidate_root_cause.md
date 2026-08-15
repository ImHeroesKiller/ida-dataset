# Candidate Root Cause

**Generated:** 2026-08-15T16:37:46+00:00
**Session:** `SESSION-20260815-812B0A`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000243`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260815-812B0A`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000243': 1, 'duplicate_id:SIG-000242': 1, 'duplicate_id:SIG-000244': 1, 'duplicate_id:SIG-000245': 1, 'duplicate_id:SIG-000241': 1}`
- `candidate CAND-AEA0DFE38EA1 entity_id=SIG-000243 reason=duplicate_id:SIG-000243 conf=0.9`
- `candidate CAND-9D97226010B1 entity_id=SIG-000242 reason=duplicate_id:SIG-000242 conf=0.9`
- `candidate CAND-4A814EC5C8F2 entity_id=SIG-000244 reason=duplicate_id:SIG-000244 conf=0.9`
- `candidate CAND-83B2C3FC577C entity_id=SIG-000245 reason=duplicate_id:SIG-000245 conf=0.9`
- `candidate CAND-AAAE67D4D77F entity_id=SIG-000241 reason=duplicate_id:SIG-000241 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-AEA0DFE38EA1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000243 | Rejected |
| CAND-9D97226010B1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000242 | Rejected |
| CAND-4A814EC5C8F2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000244 | Rejected |
| CAND-83B2C3FC577C | business_signal_library | 0.9 | False | duplicate_id:SIG-000245 | Rejected |
| CAND-AAAE67D4D77F | business_signal_library | 0.92 | False | duplicate_id:SIG-000241 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000243` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
