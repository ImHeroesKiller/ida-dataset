# Candidate Root Cause

**Generated:** 2026-08-16T07:46:40+00:00
**Session:** `SESSION-20260816-E7664D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000307`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260816-E7664D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000307': 1, 'duplicate_id:SIG-000308': 1, 'duplicate_id:SIG-000309': 1, 'duplicate_id:SIG-000306': 1, 'duplicate_id:SIG-000310': 1}`
- `candidate CAND-2B820A70E3B3 entity_id=SIG-000307 reason=duplicate_id:SIG-000307 conf=0.9`
- `candidate CAND-6FB39FA764BC entity_id=SIG-000308 reason=duplicate_id:SIG-000308 conf=0.9`
- `candidate CAND-55CDB28FE951 entity_id=SIG-000309 reason=duplicate_id:SIG-000309 conf=0.9`
- `candidate CAND-2FEFF3EBA209 entity_id=SIG-000306 reason=duplicate_id:SIG-000306 conf=0.92`
- `candidate CAND-0211B702AE55 entity_id=SIG-000310 reason=duplicate_id:SIG-000310 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-2B820A70E3B3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000307 | Rejected |
| CAND-6FB39FA764BC | business_signal_library | 0.9 | False | duplicate_id:SIG-000308 | Rejected |
| CAND-55CDB28FE951 | business_signal_library | 0.9 | False | duplicate_id:SIG-000309 | Rejected |
| CAND-2FEFF3EBA209 | business_signal_library | 0.92 | False | duplicate_id:SIG-000306 | Rejected |
| CAND-0211B702AE55 | business_signal_library | 0.9 | False | duplicate_id:SIG-000310 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000307` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
