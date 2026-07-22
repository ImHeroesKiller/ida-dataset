# Candidate Root Cause

**Generated:** 2026-07-22T04:37:00+00:00
**Session:** `SESSION-20260722-082E99`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000662`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260722-082E99`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000662': 1, 'duplicate_id:SIG-000664': 1, 'duplicate_id:SIG-000661': 1, 'duplicate_id:SIG-000660': 1, 'duplicate_id:SIG-000663': 1}`
- `candidate CAND-97E920AEA74F entity_id=SIG-000662 reason=duplicate_id:SIG-000662 conf=0.88`
- `candidate CAND-E0EEF7C1A072 entity_id=SIG-000664 reason=duplicate_id:SIG-000664 conf=0.92`
- `candidate CAND-CE396376CCB0 entity_id=SIG-000661 reason=duplicate_id:SIG-000661 conf=0.92`
- `candidate CAND-E1CC12986F55 entity_id=SIG-000660 reason=duplicate_id:SIG-000660 conf=0.9`
- `candidate CAND-86F340FBE4A0 entity_id=SIG-000663 reason=duplicate_id:SIG-000663 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-97E920AEA74F | business_signal_library | 0.88 | False | duplicate_id:SIG-000662 | Rejected |
| CAND-E0EEF7C1A072 | business_signal_library | 0.92 | False | duplicate_id:SIG-000664 | Rejected |
| CAND-CE396376CCB0 | business_signal_library | 0.92 | False | duplicate_id:SIG-000661 | Rejected |
| CAND-E1CC12986F55 | business_signal_library | 0.9 | False | duplicate_id:SIG-000660 | Rejected |
| CAND-86F340FBE4A0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000663 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000662` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
