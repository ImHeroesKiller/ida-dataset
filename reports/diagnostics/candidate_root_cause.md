# Candidate Root Cause

**Generated:** 2026-07-25T10:07:47+00:00
**Session:** `SESSION-20260725-50622A`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000831`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260725-50622A`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000831': 1, 'duplicate_id:SIG-000833': 1, 'duplicate_id:SIG-000832': 1, 'duplicate_id:SIG-000830': 1, 'duplicate_id:SIG-000834': 1}`
- `candidate CAND-BDBF926CEC7E entity_id=SIG-000831 reason=duplicate_id:SIG-000831 conf=0.92`
- `candidate CAND-D21293329A13 entity_id=SIG-000833 reason=duplicate_id:SIG-000833 conf=0.9`
- `candidate CAND-2ED9F275A7C6 entity_id=SIG-000832 reason=duplicate_id:SIG-000832 conf=0.88`
- `candidate CAND-5F4F1E4F05DC entity_id=SIG-000830 reason=duplicate_id:SIG-000830 conf=0.9`
- `candidate CAND-586C91FDF5E2 entity_id=SIG-000834 reason=duplicate_id:SIG-000834 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-BDBF926CEC7E | business_signal_library | 0.92 | False | duplicate_id:SIG-000831 | Rejected |
| CAND-D21293329A13 | business_signal_library | 0.9 | False | duplicate_id:SIG-000833 | Rejected |
| CAND-2ED9F275A7C6 | business_signal_library | 0.88 | False | duplicate_id:SIG-000832 | Rejected |
| CAND-5F4F1E4F05DC | business_signal_library | 0.9 | False | duplicate_id:SIG-000830 | Rejected |
| CAND-586C91FDF5E2 | business_signal_library | 0.92 | False | duplicate_id:SIG-000834 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000831` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
