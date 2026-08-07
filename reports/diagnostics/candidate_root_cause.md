# Candidate Root Cause

**Generated:** 2026-08-07T12:04:59+00:00
**Session:** `SESSION-20260807-176364`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001508`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260807-176364`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001508': 1, 'duplicate_id:SIG-001509': 1, 'duplicate_id:SIG-001506': 1, 'duplicate_id:SIG-001507': 1, 'duplicate_id:SIG-001505': 1}`
- `candidate CAND-9BE4CC0C7081 entity_id=SIG-001508 reason=duplicate_id:SIG-001508 conf=0.9`
- `candidate CAND-8E31C21C4D1D entity_id=SIG-001509 reason=duplicate_id:SIG-001509 conf=0.92`
- `candidate CAND-8F47E84752EB entity_id=SIG-001506 reason=duplicate_id:SIG-001506 conf=0.92`
- `candidate CAND-5A4086F44504 entity_id=SIG-001507 reason=duplicate_id:SIG-001507 conf=0.88`
- `candidate CAND-483DA361C25C entity_id=SIG-001505 reason=duplicate_id:SIG-001505 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-9BE4CC0C7081 | business_signal_library | 0.9 | False | duplicate_id:SIG-001508 | Rejected |
| CAND-8E31C21C4D1D | business_signal_library | 0.92 | False | duplicate_id:SIG-001509 | Rejected |
| CAND-8F47E84752EB | business_signal_library | 0.92 | False | duplicate_id:SIG-001506 | Rejected |
| CAND-5A4086F44504 | business_signal_library | 0.88 | False | duplicate_id:SIG-001507 | Rejected |
| CAND-483DA361C25C | business_signal_library | 0.9 | False | duplicate_id:SIG-001505 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001508` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
