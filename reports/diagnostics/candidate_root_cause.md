# Candidate Root Cause

**Generated:** 2026-08-18T09:45:21+00:00
**Session:** `SESSION-20260818-3CC7CA`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000545`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260818-3CC7CA`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000545': 1, 'duplicate_id:SIG-000543': 1, 'duplicate_id:SIG-000542': 1, 'duplicate_id:SIG-000541': 1, 'duplicate_id:SIG-000544': 1}`
- `candidate CAND-5FE7770A41C4 entity_id=SIG-000545 reason=duplicate_id:SIG-000545 conf=0.9`
- `candidate CAND-4AEEE57A67AE entity_id=SIG-000543 reason=duplicate_id:SIG-000543 conf=0.9`
- `candidate CAND-39ECA2F971B9 entity_id=SIG-000542 reason=duplicate_id:SIG-000542 conf=0.9`
- `candidate CAND-409C352D1519 entity_id=SIG-000541 reason=duplicate_id:SIG-000541 conf=0.92`
- `candidate CAND-19C606B30939 entity_id=SIG-000544 reason=duplicate_id:SIG-000544 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5FE7770A41C4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000545 | Rejected |
| CAND-4AEEE57A67AE | business_signal_library | 0.9 | False | duplicate_id:SIG-000543 | Rejected |
| CAND-39ECA2F971B9 | business_signal_library | 0.9 | False | duplicate_id:SIG-000542 | Rejected |
| CAND-409C352D1519 | business_signal_library | 0.92 | False | duplicate_id:SIG-000541 | Rejected |
| CAND-19C606B30939 | business_signal_library | 0.9 | False | duplicate_id:SIG-000544 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000545` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
