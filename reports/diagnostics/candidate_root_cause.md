# Candidate Root Cause

**Generated:** 2026-08-07T23:00:55+00:00
**Session:** `SESSION-20260807-46CA6E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001555`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260807-46CA6E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001555': 1, 'duplicate_id:SIG-001557': 1, 'duplicate_id:SIG-001556': 1, 'duplicate_id:SIG-001558': 1, 'duplicate_id:SIG-001559': 1}`
- `candidate CAND-F5B292DB96AF entity_id=SIG-001555 reason=duplicate_id:SIG-001555 conf=0.9`
- `candidate CAND-3DF822B3AB80 entity_id=SIG-001557 reason=duplicate_id:SIG-001557 conf=0.88`
- `candidate CAND-DA85F65DDD4C entity_id=SIG-001556 reason=duplicate_id:SIG-001556 conf=0.92`
- `candidate CAND-E19474CBCB52 entity_id=SIG-001558 reason=duplicate_id:SIG-001558 conf=0.9`
- `candidate CAND-311FE7DD8EA9 entity_id=SIG-001559 reason=duplicate_id:SIG-001559 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F5B292DB96AF | business_signal_library | 0.9 | False | duplicate_id:SIG-001555 | Rejected |
| CAND-3DF822B3AB80 | business_signal_library | 0.88 | False | duplicate_id:SIG-001557 | Rejected |
| CAND-DA85F65DDD4C | business_signal_library | 0.92 | False | duplicate_id:SIG-001556 | Rejected |
| CAND-E19474CBCB52 | business_signal_library | 0.9 | False | duplicate_id:SIG-001558 | Rejected |
| CAND-311FE7DD8EA9 | business_signal_library | 0.92 | False | duplicate_id:SIG-001559 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001555` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
