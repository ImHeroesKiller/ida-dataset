# Candidate Root Cause

**Generated:** 2026-08-18T18:51:56+00:00
**Session:** `SESSION-20260818-322DA8`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000587`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260818-322DA8`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000587': 1, 'duplicate_id:SIG-000588': 1, 'duplicate_id:SIG-000589': 1, 'duplicate_id:SIG-000586': 1, 'duplicate_id:SIG-000590': 1}`
- `candidate CAND-B45129AD650E entity_id=SIG-000587 reason=duplicate_id:SIG-000587 conf=0.9`
- `candidate CAND-07190E4E5702 entity_id=SIG-000588 reason=duplicate_id:SIG-000588 conf=0.9`
- `candidate CAND-C5D708703993 entity_id=SIG-000589 reason=duplicate_id:SIG-000589 conf=0.9`
- `candidate CAND-3CA0D2239532 entity_id=SIG-000586 reason=duplicate_id:SIG-000586 conf=0.92`
- `candidate CAND-694FD3C7B5F9 entity_id=SIG-000590 reason=duplicate_id:SIG-000590 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B45129AD650E | business_signal_library | 0.9 | False | duplicate_id:SIG-000587 | Rejected |
| CAND-07190E4E5702 | business_signal_library | 0.9 | False | duplicate_id:SIG-000588 | Rejected |
| CAND-C5D708703993 | business_signal_library | 0.9 | False | duplicate_id:SIG-000589 | Rejected |
| CAND-3CA0D2239532 | business_signal_library | 0.92 | False | duplicate_id:SIG-000586 | Rejected |
| CAND-694FD3C7B5F9 | business_signal_library | 0.9 | False | duplicate_id:SIG-000590 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000587` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
