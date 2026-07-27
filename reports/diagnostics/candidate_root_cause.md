# Candidate Root Cause

**Generated:** 2026-07-27T23:21:40+00:00
**Session:** `SESSION-20260727-644CF4`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000976`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260727-644CF4`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000976': 1, 'duplicate_id:SIG-000977': 1, 'duplicate_id:SIG-000975': 1, 'duplicate_id:SIG-000978': 1, 'duplicate_id:SIG-000979': 1}`
- `candidate CAND-68B7DCD71A08 entity_id=SIG-000976 reason=duplicate_id:SIG-000976 conf=0.92`
- `candidate CAND-0EBD9B9FAE87 entity_id=SIG-000977 reason=duplicate_id:SIG-000977 conf=0.88`
- `candidate CAND-EBFFEF7B1037 entity_id=SIG-000975 reason=duplicate_id:SIG-000975 conf=0.9`
- `candidate CAND-73D1B8631400 entity_id=SIG-000978 reason=duplicate_id:SIG-000978 conf=0.9`
- `candidate CAND-236F002AB5EA entity_id=SIG-000979 reason=duplicate_id:SIG-000979 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-68B7DCD71A08 | business_signal_library | 0.92 | False | duplicate_id:SIG-000976 | Rejected |
| CAND-0EBD9B9FAE87 | business_signal_library | 0.88 | False | duplicate_id:SIG-000977 | Rejected |
| CAND-EBFFEF7B1037 | business_signal_library | 0.9 | False | duplicate_id:SIG-000975 | Rejected |
| CAND-73D1B8631400 | business_signal_library | 0.9 | False | duplicate_id:SIG-000978 | Rejected |
| CAND-236F002AB5EA | business_signal_library | 0.92 | False | duplicate_id:SIG-000979 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000976` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
