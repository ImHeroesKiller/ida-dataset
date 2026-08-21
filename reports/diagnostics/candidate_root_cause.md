# Candidate Root Cause

**Generated:** 2026-08-21T16:55:29+00:00
**Session:** `SESSION-20260821-B3DA57`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000917`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260821-B3DA57`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000917': 1, 'duplicate_id:SIG-000919': 1, 'duplicate_id:SIG-000920': 1, 'duplicate_id:SIG-000916': 1, 'duplicate_id:SIG-000918': 1}`
- `candidate CAND-152B35DCC4A4 entity_id=SIG-000917 reason=duplicate_id:SIG-000917 conf=0.9`
- `candidate CAND-4DBD0515550F entity_id=SIG-000919 reason=duplicate_id:SIG-000919 conf=0.9`
- `candidate CAND-BFCF412B6175 entity_id=SIG-000920 reason=duplicate_id:SIG-000920 conf=0.9`
- `candidate CAND-BB23E96479A7 entity_id=SIG-000916 reason=duplicate_id:SIG-000916 conf=0.92`
- `candidate CAND-71B8F25C78D5 entity_id=SIG-000918 reason=duplicate_id:SIG-000918 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-152B35DCC4A4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000917 | Rejected |
| CAND-4DBD0515550F | business_signal_library | 0.9 | False | duplicate_id:SIG-000919 | Rejected |
| CAND-BFCF412B6175 | business_signal_library | 0.9 | False | duplicate_id:SIG-000920 | Rejected |
| CAND-BB23E96479A7 | business_signal_library | 0.92 | False | duplicate_id:SIG-000916 | Rejected |
| CAND-71B8F25C78D5 | business_signal_library | 0.9 | False | duplicate_id:SIG-000918 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000917` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
