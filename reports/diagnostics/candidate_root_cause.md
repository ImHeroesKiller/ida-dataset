# Candidate Root Cause

**Generated:** 2026-08-03T10:58:45+00:00
**Session:** `SESSION-20260803-3B3040`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001318`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260803-3B3040`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001318': 1, 'duplicate_id:SIG-001315': 1, 'duplicate_id:SIG-001316': 1, 'duplicate_id:SIG-001317': 1, 'duplicate_id:SIG-001319': 1}`
- `candidate CAND-7C793DAAC755 entity_id=SIG-001318 reason=duplicate_id:SIG-001318 conf=0.9`
- `candidate CAND-E922307B5CC1 entity_id=SIG-001315 reason=duplicate_id:SIG-001315 conf=0.9`
- `candidate CAND-8559589C7335 entity_id=SIG-001316 reason=duplicate_id:SIG-001316 conf=0.92`
- `candidate CAND-B1736C93F7AF entity_id=SIG-001317 reason=duplicate_id:SIG-001317 conf=0.88`
- `candidate CAND-81EB984CDD09 entity_id=SIG-001319 reason=duplicate_id:SIG-001319 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-7C793DAAC755 | business_signal_library | 0.9 | False | duplicate_id:SIG-001318 | Rejected |
| CAND-E922307B5CC1 | business_signal_library | 0.9 | False | duplicate_id:SIG-001315 | Rejected |
| CAND-8559589C7335 | business_signal_library | 0.92 | False | duplicate_id:SIG-001316 | Rejected |
| CAND-B1736C93F7AF | business_signal_library | 0.88 | False | duplicate_id:SIG-001317 | Rejected |
| CAND-81EB984CDD09 | business_signal_library | 0.92 | False | duplicate_id:SIG-001319 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001318` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
