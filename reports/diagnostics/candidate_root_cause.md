# Candidate Root Cause

**Generated:** 2026-08-19T15:51:42+00:00
**Session:** `SESSION-20260819-A3AD3A`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000686`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260819-A3AD3A`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000686': 1, 'duplicate_id:SIG-000688': 1, 'duplicate_id:SIG-000687': 1, 'duplicate_id:SIG-000689': 1, 'duplicate_id:SIG-000690': 1}`
- `candidate CAND-2D8B646DDC97 entity_id=SIG-000686 reason=duplicate_id:SIG-000686 conf=0.92`
- `candidate CAND-2F80663B0822 entity_id=SIG-000688 reason=duplicate_id:SIG-000688 conf=0.9`
- `candidate CAND-6E0B55607BB2 entity_id=SIG-000687 reason=duplicate_id:SIG-000687 conf=0.9`
- `candidate CAND-FEB58CFF92F8 entity_id=SIG-000689 reason=duplicate_id:SIG-000689 conf=0.9`
- `candidate CAND-1D8AD745C8D2 entity_id=SIG-000690 reason=duplicate_id:SIG-000690 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-2D8B646DDC97 | business_signal_library | 0.92 | False | duplicate_id:SIG-000686 | Rejected |
| CAND-2F80663B0822 | business_signal_library | 0.9 | False | duplicate_id:SIG-000688 | Rejected |
| CAND-6E0B55607BB2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000687 | Rejected |
| CAND-FEB58CFF92F8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000689 | Rejected |
| CAND-1D8AD745C8D2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000690 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000686` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
