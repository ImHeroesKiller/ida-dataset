# Candidate Root Cause

**Generated:** 2026-07-25T20:29:56+00:00
**Session:** `SESSION-20260725-A3694B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000862`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260725-A3694B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000862': 1, 'duplicate_id:SIG-000863': 1, 'duplicate_id:SIG-000864': 1, 'duplicate_id:SIG-000860': 1, 'duplicate_id:SIG-000861': 1}`
- `candidate CAND-B87E9AF53D9C entity_id=SIG-000862 reason=duplicate_id:SIG-000862 conf=0.88`
- `candidate CAND-650F46C17F4D entity_id=SIG-000863 reason=duplicate_id:SIG-000863 conf=0.9`
- `candidate CAND-7F41E075AEE4 entity_id=SIG-000864 reason=duplicate_id:SIG-000864 conf=0.92`
- `candidate CAND-A6A9981B71C4 entity_id=SIG-000860 reason=duplicate_id:SIG-000860 conf=0.9`
- `candidate CAND-852B3D49C0D2 entity_id=SIG-000861 reason=duplicate_id:SIG-000861 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B87E9AF53D9C | business_signal_library | 0.88 | False | duplicate_id:SIG-000862 | Rejected |
| CAND-650F46C17F4D | business_signal_library | 0.9 | False | duplicate_id:SIG-000863 | Rejected |
| CAND-7F41E075AEE4 | business_signal_library | 0.92 | False | duplicate_id:SIG-000864 | Rejected |
| CAND-A6A9981B71C4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000860 | Rejected |
| CAND-852B3D49C0D2 | business_signal_library | 0.92 | False | duplicate_id:SIG-000861 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000862` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
