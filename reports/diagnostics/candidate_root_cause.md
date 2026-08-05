# Candidate Root Cause

**Generated:** 2026-08-05T23:20:54+00:00
**Session:** `SESSION-20260805-BCEE07`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001445`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260805-BCEE07`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001445': 1, 'duplicate_id:SIG-001449': 1, 'duplicate_id:SIG-001447': 1, 'duplicate_id:SIG-001446': 1, 'duplicate_id:SIG-001448': 1}`
- `candidate CAND-B7CD86FC3645 entity_id=SIG-001445 reason=duplicate_id:SIG-001445 conf=0.9`
- `candidate CAND-0E8199BA9B71 entity_id=SIG-001449 reason=duplicate_id:SIG-001449 conf=0.92`
- `candidate CAND-A0F80B0CC38D entity_id=SIG-001447 reason=duplicate_id:SIG-001447 conf=0.88`
- `candidate CAND-1E8CD24846D1 entity_id=SIG-001446 reason=duplicate_id:SIG-001446 conf=0.92`
- `candidate CAND-2A0188CEB366 entity_id=SIG-001448 reason=duplicate_id:SIG-001448 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B7CD86FC3645 | business_signal_library | 0.9 | False | duplicate_id:SIG-001445 | Rejected |
| CAND-0E8199BA9B71 | business_signal_library | 0.92 | False | duplicate_id:SIG-001449 | Rejected |
| CAND-A0F80B0CC38D | business_signal_library | 0.88 | False | duplicate_id:SIG-001447 | Rejected |
| CAND-1E8CD24846D1 | business_signal_library | 0.92 | False | duplicate_id:SIG-001446 | Rejected |
| CAND-2A0188CEB366 | business_signal_library | 0.9 | False | duplicate_id:SIG-001448 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001445` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
