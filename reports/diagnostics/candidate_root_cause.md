# Candidate Root Cause

**Generated:** 2026-08-23T07:52:36+00:00
**Session:** `SESSION-20260823-9F80B0`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001098`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260823-9F80B0`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001098': 1, 'duplicate_id:SIG-001099': 1, 'duplicate_id:SIG-001097': 1, 'duplicate_id:SIG-001100': 1, 'duplicate_id:SIG-001096': 1}`
- `candidate CAND-75A4780BB52C entity_id=SIG-001098 reason=duplicate_id:SIG-001098 conf=0.9`
- `candidate CAND-C674D4131338 entity_id=SIG-001099 reason=duplicate_id:SIG-001099 conf=0.9`
- `candidate CAND-91FEE9AE3DDE entity_id=SIG-001097 reason=duplicate_id:SIG-001097 conf=0.9`
- `candidate CAND-B9849203D43A entity_id=SIG-001100 reason=duplicate_id:SIG-001100 conf=0.9`
- `candidate CAND-1CA6D29B4530 entity_id=SIG-001096 reason=duplicate_id:SIG-001096 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-75A4780BB52C | business_signal_library | 0.9 | False | duplicate_id:SIG-001098 | Rejected |
| CAND-C674D4131338 | business_signal_library | 0.9 | False | duplicate_id:SIG-001099 | Rejected |
| CAND-91FEE9AE3DDE | business_signal_library | 0.9 | False | duplicate_id:SIG-001097 | Rejected |
| CAND-B9849203D43A | business_signal_library | 0.9 | False | duplicate_id:SIG-001100 | Rejected |
| CAND-1CA6D29B4530 | business_signal_library | 0.92 | False | duplicate_id:SIG-001096 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001098` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
