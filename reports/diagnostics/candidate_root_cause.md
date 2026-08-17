# Candidate Root Cause

**Generated:** 2026-08-17T16:43:10+00:00
**Session:** `SESSION-20260817-C64414`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000465`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260817-C64414`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000465': 1, 'duplicate_id:SIG-000463': 1, 'duplicate_id:SIG-000462': 1, 'duplicate_id:SIG-000461': 1, 'duplicate_id:SIG-000464': 1}`
- `candidate CAND-5C7948F47958 entity_id=SIG-000465 reason=duplicate_id:SIG-000465 conf=0.9`
- `candidate CAND-1EF4982FC32D entity_id=SIG-000463 reason=duplicate_id:SIG-000463 conf=0.9`
- `candidate CAND-2DF856A3B5F8 entity_id=SIG-000462 reason=duplicate_id:SIG-000462 conf=0.92`
- `candidate CAND-0DFAE6195166 entity_id=SIG-000461 reason=duplicate_id:SIG-000461 conf=0.9`
- `candidate CAND-B711DBE36E77 entity_id=SIG-000464 reason=duplicate_id:SIG-000464 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5C7948F47958 | business_signal_library | 0.9 | False | duplicate_id:SIG-000465 | Rejected |
| CAND-1EF4982FC32D | business_signal_library | 0.9 | False | duplicate_id:SIG-000463 | Rejected |
| CAND-2DF856A3B5F8 | business_signal_library | 0.92 | False | duplicate_id:SIG-000462 | Rejected |
| CAND-0DFAE6195166 | business_signal_library | 0.9 | False | duplicate_id:SIG-000461 | Rejected |
| CAND-B711DBE36E77 | business_signal_library | 0.9 | False | duplicate_id:SIG-000464 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000465` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
