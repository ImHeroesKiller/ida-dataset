# Candidate Root Cause

**Generated:** 2026-08-19T07:05:04+00:00
**Session:** `SESSION-20260819-7FA021`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000644`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260819-7FA021`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000644': 1, 'duplicate_id:SIG-000642': 1, 'duplicate_id:SIG-000643': 1, 'duplicate_id:SIG-000641': 1, 'duplicate_id:SIG-000645': 1}`
- `candidate CAND-871096DF4513 entity_id=SIG-000644 reason=duplicate_id:SIG-000644 conf=0.9`
- `candidate CAND-7A4455099BE8 entity_id=SIG-000642 reason=duplicate_id:SIG-000642 conf=0.9`
- `candidate CAND-7E3B8C06DAAA entity_id=SIG-000643 reason=duplicate_id:SIG-000643 conf=0.9`
- `candidate CAND-133F4F8EA5B6 entity_id=SIG-000641 reason=duplicate_id:SIG-000641 conf=0.92`
- `candidate CAND-1A4BC67A4C2F entity_id=SIG-000645 reason=duplicate_id:SIG-000645 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-871096DF4513 | business_signal_library | 0.9 | False | duplicate_id:SIG-000644 | Rejected |
| CAND-7A4455099BE8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000642 | Rejected |
| CAND-7E3B8C06DAAA | business_signal_library | 0.9 | False | duplicate_id:SIG-000643 | Rejected |
| CAND-133F4F8EA5B6 | business_signal_library | 0.92 | False | duplicate_id:SIG-000641 | Rejected |
| CAND-1A4BC67A4C2F | business_signal_library | 0.9 | False | duplicate_id:SIG-000645 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000644` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
