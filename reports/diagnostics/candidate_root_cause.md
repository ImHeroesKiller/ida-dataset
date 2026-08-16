# Candidate Root Cause

**Generated:** 2026-08-16T16:41:29+00:00
**Session:** `SESSION-20260816-C9AF2A`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000352`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260816-C9AF2A`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000352': 1, 'duplicate_id:SIG-000351': 1, 'duplicate_id:SIG-000353': 1, 'duplicate_id:SIG-000354': 1, 'duplicate_id:SIG-000355': 1}`
- `candidate CAND-E420EE2CF144 entity_id=SIG-000352 reason=duplicate_id:SIG-000352 conf=0.9`
- `candidate CAND-B897DA4DA914 entity_id=SIG-000351 reason=duplicate_id:SIG-000351 conf=0.92`
- `candidate CAND-FD8C576F8712 entity_id=SIG-000353 reason=duplicate_id:SIG-000353 conf=0.9`
- `candidate CAND-AECB158DC803 entity_id=SIG-000354 reason=duplicate_id:SIG-000354 conf=0.9`
- `candidate CAND-CEA4A8AF03F6 entity_id=SIG-000355 reason=duplicate_id:SIG-000355 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-E420EE2CF144 | business_signal_library | 0.9 | False | duplicate_id:SIG-000352 | Rejected |
| CAND-B897DA4DA914 | business_signal_library | 0.92 | False | duplicate_id:SIG-000351 | Rejected |
| CAND-FD8C576F8712 | business_signal_library | 0.9 | False | duplicate_id:SIG-000353 | Rejected |
| CAND-AECB158DC803 | business_signal_library | 0.9 | False | duplicate_id:SIG-000354 | Rejected |
| CAND-CEA4A8AF03F6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000355 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000352` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
