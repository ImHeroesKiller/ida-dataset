# Candidate Root Cause

**Generated:** 2026-08-23T08:50:11+00:00
**Session:** `SESSION-20260823-A14FDA`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001101`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260823-A14FDA`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001101': 1, 'duplicate_id:SIG-001105': 1, 'duplicate_id:SIG-001102': 1, 'duplicate_id:SIG-001104': 1, 'duplicate_id:SIG-001103': 1}`
- `candidate CAND-991F91A9260C entity_id=SIG-001101 reason=duplicate_id:SIG-001101 conf=0.92`
- `candidate CAND-54D843E915B0 entity_id=SIG-001105 reason=duplicate_id:SIG-001105 conf=0.9`
- `candidate CAND-D1A6EC47D812 entity_id=SIG-001102 reason=duplicate_id:SIG-001102 conf=0.9`
- `candidate CAND-251747E8661F entity_id=SIG-001104 reason=duplicate_id:SIG-001104 conf=0.9`
- `candidate CAND-C7D8436CA03C entity_id=SIG-001103 reason=duplicate_id:SIG-001103 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-991F91A9260C | business_signal_library | 0.92 | False | duplicate_id:SIG-001101 | Rejected |
| CAND-54D843E915B0 | business_signal_library | 0.9 | False | duplicate_id:SIG-001105 | Rejected |
| CAND-D1A6EC47D812 | business_signal_library | 0.9 | False | duplicate_id:SIG-001102 | Rejected |
| CAND-251747E8661F | business_signal_library | 0.9 | False | duplicate_id:SIG-001104 | Rejected |
| CAND-C7D8436CA03C | business_signal_library | 0.9 | False | duplicate_id:SIG-001103 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001101` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
