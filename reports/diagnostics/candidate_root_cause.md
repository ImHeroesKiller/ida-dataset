# Candidate Root Cause

**Generated:** 2026-07-21T00:15:30+00:00
**Session:** `SESSION-20260720-4E7A2E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000597`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260720-4E7A2E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000597': 1, 'duplicate_id:SIG-000596': 1, 'duplicate_id:SIG-000598': 1, 'duplicate_id:SIG-000599': 1, 'duplicate_id:SIG-000595': 1}`
- `candidate CAND-F8A9B91246F4 entity_id=SIG-000597 reason=duplicate_id:SIG-000597 conf=0.88`
- `candidate CAND-4C67DA4E0C0E entity_id=SIG-000596 reason=duplicate_id:SIG-000596 conf=0.92`
- `candidate CAND-E2FB5168FD64 entity_id=SIG-000598 reason=duplicate_id:SIG-000598 conf=0.9`
- `candidate CAND-D7BE09E75E79 entity_id=SIG-000599 reason=duplicate_id:SIG-000599 conf=0.92`
- `candidate CAND-337276B07A53 entity_id=SIG-000595 reason=duplicate_id:SIG-000595 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F8A9B91246F4 | business_signal_library | 0.88 | False | duplicate_id:SIG-000597 | Rejected |
| CAND-4C67DA4E0C0E | business_signal_library | 0.92 | False | duplicate_id:SIG-000596 | Rejected |
| CAND-E2FB5168FD64 | business_signal_library | 0.9 | False | duplicate_id:SIG-000598 | Rejected |
| CAND-D7BE09E75E79 | business_signal_library | 0.92 | False | duplicate_id:SIG-000599 | Rejected |
| CAND-337276B07A53 | business_signal_library | 0.9 | False | duplicate_id:SIG-000595 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000597` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
