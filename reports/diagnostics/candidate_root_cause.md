# Candidate Root Cause

**Generated:** 2026-08-12T13:31:40+00:00
**Session:** `SESSION-20260812-6CB042`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001977`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260812-6CB042`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001977': 1, 'duplicate_id:SIG-001976': 1, 'duplicate_id:SIG-001979': 1, 'duplicate_id:SIG-001978': 1, 'duplicate_id:SIG-001975': 1}`
- `candidate CAND-ED195C17B615 entity_id=SIG-001977 reason=duplicate_id:SIG-001977 conf=0.88`
- `candidate CAND-D61FCEBB671F entity_id=SIG-001976 reason=duplicate_id:SIG-001976 conf=0.92`
- `candidate CAND-16FF29572CE8 entity_id=SIG-001979 reason=duplicate_id:SIG-001979 conf=0.92`
- `candidate CAND-34E2F5D63E75 entity_id=SIG-001978 reason=duplicate_id:SIG-001978 conf=0.9`
- `candidate CAND-59DB696987B1 entity_id=SIG-001975 reason=duplicate_id:SIG-001975 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-ED195C17B615 | business_signal_library | 0.88 | False | duplicate_id:SIG-001977 | Rejected |
| CAND-D61FCEBB671F | business_signal_library | 0.92 | False | duplicate_id:SIG-001976 | Rejected |
| CAND-16FF29572CE8 | business_signal_library | 0.92 | False | duplicate_id:SIG-001979 | Rejected |
| CAND-34E2F5D63E75 | business_signal_library | 0.9 | False | duplicate_id:SIG-001978 | Rejected |
| CAND-59DB696987B1 | business_signal_library | 0.9 | False | duplicate_id:SIG-001975 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001977` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
