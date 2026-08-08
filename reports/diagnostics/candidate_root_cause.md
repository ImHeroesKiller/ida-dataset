# Candidate Root Cause

**Generated:** 2026-08-08T14:53:12+00:00
**Session:** `SESSION-20260808-959AC9`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001629`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260808-959AC9`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001629': 1, 'duplicate_id:SIG-001626': 1, 'duplicate_id:SIG-001625': 1, 'duplicate_id:SIG-001627': 1, 'duplicate_id:SIG-001628': 1}`
- `candidate CAND-2A00127F1F55 entity_id=SIG-001629 reason=duplicate_id:SIG-001629 conf=0.92`
- `candidate CAND-D199D30DA990 entity_id=SIG-001626 reason=duplicate_id:SIG-001626 conf=0.92`
- `candidate CAND-FCA666AD5929 entity_id=SIG-001625 reason=duplicate_id:SIG-001625 conf=0.9`
- `candidate CAND-59D8B7323326 entity_id=SIG-001627 reason=duplicate_id:SIG-001627 conf=0.88`
- `candidate CAND-07EAB70F5841 entity_id=SIG-001628 reason=duplicate_id:SIG-001628 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-2A00127F1F55 | business_signal_library | 0.92 | False | duplicate_id:SIG-001629 | Rejected |
| CAND-D199D30DA990 | business_signal_library | 0.92 | False | duplicate_id:SIG-001626 | Rejected |
| CAND-FCA666AD5929 | business_signal_library | 0.9 | False | duplicate_id:SIG-001625 | Rejected |
| CAND-59D8B7323326 | business_signal_library | 0.88 | False | duplicate_id:SIG-001627 | Rejected |
| CAND-07EAB70F5841 | business_signal_library | 0.9 | False | duplicate_id:SIG-001628 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001629` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
