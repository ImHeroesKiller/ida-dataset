# Candidate Root Cause

**Generated:** 2026-07-21T16:05:44+00:00
**Session:** `SESSION-20260721-65FE97`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000633`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260721-65FE97`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000633': 1, 'duplicate_id:SIG-000634': 1, 'duplicate_id:SIG-000631': 1, 'duplicate_id:SIG-000632': 1, 'duplicate_id:SIG-000630': 1}`
- `candidate CAND-7FBCE3BECD50 entity_id=SIG-000633 reason=duplicate_id:SIG-000633 conf=0.9`
- `candidate CAND-E9F86E8360F1 entity_id=SIG-000634 reason=duplicate_id:SIG-000634 conf=0.92`
- `candidate CAND-4D86E7940BCB entity_id=SIG-000631 reason=duplicate_id:SIG-000631 conf=0.92`
- `candidate CAND-2E8C9A160BF1 entity_id=SIG-000632 reason=duplicate_id:SIG-000632 conf=0.88`
- `candidate CAND-1470ACD3A475 entity_id=SIG-000630 reason=duplicate_id:SIG-000630 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-7FBCE3BECD50 | business_signal_library | 0.9 | False | duplicate_id:SIG-000633 | Rejected |
| CAND-E9F86E8360F1 | business_signal_library | 0.92 | False | duplicate_id:SIG-000634 | Rejected |
| CAND-4D86E7940BCB | business_signal_library | 0.92 | False | duplicate_id:SIG-000631 | Rejected |
| CAND-2E8C9A160BF1 | business_signal_library | 0.88 | False | duplicate_id:SIG-000632 | Rejected |
| CAND-1470ACD3A475 | business_signal_library | 0.9 | False | duplicate_id:SIG-000630 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000633` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
