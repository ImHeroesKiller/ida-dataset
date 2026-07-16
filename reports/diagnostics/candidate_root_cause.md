# Candidate Root Cause

**Generated:** 2026-07-16T21:21:49+00:00
**Session:** `SESSION-20260716-9FAEE6`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000337`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260716-9FAEE6`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000337': 1, 'duplicate_id:SIG-000338': 1, 'duplicate_id:SIG-000336': 1, 'duplicate_id:SIG-000339': 1, 'duplicate_id:SIG-000335': 1}`
- `candidate CAND-5B42ED80C2B9 entity_id=SIG-000337 reason=duplicate_id:SIG-000337 conf=0.92`
- `candidate CAND-3389AE83736E entity_id=SIG-000338 reason=duplicate_id:SIG-000338 conf=0.9`
- `candidate CAND-21E82E06132D entity_id=SIG-000336 reason=duplicate_id:SIG-000336 conf=0.88`
- `candidate CAND-D049F7C164F8 entity_id=SIG-000339 reason=duplicate_id:SIG-000339 conf=0.88`
- `candidate CAND-C4A4602F901A entity_id=SIG-000335 reason=duplicate_id:SIG-000335 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5B42ED80C2B9 | business_signal_library | 0.92 | False | duplicate_id:SIG-000337 | Rejected |
| CAND-3389AE83736E | business_signal_library | 0.9 | False | duplicate_id:SIG-000338 | Rejected |
| CAND-21E82E06132D | business_signal_library | 0.88 | False | duplicate_id:SIG-000336 | Rejected |
| CAND-D049F7C164F8 | business_signal_library | 0.88 | False | duplicate_id:SIG-000339 | Rejected |
| CAND-C4A4602F901A | business_signal_library | 0.9 | False | duplicate_id:SIG-000335 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000337` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
