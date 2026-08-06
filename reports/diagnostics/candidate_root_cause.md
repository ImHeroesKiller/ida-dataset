# Candidate Root Cause

**Generated:** 2026-08-06T11:45:24+00:00
**Session:** `SESSION-20260806-82D801`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001465`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260806-82D801`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001465': 1, 'duplicate_id:SIG-001466': 1, 'duplicate_id:SIG-001468': 1, 'duplicate_id:SIG-001467': 1, 'duplicate_id:SIG-001469': 1}`
- `candidate CAND-A07D971D4CA5 entity_id=SIG-001465 reason=duplicate_id:SIG-001465 conf=0.9`
- `candidate CAND-712660CD84E1 entity_id=SIG-001466 reason=duplicate_id:SIG-001466 conf=0.92`
- `candidate CAND-FC94AFF8DAE9 entity_id=SIG-001468 reason=duplicate_id:SIG-001468 conf=0.9`
- `candidate CAND-421296AA41B4 entity_id=SIG-001467 reason=duplicate_id:SIG-001467 conf=0.88`
- `candidate CAND-7D73C1C5F091 entity_id=SIG-001469 reason=duplicate_id:SIG-001469 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A07D971D4CA5 | business_signal_library | 0.9 | False | duplicate_id:SIG-001465 | Rejected |
| CAND-712660CD84E1 | business_signal_library | 0.92 | False | duplicate_id:SIG-001466 | Rejected |
| CAND-FC94AFF8DAE9 | business_signal_library | 0.9 | False | duplicate_id:SIG-001468 | Rejected |
| CAND-421296AA41B4 | business_signal_library | 0.88 | False | duplicate_id:SIG-001467 | Rejected |
| CAND-7D73C1C5F091 | business_signal_library | 0.92 | False | duplicate_id:SIG-001469 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001465` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
