# Candidate Root Cause

**Generated:** 2026-08-11T04:05:47+00:00
**Session:** `SESSION-20260811-49AB3D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001866`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260811-49AB3D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001866': 1, 'duplicate_id:SIG-001867': 1, 'duplicate_id:SIG-001865': 1, 'duplicate_id:SIG-001868': 1, 'duplicate_id:SIG-001869': 1}`
- `candidate CAND-DF4287F714EB entity_id=SIG-001866 reason=duplicate_id:SIG-001866 conf=0.92`
- `candidate CAND-6D39D1C14DC1 entity_id=SIG-001867 reason=duplicate_id:SIG-001867 conf=0.88`
- `candidate CAND-F09E0DF164D5 entity_id=SIG-001865 reason=duplicate_id:SIG-001865 conf=0.9`
- `candidate CAND-644069F7A29A entity_id=SIG-001868 reason=duplicate_id:SIG-001868 conf=0.9`
- `candidate CAND-04076EA94FA9 entity_id=SIG-001869 reason=duplicate_id:SIG-001869 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-DF4287F714EB | business_signal_library | 0.92 | False | duplicate_id:SIG-001866 | Rejected |
| CAND-6D39D1C14DC1 | business_signal_library | 0.88 | False | duplicate_id:SIG-001867 | Rejected |
| CAND-F09E0DF164D5 | business_signal_library | 0.9 | False | duplicate_id:SIG-001865 | Rejected |
| CAND-644069F7A29A | business_signal_library | 0.9 | False | duplicate_id:SIG-001868 | Rejected |
| CAND-04076EA94FA9 | business_signal_library | 0.92 | False | duplicate_id:SIG-001869 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001866` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
