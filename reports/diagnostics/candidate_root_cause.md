# Candidate Root Cause

**Generated:** 2026-08-05T19:54:28+00:00
**Session:** `SESSION-20260805-8260BE`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001439`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260805-8260BE`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001439': 1, 'duplicate_id:SIG-001435': 1, 'duplicate_id:SIG-001438': 1, 'duplicate_id:SIG-001436': 1, 'duplicate_id:SIG-001437': 1}`
- `candidate CAND-E885D4EC698A entity_id=SIG-001439 reason=duplicate_id:SIG-001439 conf=0.92`
- `candidate CAND-C019C398CDFE entity_id=SIG-001435 reason=duplicate_id:SIG-001435 conf=0.9`
- `candidate CAND-80E6147DC1F8 entity_id=SIG-001438 reason=duplicate_id:SIG-001438 conf=0.9`
- `candidate CAND-FCE3D3F51017 entity_id=SIG-001436 reason=duplicate_id:SIG-001436 conf=0.92`
- `candidate CAND-D9FD6295A9EB entity_id=SIG-001437 reason=duplicate_id:SIG-001437 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-E885D4EC698A | business_signal_library | 0.92 | False | duplicate_id:SIG-001439 | Rejected |
| CAND-C019C398CDFE | business_signal_library | 0.9 | False | duplicate_id:SIG-001435 | Rejected |
| CAND-80E6147DC1F8 | business_signal_library | 0.9 | False | duplicate_id:SIG-001438 | Rejected |
| CAND-FCE3D3F51017 | business_signal_library | 0.92 | False | duplicate_id:SIG-001436 | Rejected |
| CAND-D9FD6295A9EB | business_signal_library | 0.88 | False | duplicate_id:SIG-001437 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001439` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
