# Candidate Root Cause

**Generated:** 2026-07-20T18:24:03+00:00
**Session:** `SESSION-20260720-8AEBBA`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000581`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260720-8AEBBA`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000581': 1, 'duplicate_id:SIG-000582': 1, 'duplicate_id:SIG-000584': 1, 'duplicate_id:SIG-000583': 1, 'duplicate_id:SIG-000580': 1}`
- `candidate CAND-0A2AD84BB8D1 entity_id=SIG-000581 reason=duplicate_id:SIG-000581 conf=0.92`
- `candidate CAND-93D94C9F6E56 entity_id=SIG-000582 reason=duplicate_id:SIG-000582 conf=0.88`
- `candidate CAND-21543B64DA49 entity_id=SIG-000584 reason=duplicate_id:SIG-000584 conf=0.92`
- `candidate CAND-A306E6CB64F3 entity_id=SIG-000583 reason=duplicate_id:SIG-000583 conf=0.9`
- `candidate CAND-1CCE2E47DF00 entity_id=SIG-000580 reason=duplicate_id:SIG-000580 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-0A2AD84BB8D1 | business_signal_library | 0.92 | False | duplicate_id:SIG-000581 | Rejected |
| CAND-93D94C9F6E56 | business_signal_library | 0.88 | False | duplicate_id:SIG-000582 | Rejected |
| CAND-21543B64DA49 | business_signal_library | 0.92 | False | duplicate_id:SIG-000584 | Rejected |
| CAND-A306E6CB64F3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000583 | Rejected |
| CAND-1CCE2E47DF00 | business_signal_library | 0.9 | False | duplicate_id:SIG-000580 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000581` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
