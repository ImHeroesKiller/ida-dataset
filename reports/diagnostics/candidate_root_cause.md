# Candidate Root Cause

**Generated:** 2026-08-13T07:56:14+00:00
**Session:** `SESSION-20260813-542336`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000014`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260813-542336`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000014': 1, 'duplicate_id:SIG-000011': 1, 'duplicate_id:SIG-000013': 1, 'duplicate_id:SIG-000015': 1, 'duplicate_id:SIG-000012': 1}`
- `candidate CAND-DBE3D1344FD9 entity_id=SIG-000014 reason=duplicate_id:SIG-000014 conf=0.9`
- `candidate CAND-FEA4744BBF52 entity_id=SIG-000011 reason=duplicate_id:SIG-000011 conf=0.92`
- `candidate CAND-A3498A1C126E entity_id=SIG-000013 reason=duplicate_id:SIG-000013 conf=0.9`
- `candidate CAND-FD6235ADBE9F entity_id=SIG-000015 reason=duplicate_id:SIG-000015 conf=0.9`
- `candidate CAND-81E787F78E61 entity_id=SIG-000012 reason=duplicate_id:SIG-000012 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-DBE3D1344FD9 | business_signal_library | 0.9 | False | duplicate_id:SIG-000014 | Rejected |
| CAND-FEA4744BBF52 | business_signal_library | 0.92 | False | duplicate_id:SIG-000011 | Rejected |
| CAND-A3498A1C126E | business_signal_library | 0.9 | False | duplicate_id:SIG-000013 | Rejected |
| CAND-FD6235ADBE9F | business_signal_library | 0.9 | False | duplicate_id:SIG-000015 | Rejected |
| CAND-81E787F78E61 | business_signal_library | 0.9 | False | duplicate_id:SIG-000012 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000014` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
