# Candidate Root Cause

**Generated:** 2026-08-07T09:18:22+00:00
**Session:** `SESSION-20260807-F4AE3C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001498`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260807-F4AE3C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001498': 1, 'duplicate_id:SIG-001497': 1, 'duplicate_id:SIG-001496': 1, 'duplicate_id:SIG-001499': 1, 'duplicate_id:SIG-001495': 1}`
- `candidate CAND-94FDCF359D24 entity_id=SIG-001498 reason=duplicate_id:SIG-001498 conf=0.9`
- `candidate CAND-3EC561ADB9A4 entity_id=SIG-001497 reason=duplicate_id:SIG-001497 conf=0.88`
- `candidate CAND-39C060ED3946 entity_id=SIG-001496 reason=duplicate_id:SIG-001496 conf=0.92`
- `candidate CAND-8C4185F1695C entity_id=SIG-001499 reason=duplicate_id:SIG-001499 conf=0.92`
- `candidate CAND-F9E7F770896E entity_id=SIG-001495 reason=duplicate_id:SIG-001495 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-94FDCF359D24 | business_signal_library | 0.9 | False | duplicate_id:SIG-001498 | Rejected |
| CAND-3EC561ADB9A4 | business_signal_library | 0.88 | False | duplicate_id:SIG-001497 | Rejected |
| CAND-39C060ED3946 | business_signal_library | 0.92 | False | duplicate_id:SIG-001496 | Rejected |
| CAND-8C4185F1695C | business_signal_library | 0.92 | False | duplicate_id:SIG-001499 | Rejected |
| CAND-F9E7F770896E | business_signal_library | 0.9 | False | duplicate_id:SIG-001495 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001498` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
