# Candidate Root Cause

**Generated:** 2026-08-08T19:51:39+00:00
**Session:** `SESSION-20260808-AD245D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001653`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260808-AD245D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001653': 1, 'duplicate_id:SIG-001650': 1, 'duplicate_id:SIG-001654': 1, 'duplicate_id:SIG-001651': 1, 'duplicate_id:SIG-001652': 1}`
- `candidate CAND-3350259D09DE entity_id=SIG-001653 reason=duplicate_id:SIG-001653 conf=0.9`
- `candidate CAND-61A96C7F45FE entity_id=SIG-001650 reason=duplicate_id:SIG-001650 conf=0.9`
- `candidate CAND-77D459AC3D53 entity_id=SIG-001654 reason=duplicate_id:SIG-001654 conf=0.92`
- `candidate CAND-1A620B43CB5C entity_id=SIG-001651 reason=duplicate_id:SIG-001651 conf=0.92`
- `candidate CAND-4DF60D34538A entity_id=SIG-001652 reason=duplicate_id:SIG-001652 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-3350259D09DE | business_signal_library | 0.9 | False | duplicate_id:SIG-001653 | Rejected |
| CAND-61A96C7F45FE | business_signal_library | 0.9 | False | duplicate_id:SIG-001650 | Rejected |
| CAND-77D459AC3D53 | business_signal_library | 0.92 | False | duplicate_id:SIG-001654 | Rejected |
| CAND-1A620B43CB5C | business_signal_library | 0.92 | False | duplicate_id:SIG-001651 | Rejected |
| CAND-4DF60D34538A | business_signal_library | 0.88 | False | duplicate_id:SIG-001652 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001653` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
