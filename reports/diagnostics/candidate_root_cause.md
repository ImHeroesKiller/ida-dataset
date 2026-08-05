# Candidate Root Cause

**Generated:** 2026-08-05T10:55:54+00:00
**Session:** `SESSION-20260805-9C0C71`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001417`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260805-9C0C71`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001417': 1, 'duplicate_id:SIG-001419': 1, 'duplicate_id:SIG-001415': 1, 'duplicate_id:SIG-001418': 1, 'duplicate_id:SIG-001416': 1}`
- `candidate CAND-33C91CA27A4F entity_id=SIG-001417 reason=duplicate_id:SIG-001417 conf=0.88`
- `candidate CAND-B882DE150772 entity_id=SIG-001419 reason=duplicate_id:SIG-001419 conf=0.92`
- `candidate CAND-91F69B2F8A9E entity_id=SIG-001415 reason=duplicate_id:SIG-001415 conf=0.9`
- `candidate CAND-D6192A22C74E entity_id=SIG-001418 reason=duplicate_id:SIG-001418 conf=0.9`
- `candidate CAND-B4AE2A653A21 entity_id=SIG-001416 reason=duplicate_id:SIG-001416 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-33C91CA27A4F | business_signal_library | 0.88 | False | duplicate_id:SIG-001417 | Rejected |
| CAND-B882DE150772 | business_signal_library | 0.92 | False | duplicate_id:SIG-001419 | Rejected |
| CAND-91F69B2F8A9E | business_signal_library | 0.9 | False | duplicate_id:SIG-001415 | Rejected |
| CAND-D6192A22C74E | business_signal_library | 0.9 | False | duplicate_id:SIG-001418 | Rejected |
| CAND-B4AE2A653A21 | business_signal_library | 0.92 | False | duplicate_id:SIG-001416 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001417` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
