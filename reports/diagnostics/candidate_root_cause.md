# Candidate Root Cause

**Generated:** 2026-08-18T11:38:49+00:00
**Session:** `SESSION-20260818-9BFE57`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000555`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260818-9BFE57`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000555': 1, 'duplicate_id:SIG-000553': 1, 'duplicate_id:SIG-000551': 1, 'duplicate_id:SIG-000554': 1, 'duplicate_id:SIG-000552': 1}`
- `candidate CAND-9229BE413B38 entity_id=SIG-000555 reason=duplicate_id:SIG-000555 conf=0.9`
- `candidate CAND-01D7E98A340B entity_id=SIG-000553 reason=duplicate_id:SIG-000553 conf=0.9`
- `candidate CAND-CDE16D36F66C entity_id=SIG-000551 reason=duplicate_id:SIG-000551 conf=0.92`
- `candidate CAND-B8C16E1739B2 entity_id=SIG-000554 reason=duplicate_id:SIG-000554 conf=0.9`
- `candidate CAND-B1F005F6B16F entity_id=SIG-000552 reason=duplicate_id:SIG-000552 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-9229BE413B38 | business_signal_library | 0.9 | False | duplicate_id:SIG-000555 | Rejected |
| CAND-01D7E98A340B | business_signal_library | 0.9 | False | duplicate_id:SIG-000553 | Rejected |
| CAND-CDE16D36F66C | business_signal_library | 0.92 | False | duplicate_id:SIG-000551 | Rejected |
| CAND-B8C16E1739B2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000554 | Rejected |
| CAND-B1F005F6B16F | business_signal_library | 0.9 | False | duplicate_id:SIG-000552 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000555` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
