# Candidate Root Cause

**Generated:** 2026-08-05T00:30:36+00:00
**Session:** `SESSION-20260805-7F7673`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001398`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260805-7F7673`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001398': 1, 'duplicate_id:SIG-001396': 1, 'duplicate_id:SIG-001395': 1, 'duplicate_id:SIG-001397': 1, 'duplicate_id:SIG-001399': 1}`
- `candidate CAND-710CDA0ACF63 entity_id=SIG-001398 reason=duplicate_id:SIG-001398 conf=0.9`
- `candidate CAND-05D50F324CA3 entity_id=SIG-001396 reason=duplicate_id:SIG-001396 conf=0.92`
- `candidate CAND-A5A9227269DB entity_id=SIG-001395 reason=duplicate_id:SIG-001395 conf=0.9`
- `candidate CAND-6D8C5E972987 entity_id=SIG-001397 reason=duplicate_id:SIG-001397 conf=0.88`
- `candidate CAND-594A3D966D95 entity_id=SIG-001399 reason=duplicate_id:SIG-001399 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-710CDA0ACF63 | business_signal_library | 0.9 | False | duplicate_id:SIG-001398 | Rejected |
| CAND-05D50F324CA3 | business_signal_library | 0.92 | False | duplicate_id:SIG-001396 | Rejected |
| CAND-A5A9227269DB | business_signal_library | 0.9 | False | duplicate_id:SIG-001395 | Rejected |
| CAND-6D8C5E972987 | business_signal_library | 0.88 | False | duplicate_id:SIG-001397 | Rejected |
| CAND-594A3D966D95 | business_signal_library | 0.92 | False | duplicate_id:SIG-001399 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001398` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
