# Candidate Root Cause

**Generated:** 2026-08-01T11:00:20+00:00
**Session:** `SESSION-20260801-1EF30E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001203`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260801-1EF30E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001203': 1, 'duplicate_id:SIG-001202': 1, 'duplicate_id:SIG-001200': 1, 'duplicate_id:SIG-001201': 1, 'duplicate_id:SIG-001204': 1}`
- `candidate CAND-D7359B056922 entity_id=SIG-001203 reason=duplicate_id:SIG-001203 conf=0.9`
- `candidate CAND-630672ACDA47 entity_id=SIG-001202 reason=duplicate_id:SIG-001202 conf=0.88`
- `candidate CAND-48FE05C26152 entity_id=SIG-001200 reason=duplicate_id:SIG-001200 conf=0.9`
- `candidate CAND-D4DDD4324148 entity_id=SIG-001201 reason=duplicate_id:SIG-001201 conf=0.92`
- `candidate CAND-6BAC190E7CC1 entity_id=SIG-001204 reason=duplicate_id:SIG-001204 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-D7359B056922 | business_signal_library | 0.9 | False | duplicate_id:SIG-001203 | Rejected |
| CAND-630672ACDA47 | business_signal_library | 0.88 | False | duplicate_id:SIG-001202 | Rejected |
| CAND-48FE05C26152 | business_signal_library | 0.9 | False | duplicate_id:SIG-001200 | Rejected |
| CAND-D4DDD4324148 | business_signal_library | 0.92 | False | duplicate_id:SIG-001201 | Rejected |
| CAND-6BAC190E7CC1 | business_signal_library | 0.92 | False | duplicate_id:SIG-001204 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001203` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
