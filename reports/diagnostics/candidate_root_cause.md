# Candidate Root Cause

**Generated:** 2026-08-16T10:38:38+00:00
**Session:** `SESSION-20260816-AC7559`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000321`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260816-AC7559`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000321': 1, 'duplicate_id:SIG-000323': 1, 'duplicate_id:SIG-000325': 1, 'duplicate_id:SIG-000324': 1, 'duplicate_id:SIG-000322': 1}`
- `candidate CAND-DC60562D95A0 entity_id=SIG-000321 reason=duplicate_id:SIG-000321 conf=0.92`
- `candidate CAND-DBF642B0045E entity_id=SIG-000323 reason=duplicate_id:SIG-000323 conf=0.9`
- `candidate CAND-D964366CD4C1 entity_id=SIG-000325 reason=duplicate_id:SIG-000325 conf=0.9`
- `candidate CAND-3A2EAF25D081 entity_id=SIG-000324 reason=duplicate_id:SIG-000324 conf=0.9`
- `candidate CAND-ADC3D1FF8B32 entity_id=SIG-000322 reason=duplicate_id:SIG-000322 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-DC60562D95A0 | business_signal_library | 0.92 | False | duplicate_id:SIG-000321 | Rejected |
| CAND-DBF642B0045E | business_signal_library | 0.9 | False | duplicate_id:SIG-000323 | Rejected |
| CAND-D964366CD4C1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000325 | Rejected |
| CAND-3A2EAF25D081 | business_signal_library | 0.9 | False | duplicate_id:SIG-000324 | Rejected |
| CAND-ADC3D1FF8B32 | business_signal_library | 0.9 | False | duplicate_id:SIG-000322 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000321` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
