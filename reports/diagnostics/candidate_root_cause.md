# Candidate Root Cause

**Generated:** 2026-08-03T16:48:04+00:00
**Session:** `SESSION-20260803-23B01C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001329`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260803-23B01C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001329': 1, 'duplicate_id:SIG-001328': 1, 'duplicate_id:SIG-001327': 1, 'duplicate_id:SIG-001325': 1, 'duplicate_id:SIG-001326': 1}`
- `candidate CAND-A721F831CF0C entity_id=SIG-001329 reason=duplicate_id:SIG-001329 conf=0.92`
- `candidate CAND-1F194DE2067E entity_id=SIG-001328 reason=duplicate_id:SIG-001328 conf=0.9`
- `candidate CAND-1391A586A69E entity_id=SIG-001327 reason=duplicate_id:SIG-001327 conf=0.88`
- `candidate CAND-21A8947C1915 entity_id=SIG-001325 reason=duplicate_id:SIG-001325 conf=0.9`
- `candidate CAND-1B8C48FFF932 entity_id=SIG-001326 reason=duplicate_id:SIG-001326 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A721F831CF0C | business_signal_library | 0.92 | False | duplicate_id:SIG-001329 | Rejected |
| CAND-1F194DE2067E | business_signal_library | 0.9 | False | duplicate_id:SIG-001328 | Rejected |
| CAND-1391A586A69E | business_signal_library | 0.88 | False | duplicate_id:SIG-001327 | Rejected |
| CAND-21A8947C1915 | business_signal_library | 0.9 | False | duplicate_id:SIG-001325 | Rejected |
| CAND-1B8C48FFF932 | business_signal_library | 0.92 | False | duplicate_id:SIG-001326 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001329` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
