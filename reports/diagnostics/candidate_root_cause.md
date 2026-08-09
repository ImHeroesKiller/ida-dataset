# Candidate Root Cause

**Generated:** 2026-08-09T14:15:12+00:00
**Session:** `SESSION-20260809-6E47E1`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001726`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260809-6E47E1`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001726': 1, 'duplicate_id:SIG-001729': 1, 'duplicate_id:SIG-001727': 1, 'duplicate_id:SIG-001728': 1, 'duplicate_id:SIG-001725': 1}`
- `candidate CAND-7E2427CA962F entity_id=SIG-001726 reason=duplicate_id:SIG-001726 conf=0.92`
- `candidate CAND-BA82B664A3B7 entity_id=SIG-001729 reason=duplicate_id:SIG-001729 conf=0.92`
- `candidate CAND-8102B22D1ABB entity_id=SIG-001727 reason=duplicate_id:SIG-001727 conf=0.88`
- `candidate CAND-5AC485B26F6D entity_id=SIG-001728 reason=duplicate_id:SIG-001728 conf=0.9`
- `candidate CAND-073EFFE45DB3 entity_id=SIG-001725 reason=duplicate_id:SIG-001725 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-7E2427CA962F | business_signal_library | 0.92 | False | duplicate_id:SIG-001726 | Rejected |
| CAND-BA82B664A3B7 | business_signal_library | 0.92 | False | duplicate_id:SIG-001729 | Rejected |
| CAND-8102B22D1ABB | business_signal_library | 0.88 | False | duplicate_id:SIG-001727 | Rejected |
| CAND-5AC485B26F6D | business_signal_library | 0.9 | False | duplicate_id:SIG-001728 | Rejected |
| CAND-073EFFE45DB3 | business_signal_library | 0.9 | False | duplicate_id:SIG-001725 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001726` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
