# Candidate Root Cause

**Generated:** 2026-08-15T22:37:11+00:00
**Session:** `SESSION-20260815-491A46`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000273`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260815-491A46`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000273': 1, 'duplicate_id:SIG-000275': 1, 'duplicate_id:SIG-000274': 1, 'duplicate_id:SIG-000272': 1, 'duplicate_id:SIG-000271': 1}`
- `candidate CAND-ADDF3A201E9A entity_id=SIG-000273 reason=duplicate_id:SIG-000273 conf=0.9`
- `candidate CAND-5E6B178E0746 entity_id=SIG-000275 reason=duplicate_id:SIG-000275 conf=0.9`
- `candidate CAND-A6A690E6F945 entity_id=SIG-000274 reason=duplicate_id:SIG-000274 conf=0.9`
- `candidate CAND-46D19E4036A0 entity_id=SIG-000272 reason=duplicate_id:SIG-000272 conf=0.9`
- `candidate CAND-9F09AACA4A77 entity_id=SIG-000271 reason=duplicate_id:SIG-000271 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-ADDF3A201E9A | business_signal_library | 0.9 | False | duplicate_id:SIG-000273 | Rejected |
| CAND-5E6B178E0746 | business_signal_library | 0.9 | False | duplicate_id:SIG-000275 | Rejected |
| CAND-A6A690E6F945 | business_signal_library | 0.9 | False | duplicate_id:SIG-000274 | Rejected |
| CAND-46D19E4036A0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000272 | Rejected |
| CAND-9F09AACA4A77 | business_signal_library | 0.92 | False | duplicate_id:SIG-000271 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000273` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
