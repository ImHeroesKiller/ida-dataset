# Candidate Root Cause

**Generated:** 2026-07-20T04:12:38+00:00
**Session:** `SESSION-20260720-C3910D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000550`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260720-C3910D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000550': 1, 'duplicate_id:SIG-000554': 1, 'duplicate_id:SIG-000553': 1, 'duplicate_id:SIG-000552': 1, 'duplicate_id:SIG-000551': 1}`
- `candidate CAND-C5E532EAF9D2 entity_id=SIG-000550 reason=duplicate_id:SIG-000550 conf=0.9`
- `candidate CAND-4D2CF9365152 entity_id=SIG-000554 reason=duplicate_id:SIG-000554 conf=0.92`
- `candidate CAND-395C339AF713 entity_id=SIG-000553 reason=duplicate_id:SIG-000553 conf=0.9`
- `candidate CAND-11A4462D7054 entity_id=SIG-000552 reason=duplicate_id:SIG-000552 conf=0.88`
- `candidate CAND-43F910B42B3B entity_id=SIG-000551 reason=duplicate_id:SIG-000551 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-C5E532EAF9D2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000550 | Rejected |
| CAND-4D2CF9365152 | business_signal_library | 0.92 | False | duplicate_id:SIG-000554 | Rejected |
| CAND-395C339AF713 | business_signal_library | 0.9 | False | duplicate_id:SIG-000553 | Rejected |
| CAND-11A4462D7054 | business_signal_library | 0.88 | False | duplicate_id:SIG-000552 | Rejected |
| CAND-43F910B42B3B | business_signal_library | 0.92 | False | duplicate_id:SIG-000551 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000550` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
