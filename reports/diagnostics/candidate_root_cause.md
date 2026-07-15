# Candidate Root Cause

**Generated:** 2026-07-15T22:23:48+00:00
**Session:** `SESSION-20260715-32351E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000284`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260715-32351E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000284': 1, 'duplicate_id:SIG-000282': 1, 'duplicate_id:SIG-000281': 1, 'duplicate_id:SIG-000283': 1, 'duplicate_id:SIG-000280': 1}`
- `candidate CAND-07B7C916E817 entity_id=SIG-000284 reason=duplicate_id:SIG-000284 conf=0.9`
- `candidate CAND-04C066C3BA7A entity_id=SIG-000282 reason=duplicate_id:SIG-000282 conf=0.88`
- `candidate CAND-F13DFE2C40FF entity_id=SIG-000281 reason=duplicate_id:SIG-000281 conf=0.92`
- `candidate CAND-878167D9920A entity_id=SIG-000283 reason=duplicate_id:SIG-000283 conf=0.85`
- `candidate CAND-A77F3743BE74 entity_id=SIG-000280 reason=duplicate_id:SIG-000280 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-07B7C916E817 | business_signal_library | 0.9 | False | duplicate_id:SIG-000284 | Rejected |
| CAND-04C066C3BA7A | business_signal_library | 0.88 | False | duplicate_id:SIG-000282 | Rejected |
| CAND-F13DFE2C40FF | business_signal_library | 0.92 | False | duplicate_id:SIG-000281 | Rejected |
| CAND-878167D9920A | business_signal_library | 0.85 | False | duplicate_id:SIG-000283 | Rejected |
| CAND-A77F3743BE74 | business_signal_library | 0.9 | False | duplicate_id:SIG-000280 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000284` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
