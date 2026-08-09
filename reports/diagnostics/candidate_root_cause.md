# Candidate Root Cause

**Generated:** 2026-08-09T19:01:24+00:00
**Session:** `SESSION-20260809-7E0F0C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001754`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260809-7E0F0C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001754': 1, 'duplicate_id:SIG-001751': 1, 'duplicate_id:SIG-001753': 1, 'duplicate_id:SIG-001752': 1, 'duplicate_id:SIG-001750': 1}`
- `candidate CAND-54888BC6ED41 entity_id=SIG-001754 reason=duplicate_id:SIG-001754 conf=0.92`
- `candidate CAND-0DED506B4E6D entity_id=SIG-001751 reason=duplicate_id:SIG-001751 conf=0.92`
- `candidate CAND-82237B9CC386 entity_id=SIG-001753 reason=duplicate_id:SIG-001753 conf=0.9`
- `candidate CAND-FF83004C3ABD entity_id=SIG-001752 reason=duplicate_id:SIG-001752 conf=0.88`
- `candidate CAND-67778A776108 entity_id=SIG-001750 reason=duplicate_id:SIG-001750 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-54888BC6ED41 | business_signal_library | 0.92 | False | duplicate_id:SIG-001754 | Rejected |
| CAND-0DED506B4E6D | business_signal_library | 0.92 | False | duplicate_id:SIG-001751 | Rejected |
| CAND-82237B9CC386 | business_signal_library | 0.9 | False | duplicate_id:SIG-001753 | Rejected |
| CAND-FF83004C3ABD | business_signal_library | 0.88 | False | duplicate_id:SIG-001752 | Rejected |
| CAND-67778A776108 | business_signal_library | 0.9 | False | duplicate_id:SIG-001750 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001754` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
