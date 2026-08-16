# Candidate Root Cause

**Generated:** 2026-08-16T05:44:26+00:00
**Session:** `SESSION-20260816-987E36`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000300`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260816-987E36`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000300': 1, 'duplicate_id:SIG-000299': 1, 'duplicate_id:SIG-000297': 1, 'duplicate_id:SIG-000296': 1, 'duplicate_id:SIG-000298': 1}`
- `candidate CAND-629BD9DE8AD0 entity_id=SIG-000300 reason=duplicate_id:SIG-000300 conf=0.9`
- `candidate CAND-1000F8C8735E entity_id=SIG-000299 reason=duplicate_id:SIG-000299 conf=0.9`
- `candidate CAND-DCE1857412C1 entity_id=SIG-000297 reason=duplicate_id:SIG-000297 conf=0.9`
- `candidate CAND-550E258BC12F entity_id=SIG-000296 reason=duplicate_id:SIG-000296 conf=0.92`
- `candidate CAND-BD68B9172CBB entity_id=SIG-000298 reason=duplicate_id:SIG-000298 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-629BD9DE8AD0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000300 | Rejected |
| CAND-1000F8C8735E | business_signal_library | 0.9 | False | duplicate_id:SIG-000299 | Rejected |
| CAND-DCE1857412C1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000297 | Rejected |
| CAND-550E258BC12F | business_signal_library | 0.92 | False | duplicate_id:SIG-000296 | Rejected |
| CAND-BD68B9172CBB | business_signal_library | 0.9 | False | duplicate_id:SIG-000298 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000300` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
