# Candidate Root Cause

**Generated:** 2026-07-24T18:39:02+00:00
**Session:** `SESSION-20260724-D3DE73`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000798`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260724-D3DE73`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000798': 1, 'duplicate_id:SIG-000797': 1, 'duplicate_id:SIG-000796': 1, 'duplicate_id:SIG-000795': 1, 'duplicate_id:SIG-000799': 1}`
- `candidate CAND-743AC5E28C95 entity_id=SIG-000798 reason=duplicate_id:SIG-000798 conf=0.9`
- `candidate CAND-8CA894DBF913 entity_id=SIG-000797 reason=duplicate_id:SIG-000797 conf=0.88`
- `candidate CAND-7AA1284B7B78 entity_id=SIG-000796 reason=duplicate_id:SIG-000796 conf=0.92`
- `candidate CAND-B019A266FAB9 entity_id=SIG-000795 reason=duplicate_id:SIG-000795 conf=0.9`
- `candidate CAND-1EFCA0BEB841 entity_id=SIG-000799 reason=duplicate_id:SIG-000799 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-743AC5E28C95 | business_signal_library | 0.9 | False | duplicate_id:SIG-000798 | Rejected |
| CAND-8CA894DBF913 | business_signal_library | 0.88 | False | duplicate_id:SIG-000797 | Rejected |
| CAND-7AA1284B7B78 | business_signal_library | 0.92 | False | duplicate_id:SIG-000796 | Rejected |
| CAND-B019A266FAB9 | business_signal_library | 0.9 | False | duplicate_id:SIG-000795 | Rejected |
| CAND-1EFCA0BEB841 | business_signal_library | 0.92 | False | duplicate_id:SIG-000799 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000798` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
