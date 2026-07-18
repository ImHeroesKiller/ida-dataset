# Candidate Root Cause

**Generated:** 2026-07-18T05:47:09+00:00
**Session:** `SESSION-20260718-A1CA71`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000416`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260718-A1CA71`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000416': 1, 'duplicate_id:SIG-000419': 1, 'duplicate_id:SIG-000415': 1, 'duplicate_id:SIG-000417': 1, 'duplicate_id:SIG-000418': 1}`
- `candidate CAND-F505032B3A22 entity_id=SIG-000416 reason=duplicate_id:SIG-000416 conf=0.92`
- `candidate CAND-4197FA6C1C4C entity_id=SIG-000419 reason=duplicate_id:SIG-000419 conf=0.92`
- `candidate CAND-5D6B8AA04843 entity_id=SIG-000415 reason=duplicate_id:SIG-000415 conf=0.9`
- `candidate CAND-73D1AE6539B6 entity_id=SIG-000417 reason=duplicate_id:SIG-000417 conf=0.88`
- `candidate CAND-827778244A56 entity_id=SIG-000418 reason=duplicate_id:SIG-000418 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F505032B3A22 | business_signal_library | 0.92 | False | duplicate_id:SIG-000416 | Rejected |
| CAND-4197FA6C1C4C | business_signal_library | 0.92 | False | duplicate_id:SIG-000419 | Rejected |
| CAND-5D6B8AA04843 | business_signal_library | 0.9 | False | duplicate_id:SIG-000415 | Rejected |
| CAND-73D1AE6539B6 | business_signal_library | 0.88 | False | duplicate_id:SIG-000417 | Rejected |
| CAND-827778244A56 | business_signal_library | 0.9 | False | duplicate_id:SIG-000418 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000416` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
