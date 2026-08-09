# Candidate Root Cause

**Generated:** 2026-08-09T04:02:43+00:00
**Session:** `SESSION-20260809-EAD308`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001680`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260809-EAD308`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001680': 1, 'duplicate_id:SIG-001683': 1, 'duplicate_id:SIG-001681': 1, 'duplicate_id:SIG-001682': 1, 'duplicate_id:SIG-001684': 1}`
- `candidate CAND-BEEF1AB8693D entity_id=SIG-001680 reason=duplicate_id:SIG-001680 conf=0.9`
- `candidate CAND-B40443B3DEED entity_id=SIG-001683 reason=duplicate_id:SIG-001683 conf=0.9`
- `candidate CAND-B347AB22D51B entity_id=SIG-001681 reason=duplicate_id:SIG-001681 conf=0.92`
- `candidate CAND-CF6C80E0F289 entity_id=SIG-001682 reason=duplicate_id:SIG-001682 conf=0.88`
- `candidate CAND-2D911E3B8AEB entity_id=SIG-001684 reason=duplicate_id:SIG-001684 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-BEEF1AB8693D | business_signal_library | 0.9 | False | duplicate_id:SIG-001680 | Rejected |
| CAND-B40443B3DEED | business_signal_library | 0.9 | False | duplicate_id:SIG-001683 | Rejected |
| CAND-B347AB22D51B | business_signal_library | 0.92 | False | duplicate_id:SIG-001681 | Rejected |
| CAND-CF6C80E0F289 | business_signal_library | 0.88 | False | duplicate_id:SIG-001682 | Rejected |
| CAND-2D911E3B8AEB | business_signal_library | 0.92 | False | duplicate_id:SIG-001684 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001680` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
