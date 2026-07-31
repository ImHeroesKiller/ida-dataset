# Candidate Root Cause

**Generated:** 2026-07-31T00:22:40+00:00
**Session:** `SESSION-20260731-15EB0D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001130`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260731-15EB0D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001130': 1, 'duplicate_id:SIG-001134': 1, 'duplicate_id:SIG-001133': 1, 'duplicate_id:SIG-001132': 1, 'duplicate_id:SIG-001131': 1}`
- `candidate CAND-EA635D13F379 entity_id=SIG-001130 reason=duplicate_id:SIG-001130 conf=0.9`
- `candidate CAND-FAB96D239525 entity_id=SIG-001134 reason=duplicate_id:SIG-001134 conf=0.92`
- `candidate CAND-F48712367466 entity_id=SIG-001133 reason=duplicate_id:SIG-001133 conf=0.9`
- `candidate CAND-E24C274426C6 entity_id=SIG-001132 reason=duplicate_id:SIG-001132 conf=0.88`
- `candidate CAND-1372BB8E91B8 entity_id=SIG-001131 reason=duplicate_id:SIG-001131 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-EA635D13F379 | business_signal_library | 0.9 | False | duplicate_id:SIG-001130 | Rejected |
| CAND-FAB96D239525 | business_signal_library | 0.92 | False | duplicate_id:SIG-001134 | Rejected |
| CAND-F48712367466 | business_signal_library | 0.9 | False | duplicate_id:SIG-001133 | Rejected |
| CAND-E24C274426C6 | business_signal_library | 0.88 | False | duplicate_id:SIG-001132 | Rejected |
| CAND-1372BB8E91B8 | business_signal_library | 0.92 | False | duplicate_id:SIG-001131 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001130` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
