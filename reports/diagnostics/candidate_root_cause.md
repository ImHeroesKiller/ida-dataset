# Candidate Root Cause

**Generated:** 2026-08-15T06:51:45+00:00
**Session:** `SESSION-20260815-CA834D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000193`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260815-CA834D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000193': 1, 'duplicate_id:SIG-000191': 1, 'duplicate_id:SIG-000192': 1, 'duplicate_id:SIG-000195': 1, 'duplicate_id:SIG-000194': 1}`
- `candidate CAND-489BDDB2FFDD entity_id=SIG-000193 reason=duplicate_id:SIG-000193 conf=0.9`
- `candidate CAND-3FAE7DF7D444 entity_id=SIG-000191 reason=duplicate_id:SIG-000191 conf=0.92`
- `candidate CAND-FFE08297D70F entity_id=SIG-000192 reason=duplicate_id:SIG-000192 conf=0.9`
- `candidate CAND-E453BC162F54 entity_id=SIG-000195 reason=duplicate_id:SIG-000195 conf=0.9`
- `candidate CAND-FD4E16E3C66B entity_id=SIG-000194 reason=duplicate_id:SIG-000194 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-489BDDB2FFDD | business_signal_library | 0.9 | False | duplicate_id:SIG-000193 | Rejected |
| CAND-3FAE7DF7D444 | business_signal_library | 0.92 | False | duplicate_id:SIG-000191 | Rejected |
| CAND-FFE08297D70F | business_signal_library | 0.9 | False | duplicate_id:SIG-000192 | Rejected |
| CAND-E453BC162F54 | business_signal_library | 0.9 | False | duplicate_id:SIG-000195 | Rejected |
| CAND-FD4E16E3C66B | business_signal_library | 0.9 | False | duplicate_id:SIG-000194 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000193` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
