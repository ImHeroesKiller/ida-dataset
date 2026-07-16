# Candidate Root Cause

**Generated:** 2026-07-16T09:35:24+00:00
**Session:** `SESSION-20260716-27B544`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000308`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260716-27B544`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000308': 1, 'duplicate_id:SIG-000306': 1, 'duplicate_id:SIG-000305': 1, 'duplicate_id:SIG-000307': 1, 'duplicate_id:SIG-000309': 1}`
- `candidate CAND-F374AE48502C entity_id=SIG-000308 reason=duplicate_id:SIG-000308 conf=0.9`
- `candidate CAND-D48639CD011F entity_id=SIG-000306 reason=duplicate_id:SIG-000306 conf=0.92`
- `candidate CAND-C1C1DC6179D6 entity_id=SIG-000305 reason=duplicate_id:SIG-000305 conf=0.9`
- `candidate CAND-2716C6F270BF entity_id=SIG-000307 reason=duplicate_id:SIG-000307 conf=0.88`
- `candidate CAND-4C5DF2E87102 entity_id=SIG-000309 reason=duplicate_id:SIG-000309 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F374AE48502C | business_signal_library | 0.9 | False | duplicate_id:SIG-000308 | Rejected |
| CAND-D48639CD011F | business_signal_library | 0.92 | False | duplicate_id:SIG-000306 | Rejected |
| CAND-C1C1DC6179D6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000305 | Rejected |
| CAND-2716C6F270BF | business_signal_library | 0.88 | False | duplicate_id:SIG-000307 | Rejected |
| CAND-4C5DF2E87102 | business_signal_library | 0.92 | False | duplicate_id:SIG-000309 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000308` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
