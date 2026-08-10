# Candidate Root Cause

**Generated:** 2026-08-10T11:27:49+00:00
**Session:** `SESSION-20260810-DCB37B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001806`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260810-DCB37B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001806': 1, 'duplicate_id:SIG-001805': 1, 'duplicate_id:SIG-001807': 1, 'duplicate_id:SIG-001809': 1, 'duplicate_id:SIG-001808': 1}`
- `candidate CAND-5195094A9189 entity_id=SIG-001806 reason=duplicate_id:SIG-001806 conf=0.92`
- `candidate CAND-B985B616C031 entity_id=SIG-001805 reason=duplicate_id:SIG-001805 conf=0.9`
- `candidate CAND-C00D7143385D entity_id=SIG-001807 reason=duplicate_id:SIG-001807 conf=0.88`
- `candidate CAND-F7D8BE4CE5F3 entity_id=SIG-001809 reason=duplicate_id:SIG-001809 conf=0.92`
- `candidate CAND-378755D4973C entity_id=SIG-001808 reason=duplicate_id:SIG-001808 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5195094A9189 | business_signal_library | 0.92 | False | duplicate_id:SIG-001806 | Rejected |
| CAND-B985B616C031 | business_signal_library | 0.9 | False | duplicate_id:SIG-001805 | Rejected |
| CAND-C00D7143385D | business_signal_library | 0.88 | False | duplicate_id:SIG-001807 | Rejected |
| CAND-F7D8BE4CE5F3 | business_signal_library | 0.92 | False | duplicate_id:SIG-001809 | Rejected |
| CAND-378755D4973C | business_signal_library | 0.9 | False | duplicate_id:SIG-001808 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001806` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
