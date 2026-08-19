# Candidate Root Cause

**Generated:** 2026-08-19T09:54:14+00:00
**Session:** `SESSION-20260819-BE2D7A`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000657`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260819-BE2D7A`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000657': 1, 'duplicate_id:SIG-000658': 1, 'duplicate_id:SIG-000660': 1, 'duplicate_id:SIG-000656': 1, 'duplicate_id:SIG-000659': 1}`
- `candidate CAND-4D9509F76F88 entity_id=SIG-000657 reason=duplicate_id:SIG-000657 conf=0.9`
- `candidate CAND-16E0F0017282 entity_id=SIG-000658 reason=duplicate_id:SIG-000658 conf=0.9`
- `candidate CAND-D60A26CE580C entity_id=SIG-000660 reason=duplicate_id:SIG-000660 conf=0.9`
- `candidate CAND-178B313E1B52 entity_id=SIG-000656 reason=duplicate_id:SIG-000656 conf=0.92`
- `candidate CAND-4C7EF9116D0C entity_id=SIG-000659 reason=duplicate_id:SIG-000659 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-4D9509F76F88 | business_signal_library | 0.9 | False | duplicate_id:SIG-000657 | Rejected |
| CAND-16E0F0017282 | business_signal_library | 0.9 | False | duplicate_id:SIG-000658 | Rejected |
| CAND-D60A26CE580C | business_signal_library | 0.9 | False | duplicate_id:SIG-000660 | Rejected |
| CAND-178B313E1B52 | business_signal_library | 0.92 | False | duplicate_id:SIG-000656 | Rejected |
| CAND-4C7EF9116D0C | business_signal_library | 0.9 | False | duplicate_id:SIG-000659 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000657` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
