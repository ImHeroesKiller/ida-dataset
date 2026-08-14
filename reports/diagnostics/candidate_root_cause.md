# Candidate Root Cause

**Generated:** 2026-08-14T17:09:41+00:00
**Session:** `SESSION-20260814-5983F6`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000126`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260814-5983F6`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000126': 1, 'duplicate_id:SIG-000130': 1, 'duplicate_id:SIG-000129': 1, 'duplicate_id:SIG-000127': 1, 'duplicate_id:SIG-000128': 1}`
- `candidate CAND-73B7C9E731F2 entity_id=SIG-000126 reason=duplicate_id:SIG-000126 conf=0.92`
- `candidate CAND-26D24569D95F entity_id=SIG-000130 reason=duplicate_id:SIG-000130 conf=0.9`
- `candidate CAND-75E80EEDA34F entity_id=SIG-000129 reason=duplicate_id:SIG-000129 conf=0.9`
- `candidate CAND-6B75C0785F73 entity_id=SIG-000127 reason=duplicate_id:SIG-000127 conf=0.9`
- `candidate CAND-AA2E82685017 entity_id=SIG-000128 reason=duplicate_id:SIG-000128 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-73B7C9E731F2 | business_signal_library | 0.92 | False | duplicate_id:SIG-000126 | Rejected |
| CAND-26D24569D95F | business_signal_library | 0.9 | False | duplicate_id:SIG-000130 | Rejected |
| CAND-75E80EEDA34F | business_signal_library | 0.9 | False | duplicate_id:SIG-000129 | Rejected |
| CAND-6B75C0785F73 | business_signal_library | 0.9 | False | duplicate_id:SIG-000127 | Rejected |
| CAND-AA2E82685017 | business_signal_library | 0.9 | False | duplicate_id:SIG-000128 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000126` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
