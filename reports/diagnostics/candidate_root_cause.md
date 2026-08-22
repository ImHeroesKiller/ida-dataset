# Candidate Root Cause

**Generated:** 2026-08-22T17:40:07+00:00
**Session:** `SESSION-20260822-2115DF`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001040`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260822-2115DF`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001040': 1, 'duplicate_id:SIG-001036': 1, 'duplicate_id:SIG-001037': 1, 'duplicate_id:SIG-001038': 1, 'duplicate_id:SIG-001039': 1}`
- `candidate CAND-74B54A8BF3A2 entity_id=SIG-001040 reason=duplicate_id:SIG-001040 conf=0.9`
- `candidate CAND-370FBBF7A154 entity_id=SIG-001036 reason=duplicate_id:SIG-001036 conf=0.92`
- `candidate CAND-1DB735EDD3E0 entity_id=SIG-001037 reason=duplicate_id:SIG-001037 conf=0.9`
- `candidate CAND-C4B9908ED691 entity_id=SIG-001038 reason=duplicate_id:SIG-001038 conf=0.9`
- `candidate CAND-2BB6081A732C entity_id=SIG-001039 reason=duplicate_id:SIG-001039 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-74B54A8BF3A2 | business_signal_library | 0.9 | False | duplicate_id:SIG-001040 | Rejected |
| CAND-370FBBF7A154 | business_signal_library | 0.92 | False | duplicate_id:SIG-001036 | Rejected |
| CAND-1DB735EDD3E0 | business_signal_library | 0.9 | False | duplicate_id:SIG-001037 | Rejected |
| CAND-C4B9908ED691 | business_signal_library | 0.9 | False | duplicate_id:SIG-001038 | Rejected |
| CAND-2BB6081A732C | business_signal_library | 0.9 | False | duplicate_id:SIG-001039 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001040` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
