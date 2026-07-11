# Candidate Root Cause

**Generated:** 2026-07-11T22:15:37+00:00
**Session:** `SESSION-20260711-4D5D42`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000063`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260711-4D5D42`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000063': 1, 'duplicate_id:SIG-000061': 1, 'duplicate_id:SIG-000060': 1, 'duplicate_id:SIG-000062': 1, 'duplicate_id:SIG-000064': 1}`
- `candidate CAND-E03F85458730 entity_id=SIG-000063 reason=duplicate_id:SIG-000063 conf=0.88`
- `candidate CAND-F556140ED8F3 entity_id=SIG-000061 reason=duplicate_id:SIG-000061 conf=0.85`
- `candidate CAND-E85253D083C6 entity_id=SIG-000060 reason=duplicate_id:SIG-000060 conf=0.9`
- `candidate CAND-FE1019F45EAB entity_id=SIG-000062 reason=duplicate_id:SIG-000062 conf=0.92`
- `candidate CAND-67DC6F00E281 entity_id=SIG-000064 reason=duplicate_id:SIG-000064 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-E03F85458730 | business_signal_library | 0.88 | False | duplicate_id:SIG-000063 | Rejected |
| CAND-F556140ED8F3 | business_signal_library | 0.85 | False | duplicate_id:SIG-000061 | Rejected |
| CAND-E85253D083C6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000060 | Rejected |
| CAND-FE1019F45EAB | business_signal_library | 0.92 | False | duplicate_id:SIG-000062 | Rejected |
| CAND-67DC6F00E281 | business_signal_library | 0.9 | False | duplicate_id:SIG-000064 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000063` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
