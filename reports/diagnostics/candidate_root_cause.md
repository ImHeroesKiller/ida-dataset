# Candidate Root Cause

**Generated:** 2026-07-27T19:54:04+00:00
**Session:** `SESSION-20260727-F49C3A`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000967`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260727-F49C3A`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000967': 1, 'duplicate_id:SIG-000969': 1, 'duplicate_id:SIG-000966': 1, 'duplicate_id:SIG-000968': 1, 'duplicate_id:SIG-000965': 1}`
- `candidate CAND-98988169BD43 entity_id=SIG-000967 reason=duplicate_id:SIG-000967 conf=0.88`
- `candidate CAND-E5D63815DCE6 entity_id=SIG-000969 reason=duplicate_id:SIG-000969 conf=0.92`
- `candidate CAND-A065A8C088D0 entity_id=SIG-000966 reason=duplicate_id:SIG-000966 conf=0.92`
- `candidate CAND-B7824DC96009 entity_id=SIG-000968 reason=duplicate_id:SIG-000968 conf=0.9`
- `candidate CAND-79611E323691 entity_id=SIG-000965 reason=duplicate_id:SIG-000965 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-98988169BD43 | business_signal_library | 0.88 | False | duplicate_id:SIG-000967 | Rejected |
| CAND-E5D63815DCE6 | business_signal_library | 0.92 | False | duplicate_id:SIG-000969 | Rejected |
| CAND-A065A8C088D0 | business_signal_library | 0.92 | False | duplicate_id:SIG-000966 | Rejected |
| CAND-B7824DC96009 | business_signal_library | 0.9 | False | duplicate_id:SIG-000968 | Rejected |
| CAND-79611E323691 | business_signal_library | 0.9 | False | duplicate_id:SIG-000965 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000967` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
