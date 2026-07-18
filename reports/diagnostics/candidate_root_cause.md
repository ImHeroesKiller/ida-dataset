# Candidate Root Cause

**Generated:** 2026-07-18T02:55:46+00:00
**Session:** `SESSION-20260718-18597D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000414`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260718-18597D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000414': 1, 'duplicate_id:SIG-000411': 1, 'duplicate_id:SIG-000410': 1, 'duplicate_id:SIG-000413': 1, 'duplicate_id:SIG-000412': 1}`
- `candidate CAND-DB4D2A6237B1 entity_id=SIG-000414 reason=duplicate_id:SIG-000414 conf=0.92`
- `candidate CAND-ABD3CF26FE51 entity_id=SIG-000411 reason=duplicate_id:SIG-000411 conf=0.92`
- `candidate CAND-3BC014FA05DB entity_id=SIG-000410 reason=duplicate_id:SIG-000410 conf=0.9`
- `candidate CAND-62C6AD0BF6E5 entity_id=SIG-000413 reason=duplicate_id:SIG-000413 conf=0.9`
- `candidate CAND-A30EA4659347 entity_id=SIG-000412 reason=duplicate_id:SIG-000412 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-DB4D2A6237B1 | business_signal_library | 0.92 | False | duplicate_id:SIG-000414 | Rejected |
| CAND-ABD3CF26FE51 | business_signal_library | 0.92 | False | duplicate_id:SIG-000411 | Rejected |
| CAND-3BC014FA05DB | business_signal_library | 0.9 | False | duplicate_id:SIG-000410 | Rejected |
| CAND-62C6AD0BF6E5 | business_signal_library | 0.9 | False | duplicate_id:SIG-000413 | Rejected |
| CAND-A30EA4659347 | business_signal_library | 0.88 | False | duplicate_id:SIG-000412 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000414` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
