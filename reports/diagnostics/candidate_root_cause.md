# Candidate Root Cause

**Generated:** 2026-08-04T04:33:34+00:00
**Session:** `SESSION-20260804-9847A3`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001351`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260804-9847A3`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001351': 1, 'duplicate_id:SIG-001353': 1, 'duplicate_id:SIG-001352': 1, 'duplicate_id:SIG-001354': 1, 'duplicate_id:SIG-001350': 1}`
- `candidate CAND-073D868173F4 entity_id=SIG-001351 reason=duplicate_id:SIG-001351 conf=0.92`
- `candidate CAND-D0E65832D1C7 entity_id=SIG-001353 reason=duplicate_id:SIG-001353 conf=0.9`
- `candidate CAND-663819AF16B3 entity_id=SIG-001352 reason=duplicate_id:SIG-001352 conf=0.88`
- `candidate CAND-73239EEC4F39 entity_id=SIG-001354 reason=duplicate_id:SIG-001354 conf=0.92`
- `candidate CAND-74A84227543C entity_id=SIG-001350 reason=duplicate_id:SIG-001350 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-073D868173F4 | business_signal_library | 0.92 | False | duplicate_id:SIG-001351 | Rejected |
| CAND-D0E65832D1C7 | business_signal_library | 0.9 | False | duplicate_id:SIG-001353 | Rejected |
| CAND-663819AF16B3 | business_signal_library | 0.88 | False | duplicate_id:SIG-001352 | Rejected |
| CAND-73239EEC4F39 | business_signal_library | 0.92 | False | duplicate_id:SIG-001354 | Rejected |
| CAND-74A84227543C | business_signal_library | 0.9 | False | duplicate_id:SIG-001350 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001351` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
