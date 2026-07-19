# Candidate Root Cause

**Generated:** 2026-07-19T18:16:24+00:00
**Session:** `SESSION-20260719-A2853E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000521`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260719-A2853E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000521': 1, 'duplicate_id:SIG-000524': 1, 'duplicate_id:SIG-000523': 1, 'duplicate_id:SIG-000520': 1, 'duplicate_id:SIG-000522': 1}`
- `candidate CAND-1582951385A0 entity_id=SIG-000521 reason=duplicate_id:SIG-000521 conf=0.92`
- `candidate CAND-6F91A10D9186 entity_id=SIG-000524 reason=duplicate_id:SIG-000524 conf=0.92`
- `candidate CAND-F050633DDA29 entity_id=SIG-000523 reason=duplicate_id:SIG-000523 conf=0.9`
- `candidate CAND-12331F57BE8D entity_id=SIG-000520 reason=duplicate_id:SIG-000520 conf=0.9`
- `candidate CAND-19F03DA96422 entity_id=SIG-000522 reason=duplicate_id:SIG-000522 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-1582951385A0 | business_signal_library | 0.92 | False | duplicate_id:SIG-000521 | Rejected |
| CAND-6F91A10D9186 | business_signal_library | 0.92 | False | duplicate_id:SIG-000524 | Rejected |
| CAND-F050633DDA29 | business_signal_library | 0.9 | False | duplicate_id:SIG-000523 | Rejected |
| CAND-12331F57BE8D | business_signal_library | 0.9 | False | duplicate_id:SIG-000520 | Rejected |
| CAND-19F03DA96422 | business_signal_library | 0.88 | False | duplicate_id:SIG-000522 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000521` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
