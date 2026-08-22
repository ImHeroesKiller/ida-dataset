# Candidate Root Cause

**Generated:** 2026-08-22T04:52:39+00:00
**Session:** `SESSION-20260822-6FFC51`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000975`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260822-6FFC51`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000975': 1, 'duplicate_id:SIG-000974': 1, 'duplicate_id:SIG-000973': 1, 'duplicate_id:SIG-000971': 1, 'duplicate_id:SIG-000972': 1}`
- `candidate CAND-6336C584014C entity_id=SIG-000975 reason=duplicate_id:SIG-000975 conf=0.9`
- `candidate CAND-334967039D4E entity_id=SIG-000974 reason=duplicate_id:SIG-000974 conf=0.9`
- `candidate CAND-2E4746CB656D entity_id=SIG-000973 reason=duplicate_id:SIG-000973 conf=0.9`
- `candidate CAND-95638E1C4B6D entity_id=SIG-000971 reason=duplicate_id:SIG-000971 conf=0.92`
- `candidate CAND-BD533E1238A2 entity_id=SIG-000972 reason=duplicate_id:SIG-000972 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-6336C584014C | business_signal_library | 0.9 | False | duplicate_id:SIG-000975 | Rejected |
| CAND-334967039D4E | business_signal_library | 0.9 | False | duplicate_id:SIG-000974 | Rejected |
| CAND-2E4746CB656D | business_signal_library | 0.9 | False | duplicate_id:SIG-000973 | Rejected |
| CAND-95638E1C4B6D | business_signal_library | 0.92 | False | duplicate_id:SIG-000971 | Rejected |
| CAND-BD533E1238A2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000972 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000975` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
