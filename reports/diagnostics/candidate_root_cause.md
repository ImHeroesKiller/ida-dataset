# Candidate Root Cause

**Generated:** 2026-07-11T23:10:09+00:00
**Session:** `SESSION-20260711-531E9D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000066`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260711-531E9D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000066': 1, 'duplicate_id:SIG-000068': 1, 'duplicate_id:SIG-000067': 1, 'duplicate_id:SIG-000069': 1, 'duplicate_id:SIG-000065': 1}`
- `candidate CAND-A618E91F5D49 entity_id=SIG-000066 reason=duplicate_id:SIG-000066 conf=0.92`
- `candidate CAND-92DA63F53BBE entity_id=SIG-000068 reason=duplicate_id:SIG-000068 conf=0.9`
- `candidate CAND-F7A5F8BFD413 entity_id=SIG-000067 reason=duplicate_id:SIG-000067 conf=0.88`
- `candidate CAND-6876EA87EE0A entity_id=SIG-000069 reason=duplicate_id:SIG-000069 conf=0.92`
- `candidate CAND-5D3559EFA3AA entity_id=SIG-000065 reason=duplicate_id:SIG-000065 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A618E91F5D49 | business_signal_library | 0.92 | False | duplicate_id:SIG-000066 | Rejected |
| CAND-92DA63F53BBE | business_signal_library | 0.9 | False | duplicate_id:SIG-000068 | Rejected |
| CAND-F7A5F8BFD413 | business_signal_library | 0.88 | False | duplicate_id:SIG-000067 | Rejected |
| CAND-6876EA87EE0A | business_signal_library | 0.92 | False | duplicate_id:SIG-000069 | Rejected |
| CAND-5D3559EFA3AA | business_signal_library | 0.9 | False | duplicate_id:SIG-000065 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000066` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
