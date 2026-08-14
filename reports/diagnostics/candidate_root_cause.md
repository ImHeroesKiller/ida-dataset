# Candidate Root Cause

**Generated:** 2026-08-14T11:58:11+00:00
**Session:** `SESSION-20260814-DC1F67`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000109`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260814-DC1F67`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000109': 1, 'duplicate_id:SIG-000110': 1, 'duplicate_id:SIG-000107': 1, 'duplicate_id:SIG-000108': 1, 'duplicate_id:SIG-000106': 1}`
- `candidate CAND-1CEDDF65D6C9 entity_id=SIG-000109 reason=duplicate_id:SIG-000109 conf=0.9`
- `candidate CAND-9F1FDCB537E7 entity_id=SIG-000110 reason=duplicate_id:SIG-000110 conf=0.9`
- `candidate CAND-8DF2CA3E694C entity_id=SIG-000107 reason=duplicate_id:SIG-000107 conf=0.9`
- `candidate CAND-31A981104138 entity_id=SIG-000108 reason=duplicate_id:SIG-000108 conf=0.9`
- `candidate CAND-8E1CF4590478 entity_id=SIG-000106 reason=duplicate_id:SIG-000106 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-1CEDDF65D6C9 | business_signal_library | 0.9 | False | duplicate_id:SIG-000109 | Rejected |
| CAND-9F1FDCB537E7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000110 | Rejected |
| CAND-8DF2CA3E694C | business_signal_library | 0.9 | False | duplicate_id:SIG-000107 | Rejected |
| CAND-31A981104138 | business_signal_library | 0.9 | False | duplicate_id:SIG-000108 | Rejected |
| CAND-8E1CF4590478 | business_signal_library | 0.92 | False | duplicate_id:SIG-000106 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000109` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
