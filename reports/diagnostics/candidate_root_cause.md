# Candidate Root Cause

**Generated:** 2026-07-28T08:54:08+00:00
**Session:** `SESSION-20260728-9787E6`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000986`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260728-9787E6`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000986': 1, 'duplicate_id:SIG-000989': 1, 'duplicate_id:SIG-000985': 1, 'duplicate_id:SIG-000987': 1, 'duplicate_id:SIG-000988': 1}`
- `candidate CAND-16C79C3441C4 entity_id=SIG-000986 reason=duplicate_id:SIG-000986 conf=0.92`
- `candidate CAND-D9513A2DF8F1 entity_id=SIG-000989 reason=duplicate_id:SIG-000989 conf=0.9`
- `candidate CAND-3C186A705BA5 entity_id=SIG-000985 reason=duplicate_id:SIG-000985 conf=0.9`
- `candidate CAND-0A934A15B204 entity_id=SIG-000987 reason=duplicate_id:SIG-000987 conf=0.9`
- `candidate CAND-1FCBC54D3AB4 entity_id=SIG-000988 reason=duplicate_id:SIG-000988 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-16C79C3441C4 | business_signal_library | 0.92 | False | duplicate_id:SIG-000986 | Rejected |
| CAND-D9513A2DF8F1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000989 | Rejected |
| CAND-3C186A705BA5 | business_signal_library | 0.9 | False | duplicate_id:SIG-000985 | Rejected |
| CAND-0A934A15B204 | business_signal_library | 0.9 | False | duplicate_id:SIG-000987 | Rejected |
| CAND-1FCBC54D3AB4 | business_signal_library | 0.92 | False | duplicate_id:SIG-000988 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000986` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
