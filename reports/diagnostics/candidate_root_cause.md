# Candidate Root Cause

**Generated:** 2026-08-13T13:27:14+00:00
**Session:** `SESSION-20260813-9093A1`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000031`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260813-9093A1`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000031': 1, 'duplicate_id:SIG-000034': 1, 'duplicate_id:SIG-000032': 1, 'duplicate_id:SIG-000033': 1, 'duplicate_id:SIG-000035': 1}`
- `candidate CAND-12B1338CFBC8 entity_id=SIG-000031 reason=duplicate_id:SIG-000031 conf=0.92`
- `candidate CAND-0E987F0F4CC7 entity_id=SIG-000034 reason=duplicate_id:SIG-000034 conf=0.9`
- `candidate CAND-07A707B27D32 entity_id=SIG-000032 reason=duplicate_id:SIG-000032 conf=0.9`
- `candidate CAND-CB5B4C17AA0F entity_id=SIG-000033 reason=duplicate_id:SIG-000033 conf=0.9`
- `candidate CAND-C9C6D48BCEE7 entity_id=SIG-000035 reason=duplicate_id:SIG-000035 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-12B1338CFBC8 | business_signal_library | 0.92 | False | duplicate_id:SIG-000031 | Rejected |
| CAND-0E987F0F4CC7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000034 | Rejected |
| CAND-07A707B27D32 | business_signal_library | 0.9 | False | duplicate_id:SIG-000032 | Rejected |
| CAND-CB5B4C17AA0F | business_signal_library | 0.9 | False | duplicate_id:SIG-000033 | Rejected |
| CAND-C9C6D48BCEE7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000035 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000031` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
