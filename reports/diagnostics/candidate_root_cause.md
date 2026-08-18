# Candidate Root Cause

**Generated:** 2026-08-18T19:41:14+00:00
**Session:** `SESSION-20260818-BDC2EC`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000594`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260818-BDC2EC`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000594': 1, 'duplicate_id:SIG-000595': 1, 'duplicate_id:SIG-000592': 1, 'duplicate_id:SIG-000593': 1, 'duplicate_id:SIG-000591': 1}`
- `candidate CAND-F9B1AD3226C3 entity_id=SIG-000594 reason=duplicate_id:SIG-000594 conf=0.9`
- `candidate CAND-7BF9D6F72001 entity_id=SIG-000595 reason=duplicate_id:SIG-000595 conf=0.9`
- `candidate CAND-D0537D966602 entity_id=SIG-000592 reason=duplicate_id:SIG-000592 conf=0.9`
- `candidate CAND-C3635A631901 entity_id=SIG-000593 reason=duplicate_id:SIG-000593 conf=0.9`
- `candidate CAND-A1D302007F3E entity_id=SIG-000591 reason=duplicate_id:SIG-000591 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F9B1AD3226C3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000594 | Rejected |
| CAND-7BF9D6F72001 | business_signal_library | 0.9 | False | duplicate_id:SIG-000595 | Rejected |
| CAND-D0537D966602 | business_signal_library | 0.9 | False | duplicate_id:SIG-000592 | Rejected |
| CAND-C3635A631901 | business_signal_library | 0.9 | False | duplicate_id:SIG-000593 | Rejected |
| CAND-A1D302007F3E | business_signal_library | 0.92 | False | duplicate_id:SIG-000591 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000594` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
