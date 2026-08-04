# Candidate Root Cause

**Generated:** 2026-08-04T11:04:56+00:00
**Session:** `SESSION-20260804-1A954C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001366`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260804-1A954C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001366': 1, 'duplicate_id:SIG-001369': 1, 'duplicate_id:SIG-001365': 1, 'duplicate_id:SIG-001368': 1, 'duplicate_id:SIG-001367': 1}`
- `candidate CAND-74A7A4D8ED7C entity_id=SIG-001366 reason=duplicate_id:SIG-001366 conf=0.92`
- `candidate CAND-03AF18C6BF3D entity_id=SIG-001369 reason=duplicate_id:SIG-001369 conf=0.92`
- `candidate CAND-B767317A01F6 entity_id=SIG-001365 reason=duplicate_id:SIG-001365 conf=0.9`
- `candidate CAND-9C9A20143048 entity_id=SIG-001368 reason=duplicate_id:SIG-001368 conf=0.9`
- `candidate CAND-B1E3A779F12D entity_id=SIG-001367 reason=duplicate_id:SIG-001367 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-74A7A4D8ED7C | business_signal_library | 0.92 | False | duplicate_id:SIG-001366 | Rejected |
| CAND-03AF18C6BF3D | business_signal_library | 0.92 | False | duplicate_id:SIG-001369 | Rejected |
| CAND-B767317A01F6 | business_signal_library | 0.9 | False | duplicate_id:SIG-001365 | Rejected |
| CAND-9C9A20143048 | business_signal_library | 0.9 | False | duplicate_id:SIG-001368 | Rejected |
| CAND-B1E3A779F12D | business_signal_library | 0.88 | False | duplicate_id:SIG-001367 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001366` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
