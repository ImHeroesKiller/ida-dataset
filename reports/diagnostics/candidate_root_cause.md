# Candidate Root Cause

**Generated:** 2026-08-18T13:55:03+00:00
**Session:** `SESSION-20260818-CBD1D0`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000561`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260818-CBD1D0`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000561': 1, 'duplicate_id:SIG-000562': 1, 'duplicate_id:SIG-000565': 1, 'duplicate_id:SIG-000563': 1, 'duplicate_id:SIG-000564': 1}`
- `candidate CAND-852BCB5F975A entity_id=SIG-000561 reason=duplicate_id:SIG-000561 conf=0.92`
- `candidate CAND-7263F76F24FD entity_id=SIG-000562 reason=duplicate_id:SIG-000562 conf=0.9`
- `candidate CAND-DE3EEE033C37 entity_id=SIG-000565 reason=duplicate_id:SIG-000565 conf=0.9`
- `candidate CAND-7BF3FCE9ADD1 entity_id=SIG-000563 reason=duplicate_id:SIG-000563 conf=0.9`
- `candidate CAND-57EF323C8943 entity_id=SIG-000564 reason=duplicate_id:SIG-000564 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-852BCB5F975A | business_signal_library | 0.92 | False | duplicate_id:SIG-000561 | Rejected |
| CAND-7263F76F24FD | business_signal_library | 0.9 | False | duplicate_id:SIG-000562 | Rejected |
| CAND-DE3EEE033C37 | business_signal_library | 0.9 | False | duplicate_id:SIG-000565 | Rejected |
| CAND-7BF3FCE9ADD1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000563 | Rejected |
| CAND-57EF323C8943 | business_signal_library | 0.9 | False | duplicate_id:SIG-000564 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000561` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
