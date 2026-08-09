# Candidate Root Cause

**Generated:** 2026-08-09T02:10:01+00:00
**Session:** `SESSION-20260809-23E887`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001678`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260809-23E887`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001678': 1, 'duplicate_id:SIG-001679': 1, 'duplicate_id:SIG-001676': 1, 'duplicate_id:SIG-001675': 1, 'duplicate_id:SIG-001677': 1}`
- `candidate CAND-575EA6E16423 entity_id=SIG-001678 reason=duplicate_id:SIG-001678 conf=0.9`
- `candidate CAND-592C40F56EBF entity_id=SIG-001679 reason=duplicate_id:SIG-001679 conf=0.92`
- `candidate CAND-101BF0FE925F entity_id=SIG-001676 reason=duplicate_id:SIG-001676 conf=0.92`
- `candidate CAND-83D6FEA2B5CA entity_id=SIG-001675 reason=duplicate_id:SIG-001675 conf=0.9`
- `candidate CAND-7BD775B6FCEF entity_id=SIG-001677 reason=duplicate_id:SIG-001677 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-575EA6E16423 | business_signal_library | 0.9 | False | duplicate_id:SIG-001678 | Rejected |
| CAND-592C40F56EBF | business_signal_library | 0.92 | False | duplicate_id:SIG-001679 | Rejected |
| CAND-101BF0FE925F | business_signal_library | 0.92 | False | duplicate_id:SIG-001676 | Rejected |
| CAND-83D6FEA2B5CA | business_signal_library | 0.9 | False | duplicate_id:SIG-001675 | Rejected |
| CAND-7BD775B6FCEF | business_signal_library | 0.88 | False | duplicate_id:SIG-001677 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001678` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
