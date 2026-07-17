# Candidate Root Cause

**Generated:** 2026-07-17T08:38:51+00:00
**Session:** `SESSION-20260717-46DE90`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000361`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260717-46DE90`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000361': 1, 'duplicate_id:SIG-000364': 1, 'duplicate_id:SIG-000363': 1, 'duplicate_id:SIG-000362': 1, 'duplicate_id:SIG-000360': 1}`
- `candidate CAND-5C9B70E345DA entity_id=SIG-000361 reason=duplicate_id:SIG-000361 conf=0.88`
- `candidate CAND-D8BAD0CC99B5 entity_id=SIG-000364 reason=duplicate_id:SIG-000364 conf=0.88`
- `candidate CAND-1EA809DA8FE0 entity_id=SIG-000363 reason=duplicate_id:SIG-000363 conf=0.9`
- `candidate CAND-00D0F92B666A entity_id=SIG-000362 reason=duplicate_id:SIG-000362 conf=0.92`
- `candidate CAND-A2DBBC4A41FE entity_id=SIG-000360 reason=duplicate_id:SIG-000360 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5C9B70E345DA | business_signal_library | 0.88 | False | duplicate_id:SIG-000361 | Rejected |
| CAND-D8BAD0CC99B5 | business_signal_library | 0.88 | False | duplicate_id:SIG-000364 | Rejected |
| CAND-1EA809DA8FE0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000363 | Rejected |
| CAND-00D0F92B666A | business_signal_library | 0.92 | False | duplicate_id:SIG-000362 | Rejected |
| CAND-A2DBBC4A41FE | business_signal_library | 0.9 | False | duplicate_id:SIG-000360 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000361` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
