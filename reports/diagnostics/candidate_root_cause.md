# Candidate Root Cause

**Generated:** 2026-07-17T19:31:42+00:00
**Session:** `SESSION-20260717-98198E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000390`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260717-98198E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000390': 1, 'duplicate_id:SIG-000394': 1, 'duplicate_id:SIG-000391': 1, 'duplicate_id:SIG-000392': 1, 'duplicate_id:SIG-000393': 1}`
- `candidate CAND-038AEC146FB1 entity_id=SIG-000390 reason=duplicate_id:SIG-000390 conf=0.9`
- `candidate CAND-B321A0F36433 entity_id=SIG-000394 reason=duplicate_id:SIG-000394 conf=0.92`
- `candidate CAND-8225E913724E entity_id=SIG-000391 reason=duplicate_id:SIG-000391 conf=0.92`
- `candidate CAND-D4E57C489876 entity_id=SIG-000392 reason=duplicate_id:SIG-000392 conf=0.88`
- `candidate CAND-435A988871DD entity_id=SIG-000393 reason=duplicate_id:SIG-000393 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-038AEC146FB1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000390 | Rejected |
| CAND-B321A0F36433 | business_signal_library | 0.92 | False | duplicate_id:SIG-000394 | Rejected |
| CAND-8225E913724E | business_signal_library | 0.92 | False | duplicate_id:SIG-000391 | Rejected |
| CAND-D4E57C489876 | business_signal_library | 0.88 | False | duplicate_id:SIG-000392 | Rejected |
| CAND-435A988871DD | business_signal_library | 0.9 | False | duplicate_id:SIG-000393 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000390` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
