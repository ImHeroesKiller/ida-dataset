# Candidate Root Cause

**Generated:** 2026-08-19T05:46:50+00:00
**Session:** `SESSION-20260819-53B3C6`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000639`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260819-53B3C6`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000639': 1, 'duplicate_id:SIG-000640': 1, 'duplicate_id:SIG-000638': 1, 'duplicate_id:SIG-000637': 1, 'duplicate_id:SIG-000636': 1}`
- `candidate CAND-7A4E83141B2D entity_id=SIG-000639 reason=duplicate_id:SIG-000639 conf=0.9`
- `candidate CAND-E776D55EBAB4 entity_id=SIG-000640 reason=duplicate_id:SIG-000640 conf=0.9`
- `candidate CAND-77FD8E8B9131 entity_id=SIG-000638 reason=duplicate_id:SIG-000638 conf=0.9`
- `candidate CAND-36D22A24F30F entity_id=SIG-000637 reason=duplicate_id:SIG-000637 conf=0.9`
- `candidate CAND-0F29392DE13A entity_id=SIG-000636 reason=duplicate_id:SIG-000636 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-7A4E83141B2D | business_signal_library | 0.9 | False | duplicate_id:SIG-000639 | Rejected |
| CAND-E776D55EBAB4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000640 | Rejected |
| CAND-77FD8E8B9131 | business_signal_library | 0.9 | False | duplicate_id:SIG-000638 | Rejected |
| CAND-36D22A24F30F | business_signal_library | 0.9 | False | duplicate_id:SIG-000637 | Rejected |
| CAND-0F29392DE13A | business_signal_library | 0.92 | False | duplicate_id:SIG-000636 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000639` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
