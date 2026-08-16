# Candidate Root Cause

**Generated:** 2026-08-16T09:43:13+00:00
**Session:** `SESSION-20260816-4F1A92`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000320`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260816-4F1A92`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000320': 1, 'duplicate_id:SIG-000316': 1, 'duplicate_id:SIG-000317': 1, 'duplicate_id:SIG-000318': 1, 'duplicate_id:SIG-000319': 1}`
- `candidate CAND-A43F4AAE025C entity_id=SIG-000320 reason=duplicate_id:SIG-000320 conf=0.9`
- `candidate CAND-085ECE295149 entity_id=SIG-000316 reason=duplicate_id:SIG-000316 conf=0.92`
- `candidate CAND-2684E4B37004 entity_id=SIG-000317 reason=duplicate_id:SIG-000317 conf=0.9`
- `candidate CAND-5AE0C4702EC2 entity_id=SIG-000318 reason=duplicate_id:SIG-000318 conf=0.9`
- `candidate CAND-482A2D9EA693 entity_id=SIG-000319 reason=duplicate_id:SIG-000319 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A43F4AAE025C | business_signal_library | 0.9 | False | duplicate_id:SIG-000320 | Rejected |
| CAND-085ECE295149 | business_signal_library | 0.92 | False | duplicate_id:SIG-000316 | Rejected |
| CAND-2684E4B37004 | business_signal_library | 0.9 | False | duplicate_id:SIG-000317 | Rejected |
| CAND-5AE0C4702EC2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000318 | Rejected |
| CAND-482A2D9EA693 | business_signal_library | 0.9 | False | duplicate_id:SIG-000319 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000320` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
