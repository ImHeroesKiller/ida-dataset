# Candidate Root Cause

**Generated:** 2026-08-09T20:59:10+00:00
**Session:** `SESSION-20260809-B4B8D9`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001764`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260809-B4B8D9`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001764': 1, 'duplicate_id:SIG-001762': 1, 'duplicate_id:SIG-001763': 1, 'duplicate_id:SIG-001760': 1, 'duplicate_id:SIG-001761': 1}`
- `candidate CAND-B4A503AA9CFE entity_id=SIG-001764 reason=duplicate_id:SIG-001764 conf=0.92`
- `candidate CAND-511A46538066 entity_id=SIG-001762 reason=duplicate_id:SIG-001762 conf=0.88`
- `candidate CAND-27ED6EBF1C37 entity_id=SIG-001763 reason=duplicate_id:SIG-001763 conf=0.9`
- `candidate CAND-316BBBDB1899 entity_id=SIG-001760 reason=duplicate_id:SIG-001760 conf=0.9`
- `candidate CAND-798DC8D891A1 entity_id=SIG-001761 reason=duplicate_id:SIG-001761 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B4A503AA9CFE | business_signal_library | 0.92 | False | duplicate_id:SIG-001764 | Rejected |
| CAND-511A46538066 | business_signal_library | 0.88 | False | duplicate_id:SIG-001762 | Rejected |
| CAND-27ED6EBF1C37 | business_signal_library | 0.9 | False | duplicate_id:SIG-001763 | Rejected |
| CAND-316BBBDB1899 | business_signal_library | 0.9 | False | duplicate_id:SIG-001760 | Rejected |
| CAND-798DC8D891A1 | business_signal_library | 0.92 | False | duplicate_id:SIG-001761 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001764` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
