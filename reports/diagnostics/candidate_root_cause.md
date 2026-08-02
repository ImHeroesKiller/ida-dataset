# Candidate Root Cause

**Generated:** 2026-08-02T11:35:39+00:00
**Session:** `SESSION-20260802-A13A6F`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001263`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260802-A13A6F`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001263': 1, 'duplicate_id:SIG-001262': 1, 'duplicate_id:SIG-001260': 1, 'duplicate_id:SIG-001261': 1, 'duplicate_id:SIG-001264': 1}`
- `candidate CAND-A97413E6ED17 entity_id=SIG-001263 reason=duplicate_id:SIG-001263 conf=0.9`
- `candidate CAND-CDDBBB7E7D40 entity_id=SIG-001262 reason=duplicate_id:SIG-001262 conf=0.88`
- `candidate CAND-1570F2C3A71D entity_id=SIG-001260 reason=duplicate_id:SIG-001260 conf=0.9`
- `candidate CAND-5647D642D056 entity_id=SIG-001261 reason=duplicate_id:SIG-001261 conf=0.92`
- `candidate CAND-3D56E35F6B0B entity_id=SIG-001264 reason=duplicate_id:SIG-001264 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A97413E6ED17 | business_signal_library | 0.9 | False | duplicate_id:SIG-001263 | Rejected |
| CAND-CDDBBB7E7D40 | business_signal_library | 0.88 | False | duplicate_id:SIG-001262 | Rejected |
| CAND-1570F2C3A71D | business_signal_library | 0.9 | False | duplicate_id:SIG-001260 | Rejected |
| CAND-5647D642D056 | business_signal_library | 0.92 | False | duplicate_id:SIG-001261 | Rejected |
| CAND-3D56E35F6B0B | business_signal_library | 0.92 | False | duplicate_id:SIG-001264 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001263` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
