# Candidate Root Cause

**Generated:** 2026-08-22T14:41:09+00:00
**Session:** `SESSION-20260822-B5C5B2`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001022`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260822-B5C5B2`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001022': 1, 'duplicate_id:SIG-001023': 1, 'duplicate_id:SIG-001024': 1, 'duplicate_id:SIG-001021': 1, 'duplicate_id:SIG-001025': 1}`
- `candidate CAND-EDA851F236D1 entity_id=SIG-001022 reason=duplicate_id:SIG-001022 conf=0.9`
- `candidate CAND-D52753E5F6BF entity_id=SIG-001023 reason=duplicate_id:SIG-001023 conf=0.9`
- `candidate CAND-59EB9108A0EC entity_id=SIG-001024 reason=duplicate_id:SIG-001024 conf=0.9`
- `candidate CAND-AC0EBFE5E1FB entity_id=SIG-001021 reason=duplicate_id:SIG-001021 conf=0.92`
- `candidate CAND-BA96021EEB4E entity_id=SIG-001025 reason=duplicate_id:SIG-001025 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-EDA851F236D1 | business_signal_library | 0.9 | False | duplicate_id:SIG-001022 | Rejected |
| CAND-D52753E5F6BF | business_signal_library | 0.9 | False | duplicate_id:SIG-001023 | Rejected |
| CAND-59EB9108A0EC | business_signal_library | 0.9 | False | duplicate_id:SIG-001024 | Rejected |
| CAND-AC0EBFE5E1FB | business_signal_library | 0.92 | False | duplicate_id:SIG-001021 | Rejected |
| CAND-BA96021EEB4E | business_signal_library | 0.9 | False | duplicate_id:SIG-001025 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001022` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
