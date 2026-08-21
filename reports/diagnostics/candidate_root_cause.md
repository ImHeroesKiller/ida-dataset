# Candidate Root Cause

**Generated:** 2026-08-21T18:56:42+00:00
**Session:** `SESSION-20260821-30136C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000929`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260821-30136C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000929': 1, 'duplicate_id:SIG-000926': 1, 'duplicate_id:SIG-000930': 1, 'duplicate_id:SIG-000928': 1, 'duplicate_id:SIG-000927': 1}`
- `candidate CAND-6C8D1808687F entity_id=SIG-000929 reason=duplicate_id:SIG-000929 conf=0.9`
- `candidate CAND-5C7E35E75395 entity_id=SIG-000926 reason=duplicate_id:SIG-000926 conf=0.92`
- `candidate CAND-E641392389BD entity_id=SIG-000930 reason=duplicate_id:SIG-000930 conf=0.9`
- `candidate CAND-B4F3AD6C5DB7 entity_id=SIG-000928 reason=duplicate_id:SIG-000928 conf=0.9`
- `candidate CAND-F76AEEDEAB9D entity_id=SIG-000927 reason=duplicate_id:SIG-000927 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-6C8D1808687F | business_signal_library | 0.9 | False | duplicate_id:SIG-000929 | Rejected |
| CAND-5C7E35E75395 | business_signal_library | 0.92 | False | duplicate_id:SIG-000926 | Rejected |
| CAND-E641392389BD | business_signal_library | 0.9 | False | duplicate_id:SIG-000930 | Rejected |
| CAND-B4F3AD6C5DB7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000928 | Rejected |
| CAND-F76AEEDEAB9D | business_signal_library | 0.9 | False | duplicate_id:SIG-000927 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000929` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
