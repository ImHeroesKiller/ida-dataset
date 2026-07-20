# Candidate Root Cause

**Generated:** 2026-07-20T09:45:20+00:00
**Session:** `SESSION-20260720-3BAC4B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000563`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260720-3BAC4B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000563': 1, 'duplicate_id:SIG-000561': 1, 'duplicate_id:SIG-000560': 1, 'duplicate_id:SIG-000564': 1, 'duplicate_id:SIG-000562': 1}`
- `candidate CAND-4BE602C3945C entity_id=SIG-000563 reason=duplicate_id:SIG-000563 conf=0.9`
- `candidate CAND-A9E110DF3597 entity_id=SIG-000561 reason=duplicate_id:SIG-000561 conf=0.92`
- `candidate CAND-72F03042AF64 entity_id=SIG-000560 reason=duplicate_id:SIG-000560 conf=0.9`
- `candidate CAND-51AA6CAE4A5A entity_id=SIG-000564 reason=duplicate_id:SIG-000564 conf=0.92`
- `candidate CAND-DCADF6F71579 entity_id=SIG-000562 reason=duplicate_id:SIG-000562 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-4BE602C3945C | business_signal_library | 0.9 | False | duplicate_id:SIG-000563 | Rejected |
| CAND-A9E110DF3597 | business_signal_library | 0.92 | False | duplicate_id:SIG-000561 | Rejected |
| CAND-72F03042AF64 | business_signal_library | 0.9 | False | duplicate_id:SIG-000560 | Rejected |
| CAND-51AA6CAE4A5A | business_signal_library | 0.92 | False | duplicate_id:SIG-000564 | Rejected |
| CAND-DCADF6F71579 | business_signal_library | 0.88 | False | duplicate_id:SIG-000562 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000563` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
