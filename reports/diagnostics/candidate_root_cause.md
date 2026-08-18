# Candidate Root Cause

**Generated:** 2026-08-18T04:46:59+00:00
**Session:** `SESSION-20260818-ECDA21`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000518`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260818-ECDA21`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000518': 1, 'duplicate_id:SIG-000517': 1, 'duplicate_id:SIG-000519': 1, 'duplicate_id:SIG-000516': 1, 'duplicate_id:SIG-000520': 1}`
- `candidate CAND-12C2F8F0AF94 entity_id=SIG-000518 reason=duplicate_id:SIG-000518 conf=0.9`
- `candidate CAND-8BF3274214D4 entity_id=SIG-000517 reason=duplicate_id:SIG-000517 conf=0.9`
- `candidate CAND-48685C4FDC9C entity_id=SIG-000519 reason=duplicate_id:SIG-000519 conf=0.9`
- `candidate CAND-D7879C4BE78D entity_id=SIG-000516 reason=duplicate_id:SIG-000516 conf=0.92`
- `candidate CAND-2FCB87764635 entity_id=SIG-000520 reason=duplicate_id:SIG-000520 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-12C2F8F0AF94 | business_signal_library | 0.9 | False | duplicate_id:SIG-000518 | Rejected |
| CAND-8BF3274214D4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000517 | Rejected |
| CAND-48685C4FDC9C | business_signal_library | 0.9 | False | duplicate_id:SIG-000519 | Rejected |
| CAND-D7879C4BE78D | business_signal_library | 0.92 | False | duplicate_id:SIG-000516 | Rejected |
| CAND-2FCB87764635 | business_signal_library | 0.9 | False | duplicate_id:SIG-000520 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000518` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
