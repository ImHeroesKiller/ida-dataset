# Candidate Root Cause

**Generated:** 2026-08-20T14:54:27+00:00
**Session:** `SESSION-20260820-8FD4D5`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000800`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260820-8FD4D5`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000800': 1, 'duplicate_id:SIG-000797': 1, 'duplicate_id:SIG-000799': 1, 'duplicate_id:SIG-000798': 1, 'duplicate_id:SIG-000796': 1}`
- `candidate CAND-5637907089A3 entity_id=SIG-000800 reason=duplicate_id:SIG-000800 conf=0.9`
- `candidate CAND-E1D8AFDC5C75 entity_id=SIG-000797 reason=duplicate_id:SIG-000797 conf=0.9`
- `candidate CAND-719E7B94540E entity_id=SIG-000799 reason=duplicate_id:SIG-000799 conf=0.9`
- `candidate CAND-D08A7DDA6D5C entity_id=SIG-000798 reason=duplicate_id:SIG-000798 conf=0.9`
- `candidate CAND-A98544D130C2 entity_id=SIG-000796 reason=duplicate_id:SIG-000796 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5637907089A3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000800 | Rejected |
| CAND-E1D8AFDC5C75 | business_signal_library | 0.9 | False | duplicate_id:SIG-000797 | Rejected |
| CAND-719E7B94540E | business_signal_library | 0.9 | False | duplicate_id:SIG-000799 | Rejected |
| CAND-D08A7DDA6D5C | business_signal_library | 0.9 | False | duplicate_id:SIG-000798 | Rejected |
| CAND-A98544D130C2 | business_signal_library | 0.92 | False | duplicate_id:SIG-000796 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000800` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
