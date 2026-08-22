# Candidate Root Cause

**Generated:** 2026-08-22T09:46:22+00:00
**Session:** `SESSION-20260822-E2D402`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000999`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260822-E2D402`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000999': 1, 'duplicate_id:SIG-001000': 1, 'duplicate_id:SIG-000996': 1, 'duplicate_id:SIG-000998': 1, 'duplicate_id:SIG-000997': 1}`
- `candidate CAND-87B9AB4E41E6 entity_id=SIG-000999 reason=duplicate_id:SIG-000999 conf=0.9`
- `candidate CAND-F8D8D05289C4 entity_id=SIG-001000 reason=duplicate_id:SIG-001000 conf=0.9`
- `candidate CAND-130D04F37C9C entity_id=SIG-000996 reason=duplicate_id:SIG-000996 conf=0.92`
- `candidate CAND-46DB8A9769D0 entity_id=SIG-000998 reason=duplicate_id:SIG-000998 conf=0.9`
- `candidate CAND-7844925A49C6 entity_id=SIG-000997 reason=duplicate_id:SIG-000997 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-87B9AB4E41E6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000999 | Rejected |
| CAND-F8D8D05289C4 | business_signal_library | 0.9 | False | duplicate_id:SIG-001000 | Rejected |
| CAND-130D04F37C9C | business_signal_library | 0.92 | False | duplicate_id:SIG-000996 | Rejected |
| CAND-46DB8A9769D0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000998 | Rejected |
| CAND-7844925A49C6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000997 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000999` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
