# Candidate Root Cause

**Generated:** 2026-08-18T05:41:35+00:00
**Session:** `SESSION-20260818-C3B071`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000522`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260818-C3B071`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000522': 1, 'duplicate_id:SIG-000525': 1, 'duplicate_id:SIG-000524': 1, 'duplicate_id:SIG-000523': 1, 'duplicate_id:SIG-000521': 1}`
- `candidate CAND-B4F456B0A64B entity_id=SIG-000522 reason=duplicate_id:SIG-000522 conf=0.9`
- `candidate CAND-1F4B63074F09 entity_id=SIG-000525 reason=duplicate_id:SIG-000525 conf=0.9`
- `candidate CAND-006C8BFB9B00 entity_id=SIG-000524 reason=duplicate_id:SIG-000524 conf=0.9`
- `candidate CAND-1284A537B689 entity_id=SIG-000523 reason=duplicate_id:SIG-000523 conf=0.9`
- `candidate CAND-0E9A33F2EA4A entity_id=SIG-000521 reason=duplicate_id:SIG-000521 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B4F456B0A64B | business_signal_library | 0.9 | False | duplicate_id:SIG-000522 | Rejected |
| CAND-1F4B63074F09 | business_signal_library | 0.9 | False | duplicate_id:SIG-000525 | Rejected |
| CAND-006C8BFB9B00 | business_signal_library | 0.9 | False | duplicate_id:SIG-000524 | Rejected |
| CAND-1284A537B689 | business_signal_library | 0.9 | False | duplicate_id:SIG-000523 | Rejected |
| CAND-0E9A33F2EA4A | business_signal_library | 0.92 | False | duplicate_id:SIG-000521 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000522` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
