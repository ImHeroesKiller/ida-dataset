# Candidate Root Cause

**Generated:** 2026-08-19T14:04:15+00:00
**Session:** `SESSION-20260819-AE30AE`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000678`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260819-AE30AE`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000678': 1, 'duplicate_id:SIG-000679': 1, 'duplicate_id:SIG-000677': 1, 'duplicate_id:SIG-000676': 1, 'duplicate_id:SIG-000680': 1}`
- `candidate CAND-4F502B549D6D entity_id=SIG-000678 reason=duplicate_id:SIG-000678 conf=0.9`
- `candidate CAND-F0C7223381EE entity_id=SIG-000679 reason=duplicate_id:SIG-000679 conf=0.9`
- `candidate CAND-A5C0E89985C7 entity_id=SIG-000677 reason=duplicate_id:SIG-000677 conf=0.9`
- `candidate CAND-C513FE6FDF82 entity_id=SIG-000676 reason=duplicate_id:SIG-000676 conf=0.92`
- `candidate CAND-1B5691E9F3DD entity_id=SIG-000680 reason=duplicate_id:SIG-000680 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-4F502B549D6D | business_signal_library | 0.9 | False | duplicate_id:SIG-000678 | Rejected |
| CAND-F0C7223381EE | business_signal_library | 0.9 | False | duplicate_id:SIG-000679 | Rejected |
| CAND-A5C0E89985C7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000677 | Rejected |
| CAND-C513FE6FDF82 | business_signal_library | 0.92 | False | duplicate_id:SIG-000676 | Rejected |
| CAND-1B5691E9F3DD | business_signal_library | 0.9 | False | duplicate_id:SIG-000680 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000678` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
