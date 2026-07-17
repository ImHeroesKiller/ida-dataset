# Candidate Root Cause

**Generated:** 2026-07-17T14:00:23+00:00
**Session:** `SESSION-20260717-36EF89`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000377`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260717-36EF89`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000377': 1, 'duplicate_id:SIG-000376': 1, 'duplicate_id:SIG-000378': 1, 'duplicate_id:SIG-000375': 1, 'duplicate_id:SIG-000379': 1}`
- `candidate CAND-6A3DE0C21A2A entity_id=SIG-000377 reason=duplicate_id:SIG-000377 conf=0.88`
- `candidate CAND-9068E73AD72F entity_id=SIG-000376 reason=duplicate_id:SIG-000376 conf=0.92`
- `candidate CAND-A4897B61D868 entity_id=SIG-000378 reason=duplicate_id:SIG-000378 conf=0.9`
- `candidate CAND-EBC9E971CA0E entity_id=SIG-000375 reason=duplicate_id:SIG-000375 conf=0.9`
- `candidate CAND-D8D8FADC99AF entity_id=SIG-000379 reason=duplicate_id:SIG-000379 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-6A3DE0C21A2A | business_signal_library | 0.88 | False | duplicate_id:SIG-000377 | Rejected |
| CAND-9068E73AD72F | business_signal_library | 0.92 | False | duplicate_id:SIG-000376 | Rejected |
| CAND-A4897B61D868 | business_signal_library | 0.9 | False | duplicate_id:SIG-000378 | Rejected |
| CAND-EBC9E971CA0E | business_signal_library | 0.9 | False | duplicate_id:SIG-000375 | Rejected |
| CAND-D8D8FADC99AF | business_signal_library | 0.92 | False | duplicate_id:SIG-000379 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000377` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
