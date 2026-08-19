# Candidate Root Cause

**Generated:** 2026-08-19T11:46:01+00:00
**Session:** `SESSION-20260819-5FDD78`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000668`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260819-5FDD78`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000668': 1, 'duplicate_id:SIG-000666': 1, 'duplicate_id:SIG-000669': 1, 'duplicate_id:SIG-000670': 1, 'duplicate_id:SIG-000667': 1}`
- `candidate CAND-B2674C0AD578 entity_id=SIG-000668 reason=duplicate_id:SIG-000668 conf=0.9`
- `candidate CAND-B0F0E39921F8 entity_id=SIG-000666 reason=duplicate_id:SIG-000666 conf=0.92`
- `candidate CAND-883317983864 entity_id=SIG-000669 reason=duplicate_id:SIG-000669 conf=0.9`
- `candidate CAND-8DF30E618420 entity_id=SIG-000670 reason=duplicate_id:SIG-000670 conf=0.9`
- `candidate CAND-3A368BEDB325 entity_id=SIG-000667 reason=duplicate_id:SIG-000667 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B2674C0AD578 | business_signal_library | 0.9 | False | duplicate_id:SIG-000668 | Rejected |
| CAND-B0F0E39921F8 | business_signal_library | 0.92 | False | duplicate_id:SIG-000666 | Rejected |
| CAND-883317983864 | business_signal_library | 0.9 | False | duplicate_id:SIG-000669 | Rejected |
| CAND-8DF30E618420 | business_signal_library | 0.9 | False | duplicate_id:SIG-000670 | Rejected |
| CAND-3A368BEDB325 | business_signal_library | 0.9 | False | duplicate_id:SIG-000667 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000668` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
