# Candidate Root Cause

**Generated:** 2026-08-22T20:42:42+00:00
**Session:** `SESSION-20260822-591071`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001054`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260822-591071`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001054': 1, 'duplicate_id:SIG-001055': 1, 'duplicate_id:SIG-001053': 1, 'duplicate_id:SIG-001051': 1, 'duplicate_id:SIG-001052': 1}`
- `candidate CAND-EAAAB56AB09A entity_id=SIG-001054 reason=duplicate_id:SIG-001054 conf=0.9`
- `candidate CAND-02CB67A3C06F entity_id=SIG-001055 reason=duplicate_id:SIG-001055 conf=0.9`
- `candidate CAND-0B6D550C4861 entity_id=SIG-001053 reason=duplicate_id:SIG-001053 conf=0.9`
- `candidate CAND-D256C3477CFA entity_id=SIG-001051 reason=duplicate_id:SIG-001051 conf=0.92`
- `candidate CAND-9BCBA85DA2B0 entity_id=SIG-001052 reason=duplicate_id:SIG-001052 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-EAAAB56AB09A | business_signal_library | 0.9 | False | duplicate_id:SIG-001054 | Rejected |
| CAND-02CB67A3C06F | business_signal_library | 0.9 | False | duplicate_id:SIG-001055 | Rejected |
| CAND-0B6D550C4861 | business_signal_library | 0.9 | False | duplicate_id:SIG-001053 | Rejected |
| CAND-D256C3477CFA | business_signal_library | 0.92 | False | duplicate_id:SIG-001051 | Rejected |
| CAND-9BCBA85DA2B0 | business_signal_library | 0.9 | False | duplicate_id:SIG-001052 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001054` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
