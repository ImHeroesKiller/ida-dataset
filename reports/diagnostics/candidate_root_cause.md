# Candidate Root Cause

**Generated:** 2026-08-18T04:02:54+00:00
**Session:** `SESSION-20260818-0CE495`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000512`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260818-0CE495`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000512': 1, 'duplicate_id:SIG-000514': 1, 'duplicate_id:SIG-000513': 1, 'duplicate_id:SIG-000511': 1, 'duplicate_id:SIG-000515': 1}`
- `candidate CAND-2510B3B49A9F entity_id=SIG-000512 reason=duplicate_id:SIG-000512 conf=0.9`
- `candidate CAND-63ACB5538A13 entity_id=SIG-000514 reason=duplicate_id:SIG-000514 conf=0.9`
- `candidate CAND-F92E5A2358F6 entity_id=SIG-000513 reason=duplicate_id:SIG-000513 conf=0.9`
- `candidate CAND-643BE9E80E19 entity_id=SIG-000511 reason=duplicate_id:SIG-000511 conf=0.92`
- `candidate CAND-90698FC86CF6 entity_id=SIG-000515 reason=duplicate_id:SIG-000515 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-2510B3B49A9F | business_signal_library | 0.9 | False | duplicate_id:SIG-000512 | Rejected |
| CAND-63ACB5538A13 | business_signal_library | 0.9 | False | duplicate_id:SIG-000514 | Rejected |
| CAND-F92E5A2358F6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000513 | Rejected |
| CAND-643BE9E80E19 | business_signal_library | 0.92 | False | duplicate_id:SIG-000511 | Rejected |
| CAND-90698FC86CF6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000515 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000512` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
