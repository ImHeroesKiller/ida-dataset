# Candidate Root Cause

**Generated:** 2026-08-12T08:05:10+00:00
**Session:** `SESSION-20260812-33A7BC`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001959`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260812-33A7BC`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001959': 1, 'duplicate_id:SIG-001957': 1, 'duplicate_id:SIG-001955': 1, 'duplicate_id:SIG-001958': 1, 'duplicate_id:SIG-001956': 1}`
- `candidate CAND-0D77D0AC73C4 entity_id=SIG-001959 reason=duplicate_id:SIG-001959 conf=0.92`
- `candidate CAND-549FFDC596DB entity_id=SIG-001957 reason=duplicate_id:SIG-001957 conf=0.88`
- `candidate CAND-731F12EE5C12 entity_id=SIG-001955 reason=duplicate_id:SIG-001955 conf=0.9`
- `candidate CAND-FB7CCD02B2B2 entity_id=SIG-001958 reason=duplicate_id:SIG-001958 conf=0.9`
- `candidate CAND-2FBB0FBE5B4B entity_id=SIG-001956 reason=duplicate_id:SIG-001956 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-0D77D0AC73C4 | business_signal_library | 0.92 | False | duplicate_id:SIG-001959 | Rejected |
| CAND-549FFDC596DB | business_signal_library | 0.88 | False | duplicate_id:SIG-001957 | Rejected |
| CAND-731F12EE5C12 | business_signal_library | 0.9 | False | duplicate_id:SIG-001955 | Rejected |
| CAND-FB7CCD02B2B2 | business_signal_library | 0.9 | False | duplicate_id:SIG-001958 | Rejected |
| CAND-2FBB0FBE5B4B | business_signal_library | 0.92 | False | duplicate_id:SIG-001956 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001959` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
