# Candidate Root Cause

**Generated:** 2026-07-30T16:47:07+00:00
**Session:** `SESSION-20260730-59B7AA`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001110`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260730-59B7AA`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001110': 1, 'duplicate_id:SIG-001112': 1, 'duplicate_id:SIG-001113': 1, 'duplicate_id:SIG-001114': 1, 'duplicate_id:SIG-001111': 1}`
- `candidate CAND-407122850648 entity_id=SIG-001110 reason=duplicate_id:SIG-001110 conf=0.9`
- `candidate CAND-82F7532AEFAC entity_id=SIG-001112 reason=duplicate_id:SIG-001112 conf=0.88`
- `candidate CAND-5362ED51506C entity_id=SIG-001113 reason=duplicate_id:SIG-001113 conf=0.9`
- `candidate CAND-9A027E7A50B6 entity_id=SIG-001114 reason=duplicate_id:SIG-001114 conf=0.92`
- `candidate CAND-F116DFEA6F4E entity_id=SIG-001111 reason=duplicate_id:SIG-001111 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-407122850648 | business_signal_library | 0.9 | False | duplicate_id:SIG-001110 | Rejected |
| CAND-82F7532AEFAC | business_signal_library | 0.88 | False | duplicate_id:SIG-001112 | Rejected |
| CAND-5362ED51506C | business_signal_library | 0.9 | False | duplicate_id:SIG-001113 | Rejected |
| CAND-9A027E7A50B6 | business_signal_library | 0.92 | False | duplicate_id:SIG-001114 | Rejected |
| CAND-F116DFEA6F4E | business_signal_library | 0.92 | False | duplicate_id:SIG-001111 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001110` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
