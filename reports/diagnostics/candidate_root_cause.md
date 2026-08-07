# Candidate Root Cause

**Generated:** 2026-08-07T23:52:58+00:00
**Session:** `SESSION-20260807-E9CF12`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001562`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260807-E9CF12`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001562': 1, 'duplicate_id:SIG-001564': 1, 'duplicate_id:SIG-001563': 1, 'duplicate_id:SIG-001560': 1, 'duplicate_id:SIG-001561': 1}`
- `candidate CAND-352716BB613B entity_id=SIG-001562 reason=duplicate_id:SIG-001562 conf=0.88`
- `candidate CAND-EC55D7E9B05D entity_id=SIG-001564 reason=duplicate_id:SIG-001564 conf=0.92`
- `candidate CAND-CEFDC07E10DB entity_id=SIG-001563 reason=duplicate_id:SIG-001563 conf=0.9`
- `candidate CAND-A7421251B96C entity_id=SIG-001560 reason=duplicate_id:SIG-001560 conf=0.9`
- `candidate CAND-7C58040827A8 entity_id=SIG-001561 reason=duplicate_id:SIG-001561 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-352716BB613B | business_signal_library | 0.88 | False | duplicate_id:SIG-001562 | Rejected |
| CAND-EC55D7E9B05D | business_signal_library | 0.92 | False | duplicate_id:SIG-001564 | Rejected |
| CAND-CEFDC07E10DB | business_signal_library | 0.9 | False | duplicate_id:SIG-001563 | Rejected |
| CAND-A7421251B96C | business_signal_library | 0.9 | False | duplicate_id:SIG-001560 | Rejected |
| CAND-7C58040827A8 | business_signal_library | 0.92 | False | duplicate_id:SIG-001561 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001562` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
