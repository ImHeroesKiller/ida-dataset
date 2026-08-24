# Candidate Root Cause

**Generated:** 2026-08-24T23:38:50+00:00
**Session:** `SESSION-20260824-ADDBE0`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001236`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260824-ADDBE0`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001236': 1, 'duplicate_id:SIG-001237': 1, 'duplicate_id:SIG-001238': 1, 'duplicate_id:SIG-001240': 1, 'duplicate_id:SIG-001239': 1}`
- `candidate CAND-ABA5E7A2FDE1 entity_id=SIG-001236 reason=duplicate_id:SIG-001236 conf=0.92`
- `candidate CAND-023711BADF3F entity_id=SIG-001237 reason=duplicate_id:SIG-001237 conf=0.9`
- `candidate CAND-BD15901DB6A8 entity_id=SIG-001238 reason=duplicate_id:SIG-001238 conf=0.9`
- `candidate CAND-06159F675A79 entity_id=SIG-001240 reason=duplicate_id:SIG-001240 conf=0.9`
- `candidate CAND-9F1A3E1A6EF5 entity_id=SIG-001239 reason=duplicate_id:SIG-001239 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-ABA5E7A2FDE1 | business_signal_library | 0.92 | False | duplicate_id:SIG-001236 | Rejected |
| CAND-023711BADF3F | business_signal_library | 0.9 | False | duplicate_id:SIG-001237 | Rejected |
| CAND-BD15901DB6A8 | business_signal_library | 0.9 | False | duplicate_id:SIG-001238 | Rejected |
| CAND-06159F675A79 | business_signal_library | 0.9 | False | duplicate_id:SIG-001240 | Rejected |
| CAND-9F1A3E1A6EF5 | business_signal_library | 0.9 | False | duplicate_id:SIG-001239 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001236` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
