# Candidate Root Cause

**Generated:** 2026-07-15T18:31:21+00:00
**Session:** `SESSION-20260715-A8C770`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000274`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260715-A8C770`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000274': 1, 'duplicate_id:SIG-000273': 1, 'duplicate_id:SIG-000271': 1, 'duplicate_id:SIG-000272': 1, 'duplicate_id:SIG-000270': 1}`
- `candidate CAND-64C18FF07A8C entity_id=SIG-000274 reason=duplicate_id:SIG-000274 conf=0.9`
- `candidate CAND-0861753BB225 entity_id=SIG-000273 reason=duplicate_id:SIG-000273 conf=0.85`
- `candidate CAND-EC98EFAD5D20 entity_id=SIG-000271 reason=duplicate_id:SIG-000271 conf=0.88`
- `candidate CAND-9F631544185E entity_id=SIG-000272 reason=duplicate_id:SIG-000272 conf=0.92`
- `candidate CAND-19F6DC628967 entity_id=SIG-000270 reason=duplicate_id:SIG-000270 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-64C18FF07A8C | business_signal_library | 0.9 | False | duplicate_id:SIG-000274 | Rejected |
| CAND-0861753BB225 | business_signal_library | 0.85 | False | duplicate_id:SIG-000273 | Rejected |
| CAND-EC98EFAD5D20 | business_signal_library | 0.88 | False | duplicate_id:SIG-000271 | Rejected |
| CAND-9F631544185E | business_signal_library | 0.92 | False | duplicate_id:SIG-000272 | Rejected |
| CAND-19F6DC628967 | business_signal_library | 0.9 | False | duplicate_id:SIG-000270 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000274` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
