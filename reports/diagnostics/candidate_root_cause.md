# Candidate Root Cause

**Generated:** 2026-07-11T21:10:32+00:00
**Session:** `SESSION-20260711-EDE650`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000055`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260711-EDE650`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000055': 1, 'duplicate_id:SIG-000059': 1, 'duplicate_id:SIG-000056': 1, 'duplicate_id:SIG-000057': 1, 'duplicate_id:SIG-000058': 1}`
- `candidate CAND-7A26546AE0E6 entity_id=SIG-000055 reason=duplicate_id:SIG-000055 conf=0.9`
- `candidate CAND-A389E1A938FA entity_id=SIG-000059 reason=duplicate_id:SIG-000059 conf=0.92`
- `candidate CAND-DD58471BEAE1 entity_id=SIG-000056 reason=duplicate_id:SIG-000056 conf=0.92`
- `candidate CAND-ED5254A7B5D5 entity_id=SIG-000057 reason=duplicate_id:SIG-000057 conf=0.88`
- `candidate CAND-EBCFF6FBBF0E entity_id=SIG-000058 reason=duplicate_id:SIG-000058 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-7A26546AE0E6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000055 | Rejected |
| CAND-A389E1A938FA | business_signal_library | 0.92 | False | duplicate_id:SIG-000059 | Rejected |
| CAND-DD58471BEAE1 | business_signal_library | 0.92 | False | duplicate_id:SIG-000056 | Rejected |
| CAND-ED5254A7B5D5 | business_signal_library | 0.88 | False | duplicate_id:SIG-000057 | Rejected |
| CAND-EBCFF6FBBF0E | business_signal_library | 0.9 | False | duplicate_id:SIG-000058 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000055` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
