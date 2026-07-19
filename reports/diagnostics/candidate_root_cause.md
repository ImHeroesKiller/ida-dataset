# Candidate Root Cause

**Generated:** 2026-07-19T00:13:16+00:00
**Session:** `SESSION-20260718-4B3382`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000477`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260718-4B3382`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000477': 1, 'duplicate_id:SIG-000476': 1, 'duplicate_id:SIG-000479': 1, 'duplicate_id:SIG-000478': 1, 'duplicate_id:SIG-000475': 1}`
- `candidate CAND-2F0DD0970F41 entity_id=SIG-000477 reason=duplicate_id:SIG-000477 conf=0.92`
- `candidate CAND-4DBE3AE87C34 entity_id=SIG-000476 reason=duplicate_id:SIG-000476 conf=0.88`
- `candidate CAND-B3243225A342 entity_id=SIG-000479 reason=duplicate_id:SIG-000479 conf=0.88`
- `candidate CAND-40085C84C1E7 entity_id=SIG-000478 reason=duplicate_id:SIG-000478 conf=0.9`
- `candidate CAND-193C5E63B0F0 entity_id=SIG-000475 reason=duplicate_id:SIG-000475 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-2F0DD0970F41 | business_signal_library | 0.92 | False | duplicate_id:SIG-000477 | Rejected |
| CAND-4DBE3AE87C34 | business_signal_library | 0.88 | False | duplicate_id:SIG-000476 | Rejected |
| CAND-B3243225A342 | business_signal_library | 0.88 | False | duplicate_id:SIG-000479 | Rejected |
| CAND-40085C84C1E7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000478 | Rejected |
| CAND-193C5E63B0F0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000475 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000477` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
