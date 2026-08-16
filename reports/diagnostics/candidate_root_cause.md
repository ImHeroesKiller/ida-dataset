# Candidate Root Cause

**Generated:** 2026-08-16T21:32:16+00:00
**Session:** `SESSION-20260816-6F667B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000377`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260816-6F667B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000377': 1, 'duplicate_id:SIG-000376': 1, 'duplicate_id:SIG-000378': 1, 'duplicate_id:SIG-000380': 1, 'duplicate_id:SIG-000379': 1}`
- `candidate CAND-F02E302B5EC9 entity_id=SIG-000377 reason=duplicate_id:SIG-000377 conf=0.9`
- `candidate CAND-1A7643E1F3D1 entity_id=SIG-000376 reason=duplicate_id:SIG-000376 conf=0.92`
- `candidate CAND-DF7E5A75D23C entity_id=SIG-000378 reason=duplicate_id:SIG-000378 conf=0.9`
- `candidate CAND-358E363D512F entity_id=SIG-000380 reason=duplicate_id:SIG-000380 conf=0.9`
- `candidate CAND-44BED1CBE4EB entity_id=SIG-000379 reason=duplicate_id:SIG-000379 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F02E302B5EC9 | business_signal_library | 0.9 | False | duplicate_id:SIG-000377 | Rejected |
| CAND-1A7643E1F3D1 | business_signal_library | 0.92 | False | duplicate_id:SIG-000376 | Rejected |
| CAND-DF7E5A75D23C | business_signal_library | 0.9 | False | duplicate_id:SIG-000378 | Rejected |
| CAND-358E363D512F | business_signal_library | 0.9 | False | duplicate_id:SIG-000380 | Rejected |
| CAND-44BED1CBE4EB | business_signal_library | 0.9 | False | duplicate_id:SIG-000379 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000377` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
