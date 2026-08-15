# Candidate Root Cause

**Generated:** 2026-08-15T09:41:51+00:00
**Session:** `SESSION-20260815-E98359`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000209`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260815-E98359`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000209': 1, 'duplicate_id:SIG-000208': 1, 'duplicate_id:SIG-000207': 1, 'duplicate_id:SIG-000206': 1, 'duplicate_id:SIG-000210': 1}`
- `candidate CAND-90C1F80EE911 entity_id=SIG-000209 reason=duplicate_id:SIG-000209 conf=0.9`
- `candidate CAND-E0A49C854440 entity_id=SIG-000208 reason=duplicate_id:SIG-000208 conf=0.9`
- `candidate CAND-3D80B53FE14D entity_id=SIG-000207 reason=duplicate_id:SIG-000207 conf=0.9`
- `candidate CAND-18391326BBE3 entity_id=SIG-000206 reason=duplicate_id:SIG-000206 conf=0.92`
- `candidate CAND-CE43E3FE2ACE entity_id=SIG-000210 reason=duplicate_id:SIG-000210 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-90C1F80EE911 | business_signal_library | 0.9 | False | duplicate_id:SIG-000209 | Rejected |
| CAND-E0A49C854440 | business_signal_library | 0.9 | False | duplicate_id:SIG-000208 | Rejected |
| CAND-3D80B53FE14D | business_signal_library | 0.9 | False | duplicate_id:SIG-000207 | Rejected |
| CAND-18391326BBE3 | business_signal_library | 0.92 | False | duplicate_id:SIG-000206 | Rejected |
| CAND-CE43E3FE2ACE | business_signal_library | 0.9 | False | duplicate_id:SIG-000210 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000209` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
