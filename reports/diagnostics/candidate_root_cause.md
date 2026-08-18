# Candidate Root Cause

**Generated:** 2026-08-18T17:42:44+00:00
**Session:** `SESSION-20260818-222146`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000585`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260818-222146`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000585': 1, 'duplicate_id:SIG-000582': 1, 'duplicate_id:SIG-000583': 1, 'duplicate_id:SIG-000584': 1, 'duplicate_id:SIG-000581': 1}`
- `candidate CAND-12546D9A7B6A entity_id=SIG-000585 reason=duplicate_id:SIG-000585 conf=0.9`
- `candidate CAND-416AE5782CFB entity_id=SIG-000582 reason=duplicate_id:SIG-000582 conf=0.9`
- `candidate CAND-47AC16E6F5B7 entity_id=SIG-000583 reason=duplicate_id:SIG-000583 conf=0.9`
- `candidate CAND-21C33A19BBE1 entity_id=SIG-000584 reason=duplicate_id:SIG-000584 conf=0.9`
- `candidate CAND-96C198C008BF entity_id=SIG-000581 reason=duplicate_id:SIG-000581 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-12546D9A7B6A | business_signal_library | 0.9 | False | duplicate_id:SIG-000585 | Rejected |
| CAND-416AE5782CFB | business_signal_library | 0.9 | False | duplicate_id:SIG-000582 | Rejected |
| CAND-47AC16E6F5B7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000583 | Rejected |
| CAND-21C33A19BBE1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000584 | Rejected |
| CAND-96C198C008BF | business_signal_library | 0.92 | False | duplicate_id:SIG-000581 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000585` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
