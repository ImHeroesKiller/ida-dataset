# Candidate Root Cause

**Generated:** 2026-08-22T10:43:21+00:00
**Session:** `SESSION-20260822-886DE7`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001005`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260822-886DE7`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001005': 1, 'duplicate_id:SIG-001001': 1, 'duplicate_id:SIG-001003': 1, 'duplicate_id:SIG-001004': 1, 'duplicate_id:SIG-001002': 1}`
- `candidate CAND-E244E30DA300 entity_id=SIG-001005 reason=duplicate_id:SIG-001005 conf=0.9`
- `candidate CAND-27601693589B entity_id=SIG-001001 reason=duplicate_id:SIG-001001 conf=0.92`
- `candidate CAND-9E7A2CF22F23 entity_id=SIG-001003 reason=duplicate_id:SIG-001003 conf=0.9`
- `candidate CAND-74D5AFAD0A67 entity_id=SIG-001004 reason=duplicate_id:SIG-001004 conf=0.9`
- `candidate CAND-CC08632EAB2C entity_id=SIG-001002 reason=duplicate_id:SIG-001002 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-E244E30DA300 | business_signal_library | 0.9 | False | duplicate_id:SIG-001005 | Rejected |
| CAND-27601693589B | business_signal_library | 0.92 | False | duplicate_id:SIG-001001 | Rejected |
| CAND-9E7A2CF22F23 | business_signal_library | 0.9 | False | duplicate_id:SIG-001003 | Rejected |
| CAND-74D5AFAD0A67 | business_signal_library | 0.9 | False | duplicate_id:SIG-001004 | Rejected |
| CAND-CC08632EAB2C | business_signal_library | 0.9 | False | duplicate_id:SIG-001002 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001005` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
