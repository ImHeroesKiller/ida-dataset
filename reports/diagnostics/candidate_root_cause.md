# Candidate Root Cause

**Generated:** 2026-08-18T22:37:08+00:00
**Session:** `SESSION-20260818-BF0BAE`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000609`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260818-BF0BAE`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000609': 1, 'duplicate_id:SIG-000608': 1, 'duplicate_id:SIG-000610': 1, 'duplicate_id:SIG-000606': 1, 'duplicate_id:SIG-000607': 1}`
- `candidate CAND-A22D1F4F1D24 entity_id=SIG-000609 reason=duplicate_id:SIG-000609 conf=0.9`
- `candidate CAND-E2BDC8D0ABA6 entity_id=SIG-000608 reason=duplicate_id:SIG-000608 conf=0.9`
- `candidate CAND-07A3B8CBA5DB entity_id=SIG-000610 reason=duplicate_id:SIG-000610 conf=0.9`
- `candidate CAND-9EDBAD65884A entity_id=SIG-000606 reason=duplicate_id:SIG-000606 conf=0.92`
- `candidate CAND-6C7EF28D32B2 entity_id=SIG-000607 reason=duplicate_id:SIG-000607 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A22D1F4F1D24 | business_signal_library | 0.9 | False | duplicate_id:SIG-000609 | Rejected |
| CAND-E2BDC8D0ABA6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000608 | Rejected |
| CAND-07A3B8CBA5DB | business_signal_library | 0.9 | False | duplicate_id:SIG-000610 | Rejected |
| CAND-9EDBAD65884A | business_signal_library | 0.92 | False | duplicate_id:SIG-000606 | Rejected |
| CAND-6C7EF28D32B2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000607 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000609` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
