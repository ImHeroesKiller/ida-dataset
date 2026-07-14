# Candidate Root Cause

**Generated:** 2026-07-14T18:27:40+00:00
**Session:** `SESSION-20260714-712073`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000215`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260714-712073`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000215': 1, 'duplicate_id:SIG-000216': 1, 'duplicate_id:SIG-000218': 1, 'duplicate_id:SIG-000219': 1, 'duplicate_id:SIG-000217': 1}`
- `candidate CAND-85482B986F29 entity_id=SIG-000215 reason=duplicate_id:SIG-000215 conf=0.9`
- `candidate CAND-9E26D78C17C2 entity_id=SIG-000216 reason=duplicate_id:SIG-000216 conf=0.88`
- `candidate CAND-9FE6DEC7F40A entity_id=SIG-000218 reason=duplicate_id:SIG-000218 conf=0.85`
- `candidate CAND-C2EAB3AF971B entity_id=SIG-000219 reason=duplicate_id:SIG-000219 conf=0.9`
- `candidate CAND-C366A6729037 entity_id=SIG-000217 reason=duplicate_id:SIG-000217 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-85482B986F29 | business_signal_library | 0.9 | False | duplicate_id:SIG-000215 | Rejected |
| CAND-9E26D78C17C2 | business_signal_library | 0.88 | False | duplicate_id:SIG-000216 | Rejected |
| CAND-9FE6DEC7F40A | business_signal_library | 0.85 | False | duplicate_id:SIG-000218 | Rejected |
| CAND-C2EAB3AF971B | business_signal_library | 0.9 | False | duplicate_id:SIG-000219 | Rejected |
| CAND-C366A6729037 | business_signal_library | 0.92 | False | duplicate_id:SIG-000217 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000215` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
