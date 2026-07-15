# Candidate Root Cause

**Generated:** 2026-07-15T16:46:49+00:00
**Session:** `SESSION-20260715-A0146E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000269`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260715-A0146E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000269': 1, 'duplicate_id:SIG-000265': 1, 'duplicate_id:SIG-000266': 1, 'duplicate_id:SIG-000268': 1, 'duplicate_id:SIG-000267': 1}`
- `candidate CAND-5DD7F6DF2E0D entity_id=SIG-000269 reason=duplicate_id:SIG-000269 conf=0.9`
- `candidate CAND-21FE4F267D77 entity_id=SIG-000265 reason=duplicate_id:SIG-000265 conf=0.9`
- `candidate CAND-48E88C855434 entity_id=SIG-000266 reason=duplicate_id:SIG-000266 conf=0.88`
- `candidate CAND-3701ED8B8DE9 entity_id=SIG-000268 reason=duplicate_id:SIG-000268 conf=0.85`
- `candidate CAND-889942AB4A28 entity_id=SIG-000267 reason=duplicate_id:SIG-000267 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5DD7F6DF2E0D | business_signal_library | 0.9 | False | duplicate_id:SIG-000269 | Rejected |
| CAND-21FE4F267D77 | business_signal_library | 0.9 | False | duplicate_id:SIG-000265 | Rejected |
| CAND-48E88C855434 | business_signal_library | 0.88 | False | duplicate_id:SIG-000266 | Rejected |
| CAND-3701ED8B8DE9 | business_signal_library | 0.85 | False | duplicate_id:SIG-000268 | Rejected |
| CAND-889942AB4A28 | business_signal_library | 0.92 | False | duplicate_id:SIG-000267 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000269` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
