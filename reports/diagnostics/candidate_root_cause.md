# Candidate Root Cause

**Generated:** 2026-08-15T03:53:58+00:00
**Session:** `SESSION-20260815-7C143D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000176`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260815-7C143D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000176': 1, 'duplicate_id:SIG-000178': 1, 'duplicate_id:SIG-000177': 1, 'duplicate_id:SIG-000179': 1, 'duplicate_id:SIG-000180': 1}`
- `candidate CAND-A47B664B7491 entity_id=SIG-000176 reason=duplicate_id:SIG-000176 conf=0.92`
- `candidate CAND-FFBEEFD78010 entity_id=SIG-000178 reason=duplicate_id:SIG-000178 conf=0.9`
- `candidate CAND-3CBD5FA93BBB entity_id=SIG-000177 reason=duplicate_id:SIG-000177 conf=0.9`
- `candidate CAND-18691D87CF6A entity_id=SIG-000179 reason=duplicate_id:SIG-000179 conf=0.9`
- `candidate CAND-EF035B5EAEE7 entity_id=SIG-000180 reason=duplicate_id:SIG-000180 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A47B664B7491 | business_signal_library | 0.92 | False | duplicate_id:SIG-000176 | Rejected |
| CAND-FFBEEFD78010 | business_signal_library | 0.9 | False | duplicate_id:SIG-000178 | Rejected |
| CAND-3CBD5FA93BBB | business_signal_library | 0.9 | False | duplicate_id:SIG-000177 | Rejected |
| CAND-18691D87CF6A | business_signal_library | 0.9 | False | duplicate_id:SIG-000179 | Rejected |
| CAND-EF035B5EAEE7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000180 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000176` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
