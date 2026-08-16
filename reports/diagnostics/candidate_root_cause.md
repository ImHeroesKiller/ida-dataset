# Candidate Root Cause

**Generated:** 2026-08-16T08:45:59+00:00
**Session:** `SESSION-20260816-4195AB`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000314`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260816-4195AB`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000314': 1, 'duplicate_id:SIG-000311': 1, 'duplicate_id:SIG-000312': 1, 'duplicate_id:SIG-000313': 1, 'duplicate_id:SIG-000315': 1}`
- `candidate CAND-F3C993DACD58 entity_id=SIG-000314 reason=duplicate_id:SIG-000314 conf=0.9`
- `candidate CAND-BEC436BA5226 entity_id=SIG-000311 reason=duplicate_id:SIG-000311 conf=0.92`
- `candidate CAND-11BFC43CFB55 entity_id=SIG-000312 reason=duplicate_id:SIG-000312 conf=0.9`
- `candidate CAND-6D629AA09A93 entity_id=SIG-000313 reason=duplicate_id:SIG-000313 conf=0.9`
- `candidate CAND-FBE29B825B38 entity_id=SIG-000315 reason=duplicate_id:SIG-000315 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F3C993DACD58 | business_signal_library | 0.9 | False | duplicate_id:SIG-000314 | Rejected |
| CAND-BEC436BA5226 | business_signal_library | 0.92 | False | duplicate_id:SIG-000311 | Rejected |
| CAND-11BFC43CFB55 | business_signal_library | 0.9 | False | duplicate_id:SIG-000312 | Rejected |
| CAND-6D629AA09A93 | business_signal_library | 0.9 | False | duplicate_id:SIG-000313 | Rejected |
| CAND-FBE29B825B38 | business_signal_library | 0.9 | False | duplicate_id:SIG-000315 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000314` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
