# Candidate Root Cause

**Generated:** 2026-08-01T06:18:29+00:00
**Session:** `SESSION-20260801-EC1509`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001193`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260801-EC1509`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001193': 1, 'duplicate_id:SIG-001192': 1, 'duplicate_id:SIG-001190': 1, 'duplicate_id:SIG-001194': 1, 'duplicate_id:SIG-001191': 1}`
- `candidate CAND-F235382A9F71 entity_id=SIG-001193 reason=duplicate_id:SIG-001193 conf=0.9`
- `candidate CAND-012D1CEC7F6D entity_id=SIG-001192 reason=duplicate_id:SIG-001192 conf=0.88`
- `candidate CAND-57FC4DD9AD32 entity_id=SIG-001190 reason=duplicate_id:SIG-001190 conf=0.9`
- `candidate CAND-751909187A47 entity_id=SIG-001194 reason=duplicate_id:SIG-001194 conf=0.92`
- `candidate CAND-6F5C0E25102B entity_id=SIG-001191 reason=duplicate_id:SIG-001191 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F235382A9F71 | business_signal_library | 0.9 | False | duplicate_id:SIG-001193 | Rejected |
| CAND-012D1CEC7F6D | business_signal_library | 0.88 | False | duplicate_id:SIG-001192 | Rejected |
| CAND-57FC4DD9AD32 | business_signal_library | 0.9 | False | duplicate_id:SIG-001190 | Rejected |
| CAND-751909187A47 | business_signal_library | 0.92 | False | duplicate_id:SIG-001194 | Rejected |
| CAND-6F5C0E25102B | business_signal_library | 0.92 | False | duplicate_id:SIG-001191 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001193` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
