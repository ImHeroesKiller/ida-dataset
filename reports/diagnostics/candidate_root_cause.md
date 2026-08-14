# Candidate Root Cause

**Generated:** 2026-08-14T15:07:01+00:00
**Session:** `SESSION-20260814-CF4B2E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000118`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260814-CF4B2E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000118': 1, 'duplicate_id:SIG-000120': 1, 'duplicate_id:SIG-000117': 1, 'duplicate_id:SIG-000119': 1, 'duplicate_id:SIG-000116': 1}`
- `candidate CAND-6AF9125B136D entity_id=SIG-000118 reason=duplicate_id:SIG-000118 conf=0.9`
- `candidate CAND-E2C644AB506C entity_id=SIG-000120 reason=duplicate_id:SIG-000120 conf=0.9`
- `candidate CAND-BB3C7668DA1B entity_id=SIG-000117 reason=duplicate_id:SIG-000117 conf=0.9`
- `candidate CAND-779F4892608F entity_id=SIG-000119 reason=duplicate_id:SIG-000119 conf=0.9`
- `candidate CAND-8833C545A578 entity_id=SIG-000116 reason=duplicate_id:SIG-000116 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-6AF9125B136D | business_signal_library | 0.9 | False | duplicate_id:SIG-000118 | Rejected |
| CAND-E2C644AB506C | business_signal_library | 0.9 | False | duplicate_id:SIG-000120 | Rejected |
| CAND-BB3C7668DA1B | business_signal_library | 0.9 | False | duplicate_id:SIG-000117 | Rejected |
| CAND-779F4892608F | business_signal_library | 0.9 | False | duplicate_id:SIG-000119 | Rejected |
| CAND-8833C545A578 | business_signal_library | 0.92 | False | duplicate_id:SIG-000116 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000118` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
