# Candidate Root Cause

**Generated:** 2026-07-18T23:10:22+00:00
**Session:** `SESSION-20260718-CDEDA7`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000471`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260718-CDEDA7`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000471': 1, 'duplicate_id:SIG-000472': 1, 'duplicate_id:SIG-000473': 1, 'duplicate_id:SIG-000474': 1, 'duplicate_id:SIG-000470': 1}`
- `candidate CAND-148A618804CB entity_id=SIG-000471 reason=duplicate_id:SIG-000471 conf=0.92`
- `candidate CAND-8EE68249F6AB entity_id=SIG-000472 reason=duplicate_id:SIG-000472 conf=0.9`
- `candidate CAND-F18B12F4FAE7 entity_id=SIG-000473 reason=duplicate_id:SIG-000473 conf=0.92`
- `candidate CAND-CE114C00B870 entity_id=SIG-000474 reason=duplicate_id:SIG-000474 conf=0.9`
- `candidate CAND-0616C3422B01 entity_id=SIG-000470 reason=duplicate_id:SIG-000470 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-148A618804CB | business_signal_library | 0.92 | False | duplicate_id:SIG-000471 | Rejected |
| CAND-8EE68249F6AB | business_signal_library | 0.9 | False | duplicate_id:SIG-000472 | Rejected |
| CAND-F18B12F4FAE7 | business_signal_library | 0.92 | False | duplicate_id:SIG-000473 | Rejected |
| CAND-CE114C00B870 | business_signal_library | 0.9 | False | duplicate_id:SIG-000474 | Rejected |
| CAND-0616C3422B01 | business_signal_library | 0.9 | False | duplicate_id:SIG-000470 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000471` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
