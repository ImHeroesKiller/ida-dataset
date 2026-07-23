# Candidate Root Cause

**Generated:** 2026-07-23T08:57:31+00:00
**Session:** `SESSION-20260723-959E63`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000722`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260723-959E63`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000722': 1, 'duplicate_id:SIG-000721': 1, 'duplicate_id:SIG-000723': 1, 'duplicate_id:SIG-000724': 1, 'duplicate_id:SIG-000720': 1}`
- `candidate CAND-7D749DE19BB1 entity_id=SIG-000722 reason=duplicate_id:SIG-000722 conf=0.88`
- `candidate CAND-737C86E600D3 entity_id=SIG-000721 reason=duplicate_id:SIG-000721 conf=0.92`
- `candidate CAND-3443E138792E entity_id=SIG-000723 reason=duplicate_id:SIG-000723 conf=0.9`
- `candidate CAND-D2315C3B5261 entity_id=SIG-000724 reason=duplicate_id:SIG-000724 conf=0.92`
- `candidate CAND-1A640C5A2689 entity_id=SIG-000720 reason=duplicate_id:SIG-000720 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-7D749DE19BB1 | business_signal_library | 0.88 | False | duplicate_id:SIG-000722 | Rejected |
| CAND-737C86E600D3 | business_signal_library | 0.92 | False | duplicate_id:SIG-000721 | Rejected |
| CAND-3443E138792E | business_signal_library | 0.9 | False | duplicate_id:SIG-000723 | Rejected |
| CAND-D2315C3B5261 | business_signal_library | 0.92 | False | duplicate_id:SIG-000724 | Rejected |
| CAND-1A640C5A2689 | business_signal_library | 0.9 | False | duplicate_id:SIG-000720 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000722` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
