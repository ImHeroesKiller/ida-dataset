# Candidate Root Cause

**Generated:** 2026-08-08T03:45:23+00:00
**Session:** `SESSION-20260808-841C51`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001573`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260808-841C51`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001573': 1, 'duplicate_id:SIG-001571': 1, 'duplicate_id:SIG-001574': 1, 'duplicate_id:SIG-001570': 1, 'duplicate_id:SIG-001572': 1}`
- `candidate CAND-0874650619A0 entity_id=SIG-001573 reason=duplicate_id:SIG-001573 conf=0.9`
- `candidate CAND-8D135411B9DA entity_id=SIG-001571 reason=duplicate_id:SIG-001571 conf=0.92`
- `candidate CAND-B519DA9E6909 entity_id=SIG-001574 reason=duplicate_id:SIG-001574 conf=0.92`
- `candidate CAND-2C0CB0C65472 entity_id=SIG-001570 reason=duplicate_id:SIG-001570 conf=0.9`
- `candidate CAND-0C123D1A14D8 entity_id=SIG-001572 reason=duplicate_id:SIG-001572 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-0874650619A0 | business_signal_library | 0.9 | False | duplicate_id:SIG-001573 | Rejected |
| CAND-8D135411B9DA | business_signal_library | 0.92 | False | duplicate_id:SIG-001571 | Rejected |
| CAND-B519DA9E6909 | business_signal_library | 0.92 | False | duplicate_id:SIG-001574 | Rejected |
| CAND-2C0CB0C65472 | business_signal_library | 0.9 | False | duplicate_id:SIG-001570 | Rejected |
| CAND-0C123D1A14D8 | business_signal_library | 0.88 | False | duplicate_id:SIG-001572 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001573` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
