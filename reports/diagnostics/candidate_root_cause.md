# Candidate Root Cause

**Generated:** 2026-08-17T11:42:05+00:00
**Session:** `SESSION-20260817-E3916A`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000439`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260817-E3916A`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000439': 1, 'duplicate_id:SIG-000436': 1, 'duplicate_id:SIG-000440': 1, 'duplicate_id:SIG-000437': 1, 'duplicate_id:SIG-000438': 1}`
- `candidate CAND-6C16C3789B2E entity_id=SIG-000439 reason=duplicate_id:SIG-000439 conf=0.9`
- `candidate CAND-72A4D9CCBCF7 entity_id=SIG-000436 reason=duplicate_id:SIG-000436 conf=0.92`
- `candidate CAND-8FFC01A632B7 entity_id=SIG-000440 reason=duplicate_id:SIG-000440 conf=0.9`
- `candidate CAND-D40B2465B054 entity_id=SIG-000437 reason=duplicate_id:SIG-000437 conf=0.9`
- `candidate CAND-8183A61CB729 entity_id=SIG-000438 reason=duplicate_id:SIG-000438 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-6C16C3789B2E | business_signal_library | 0.9 | False | duplicate_id:SIG-000439 | Rejected |
| CAND-72A4D9CCBCF7 | business_signal_library | 0.92 | False | duplicate_id:SIG-000436 | Rejected |
| CAND-8FFC01A632B7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000440 | Rejected |
| CAND-D40B2465B054 | business_signal_library | 0.9 | False | duplicate_id:SIG-000437 | Rejected |
| CAND-8183A61CB729 | business_signal_library | 0.9 | False | duplicate_id:SIG-000438 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000439` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
