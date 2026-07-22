# Candidate Root Cause

**Generated:** 2026-07-22T17:44:57+00:00
**Session:** `SESSION-20260722-A83C8F`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000692`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260722-A83C8F`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000692': 1, 'duplicate_id:SIG-000691': 1, 'duplicate_id:SIG-000690': 1, 'duplicate_id:SIG-000694': 1, 'duplicate_id:SIG-000693': 1}`
- `candidate CAND-9248F988AF6F entity_id=SIG-000692 reason=duplicate_id:SIG-000692 conf=0.88`
- `candidate CAND-F997F31C1E4B entity_id=SIG-000691 reason=duplicate_id:SIG-000691 conf=0.92`
- `candidate CAND-A0155041660E entity_id=SIG-000690 reason=duplicate_id:SIG-000690 conf=0.9`
- `candidate CAND-FCA5FD99BDA3 entity_id=SIG-000694 reason=duplicate_id:SIG-000694 conf=0.92`
- `candidate CAND-B0EFBCFC0B6A entity_id=SIG-000693 reason=duplicate_id:SIG-000693 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-9248F988AF6F | business_signal_library | 0.88 | False | duplicate_id:SIG-000692 | Rejected |
| CAND-F997F31C1E4B | business_signal_library | 0.92 | False | duplicate_id:SIG-000691 | Rejected |
| CAND-A0155041660E | business_signal_library | 0.9 | False | duplicate_id:SIG-000690 | Rejected |
| CAND-FCA5FD99BDA3 | business_signal_library | 0.92 | False | duplicate_id:SIG-000694 | Rejected |
| CAND-B0EFBCFC0B6A | business_signal_library | 0.9 | False | duplicate_id:SIG-000693 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000692` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
