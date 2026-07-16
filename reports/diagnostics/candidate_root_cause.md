# Candidate Root Cause

**Generated:** 2026-07-16T08:42:27+00:00
**Session:** `SESSION-20260716-27E30C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000303`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260716-27E30C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000303': 1, 'duplicate_id:SIG-000301': 1, 'duplicate_id:SIG-000300': 1, 'duplicate_id:SIG-000302': 1, 'duplicate_id:SIG-000304': 1}`
- `candidate CAND-E9B09F9060BC entity_id=SIG-000303 reason=duplicate_id:SIG-000303 conf=0.9`
- `candidate CAND-F748B18D842F entity_id=SIG-000301 reason=duplicate_id:SIG-000301 conf=0.92`
- `candidate CAND-2E136E0F0FD2 entity_id=SIG-000300 reason=duplicate_id:SIG-000300 conf=0.9`
- `candidate CAND-9AF15FF14EFE entity_id=SIG-000302 reason=duplicate_id:SIG-000302 conf=0.88`
- `candidate CAND-AC055699CA16 entity_id=SIG-000304 reason=duplicate_id:SIG-000304 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-E9B09F9060BC | business_signal_library | 0.9 | False | duplicate_id:SIG-000303 | Rejected |
| CAND-F748B18D842F | business_signal_library | 0.92 | False | duplicate_id:SIG-000301 | Rejected |
| CAND-2E136E0F0FD2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000300 | Rejected |
| CAND-9AF15FF14EFE | business_signal_library | 0.88 | False | duplicate_id:SIG-000302 | Rejected |
| CAND-AC055699CA16 | business_signal_library | 0.92 | False | duplicate_id:SIG-000304 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000303` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
