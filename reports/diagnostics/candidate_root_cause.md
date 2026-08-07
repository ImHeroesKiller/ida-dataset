# Candidate Root Cause

**Generated:** 2026-08-07T16:15:35+00:00
**Session:** `SESSION-20260807-B4384A`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001522`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260807-B4384A`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001522': 1, 'duplicate_id:SIG-001521': 1, 'duplicate_id:SIG-001520': 1, 'duplicate_id:SIG-001523': 1, 'duplicate_id:SIG-001524': 1}`
- `candidate CAND-2A37DE0C49B4 entity_id=SIG-001522 reason=duplicate_id:SIG-001522 conf=0.88`
- `candidate CAND-D2D79C15A4AA entity_id=SIG-001521 reason=duplicate_id:SIG-001521 conf=0.92`
- `candidate CAND-57633E3C155F entity_id=SIG-001520 reason=duplicate_id:SIG-001520 conf=0.9`
- `candidate CAND-603DEB3BAE13 entity_id=SIG-001523 reason=duplicate_id:SIG-001523 conf=0.9`
- `candidate CAND-36E3A36E10E4 entity_id=SIG-001524 reason=duplicate_id:SIG-001524 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-2A37DE0C49B4 | business_signal_library | 0.88 | False | duplicate_id:SIG-001522 | Rejected |
| CAND-D2D79C15A4AA | business_signal_library | 0.92 | False | duplicate_id:SIG-001521 | Rejected |
| CAND-57633E3C155F | business_signal_library | 0.9 | False | duplicate_id:SIG-001520 | Rejected |
| CAND-603DEB3BAE13 | business_signal_library | 0.9 | False | duplicate_id:SIG-001523 | Rejected |
| CAND-36E3A36E10E4 | business_signal_library | 0.92 | False | duplicate_id:SIG-001524 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001522` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
