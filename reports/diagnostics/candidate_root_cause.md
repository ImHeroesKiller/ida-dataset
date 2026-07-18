# Candidate Root Cause

**Generated:** 2026-07-18T19:29:50+00:00
**Session:** `SESSION-20260718-03DAB7`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000458`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260718-03DAB7`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000458': 1, 'duplicate_id:SIG-000456': 1, 'duplicate_id:SIG-000455': 1, 'duplicate_id:SIG-000457': 1, 'duplicate_id:SIG-000459': 1}`
- `candidate CAND-750977DE12FE entity_id=SIG-000458 reason=duplicate_id:SIG-000458 conf=0.9`
- `candidate CAND-6F2B5573C965 entity_id=SIG-000456 reason=duplicate_id:SIG-000456 conf=0.92`
- `candidate CAND-E7FF938334D5 entity_id=SIG-000455 reason=duplicate_id:SIG-000455 conf=0.9`
- `candidate CAND-EECDF97B2E0F entity_id=SIG-000457 reason=duplicate_id:SIG-000457 conf=0.88`
- `candidate CAND-0222049A00F3 entity_id=SIG-000459 reason=duplicate_id:SIG-000459 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-750977DE12FE | business_signal_library | 0.9 | False | duplicate_id:SIG-000458 | Rejected |
| CAND-6F2B5573C965 | business_signal_library | 0.92 | False | duplicate_id:SIG-000456 | Rejected |
| CAND-E7FF938334D5 | business_signal_library | 0.9 | False | duplicate_id:SIG-000455 | Rejected |
| CAND-EECDF97B2E0F | business_signal_library | 0.88 | False | duplicate_id:SIG-000457 | Rejected |
| CAND-0222049A00F3 | business_signal_library | 0.92 | False | duplicate_id:SIG-000459 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000458` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
