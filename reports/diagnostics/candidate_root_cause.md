# Candidate Root Cause

**Generated:** 2026-07-18T11:22:57+00:00
**Session:** `SESSION-20260718-4407D8`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000432`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260718-4407D8`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000432': 1, 'duplicate_id:SIG-000430': 1, 'duplicate_id:SIG-000433': 1, 'duplicate_id:SIG-000431': 1, 'duplicate_id:SIG-000434': 1}`
- `candidate CAND-3F6ECD6759E7 entity_id=SIG-000432 reason=duplicate_id:SIG-000432 conf=0.88`
- `candidate CAND-A1F0E79330D4 entity_id=SIG-000430 reason=duplicate_id:SIG-000430 conf=0.9`
- `candidate CAND-82092104628F entity_id=SIG-000433 reason=duplicate_id:SIG-000433 conf=0.9`
- `candidate CAND-C1D7A8DE26A9 entity_id=SIG-000431 reason=duplicate_id:SIG-000431 conf=0.92`
- `candidate CAND-3D7023F3ACD6 entity_id=SIG-000434 reason=duplicate_id:SIG-000434 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-3F6ECD6759E7 | business_signal_library | 0.88 | False | duplicate_id:SIG-000432 | Rejected |
| CAND-A1F0E79330D4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000430 | Rejected |
| CAND-82092104628F | business_signal_library | 0.9 | False | duplicate_id:SIG-000433 | Rejected |
| CAND-C1D7A8DE26A9 | business_signal_library | 0.92 | False | duplicate_id:SIG-000431 | Rejected |
| CAND-3D7023F3ACD6 | business_signal_library | 0.92 | False | duplicate_id:SIG-000434 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000432` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
