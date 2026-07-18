# Candidate Root Cause

**Generated:** 2026-07-18T00:13:17+00:00
**Session:** `SESSION-20260717-FE9BF6`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000409`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260717-FE9BF6`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000409': 1, 'duplicate_id:SIG-000408': 1, 'duplicate_id:SIG-000407': 1, 'duplicate_id:SIG-000406': 1, 'duplicate_id:SIG-000405': 1}`
- `candidate CAND-2579CEF9131B entity_id=SIG-000409 reason=duplicate_id:SIG-000409 conf=0.92`
- `candidate CAND-BAEC0C237D19 entity_id=SIG-000408 reason=duplicate_id:SIG-000408 conf=0.9`
- `candidate CAND-BAD46F2FFC45 entity_id=SIG-000407 reason=duplicate_id:SIG-000407 conf=0.88`
- `candidate CAND-51BBBA2451C8 entity_id=SIG-000406 reason=duplicate_id:SIG-000406 conf=0.92`
- `candidate CAND-E5A3B0E6E924 entity_id=SIG-000405 reason=duplicate_id:SIG-000405 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-2579CEF9131B | business_signal_library | 0.92 | False | duplicate_id:SIG-000409 | Rejected |
| CAND-BAEC0C237D19 | business_signal_library | 0.9 | False | duplicate_id:SIG-000408 | Rejected |
| CAND-BAD46F2FFC45 | business_signal_library | 0.88 | False | duplicate_id:SIG-000407 | Rejected |
| CAND-51BBBA2451C8 | business_signal_library | 0.92 | False | duplicate_id:SIG-000406 | Rejected |
| CAND-E5A3B0E6E924 | business_signal_library | 0.9 | False | duplicate_id:SIG-000405 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000409` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
