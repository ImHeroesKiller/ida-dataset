# Candidate Root Cause

**Generated:** 2026-08-13T19:27:27+00:00
**Session:** `SESSION-20260813-93D19B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000054`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260813-93D19B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000054': 1, 'duplicate_id:SIG-000052': 1, 'duplicate_id:SIG-000051': 1, 'duplicate_id:SIG-000055': 1, 'duplicate_id:SIG-000053': 1}`
- `candidate CAND-6A071F427DC7 entity_id=SIG-000054 reason=duplicate_id:SIG-000054 conf=0.9`
- `candidate CAND-820B8132A919 entity_id=SIG-000052 reason=duplicate_id:SIG-000052 conf=0.9`
- `candidate CAND-817B389C8ADB entity_id=SIG-000051 reason=duplicate_id:SIG-000051 conf=0.92`
- `candidate CAND-06A65C9FC7EC entity_id=SIG-000055 reason=duplicate_id:SIG-000055 conf=0.9`
- `candidate CAND-D584860559B4 entity_id=SIG-000053 reason=duplicate_id:SIG-000053 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-6A071F427DC7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000054 | Rejected |
| CAND-820B8132A919 | business_signal_library | 0.9 | False | duplicate_id:SIG-000052 | Rejected |
| CAND-817B389C8ADB | business_signal_library | 0.92 | False | duplicate_id:SIG-000051 | Rejected |
| CAND-06A65C9FC7EC | business_signal_library | 0.9 | False | duplicate_id:SIG-000055 | Rejected |
| CAND-D584860559B4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000053 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000054` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
