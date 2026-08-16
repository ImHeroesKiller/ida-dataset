# Candidate Root Cause

**Generated:** 2026-08-16T13:06:32+00:00
**Session:** `SESSION-20260816-516791`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000333`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260816-516791`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000333': 1, 'duplicate_id:SIG-000334': 1, 'duplicate_id:SIG-000335': 1, 'duplicate_id:SIG-000332': 1, 'duplicate_id:SIG-000331': 1}`
- `candidate CAND-5CC7784598BF entity_id=SIG-000333 reason=duplicate_id:SIG-000333 conf=0.9`
- `candidate CAND-0BE61B2AF8F8 entity_id=SIG-000334 reason=duplicate_id:SIG-000334 conf=0.9`
- `candidate CAND-DD1703FEE8AF entity_id=SIG-000335 reason=duplicate_id:SIG-000335 conf=0.9`
- `candidate CAND-5A6A77AF84E8 entity_id=SIG-000332 reason=duplicate_id:SIG-000332 conf=0.9`
- `candidate CAND-FD1DC60B6094 entity_id=SIG-000331 reason=duplicate_id:SIG-000331 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5CC7784598BF | business_signal_library | 0.9 | False | duplicate_id:SIG-000333 | Rejected |
| CAND-0BE61B2AF8F8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000334 | Rejected |
| CAND-DD1703FEE8AF | business_signal_library | 0.9 | False | duplicate_id:SIG-000335 | Rejected |
| CAND-5A6A77AF84E8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000332 | Rejected |
| CAND-FD1DC60B6094 | business_signal_library | 0.92 | False | duplicate_id:SIG-000331 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000333` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
