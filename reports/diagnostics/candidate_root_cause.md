# Candidate Root Cause

**Generated:** 2026-08-17T18:54:44+00:00
**Session:** `SESSION-20260817-7944FD`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000472`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260817-7944FD`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000472': 1, 'duplicate_id:SIG-000474': 1, 'duplicate_id:SIG-000473': 1, 'duplicate_id:SIG-000471': 1, 'duplicate_id:SIG-000475': 1}`
- `candidate CAND-24BF7DD8EDFC entity_id=SIG-000472 reason=duplicate_id:SIG-000472 conf=0.9`
- `candidate CAND-BAF9054356CF entity_id=SIG-000474 reason=duplicate_id:SIG-000474 conf=0.9`
- `candidate CAND-D30E3D768B9E entity_id=SIG-000473 reason=duplicate_id:SIG-000473 conf=0.9`
- `candidate CAND-D91DB101EF9B entity_id=SIG-000471 reason=duplicate_id:SIG-000471 conf=0.92`
- `candidate CAND-93D7B2D733B4 entity_id=SIG-000475 reason=duplicate_id:SIG-000475 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-24BF7DD8EDFC | business_signal_library | 0.9 | False | duplicate_id:SIG-000472 | Rejected |
| CAND-BAF9054356CF | business_signal_library | 0.9 | False | duplicate_id:SIG-000474 | Rejected |
| CAND-D30E3D768B9E | business_signal_library | 0.9 | False | duplicate_id:SIG-000473 | Rejected |
| CAND-D91DB101EF9B | business_signal_library | 0.92 | False | duplicate_id:SIG-000471 | Rejected |
| CAND-93D7B2D733B4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000475 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000472` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
