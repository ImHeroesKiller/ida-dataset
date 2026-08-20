# Candidate Root Cause

**Generated:** 2026-08-20T17:49:27+00:00
**Session:** `SESSION-20260820-6D770B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000812`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260820-6D770B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000812': 1, 'duplicate_id:SIG-000815': 1, 'duplicate_id:SIG-000814': 1, 'duplicate_id:SIG-000813': 1, 'duplicate_id:SIG-000811': 1}`
- `candidate CAND-63FEA7CBE7EF entity_id=SIG-000812 reason=duplicate_id:SIG-000812 conf=0.9`
- `candidate CAND-954B005A6317 entity_id=SIG-000815 reason=duplicate_id:SIG-000815 conf=0.9`
- `candidate CAND-C9E98305B3DB entity_id=SIG-000814 reason=duplicate_id:SIG-000814 conf=0.9`
- `candidate CAND-504A28CD5526 entity_id=SIG-000813 reason=duplicate_id:SIG-000813 conf=0.9`
- `candidate CAND-307F23EDAD75 entity_id=SIG-000811 reason=duplicate_id:SIG-000811 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-63FEA7CBE7EF | business_signal_library | 0.9 | False | duplicate_id:SIG-000812 | Rejected |
| CAND-954B005A6317 | business_signal_library | 0.9 | False | duplicate_id:SIG-000815 | Rejected |
| CAND-C9E98305B3DB | business_signal_library | 0.9 | False | duplicate_id:SIG-000814 | Rejected |
| CAND-504A28CD5526 | business_signal_library | 0.9 | False | duplicate_id:SIG-000813 | Rejected |
| CAND-307F23EDAD75 | business_signal_library | 0.92 | False | duplicate_id:SIG-000811 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000812` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
