# Candidate Root Cause

**Generated:** 2026-08-15T17:31:27+00:00
**Session:** `SESSION-20260815-3CD129`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000250`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260815-3CD129`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000250': 1, 'duplicate_id:SIG-000246': 1, 'duplicate_id:SIG-000248': 1, 'duplicate_id:SIG-000249': 1, 'duplicate_id:SIG-000247': 1}`
- `candidate CAND-0CBFCC3693F4 entity_id=SIG-000250 reason=duplicate_id:SIG-000250 conf=0.9`
- `candidate CAND-6B8D381EE9E5 entity_id=SIG-000246 reason=duplicate_id:SIG-000246 conf=0.92`
- `candidate CAND-5A9582A71A21 entity_id=SIG-000248 reason=duplicate_id:SIG-000248 conf=0.9`
- `candidate CAND-9283156F2D22 entity_id=SIG-000249 reason=duplicate_id:SIG-000249 conf=0.9`
- `candidate CAND-664086CCCF41 entity_id=SIG-000247 reason=duplicate_id:SIG-000247 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-0CBFCC3693F4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000250 | Rejected |
| CAND-6B8D381EE9E5 | business_signal_library | 0.92 | False | duplicate_id:SIG-000246 | Rejected |
| CAND-5A9582A71A21 | business_signal_library | 0.9 | False | duplicate_id:SIG-000248 | Rejected |
| CAND-9283156F2D22 | business_signal_library | 0.9 | False | duplicate_id:SIG-000249 | Rejected |
| CAND-664086CCCF41 | business_signal_library | 0.9 | False | duplicate_id:SIG-000247 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000250` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
