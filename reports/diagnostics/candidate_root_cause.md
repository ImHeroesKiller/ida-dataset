# Candidate Root Cause

**Generated:** 2026-08-08T09:04:01+00:00
**Session:** `SESSION-20260808-751B9D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001599`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260808-751B9D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001599': 1, 'duplicate_id:SIG-001597': 1, 'duplicate_id:SIG-001598': 1, 'duplicate_id:SIG-001595': 1, 'duplicate_id:SIG-001596': 1}`
- `candidate CAND-FD19CA7DFE51 entity_id=SIG-001599 reason=duplicate_id:SIG-001599 conf=0.92`
- `candidate CAND-C1DDDE960B91 entity_id=SIG-001597 reason=duplicate_id:SIG-001597 conf=0.88`
- `candidate CAND-BFBA2C158E6E entity_id=SIG-001598 reason=duplicate_id:SIG-001598 conf=0.9`
- `candidate CAND-F3D7F6BE6C38 entity_id=SIG-001595 reason=duplicate_id:SIG-001595 conf=0.9`
- `candidate CAND-91DE0021B142 entity_id=SIG-001596 reason=duplicate_id:SIG-001596 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-FD19CA7DFE51 | business_signal_library | 0.92 | False | duplicate_id:SIG-001599 | Rejected |
| CAND-C1DDDE960B91 | business_signal_library | 0.88 | False | duplicate_id:SIG-001597 | Rejected |
| CAND-BFBA2C158E6E | business_signal_library | 0.9 | False | duplicate_id:SIG-001598 | Rejected |
| CAND-F3D7F6BE6C38 | business_signal_library | 0.9 | False | duplicate_id:SIG-001595 | Rejected |
| CAND-91DE0021B142 | business_signal_library | 0.92 | False | duplicate_id:SIG-001596 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001599` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
