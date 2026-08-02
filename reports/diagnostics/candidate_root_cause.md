# Candidate Root Cause

**Generated:** 2026-08-02T03:14:34+00:00
**Session:** `SESSION-20260802-4816AC`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001243`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260802-4816AC`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001243': 1, 'duplicate_id:SIG-001244': 1, 'duplicate_id:SIG-001240': 1, 'duplicate_id:SIG-001241': 1, 'duplicate_id:SIG-001242': 1}`
- `candidate CAND-5AB4EF81E30A entity_id=SIG-001243 reason=duplicate_id:SIG-001243 conf=0.9`
- `candidate CAND-F48E277E249E entity_id=SIG-001244 reason=duplicate_id:SIG-001244 conf=0.92`
- `candidate CAND-31FB27ABBC2F entity_id=SIG-001240 reason=duplicate_id:SIG-001240 conf=0.9`
- `candidate CAND-26C569200887 entity_id=SIG-001241 reason=duplicate_id:SIG-001241 conf=0.92`
- `candidate CAND-9A6361C97A1E entity_id=SIG-001242 reason=duplicate_id:SIG-001242 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5AB4EF81E30A | business_signal_library | 0.9 | False | duplicate_id:SIG-001243 | Rejected |
| CAND-F48E277E249E | business_signal_library | 0.92 | False | duplicate_id:SIG-001244 | Rejected |
| CAND-31FB27ABBC2F | business_signal_library | 0.9 | False | duplicate_id:SIG-001240 | Rejected |
| CAND-26C569200887 | business_signal_library | 0.92 | False | duplicate_id:SIG-001241 | Rejected |
| CAND-9A6361C97A1E | business_signal_library | 0.88 | False | duplicate_id:SIG-001242 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001243` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
