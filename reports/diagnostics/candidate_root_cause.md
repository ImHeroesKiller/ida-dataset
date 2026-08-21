# Candidate Root Cause

**Generated:** 2026-08-21T08:01:45+00:00
**Session:** `SESSION-20260821-71F6AF`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000874`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260821-71F6AF`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000874': 1, 'duplicate_id:SIG-000873': 1, 'duplicate_id:SIG-000871': 1, 'duplicate_id:SIG-000875': 1, 'duplicate_id:SIG-000872': 1}`
- `candidate CAND-B5C4FD4D726C entity_id=SIG-000874 reason=duplicate_id:SIG-000874 conf=0.9`
- `candidate CAND-4D80BC45E4C4 entity_id=SIG-000873 reason=duplicate_id:SIG-000873 conf=0.9`
- `candidate CAND-6D2871762E43 entity_id=SIG-000871 reason=duplicate_id:SIG-000871 conf=0.92`
- `candidate CAND-71370A7D7F2A entity_id=SIG-000875 reason=duplicate_id:SIG-000875 conf=0.9`
- `candidate CAND-1BA855978714 entity_id=SIG-000872 reason=duplicate_id:SIG-000872 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B5C4FD4D726C | business_signal_library | 0.9 | False | duplicate_id:SIG-000874 | Rejected |
| CAND-4D80BC45E4C4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000873 | Rejected |
| CAND-6D2871762E43 | business_signal_library | 0.92 | False | duplicate_id:SIG-000871 | Rejected |
| CAND-71370A7D7F2A | business_signal_library | 0.9 | False | duplicate_id:SIG-000875 | Rejected |
| CAND-1BA855978714 | business_signal_library | 0.9 | False | duplicate_id:SIG-000872 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000874` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
