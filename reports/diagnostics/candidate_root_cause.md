# Candidate Root Cause

**Generated:** 2026-08-23T23:40:26+00:00
**Session:** `SESSION-20260823-0FD781`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001177`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260823-0FD781`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001177': 1, 'duplicate_id:SIG-001178': 1, 'duplicate_id:SIG-001179': 1, 'duplicate_id:SIG-001176': 1, 'duplicate_id:SIG-001180': 1}`
- `candidate CAND-A0D89BAA93AB entity_id=SIG-001177 reason=duplicate_id:SIG-001177 conf=0.9`
- `candidate CAND-8E25ED737761 entity_id=SIG-001178 reason=duplicate_id:SIG-001178 conf=0.9`
- `candidate CAND-A65B6F99E041 entity_id=SIG-001179 reason=duplicate_id:SIG-001179 conf=0.9`
- `candidate CAND-C19E2C64623A entity_id=SIG-001176 reason=duplicate_id:SIG-001176 conf=0.92`
- `candidate CAND-260CD7E45B44 entity_id=SIG-001180 reason=duplicate_id:SIG-001180 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A0D89BAA93AB | business_signal_library | 0.9 | False | duplicate_id:SIG-001177 | Rejected |
| CAND-8E25ED737761 | business_signal_library | 0.9 | False | duplicate_id:SIG-001178 | Rejected |
| CAND-A65B6F99E041 | business_signal_library | 0.9 | False | duplicate_id:SIG-001179 | Rejected |
| CAND-C19E2C64623A | business_signal_library | 0.92 | False | duplicate_id:SIG-001176 | Rejected |
| CAND-260CD7E45B44 | business_signal_library | 0.9 | False | duplicate_id:SIG-001180 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001177` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
