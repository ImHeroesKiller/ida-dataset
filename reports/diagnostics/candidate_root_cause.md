# Candidate Root Cause

**Generated:** 2026-08-20T14:07:42+00:00
**Session:** `SESSION-20260820-16A718`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000793`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260820-16A718`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000793': 1, 'duplicate_id:SIG-000795': 1, 'duplicate_id:SIG-000792': 1, 'duplicate_id:SIG-000794': 1, 'duplicate_id:SIG-000791': 1}`
- `candidate CAND-71E2291084BA entity_id=SIG-000793 reason=duplicate_id:SIG-000793 conf=0.9`
- `candidate CAND-114CFB7B87C1 entity_id=SIG-000795 reason=duplicate_id:SIG-000795 conf=0.9`
- `candidate CAND-6AD6B26DF314 entity_id=SIG-000792 reason=duplicate_id:SIG-000792 conf=0.9`
- `candidate CAND-50CCA8E9E9F2 entity_id=SIG-000794 reason=duplicate_id:SIG-000794 conf=0.9`
- `candidate CAND-FC02709DF4AD entity_id=SIG-000791 reason=duplicate_id:SIG-000791 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-71E2291084BA | business_signal_library | 0.9 | False | duplicate_id:SIG-000793 | Rejected |
| CAND-114CFB7B87C1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000795 | Rejected |
| CAND-6AD6B26DF314 | business_signal_library | 0.9 | False | duplicate_id:SIG-000792 | Rejected |
| CAND-50CCA8E9E9F2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000794 | Rejected |
| CAND-FC02709DF4AD | business_signal_library | 0.92 | False | duplicate_id:SIG-000791 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000793` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
