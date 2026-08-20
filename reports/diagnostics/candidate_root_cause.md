# Candidate Root Cause

**Generated:** 2026-08-20T15:53:56+00:00
**Session:** `SESSION-20260820-C0F818`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000804`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260820-C0F818`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000804': 1, 'duplicate_id:SIG-000801': 1, 'duplicate_id:SIG-000802': 1, 'duplicate_id:SIG-000805': 1, 'duplicate_id:SIG-000803': 1}`
- `candidate CAND-686E720DCBF5 entity_id=SIG-000804 reason=duplicate_id:SIG-000804 conf=0.9`
- `candidate CAND-6DD7ED0837FA entity_id=SIG-000801 reason=duplicate_id:SIG-000801 conf=0.92`
- `candidate CAND-3D9AD026D98F entity_id=SIG-000802 reason=duplicate_id:SIG-000802 conf=0.9`
- `candidate CAND-FA63771FE15D entity_id=SIG-000805 reason=duplicate_id:SIG-000805 conf=0.9`
- `candidate CAND-3BB7F2E91C1B entity_id=SIG-000803 reason=duplicate_id:SIG-000803 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-686E720DCBF5 | business_signal_library | 0.9 | False | duplicate_id:SIG-000804 | Rejected |
| CAND-6DD7ED0837FA | business_signal_library | 0.92 | False | duplicate_id:SIG-000801 | Rejected |
| CAND-3D9AD026D98F | business_signal_library | 0.9 | False | duplicate_id:SIG-000802 | Rejected |
| CAND-FA63771FE15D | business_signal_library | 0.9 | False | duplicate_id:SIG-000805 | Rejected |
| CAND-3BB7F2E91C1B | business_signal_library | 0.9 | False | duplicate_id:SIG-000803 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000804` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
