# Candidate Root Cause

**Generated:** 2026-08-09T10:54:41+00:00
**Session:** `SESSION-20260809-C3931D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001712`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260809-C3931D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001712': 1, 'duplicate_id:SIG-001714': 1, 'duplicate_id:SIG-001711': 1, 'duplicate_id:SIG-001710': 1, 'duplicate_id:SIG-001713': 1}`
- `candidate CAND-142B9F6713E6 entity_id=SIG-001712 reason=duplicate_id:SIG-001712 conf=0.88`
- `candidate CAND-EEAD220E230C entity_id=SIG-001714 reason=duplicate_id:SIG-001714 conf=0.92`
- `candidate CAND-64DAB0DAF43C entity_id=SIG-001711 reason=duplicate_id:SIG-001711 conf=0.92`
- `candidate CAND-6A36195C4C20 entity_id=SIG-001710 reason=duplicate_id:SIG-001710 conf=0.9`
- `candidate CAND-4EC22A8B5198 entity_id=SIG-001713 reason=duplicate_id:SIG-001713 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-142B9F6713E6 | business_signal_library | 0.88 | False | duplicate_id:SIG-001712 | Rejected |
| CAND-EEAD220E230C | business_signal_library | 0.92 | False | duplicate_id:SIG-001714 | Rejected |
| CAND-64DAB0DAF43C | business_signal_library | 0.92 | False | duplicate_id:SIG-001711 | Rejected |
| CAND-6A36195C4C20 | business_signal_library | 0.9 | False | duplicate_id:SIG-001710 | Rejected |
| CAND-4EC22A8B5198 | business_signal_library | 0.9 | False | duplicate_id:SIG-001713 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001712` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
