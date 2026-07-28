# Candidate Root Cause

**Generated:** 2026-07-28T14:28:37+00:00
**Session:** `SESSION-20260728-C90A90`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000997`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260728-C90A90`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000997': 1, 'duplicate_id:SIG-000999': 1, 'duplicate_id:SIG-000996': 1, 'duplicate_id:SIG-000995': 1, 'duplicate_id:SIG-000998': 1}`
- `candidate CAND-122311A8BD1E entity_id=SIG-000997 reason=duplicate_id:SIG-000997 conf=0.88`
- `candidate CAND-9A17A5C71185 entity_id=SIG-000999 reason=duplicate_id:SIG-000999 conf=0.92`
- `candidate CAND-1BA7FE00FA0B entity_id=SIG-000996 reason=duplicate_id:SIG-000996 conf=0.92`
- `candidate CAND-85ED54C0307F entity_id=SIG-000995 reason=duplicate_id:SIG-000995 conf=0.9`
- `candidate CAND-93557F3F4CA5 entity_id=SIG-000998 reason=duplicate_id:SIG-000998 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-122311A8BD1E | business_signal_library | 0.88 | False | duplicate_id:SIG-000997 | Rejected |
| CAND-9A17A5C71185 | business_signal_library | 0.92 | False | duplicate_id:SIG-000999 | Rejected |
| CAND-1BA7FE00FA0B | business_signal_library | 0.92 | False | duplicate_id:SIG-000996 | Rejected |
| CAND-85ED54C0307F | business_signal_library | 0.9 | False | duplicate_id:SIG-000995 | Rejected |
| CAND-93557F3F4CA5 | business_signal_library | 0.9 | False | duplicate_id:SIG-000998 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000997` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
