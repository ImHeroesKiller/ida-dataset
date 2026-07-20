# Candidate Root Cause

**Generated:** 2026-07-20T10:32:57+00:00
**Session:** `SESSION-20260720-4E5AF8`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000569`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260720-4E5AF8`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000569': 1, 'duplicate_id:SIG-000565': 1, 'duplicate_id:SIG-000566': 1, 'duplicate_id:SIG-000568': 1, 'duplicate_id:SIG-000567': 1}`
- `candidate CAND-B92BD808582F entity_id=SIG-000569 reason=duplicate_id:SIG-000569 conf=0.92`
- `candidate CAND-82A4D82D7F89 entity_id=SIG-000565 reason=duplicate_id:SIG-000565 conf=0.9`
- `candidate CAND-8C92B488A9BC entity_id=SIG-000566 reason=duplicate_id:SIG-000566 conf=0.92`
- `candidate CAND-ACCA18CAC52C entity_id=SIG-000568 reason=duplicate_id:SIG-000568 conf=0.9`
- `candidate CAND-F3B9A3E0D22E entity_id=SIG-000567 reason=duplicate_id:SIG-000567 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B92BD808582F | business_signal_library | 0.92 | False | duplicate_id:SIG-000569 | Rejected |
| CAND-82A4D82D7F89 | business_signal_library | 0.9 | False | duplicate_id:SIG-000565 | Rejected |
| CAND-8C92B488A9BC | business_signal_library | 0.92 | False | duplicate_id:SIG-000566 | Rejected |
| CAND-ACCA18CAC52C | business_signal_library | 0.9 | False | duplicate_id:SIG-000568 | Rejected |
| CAND-F3B9A3E0D22E | business_signal_library | 0.88 | False | duplicate_id:SIG-000567 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000569` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
