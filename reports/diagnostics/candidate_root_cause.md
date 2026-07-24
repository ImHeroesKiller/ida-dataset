# Candidate Root Cause

**Generated:** 2026-07-24T00:21:01+00:00
**Session:** `SESSION-20260724-43C327`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000759`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260724-43C327`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000759': 1, 'duplicate_id:SIG-000756': 1, 'duplicate_id:SIG-000758': 1, 'duplicate_id:SIG-000757': 1, 'duplicate_id:SIG-000755': 1}`
- `candidate CAND-CEDD598C0C49 entity_id=SIG-000759 reason=duplicate_id:SIG-000759 conf=0.92`
- `candidate CAND-F7E7A8AFE462 entity_id=SIG-000756 reason=duplicate_id:SIG-000756 conf=0.92`
- `candidate CAND-B3EC84956EAD entity_id=SIG-000758 reason=duplicate_id:SIG-000758 conf=0.9`
- `candidate CAND-B97D9405E582 entity_id=SIG-000757 reason=duplicate_id:SIG-000757 conf=0.88`
- `candidate CAND-B709EC315BC7 entity_id=SIG-000755 reason=duplicate_id:SIG-000755 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-CEDD598C0C49 | business_signal_library | 0.92 | False | duplicate_id:SIG-000759 | Rejected |
| CAND-F7E7A8AFE462 | business_signal_library | 0.92 | False | duplicate_id:SIG-000756 | Rejected |
| CAND-B3EC84956EAD | business_signal_library | 0.9 | False | duplicate_id:SIG-000758 | Rejected |
| CAND-B97D9405E582 | business_signal_library | 0.88 | False | duplicate_id:SIG-000757 | Rejected |
| CAND-B709EC315BC7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000755 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000759` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
