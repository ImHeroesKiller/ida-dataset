# Candidate Root Cause

**Generated:** 2026-08-05T13:14:15+00:00
**Session:** `SESSION-20260805-AB3DD6`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001423`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260805-AB3DD6`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001423': 1, 'duplicate_id:SIG-001422': 1, 'duplicate_id:SIG-001424': 1, 'duplicate_id:SIG-001421': 1, 'duplicate_id:SIG-001420': 1}`
- `candidate CAND-93A3D7CC4190 entity_id=SIG-001423 reason=duplicate_id:SIG-001423 conf=0.92`
- `candidate CAND-D407350299E9 entity_id=SIG-001422 reason=duplicate_id:SIG-001422 conf=0.9`
- `candidate CAND-3480E98C3CEA entity_id=SIG-001424 reason=duplicate_id:SIG-001424 conf=0.9`
- `candidate CAND-0011AB4C4C32 entity_id=SIG-001421 reason=duplicate_id:SIG-001421 conf=0.92`
- `candidate CAND-A98665157EA6 entity_id=SIG-001420 reason=duplicate_id:SIG-001420 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-93A3D7CC4190 | business_signal_library | 0.92 | False | duplicate_id:SIG-001423 | Rejected |
| CAND-D407350299E9 | business_signal_library | 0.9 | False | duplicate_id:SIG-001422 | Rejected |
| CAND-3480E98C3CEA | business_signal_library | 0.9 | False | duplicate_id:SIG-001424 | Rejected |
| CAND-0011AB4C4C32 | business_signal_library | 0.92 | False | duplicate_id:SIG-001421 | Rejected |
| CAND-A98665157EA6 | business_signal_library | 0.9 | False | duplicate_id:SIG-001420 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001423` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
