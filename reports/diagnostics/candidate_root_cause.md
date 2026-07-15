# Candidate Root Cause

**Generated:** 2026-07-15T11:16:54+00:00
**Session:** `SESSION-20260715-EA566F`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000250`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260715-EA566F`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000250': 1, 'duplicate_id:SIG-000252': 1, 'duplicate_id:SIG-000254': 1, 'duplicate_id:SIG-000253': 1, 'duplicate_id:SIG-000251': 1}`
- `candidate CAND-2D8A81CCB806 entity_id=SIG-000250 reason=duplicate_id:SIG-000250 conf=0.9`
- `candidate CAND-517F72A8C9B6 entity_id=SIG-000252 reason=duplicate_id:SIG-000252 conf=0.92`
- `candidate CAND-F3BB1542ED2A entity_id=SIG-000254 reason=duplicate_id:SIG-000254 conf=0.9`
- `candidate CAND-511785536996 entity_id=SIG-000253 reason=duplicate_id:SIG-000253 conf=0.85`
- `candidate CAND-FF817076E24D entity_id=SIG-000251 reason=duplicate_id:SIG-000251 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-2D8A81CCB806 | business_signal_library | 0.9 | False | duplicate_id:SIG-000250 | Rejected |
| CAND-517F72A8C9B6 | business_signal_library | 0.92 | False | duplicate_id:SIG-000252 | Rejected |
| CAND-F3BB1542ED2A | business_signal_library | 0.9 | False | duplicate_id:SIG-000254 | Rejected |
| CAND-511785536996 | business_signal_library | 0.85 | False | duplicate_id:SIG-000253 | Rejected |
| CAND-FF817076E24D | business_signal_library | 0.88 | False | duplicate_id:SIG-000251 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000250` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
