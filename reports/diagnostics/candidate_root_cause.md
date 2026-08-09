# Candidate Root Cause

**Generated:** 2026-08-09T05:25:14+00:00
**Session:** `SESSION-20260809-27FEE2`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001687`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260809-27FEE2`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001687': 1, 'duplicate_id:SIG-001686': 1, 'duplicate_id:SIG-001685': 1, 'duplicate_id:SIG-001689': 1, 'duplicate_id:SIG-001688': 1}`
- `candidate CAND-FE1B7B8AFA81 entity_id=SIG-001687 reason=duplicate_id:SIG-001687 conf=0.88`
- `candidate CAND-714EA768C8AF entity_id=SIG-001686 reason=duplicate_id:SIG-001686 conf=0.92`
- `candidate CAND-BC43C1233A8C entity_id=SIG-001685 reason=duplicate_id:SIG-001685 conf=0.9`
- `candidate CAND-AFB22C3F061C entity_id=SIG-001689 reason=duplicate_id:SIG-001689 conf=0.92`
- `candidate CAND-6FF092643723 entity_id=SIG-001688 reason=duplicate_id:SIG-001688 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-FE1B7B8AFA81 | business_signal_library | 0.88 | False | duplicate_id:SIG-001687 | Rejected |
| CAND-714EA768C8AF | business_signal_library | 0.92 | False | duplicate_id:SIG-001686 | Rejected |
| CAND-BC43C1233A8C | business_signal_library | 0.9 | False | duplicate_id:SIG-001685 | Rejected |
| CAND-AFB22C3F061C | business_signal_library | 0.92 | False | duplicate_id:SIG-001689 | Rejected |
| CAND-6FF092643723 | business_signal_library | 0.9 | False | duplicate_id:SIG-001688 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001687` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
