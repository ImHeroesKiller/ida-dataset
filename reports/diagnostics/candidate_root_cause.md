# Candidate Root Cause

**Generated:** 2026-07-11T17:10:54+00:00
**Session:** `SESSION-20260711-29CE5A`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000049`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260711-29CE5A`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000049': 1, 'duplicate_id:SIG-000048': 1, 'duplicate_id:SIG-000046': 1, 'duplicate_id:SIG-000045': 1, 'duplicate_id:SIG-000047': 1}`
- `candidate CAND-F217859B8182 entity_id=SIG-000049 reason=duplicate_id:SIG-000049 conf=0.88`
- `candidate CAND-C781226E4FF8 entity_id=SIG-000048 reason=duplicate_id:SIG-000048 conf=0.9`
- `candidate CAND-8FC4C3383B9A entity_id=SIG-000046 reason=duplicate_id:SIG-000046 conf=0.9`
- `candidate CAND-9ADA504ABA88 entity_id=SIG-000045 reason=duplicate_id:SIG-000045 conf=0.92`
- `candidate CAND-F02A999980DE entity_id=SIG-000047 reason=duplicate_id:SIG-000047 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F217859B8182 | business_signal_library | 0.88 | False | duplicate_id:SIG-000049 | Rejected |
| CAND-C781226E4FF8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000048 | Rejected |
| CAND-8FC4C3383B9A | business_signal_library | 0.9 | False | duplicate_id:SIG-000046 | Rejected |
| CAND-9ADA504ABA88 | business_signal_library | 0.92 | False | duplicate_id:SIG-000045 | Rejected |
| CAND-F02A999980DE | business_signal_library | 0.88 | False | duplicate_id:SIG-000047 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000049` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
