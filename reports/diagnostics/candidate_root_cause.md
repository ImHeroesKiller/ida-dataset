# Candidate Root Cause

**Generated:** 2026-07-30T00:19:40+00:00
**Session:** `SESSION-20260730-EDC259`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001076`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260730-EDC259`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001076': 1, 'duplicate_id:SIG-001075': 1, 'duplicate_id:SIG-001079': 1, 'duplicate_id:SIG-001077': 1, 'duplicate_id:SIG-001078': 1}`
- `candidate CAND-B23D3C500E03 entity_id=SIG-001076 reason=duplicate_id:SIG-001076 conf=0.92`
- `candidate CAND-17083BF656DA entity_id=SIG-001075 reason=duplicate_id:SIG-001075 conf=0.9`
- `candidate CAND-0E31274C84D8 entity_id=SIG-001079 reason=duplicate_id:SIG-001079 conf=0.92`
- `candidate CAND-7A151647C71A entity_id=SIG-001077 reason=duplicate_id:SIG-001077 conf=0.88`
- `candidate CAND-978774C96F0C entity_id=SIG-001078 reason=duplicate_id:SIG-001078 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B23D3C500E03 | business_signal_library | 0.92 | False | duplicate_id:SIG-001076 | Rejected |
| CAND-17083BF656DA | business_signal_library | 0.9 | False | duplicate_id:SIG-001075 | Rejected |
| CAND-0E31274C84D8 | business_signal_library | 0.92 | False | duplicate_id:SIG-001079 | Rejected |
| CAND-7A151647C71A | business_signal_library | 0.88 | False | duplicate_id:SIG-001077 | Rejected |
| CAND-978774C96F0C | business_signal_library | 0.9 | False | duplicate_id:SIG-001078 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001076` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
