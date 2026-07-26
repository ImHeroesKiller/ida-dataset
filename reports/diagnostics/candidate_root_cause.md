# Candidate Root Cause

**Generated:** 2026-07-26T08:52:05+00:00
**Session:** `SESSION-20260726-5E417F`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000885`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260726-5E417F`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000885': 1, 'duplicate_id:SIG-000888': 1, 'duplicate_id:SIG-000889': 1, 'duplicate_id:SIG-000887': 1, 'duplicate_id:SIG-000886': 1}`
- `candidate CAND-39003F74B1CB entity_id=SIG-000885 reason=duplicate_id:SIG-000885 conf=0.9`
- `candidate CAND-96CE6EC3115B entity_id=SIG-000888 reason=duplicate_id:SIG-000888 conf=0.9`
- `candidate CAND-CBA5FBBAE0CF entity_id=SIG-000889 reason=duplicate_id:SIG-000889 conf=0.92`
- `candidate CAND-AF028ED1DBC0 entity_id=SIG-000887 reason=duplicate_id:SIG-000887 conf=0.88`
- `candidate CAND-1309E420EDA8 entity_id=SIG-000886 reason=duplicate_id:SIG-000886 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-39003F74B1CB | business_signal_library | 0.9 | False | duplicate_id:SIG-000885 | Rejected |
| CAND-96CE6EC3115B | business_signal_library | 0.9 | False | duplicate_id:SIG-000888 | Rejected |
| CAND-CBA5FBBAE0CF | business_signal_library | 0.92 | False | duplicate_id:SIG-000889 | Rejected |
| CAND-AF028ED1DBC0 | business_signal_library | 0.88 | False | duplicate_id:SIG-000887 | Rejected |
| CAND-1309E420EDA8 | business_signal_library | 0.92 | False | duplicate_id:SIG-000886 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000885` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
