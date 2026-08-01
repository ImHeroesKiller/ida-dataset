# Candidate Root Cause

**Generated:** 2026-08-01T16:19:11+00:00
**Session:** `SESSION-20260801-3068C4`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001216`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260801-3068C4`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001216': 1, 'duplicate_id:SIG-001215': 1, 'duplicate_id:SIG-001219': 1, 'duplicate_id:SIG-001218': 1, 'duplicate_id:SIG-001217': 1}`
- `candidate CAND-397D159E2FFD entity_id=SIG-001216 reason=duplicate_id:SIG-001216 conf=0.92`
- `candidate CAND-440153B89476 entity_id=SIG-001215 reason=duplicate_id:SIG-001215 conf=0.9`
- `candidate CAND-E60AB7315135 entity_id=SIG-001219 reason=duplicate_id:SIG-001219 conf=0.92`
- `candidate CAND-D9687C961BC4 entity_id=SIG-001218 reason=duplicate_id:SIG-001218 conf=0.9`
- `candidate CAND-D87E7C66872B entity_id=SIG-001217 reason=duplicate_id:SIG-001217 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-397D159E2FFD | business_signal_library | 0.92 | False | duplicate_id:SIG-001216 | Rejected |
| CAND-440153B89476 | business_signal_library | 0.9 | False | duplicate_id:SIG-001215 | Rejected |
| CAND-E60AB7315135 | business_signal_library | 0.92 | False | duplicate_id:SIG-001219 | Rejected |
| CAND-D9687C961BC4 | business_signal_library | 0.9 | False | duplicate_id:SIG-001218 | Rejected |
| CAND-D87E7C66872B | business_signal_library | 0.88 | False | duplicate_id:SIG-001217 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001216` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
