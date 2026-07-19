# Candidate Root Cause

**Generated:** 2026-07-19T19:37:12+00:00
**Session:** `SESSION-20260719-4FF94A`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000528`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260719-4FF94A`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000528': 1, 'duplicate_id:SIG-000529': 1, 'duplicate_id:SIG-000526': 1, 'duplicate_id:SIG-000525': 1, 'duplicate_id:SIG-000527': 1}`
- `candidate CAND-6C8986987B73 entity_id=SIG-000528 reason=duplicate_id:SIG-000528 conf=0.9`
- `candidate CAND-505188456873 entity_id=SIG-000529 reason=duplicate_id:SIG-000529 conf=0.92`
- `candidate CAND-4810A3CB5367 entity_id=SIG-000526 reason=duplicate_id:SIG-000526 conf=0.92`
- `candidate CAND-DA76C8A4F5C8 entity_id=SIG-000525 reason=duplicate_id:SIG-000525 conf=0.9`
- `candidate CAND-00972772A4C9 entity_id=SIG-000527 reason=duplicate_id:SIG-000527 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-6C8986987B73 | business_signal_library | 0.9 | False | duplicate_id:SIG-000528 | Rejected |
| CAND-505188456873 | business_signal_library | 0.92 | False | duplicate_id:SIG-000529 | Rejected |
| CAND-4810A3CB5367 | business_signal_library | 0.92 | False | duplicate_id:SIG-000526 | Rejected |
| CAND-DA76C8A4F5C8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000525 | Rejected |
| CAND-00972772A4C9 | business_signal_library | 0.88 | False | duplicate_id:SIG-000527 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000528` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
