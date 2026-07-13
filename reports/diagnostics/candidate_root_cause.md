# Candidate Root Cause

**Generated:** 2026-07-13T23:12:18+00:00
**Session:** `SESSION-20260713-740D9E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000178`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260713-740D9E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000178': 1, 'duplicate_id:SIG-000176': 1, 'duplicate_id:SIG-000177': 1, 'duplicate_id:SIG-000179': 1, 'duplicate_id:SIG-000175': 1}`
- `candidate CAND-E35532E96B4A entity_id=SIG-000178 reason=duplicate_id:SIG-000178 conf=0.9`
- `candidate CAND-1A5F7C71EE15 entity_id=SIG-000176 reason=duplicate_id:SIG-000176 conf=0.92`
- `candidate CAND-D76C55B2F176 entity_id=SIG-000177 reason=duplicate_id:SIG-000177 conf=0.88`
- `candidate CAND-ACDD97DE1D0B entity_id=SIG-000179 reason=duplicate_id:SIG-000179 conf=0.92`
- `candidate CAND-E4C04538CE5F entity_id=SIG-000175 reason=duplicate_id:SIG-000175 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-E35532E96B4A | business_signal_library | 0.9 | False | duplicate_id:SIG-000178 | Rejected |
| CAND-1A5F7C71EE15 | business_signal_library | 0.92 | False | duplicate_id:SIG-000176 | Rejected |
| CAND-D76C55B2F176 | business_signal_library | 0.88 | False | duplicate_id:SIG-000177 | Rejected |
| CAND-ACDD97DE1D0B | business_signal_library | 0.92 | False | duplicate_id:SIG-000179 | Rejected |
| CAND-E4C04538CE5F | business_signal_library | 0.9 | False | duplicate_id:SIG-000175 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000178` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
