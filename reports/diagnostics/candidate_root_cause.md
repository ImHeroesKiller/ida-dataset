# Candidate Root Cause

**Generated:** 2026-08-19T14:54:51+00:00
**Session:** `SESSION-20260819-260CAE`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000683`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260819-260CAE`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000683': 1, 'duplicate_id:SIG-000685': 1, 'duplicate_id:SIG-000682': 1, 'duplicate_id:SIG-000681': 1, 'duplicate_id:SIG-000684': 1}`
- `candidate CAND-F9DAF5CDC0C7 entity_id=SIG-000683 reason=duplicate_id:SIG-000683 conf=0.9`
- `candidate CAND-5CED573A3F9D entity_id=SIG-000685 reason=duplicate_id:SIG-000685 conf=0.9`
- `candidate CAND-B96FC8EC2619 entity_id=SIG-000682 reason=duplicate_id:SIG-000682 conf=0.9`
- `candidate CAND-B5190DFC18C8 entity_id=SIG-000681 reason=duplicate_id:SIG-000681 conf=0.92`
- `candidate CAND-09D72339E53C entity_id=SIG-000684 reason=duplicate_id:SIG-000684 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F9DAF5CDC0C7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000683 | Rejected |
| CAND-5CED573A3F9D | business_signal_library | 0.9 | False | duplicate_id:SIG-000685 | Rejected |
| CAND-B96FC8EC2619 | business_signal_library | 0.9 | False | duplicate_id:SIG-000682 | Rejected |
| CAND-B5190DFC18C8 | business_signal_library | 0.92 | False | duplicate_id:SIG-000681 | Rejected |
| CAND-09D72339E53C | business_signal_library | 0.9 | False | duplicate_id:SIG-000684 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000683` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
