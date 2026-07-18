# Candidate Root Cause

**Generated:** 2026-07-18T16:21:39+00:00
**Session:** `SESSION-20260718-5AE40A`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000445`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260718-5AE40A`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000445': 1, 'duplicate_id:SIG-000446': 1, 'duplicate_id:SIG-000449': 1, 'duplicate_id:SIG-000448': 1, 'duplicate_id:SIG-000447': 1}`
- `candidate CAND-D131CB4FFAB0 entity_id=SIG-000445 reason=duplicate_id:SIG-000445 conf=0.9`
- `candidate CAND-F7A5D2B8A3B1 entity_id=SIG-000446 reason=duplicate_id:SIG-000446 conf=0.92`
- `candidate CAND-0C71BF1FC76C entity_id=SIG-000449 reason=duplicate_id:SIG-000449 conf=0.92`
- `candidate CAND-3D8866CD9B0D entity_id=SIG-000448 reason=duplicate_id:SIG-000448 conf=0.9`
- `candidate CAND-48CA4C5065BC entity_id=SIG-000447 reason=duplicate_id:SIG-000447 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-D131CB4FFAB0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000445 | Rejected |
| CAND-F7A5D2B8A3B1 | business_signal_library | 0.92 | False | duplicate_id:SIG-000446 | Rejected |
| CAND-0C71BF1FC76C | business_signal_library | 0.92 | False | duplicate_id:SIG-000449 | Rejected |
| CAND-3D8866CD9B0D | business_signal_library | 0.9 | False | duplicate_id:SIG-000448 | Rejected |
| CAND-48CA4C5065BC | business_signal_library | 0.88 | False | duplicate_id:SIG-000447 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000445` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
