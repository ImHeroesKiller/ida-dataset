# Candidate Root Cause

**Generated:** 2026-08-22T04:01:33+00:00
**Session:** `SESSION-20260822-DF4EA2`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000967`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260822-DF4EA2`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000967': 1, 'duplicate_id:SIG-000969': 1, 'duplicate_id:SIG-000968': 1, 'duplicate_id:SIG-000970': 1, 'duplicate_id:SIG-000966': 1}`
- `candidate CAND-C9477F24F56B entity_id=SIG-000967 reason=duplicate_id:SIG-000967 conf=0.9`
- `candidate CAND-D09395D197C0 entity_id=SIG-000969 reason=duplicate_id:SIG-000969 conf=0.9`
- `candidate CAND-8EC6B918C836 entity_id=SIG-000968 reason=duplicate_id:SIG-000968 conf=0.9`
- `candidate CAND-88468E4F9301 entity_id=SIG-000970 reason=duplicate_id:SIG-000970 conf=0.9`
- `candidate CAND-673C4E6309ED entity_id=SIG-000966 reason=duplicate_id:SIG-000966 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-C9477F24F56B | business_signal_library | 0.9 | False | duplicate_id:SIG-000967 | Rejected |
| CAND-D09395D197C0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000969 | Rejected |
| CAND-8EC6B918C836 | business_signal_library | 0.9 | False | duplicate_id:SIG-000968 | Rejected |
| CAND-88468E4F9301 | business_signal_library | 0.9 | False | duplicate_id:SIG-000970 | Rejected |
| CAND-673C4E6309ED | business_signal_library | 0.92 | False | duplicate_id:SIG-000966 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000967` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
