# Candidate Root Cause

**Generated:** 2026-08-20T08:01:01+00:00
**Session:** `SESSION-20260820-C51A55`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000761`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260820-C51A55`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000761': 1, 'duplicate_id:SIG-000765': 1, 'duplicate_id:SIG-000762': 1, 'duplicate_id:SIG-000763': 1, 'duplicate_id:SIG-000764': 1}`
- `candidate CAND-0B8E0E9C9EF8 entity_id=SIG-000761 reason=duplicate_id:SIG-000761 conf=0.92`
- `candidate CAND-D99F0A199EB5 entity_id=SIG-000765 reason=duplicate_id:SIG-000765 conf=0.9`
- `candidate CAND-47D948E325CE entity_id=SIG-000762 reason=duplicate_id:SIG-000762 conf=0.9`
- `candidate CAND-367DECCCEB56 entity_id=SIG-000763 reason=duplicate_id:SIG-000763 conf=0.9`
- `candidate CAND-1E029C32BF84 entity_id=SIG-000764 reason=duplicate_id:SIG-000764 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-0B8E0E9C9EF8 | business_signal_library | 0.92 | False | duplicate_id:SIG-000761 | Rejected |
| CAND-D99F0A199EB5 | business_signal_library | 0.9 | False | duplicate_id:SIG-000765 | Rejected |
| CAND-47D948E325CE | business_signal_library | 0.9 | False | duplicate_id:SIG-000762 | Rejected |
| CAND-367DECCCEB56 | business_signal_library | 0.9 | False | duplicate_id:SIG-000763 | Rejected |
| CAND-1E029C32BF84 | business_signal_library | 0.9 | False | duplicate_id:SIG-000764 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000761` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
