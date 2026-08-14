# Candidate Root Cause

**Generated:** 2026-08-14T10:18:12+00:00
**Session:** `SESSION-20260814-368598`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000101`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260814-368598`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000101': 1, 'duplicate_id:SIG-000104': 1, 'duplicate_id:SIG-000105': 1, 'duplicate_id:SIG-000102': 1, 'duplicate_id:SIG-000103': 1}`
- `candidate CAND-56740FEAFC9A entity_id=SIG-000101 reason=duplicate_id:SIG-000101 conf=0.92`
- `candidate CAND-0CF8E9319D61 entity_id=SIG-000104 reason=duplicate_id:SIG-000104 conf=0.9`
- `candidate CAND-FD5688C6B739 entity_id=SIG-000105 reason=duplicate_id:SIG-000105 conf=0.9`
- `candidate CAND-59868836AFEF entity_id=SIG-000102 reason=duplicate_id:SIG-000102 conf=0.9`
- `candidate CAND-631EDCFABEDE entity_id=SIG-000103 reason=duplicate_id:SIG-000103 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-56740FEAFC9A | business_signal_library | 0.92 | False | duplicate_id:SIG-000101 | Rejected |
| CAND-0CF8E9319D61 | business_signal_library | 0.9 | False | duplicate_id:SIG-000104 | Rejected |
| CAND-FD5688C6B739 | business_signal_library | 0.9 | False | duplicate_id:SIG-000105 | Rejected |
| CAND-59868836AFEF | business_signal_library | 0.9 | False | duplicate_id:SIG-000102 | Rejected |
| CAND-631EDCFABEDE | business_signal_library | 0.9 | False | duplicate_id:SIG-000103 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000101` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
