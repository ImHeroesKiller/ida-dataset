# Candidate Root Cause

**Generated:** 2026-07-24T08:53:07+00:00
**Session:** `SESSION-20260724-704DC5`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000770`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260724-704DC5`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000770': 1, 'duplicate_id:SIG-000773': 1, 'duplicate_id:SIG-000774': 1, 'duplicate_id:SIG-000772': 1, 'duplicate_id:SIG-000771': 1}`
- `candidate CAND-EBC58D31B04D entity_id=SIG-000770 reason=duplicate_id:SIG-000770 conf=0.9`
- `candidate CAND-59898AB02D67 entity_id=SIG-000773 reason=duplicate_id:SIG-000773 conf=0.9`
- `candidate CAND-C58DBEB5E503 entity_id=SIG-000774 reason=duplicate_id:SIG-000774 conf=0.92`
- `candidate CAND-54CFF5A229B2 entity_id=SIG-000772 reason=duplicate_id:SIG-000772 conf=0.88`
- `candidate CAND-DB0C77467BCD entity_id=SIG-000771 reason=duplicate_id:SIG-000771 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-EBC58D31B04D | business_signal_library | 0.9 | False | duplicate_id:SIG-000770 | Rejected |
| CAND-59898AB02D67 | business_signal_library | 0.9 | False | duplicate_id:SIG-000773 | Rejected |
| CAND-C58DBEB5E503 | business_signal_library | 0.92 | False | duplicate_id:SIG-000774 | Rejected |
| CAND-54CFF5A229B2 | business_signal_library | 0.88 | False | duplicate_id:SIG-000772 | Rejected |
| CAND-DB0C77467BCD | business_signal_library | 0.92 | False | duplicate_id:SIG-000771 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000770` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
