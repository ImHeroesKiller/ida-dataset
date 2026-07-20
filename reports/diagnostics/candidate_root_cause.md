# Candidate Root Cause

**Generated:** 2026-07-20T13:27:44+00:00
**Session:** `SESSION-20260720-5ECD97`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000573`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260720-5ECD97`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000573': 1, 'duplicate_id:SIG-000571': 1, 'duplicate_id:SIG-000572': 1, 'duplicate_id:SIG-000574': 1, 'duplicate_id:SIG-000570': 1}`
- `candidate CAND-F568284A1277 entity_id=SIG-000573 reason=duplicate_id:SIG-000573 conf=0.9`
- `candidate CAND-A9231D3136C6 entity_id=SIG-000571 reason=duplicate_id:SIG-000571 conf=0.92`
- `candidate CAND-698FCE602610 entity_id=SIG-000572 reason=duplicate_id:SIG-000572 conf=0.88`
- `candidate CAND-8E53FF0EFEFD entity_id=SIG-000574 reason=duplicate_id:SIG-000574 conf=0.92`
- `candidate CAND-42D04DF06B7C entity_id=SIG-000570 reason=duplicate_id:SIG-000570 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F568284A1277 | business_signal_library | 0.9 | False | duplicate_id:SIG-000573 | Rejected |
| CAND-A9231D3136C6 | business_signal_library | 0.92 | False | duplicate_id:SIG-000571 | Rejected |
| CAND-698FCE602610 | business_signal_library | 0.88 | False | duplicate_id:SIG-000572 | Rejected |
| CAND-8E53FF0EFEFD | business_signal_library | 0.92 | False | duplicate_id:SIG-000574 | Rejected |
| CAND-42D04DF06B7C | business_signal_library | 0.9 | False | duplicate_id:SIG-000570 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000573` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
