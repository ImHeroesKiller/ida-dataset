# Candidate Root Cause

**Generated:** 2026-07-18T17:31:08+00:00
**Session:** `SESSION-20260718-B7CC9B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000451`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260718-B7CC9B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000451': 1, 'duplicate_id:SIG-000454': 1, 'duplicate_id:SIG-000453': 1, 'duplicate_id:SIG-000450': 1, 'duplicate_id:SIG-000452': 1}`
- `candidate CAND-36DE50535C89 entity_id=SIG-000451 reason=duplicate_id:SIG-000451 conf=0.92`
- `candidate CAND-AAF79817E0F5 entity_id=SIG-000454 reason=duplicate_id:SIG-000454 conf=0.92`
- `candidate CAND-062184970B6C entity_id=SIG-000453 reason=duplicate_id:SIG-000453 conf=0.9`
- `candidate CAND-FD6D7F497FB8 entity_id=SIG-000450 reason=duplicate_id:SIG-000450 conf=0.9`
- `candidate CAND-EEF98DC3EFBE entity_id=SIG-000452 reason=duplicate_id:SIG-000452 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-36DE50535C89 | business_signal_library | 0.92 | False | duplicate_id:SIG-000451 | Rejected |
| CAND-AAF79817E0F5 | business_signal_library | 0.92 | False | duplicate_id:SIG-000454 | Rejected |
| CAND-062184970B6C | business_signal_library | 0.9 | False | duplicate_id:SIG-000453 | Rejected |
| CAND-FD6D7F497FB8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000450 | Rejected |
| CAND-EEF98DC3EFBE | business_signal_library | 0.88 | False | duplicate_id:SIG-000452 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000451` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
