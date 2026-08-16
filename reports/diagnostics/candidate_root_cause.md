# Candidate Root Cause

**Generated:** 2026-08-16T03:15:59+00:00
**Session:** `SESSION-20260816-ED8FDD`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000289`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260816-ED8FDD`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000289': 1, 'duplicate_id:SIG-000288': 1, 'duplicate_id:SIG-000287': 1, 'duplicate_id:SIG-000290': 1, 'duplicate_id:SIG-000286': 1}`
- `candidate CAND-F9F529854FD4 entity_id=SIG-000289 reason=duplicate_id:SIG-000289 conf=0.9`
- `candidate CAND-A468B52565DB entity_id=SIG-000288 reason=duplicate_id:SIG-000288 conf=0.9`
- `candidate CAND-7009B455E834 entity_id=SIG-000287 reason=duplicate_id:SIG-000287 conf=0.9`
- `candidate CAND-5ED3736F6EF4 entity_id=SIG-000290 reason=duplicate_id:SIG-000290 conf=0.9`
- `candidate CAND-5B056552BDB6 entity_id=SIG-000286 reason=duplicate_id:SIG-000286 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F9F529854FD4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000289 | Rejected |
| CAND-A468B52565DB | business_signal_library | 0.9 | False | duplicate_id:SIG-000288 | Rejected |
| CAND-7009B455E834 | business_signal_library | 0.9 | False | duplicate_id:SIG-000287 | Rejected |
| CAND-5ED3736F6EF4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000290 | Rejected |
| CAND-5B056552BDB6 | business_signal_library | 0.92 | False | duplicate_id:SIG-000286 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000289` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
