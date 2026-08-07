# Candidate Root Cause

**Generated:** 2026-08-07T21:58:33+00:00
**Session:** `SESSION-20260807-2103FD`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001552`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260807-2103FD`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001552': 1, 'duplicate_id:SIG-001550': 1, 'duplicate_id:SIG-001554': 1, 'duplicate_id:SIG-001553': 1, 'duplicate_id:SIG-001551': 1}`
- `candidate CAND-0CB06A698FE2 entity_id=SIG-001552 reason=duplicate_id:SIG-001552 conf=0.88`
- `candidate CAND-25E3CEC8CB75 entity_id=SIG-001550 reason=duplicate_id:SIG-001550 conf=0.9`
- `candidate CAND-C23507BCA31E entity_id=SIG-001554 reason=duplicate_id:SIG-001554 conf=0.92`
- `candidate CAND-FAFA54180AFD entity_id=SIG-001553 reason=duplicate_id:SIG-001553 conf=0.9`
- `candidate CAND-32E58E59346E entity_id=SIG-001551 reason=duplicate_id:SIG-001551 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-0CB06A698FE2 | business_signal_library | 0.88 | False | duplicate_id:SIG-001552 | Rejected |
| CAND-25E3CEC8CB75 | business_signal_library | 0.9 | False | duplicate_id:SIG-001550 | Rejected |
| CAND-C23507BCA31E | business_signal_library | 0.92 | False | duplicate_id:SIG-001554 | Rejected |
| CAND-FAFA54180AFD | business_signal_library | 0.9 | False | duplicate_id:SIG-001553 | Rejected |
| CAND-32E58E59346E | business_signal_library | 0.92 | False | duplicate_id:SIG-001551 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001552` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
