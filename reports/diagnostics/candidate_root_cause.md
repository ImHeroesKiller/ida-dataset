# Candidate Root Cause

**Generated:** 2026-08-20T09:54:17+00:00
**Session:** `SESSION-20260820-B837D8`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000773`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260820-B837D8`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000773': 1, 'duplicate_id:SIG-000772': 1, 'duplicate_id:SIG-000774': 1, 'duplicate_id:SIG-000771': 1, 'duplicate_id:SIG-000775': 1}`
- `candidate CAND-5E16847FFAFC entity_id=SIG-000773 reason=duplicate_id:SIG-000773 conf=0.9`
- `candidate CAND-CB11750AD7F3 entity_id=SIG-000772 reason=duplicate_id:SIG-000772 conf=0.9`
- `candidate CAND-728277C934C8 entity_id=SIG-000774 reason=duplicate_id:SIG-000774 conf=0.9`
- `candidate CAND-3BBF19683D5F entity_id=SIG-000771 reason=duplicate_id:SIG-000771 conf=0.92`
- `candidate CAND-5CB15E38EAFA entity_id=SIG-000775 reason=duplicate_id:SIG-000775 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5E16847FFAFC | business_signal_library | 0.9 | False | duplicate_id:SIG-000773 | Rejected |
| CAND-CB11750AD7F3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000772 | Rejected |
| CAND-728277C934C8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000774 | Rejected |
| CAND-3BBF19683D5F | business_signal_library | 0.92 | False | duplicate_id:SIG-000771 | Rejected |
| CAND-5CB15E38EAFA | business_signal_library | 0.9 | False | duplicate_id:SIG-000775 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000773` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
