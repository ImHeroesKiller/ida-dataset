# Candidate Root Cause

**Generated:** 2026-08-10T20:17:29+00:00
**Session:** `SESSION-20260810-9F3D4E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001839`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260810-9F3D4E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001839': 1, 'duplicate_id:SIG-001837': 1, 'duplicate_id:SIG-001835': 1, 'duplicate_id:SIG-001836': 1, 'duplicate_id:SIG-001838': 1}`
- `candidate CAND-1A6F0FD231F6 entity_id=SIG-001839 reason=duplicate_id:SIG-001839 conf=0.92`
- `candidate CAND-E100B2AE9CA6 entity_id=SIG-001837 reason=duplicate_id:SIG-001837 conf=0.88`
- `candidate CAND-19505A89FB6D entity_id=SIG-001835 reason=duplicate_id:SIG-001835 conf=0.9`
- `candidate CAND-ED556265E4E4 entity_id=SIG-001836 reason=duplicate_id:SIG-001836 conf=0.92`
- `candidate CAND-F41A88CCD83E entity_id=SIG-001838 reason=duplicate_id:SIG-001838 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-1A6F0FD231F6 | business_signal_library | 0.92 | False | duplicate_id:SIG-001839 | Rejected |
| CAND-E100B2AE9CA6 | business_signal_library | 0.88 | False | duplicate_id:SIG-001837 | Rejected |
| CAND-19505A89FB6D | business_signal_library | 0.9 | False | duplicate_id:SIG-001835 | Rejected |
| CAND-ED556265E4E4 | business_signal_library | 0.92 | False | duplicate_id:SIG-001836 | Rejected |
| CAND-F41A88CCD83E | business_signal_library | 0.9 | False | duplicate_id:SIG-001838 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001839` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
