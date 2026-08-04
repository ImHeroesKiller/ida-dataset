# Candidate Root Cause

**Generated:** 2026-08-04T08:03:13+00:00
**Session:** `SESSION-20260804-11F65D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001358`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260804-11F65D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001358': 1, 'duplicate_id:SIG-001357': 1, 'duplicate_id:SIG-001356': 1, 'duplicate_id:SIG-001355': 1, 'duplicate_id:SIG-001359': 1}`
- `candidate CAND-B1DE81DFD822 entity_id=SIG-001358 reason=duplicate_id:SIG-001358 conf=0.9`
- `candidate CAND-D3523587590B entity_id=SIG-001357 reason=duplicate_id:SIG-001357 conf=0.88`
- `candidate CAND-323B7F571169 entity_id=SIG-001356 reason=duplicate_id:SIG-001356 conf=0.92`
- `candidate CAND-38B3F953589F entity_id=SIG-001355 reason=duplicate_id:SIG-001355 conf=0.9`
- `candidate CAND-EA097C8738BC entity_id=SIG-001359 reason=duplicate_id:SIG-001359 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B1DE81DFD822 | business_signal_library | 0.9 | False | duplicate_id:SIG-001358 | Rejected |
| CAND-D3523587590B | business_signal_library | 0.88 | False | duplicate_id:SIG-001357 | Rejected |
| CAND-323B7F571169 | business_signal_library | 0.92 | False | duplicate_id:SIG-001356 | Rejected |
| CAND-38B3F953589F | business_signal_library | 0.9 | False | duplicate_id:SIG-001355 | Rejected |
| CAND-EA097C8738BC | business_signal_library | 0.92 | False | duplicate_id:SIG-001359 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001358` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
