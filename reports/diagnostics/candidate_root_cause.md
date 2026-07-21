# Candidate Root Cause

**Generated:** 2026-07-21T23:19:30+00:00
**Session:** `SESSION-20260721-3CEC09`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000650`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260721-3CEC09`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000650': 1, 'duplicate_id:SIG-000652': 1, 'duplicate_id:SIG-000651': 1, 'duplicate_id:SIG-000653': 1, 'duplicate_id:SIG-000654': 1}`
- `candidate CAND-A23E98EA074F entity_id=SIG-000650 reason=duplicate_id:SIG-000650 conf=0.9`
- `candidate CAND-B8AC5718E1F9 entity_id=SIG-000652 reason=duplicate_id:SIG-000652 conf=0.88`
- `candidate CAND-C5EB632EA68C entity_id=SIG-000651 reason=duplicate_id:SIG-000651 conf=0.92`
- `candidate CAND-1FB6EEA8DA5F entity_id=SIG-000653 reason=duplicate_id:SIG-000653 conf=0.9`
- `candidate CAND-BD1BDE2903BC entity_id=SIG-000654 reason=duplicate_id:SIG-000654 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A23E98EA074F | business_signal_library | 0.9 | False | duplicate_id:SIG-000650 | Rejected |
| CAND-B8AC5718E1F9 | business_signal_library | 0.88 | False | duplicate_id:SIG-000652 | Rejected |
| CAND-C5EB632EA68C | business_signal_library | 0.92 | False | duplicate_id:SIG-000651 | Rejected |
| CAND-1FB6EEA8DA5F | business_signal_library | 0.9 | False | duplicate_id:SIG-000653 | Rejected |
| CAND-BD1BDE2903BC | business_signal_library | 0.92 | False | duplicate_id:SIG-000654 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000650` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
