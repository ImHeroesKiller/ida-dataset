# Candidate Root Cause

**Generated:** 2026-08-23T16:45:52+00:00
**Session:** `SESSION-20260823-FDDA67`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001145`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260823-FDDA67`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001145': 1, 'duplicate_id:SIG-001144': 1, 'duplicate_id:SIG-001141': 1, 'duplicate_id:SIG-001142': 1, 'duplicate_id:SIG-001143': 1}`
- `candidate CAND-375C1D713A77 entity_id=SIG-001145 reason=duplicate_id:SIG-001145 conf=0.9`
- `candidate CAND-A8D6F837F0CC entity_id=SIG-001144 reason=duplicate_id:SIG-001144 conf=0.9`
- `candidate CAND-FE76EE409855 entity_id=SIG-001141 reason=duplicate_id:SIG-001141 conf=0.92`
- `candidate CAND-BAB85E661C5B entity_id=SIG-001142 reason=duplicate_id:SIG-001142 conf=0.9`
- `candidate CAND-9F977E7A8FE3 entity_id=SIG-001143 reason=duplicate_id:SIG-001143 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-375C1D713A77 | business_signal_library | 0.9 | False | duplicate_id:SIG-001145 | Rejected |
| CAND-A8D6F837F0CC | business_signal_library | 0.9 | False | duplicate_id:SIG-001144 | Rejected |
| CAND-FE76EE409855 | business_signal_library | 0.92 | False | duplicate_id:SIG-001141 | Rejected |
| CAND-BAB85E661C5B | business_signal_library | 0.9 | False | duplicate_id:SIG-001142 | Rejected |
| CAND-9F977E7A8FE3 | business_signal_library | 0.9 | False | duplicate_id:SIG-001143 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001145` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
