# Candidate Root Cause

**Generated:** 2026-08-09T15:53:18+00:00
**Session:** `SESSION-20260809-CD4716`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001738`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260809-CD4716`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001738': 1, 'duplicate_id:SIG-001736': 1, 'duplicate_id:SIG-001739': 1, 'duplicate_id:SIG-001735': 1, 'duplicate_id:SIG-001737': 1}`
- `candidate CAND-04387E7A7BF6 entity_id=SIG-001738 reason=duplicate_id:SIG-001738 conf=0.9`
- `candidate CAND-0A403C331931 entity_id=SIG-001736 reason=duplicate_id:SIG-001736 conf=0.92`
- `candidate CAND-72D139C21678 entity_id=SIG-001739 reason=duplicate_id:SIG-001739 conf=0.92`
- `candidate CAND-DDDDF4277D7A entity_id=SIG-001735 reason=duplicate_id:SIG-001735 conf=0.9`
- `candidate CAND-5E7C72967CC5 entity_id=SIG-001737 reason=duplicate_id:SIG-001737 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-04387E7A7BF6 | business_signal_library | 0.9 | False | duplicate_id:SIG-001738 | Rejected |
| CAND-0A403C331931 | business_signal_library | 0.92 | False | duplicate_id:SIG-001736 | Rejected |
| CAND-72D139C21678 | business_signal_library | 0.92 | False | duplicate_id:SIG-001739 | Rejected |
| CAND-DDDDF4277D7A | business_signal_library | 0.9 | False | duplicate_id:SIG-001735 | Rejected |
| CAND-5E7C72967CC5 | business_signal_library | 0.88 | False | duplicate_id:SIG-001737 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001738` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
