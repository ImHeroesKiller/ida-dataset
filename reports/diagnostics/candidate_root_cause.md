# Candidate Root Cause

**Generated:** 2026-08-23T22:41:36+00:00
**Session:** `SESSION-20260823-D2583B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001172`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260823-D2583B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001172': 1, 'duplicate_id:SIG-001173': 1, 'duplicate_id:SIG-001171': 1, 'duplicate_id:SIG-001175': 1, 'duplicate_id:SIG-001174': 1}`
- `candidate CAND-5E9F5B418588 entity_id=SIG-001172 reason=duplicate_id:SIG-001172 conf=0.9`
- `candidate CAND-742ECEB0FBF0 entity_id=SIG-001173 reason=duplicate_id:SIG-001173 conf=0.9`
- `candidate CAND-424E0F360437 entity_id=SIG-001171 reason=duplicate_id:SIG-001171 conf=0.92`
- `candidate CAND-DE376C883F3A entity_id=SIG-001175 reason=duplicate_id:SIG-001175 conf=0.9`
- `candidate CAND-B29E49E0B9E8 entity_id=SIG-001174 reason=duplicate_id:SIG-001174 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5E9F5B418588 | business_signal_library | 0.9 | False | duplicate_id:SIG-001172 | Rejected |
| CAND-742ECEB0FBF0 | business_signal_library | 0.9 | False | duplicate_id:SIG-001173 | Rejected |
| CAND-424E0F360437 | business_signal_library | 0.92 | False | duplicate_id:SIG-001171 | Rejected |
| CAND-DE376C883F3A | business_signal_library | 0.9 | False | duplicate_id:SIG-001175 | Rejected |
| CAND-B29E49E0B9E8 | business_signal_library | 0.9 | False | duplicate_id:SIG-001174 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001172` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
