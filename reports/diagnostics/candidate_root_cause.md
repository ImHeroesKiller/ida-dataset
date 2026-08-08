# Candidate Root Cause

**Generated:** 2026-08-08T06:09:21+00:00
**Session:** `SESSION-20260808-D9A00F`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001580`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260808-D9A00F`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001580': 1, 'duplicate_id:SIG-001584': 1, 'duplicate_id:SIG-001581': 1, 'duplicate_id:SIG-001582': 1, 'duplicate_id:SIG-001583': 1}`
- `candidate CAND-4FBF63E4F9E3 entity_id=SIG-001580 reason=duplicate_id:SIG-001580 conf=0.9`
- `candidate CAND-BE6D3FB97AE2 entity_id=SIG-001584 reason=duplicate_id:SIG-001584 conf=0.92`
- `candidate CAND-5B6B79CF546A entity_id=SIG-001581 reason=duplicate_id:SIG-001581 conf=0.92`
- `candidate CAND-3E51C7A93E95 entity_id=SIG-001582 reason=duplicate_id:SIG-001582 conf=0.88`
- `candidate CAND-D4AB08B7B879 entity_id=SIG-001583 reason=duplicate_id:SIG-001583 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-4FBF63E4F9E3 | business_signal_library | 0.9 | False | duplicate_id:SIG-001580 | Rejected |
| CAND-BE6D3FB97AE2 | business_signal_library | 0.92 | False | duplicate_id:SIG-001584 | Rejected |
| CAND-5B6B79CF546A | business_signal_library | 0.92 | False | duplicate_id:SIG-001581 | Rejected |
| CAND-3E51C7A93E95 | business_signal_library | 0.88 | False | duplicate_id:SIG-001582 | Rejected |
| CAND-D4AB08B7B879 | business_signal_library | 0.9 | False | duplicate_id:SIG-001583 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001580` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
