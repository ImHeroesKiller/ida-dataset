# Candidate Root Cause

**Generated:** 2026-07-22T00:21:12+00:00
**Session:** `SESSION-20260722-28DDA8`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000656`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260722-28DDA8`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000656': 1, 'duplicate_id:SIG-000659': 1, 'duplicate_id:SIG-000658': 1, 'duplicate_id:SIG-000657': 1, 'duplicate_id:SIG-000655': 1}`
- `candidate CAND-5989B725D1FF entity_id=SIG-000656 reason=duplicate_id:SIG-000656 conf=0.92`
- `candidate CAND-2B8BDED90566 entity_id=SIG-000659 reason=duplicate_id:SIG-000659 conf=0.92`
- `candidate CAND-2BF416D44F71 entity_id=SIG-000658 reason=duplicate_id:SIG-000658 conf=0.9`
- `candidate CAND-C9E95C91583A entity_id=SIG-000657 reason=duplicate_id:SIG-000657 conf=0.88`
- `candidate CAND-474B8ECEE4BF entity_id=SIG-000655 reason=duplicate_id:SIG-000655 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5989B725D1FF | business_signal_library | 0.92 | False | duplicate_id:SIG-000656 | Rejected |
| CAND-2B8BDED90566 | business_signal_library | 0.92 | False | duplicate_id:SIG-000659 | Rejected |
| CAND-2BF416D44F71 | business_signal_library | 0.9 | False | duplicate_id:SIG-000658 | Rejected |
| CAND-C9E95C91583A | business_signal_library | 0.88 | False | duplicate_id:SIG-000657 | Rejected |
| CAND-474B8ECEE4BF | business_signal_library | 0.9 | False | duplicate_id:SIG-000655 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000656` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
