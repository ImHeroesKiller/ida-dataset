# Candidate Root Cause

**Generated:** 2026-08-18T01:30:27+00:00
**Session:** `SESSION-20260818-15E21E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000501`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260818-15E21E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000501': 1, 'duplicate_id:SIG-000504': 1, 'duplicate_id:SIG-000502': 1, 'duplicate_id:SIG-000505': 1, 'duplicate_id:SIG-000503': 1}`
- `candidate CAND-25F00B103176 entity_id=SIG-000501 reason=duplicate_id:SIG-000501 conf=0.92`
- `candidate CAND-2F5CC7517676 entity_id=SIG-000504 reason=duplicate_id:SIG-000504 conf=0.9`
- `candidate CAND-9E9527316F21 entity_id=SIG-000502 reason=duplicate_id:SIG-000502 conf=0.9`
- `candidate CAND-B3260C8CAE6D entity_id=SIG-000505 reason=duplicate_id:SIG-000505 conf=0.9`
- `candidate CAND-DBD66BDAC801 entity_id=SIG-000503 reason=duplicate_id:SIG-000503 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-25F00B103176 | business_signal_library | 0.92 | False | duplicate_id:SIG-000501 | Rejected |
| CAND-2F5CC7517676 | business_signal_library | 0.9 | False | duplicate_id:SIG-000504 | Rejected |
| CAND-9E9527316F21 | business_signal_library | 0.9 | False | duplicate_id:SIG-000502 | Rejected |
| CAND-B3260C8CAE6D | business_signal_library | 0.9 | False | duplicate_id:SIG-000505 | Rejected |
| CAND-DBD66BDAC801 | business_signal_library | 0.9 | False | duplicate_id:SIG-000503 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000501` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
