# Candidate Root Cause

**Generated:** 2026-08-17T13:00:17+00:00
**Session:** `SESSION-20260817-DBDFC4`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000445`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260817-DBDFC4`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000445': 1, 'duplicate_id:SIG-000442': 1, 'duplicate_id:SIG-000444': 1, 'duplicate_id:SIG-000443': 1, 'duplicate_id:SIG-000441': 1}`
- `candidate CAND-C2CCD1D8CED8 entity_id=SIG-000445 reason=duplicate_id:SIG-000445 conf=0.9`
- `candidate CAND-80E9E6522970 entity_id=SIG-000442 reason=duplicate_id:SIG-000442 conf=0.9`
- `candidate CAND-B74ED3963CC3 entity_id=SIG-000444 reason=duplicate_id:SIG-000444 conf=0.9`
- `candidate CAND-73B75880E6EF entity_id=SIG-000443 reason=duplicate_id:SIG-000443 conf=0.9`
- `candidate CAND-A5325537DF31 entity_id=SIG-000441 reason=duplicate_id:SIG-000441 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-C2CCD1D8CED8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000445 | Rejected |
| CAND-80E9E6522970 | business_signal_library | 0.9 | False | duplicate_id:SIG-000442 | Rejected |
| CAND-B74ED3963CC3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000444 | Rejected |
| CAND-73B75880E6EF | business_signal_library | 0.9 | False | duplicate_id:SIG-000443 | Rejected |
| CAND-A5325537DF31 | business_signal_library | 0.92 | False | duplicate_id:SIG-000441 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000445` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
