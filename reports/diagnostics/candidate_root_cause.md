# Candidate Root Cause

**Generated:** 2026-08-13T20:57:59+00:00
**Session:** `SESSION-20260813-A2A767`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000057`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260813-A2A767`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000057': 1, 'duplicate_id:SIG-000058': 1, 'duplicate_id:SIG-000056': 1, 'duplicate_id:SIG-000060': 1, 'duplicate_id:SIG-000059': 1}`
- `candidate CAND-7B83442CAF6D entity_id=SIG-000057 reason=duplicate_id:SIG-000057 conf=0.9`
- `candidate CAND-CDE9763E62E5 entity_id=SIG-000058 reason=duplicate_id:SIG-000058 conf=0.9`
- `candidate CAND-127838E76E71 entity_id=SIG-000056 reason=duplicate_id:SIG-000056 conf=0.92`
- `candidate CAND-769FB255C888 entity_id=SIG-000060 reason=duplicate_id:SIG-000060 conf=0.9`
- `candidate CAND-A61EDC8E9477 entity_id=SIG-000059 reason=duplicate_id:SIG-000059 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-7B83442CAF6D | business_signal_library | 0.9 | False | duplicate_id:SIG-000057 | Rejected |
| CAND-CDE9763E62E5 | business_signal_library | 0.9 | False | duplicate_id:SIG-000058 | Rejected |
| CAND-127838E76E71 | business_signal_library | 0.92 | False | duplicate_id:SIG-000056 | Rejected |
| CAND-769FB255C888 | business_signal_library | 0.9 | False | duplicate_id:SIG-000060 | Rejected |
| CAND-A61EDC8E9477 | business_signal_library | 0.9 | False | duplicate_id:SIG-000059 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000057` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
