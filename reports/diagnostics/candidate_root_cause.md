# Candidate Root Cause

**Generated:** 2026-08-08T20:51:24+00:00
**Session:** `SESSION-20260808-E0FD11`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001658`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260808-E0FD11`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001658': 1, 'duplicate_id:SIG-001656': 1, 'duplicate_id:SIG-001655': 1, 'duplicate_id:SIG-001659': 1, 'duplicate_id:SIG-001657': 1}`
- `candidate CAND-9AB8FB86E74F entity_id=SIG-001658 reason=duplicate_id:SIG-001658 conf=0.9`
- `candidate CAND-672A419F7614 entity_id=SIG-001656 reason=duplicate_id:SIG-001656 conf=0.92`
- `candidate CAND-DEF0AA868C1F entity_id=SIG-001655 reason=duplicate_id:SIG-001655 conf=0.9`
- `candidate CAND-AB8058A301E1 entity_id=SIG-001659 reason=duplicate_id:SIG-001659 conf=0.92`
- `candidate CAND-425B7D6BA9AC entity_id=SIG-001657 reason=duplicate_id:SIG-001657 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-9AB8FB86E74F | business_signal_library | 0.9 | False | duplicate_id:SIG-001658 | Rejected |
| CAND-672A419F7614 | business_signal_library | 0.92 | False | duplicate_id:SIG-001656 | Rejected |
| CAND-DEF0AA868C1F | business_signal_library | 0.9 | False | duplicate_id:SIG-001655 | Rejected |
| CAND-AB8058A301E1 | business_signal_library | 0.92 | False | duplicate_id:SIG-001659 | Rejected |
| CAND-425B7D6BA9AC | business_signal_library | 0.88 | False | duplicate_id:SIG-001657 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001658` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
