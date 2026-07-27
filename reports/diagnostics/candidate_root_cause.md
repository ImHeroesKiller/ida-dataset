# Candidate Root Cause

**Generated:** 2026-07-27T21:31:58+00:00
**Session:** `SESSION-20260727-B8E0F1`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000972`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260727-B8E0F1`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000972': 1, 'duplicate_id:SIG-000971': 1, 'duplicate_id:SIG-000974': 1, 'duplicate_id:SIG-000970': 1, 'duplicate_id:SIG-000973': 1}`
- `candidate CAND-B07DC8071676 entity_id=SIG-000972 reason=duplicate_id:SIG-000972 conf=0.88`
- `candidate CAND-127693D9E630 entity_id=SIG-000971 reason=duplicate_id:SIG-000971 conf=0.92`
- `candidate CAND-114EFC83384A entity_id=SIG-000974 reason=duplicate_id:SIG-000974 conf=0.92`
- `candidate CAND-6F938B24B48F entity_id=SIG-000970 reason=duplicate_id:SIG-000970 conf=0.9`
- `candidate CAND-6FD841E0B2F5 entity_id=SIG-000973 reason=duplicate_id:SIG-000973 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B07DC8071676 | business_signal_library | 0.88 | False | duplicate_id:SIG-000972 | Rejected |
| CAND-127693D9E630 | business_signal_library | 0.92 | False | duplicate_id:SIG-000971 | Rejected |
| CAND-114EFC83384A | business_signal_library | 0.92 | False | duplicate_id:SIG-000974 | Rejected |
| CAND-6F938B24B48F | business_signal_library | 0.9 | False | duplicate_id:SIG-000970 | Rejected |
| CAND-6FD841E0B2F5 | business_signal_library | 0.9 | False | duplicate_id:SIG-000973 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000972` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
