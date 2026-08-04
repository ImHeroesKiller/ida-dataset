# Candidate Root Cause

**Generated:** 2026-08-04T13:20:24+00:00
**Session:** `SESSION-20260804-33D8C7`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001373`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260804-33D8C7`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001373': 1, 'duplicate_id:SIG-001370': 1, 'duplicate_id:SIG-001374': 1, 'duplicate_id:SIG-001371': 1, 'duplicate_id:SIG-001372': 1}`
- `candidate CAND-73438698DAB7 entity_id=SIG-001373 reason=duplicate_id:SIG-001373 conf=0.9`
- `candidate CAND-37B8BEFE0466 entity_id=SIG-001370 reason=duplicate_id:SIG-001370 conf=0.9`
- `candidate CAND-9A3BAC7A8641 entity_id=SIG-001374 reason=duplicate_id:SIG-001374 conf=0.92`
- `candidate CAND-B17A5D193A6F entity_id=SIG-001371 reason=duplicate_id:SIG-001371 conf=0.92`
- `candidate CAND-D7D413B38E06 entity_id=SIG-001372 reason=duplicate_id:SIG-001372 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-73438698DAB7 | business_signal_library | 0.9 | False | duplicate_id:SIG-001373 | Rejected |
| CAND-37B8BEFE0466 | business_signal_library | 0.9 | False | duplicate_id:SIG-001370 | Rejected |
| CAND-9A3BAC7A8641 | business_signal_library | 0.92 | False | duplicate_id:SIG-001374 | Rejected |
| CAND-B17A5D193A6F | business_signal_library | 0.92 | False | duplicate_id:SIG-001371 | Rejected |
| CAND-D7D413B38E06 | business_signal_library | 0.88 | False | duplicate_id:SIG-001372 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001373` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
