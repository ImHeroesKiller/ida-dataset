# Candidate Root Cause

**Generated:** 2026-08-08T21:52:02+00:00
**Session:** `SESSION-20260808-9D139C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001662`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260808-9D139C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001662': 1, 'duplicate_id:SIG-001663': 1, 'duplicate_id:SIG-001661': 1, 'duplicate_id:SIG-001664': 1, 'duplicate_id:SIG-001660': 1}`
- `candidate CAND-A3CB4730DAAB entity_id=SIG-001662 reason=duplicate_id:SIG-001662 conf=0.88`
- `candidate CAND-B125D63595FF entity_id=SIG-001663 reason=duplicate_id:SIG-001663 conf=0.9`
- `candidate CAND-ADBEF1D74842 entity_id=SIG-001661 reason=duplicate_id:SIG-001661 conf=0.92`
- `candidate CAND-B2D4E8A05C4F entity_id=SIG-001664 reason=duplicate_id:SIG-001664 conf=0.92`
- `candidate CAND-FD6D13FEC24B entity_id=SIG-001660 reason=duplicate_id:SIG-001660 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A3CB4730DAAB | business_signal_library | 0.88 | False | duplicate_id:SIG-001662 | Rejected |
| CAND-B125D63595FF | business_signal_library | 0.9 | False | duplicate_id:SIG-001663 | Rejected |
| CAND-ADBEF1D74842 | business_signal_library | 0.92 | False | duplicate_id:SIG-001661 | Rejected |
| CAND-B2D4E8A05C4F | business_signal_library | 0.92 | False | duplicate_id:SIG-001664 | Rejected |
| CAND-FD6D13FEC24B | business_signal_library | 0.9 | False | duplicate_id:SIG-001660 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001662` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
