# Candidate Root Cause

**Generated:** 2026-07-19T16:23:36+00:00
**Session:** `SESSION-20260719-030FFC`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000517`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260719-030FFC`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000517': 1, 'duplicate_id:SIG-000519': 1, 'duplicate_id:SIG-000516': 1, 'duplicate_id:SIG-000518': 1, 'duplicate_id:SIG-000515': 1}`
- `candidate CAND-5B2097AFAC7F entity_id=SIG-000517 reason=duplicate_id:SIG-000517 conf=0.88`
- `candidate CAND-F2BAD55CB4B1 entity_id=SIG-000519 reason=duplicate_id:SIG-000519 conf=0.92`
- `candidate CAND-A578B5855651 entity_id=SIG-000516 reason=duplicate_id:SIG-000516 conf=0.92`
- `candidate CAND-D621061E1E12 entity_id=SIG-000518 reason=duplicate_id:SIG-000518 conf=0.9`
- `candidate CAND-237B156FF880 entity_id=SIG-000515 reason=duplicate_id:SIG-000515 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5B2097AFAC7F | business_signal_library | 0.88 | False | duplicate_id:SIG-000517 | Rejected |
| CAND-F2BAD55CB4B1 | business_signal_library | 0.92 | False | duplicate_id:SIG-000519 | Rejected |
| CAND-A578B5855651 | business_signal_library | 0.92 | False | duplicate_id:SIG-000516 | Rejected |
| CAND-D621061E1E12 | business_signal_library | 0.9 | False | duplicate_id:SIG-000518 | Rejected |
| CAND-237B156FF880 | business_signal_library | 0.9 | False | duplicate_id:SIG-000515 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000517` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
