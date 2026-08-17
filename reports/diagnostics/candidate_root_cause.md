# Candidate Root Cause

**Generated:** 2026-08-17T15:40:01+00:00
**Session:** `SESSION-20260817-096534`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000459`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260817-096534`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000459': 1, 'duplicate_id:SIG-000456': 1, 'duplicate_id:SIG-000458': 1, 'duplicate_id:SIG-000460': 1, 'duplicate_id:SIG-000457': 1}`
- `candidate CAND-79142EE705B4 entity_id=SIG-000459 reason=duplicate_id:SIG-000459 conf=0.9`
- `candidate CAND-0D2E480D37F8 entity_id=SIG-000456 reason=duplicate_id:SIG-000456 conf=0.92`
- `candidate CAND-B544FF3D42D5 entity_id=SIG-000458 reason=duplicate_id:SIG-000458 conf=0.9`
- `candidate CAND-2DA66D904EFC entity_id=SIG-000460 reason=duplicate_id:SIG-000460 conf=0.9`
- `candidate CAND-4ACD578CCF23 entity_id=SIG-000457 reason=duplicate_id:SIG-000457 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-79142EE705B4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000459 | Rejected |
| CAND-0D2E480D37F8 | business_signal_library | 0.92 | False | duplicate_id:SIG-000456 | Rejected |
| CAND-B544FF3D42D5 | business_signal_library | 0.9 | False | duplicate_id:SIG-000458 | Rejected |
| CAND-2DA66D904EFC | business_signal_library | 0.9 | False | duplicate_id:SIG-000460 | Rejected |
| CAND-4ACD578CCF23 | business_signal_library | 0.9 | False | duplicate_id:SIG-000457 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000459` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
