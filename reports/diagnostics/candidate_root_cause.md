# Candidate Root Cause

**Generated:** 2026-08-08T10:00:48+00:00
**Session:** `SESSION-20260808-86A932`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001604`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260808-86A932`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001604': 1, 'duplicate_id:SIG-001600': 1, 'duplicate_id:SIG-001603': 1, 'duplicate_id:SIG-001601': 1, 'duplicate_id:SIG-001602': 1}`
- `candidate CAND-4611984E0968 entity_id=SIG-001604 reason=duplicate_id:SIG-001604 conf=0.92`
- `candidate CAND-139A0E8A5CAA entity_id=SIG-001600 reason=duplicate_id:SIG-001600 conf=0.9`
- `candidate CAND-0466F9D71E3E entity_id=SIG-001603 reason=duplicate_id:SIG-001603 conf=0.9`
- `candidate CAND-85036C18E04A entity_id=SIG-001601 reason=duplicate_id:SIG-001601 conf=0.92`
- `candidate CAND-5C77576FBBD8 entity_id=SIG-001602 reason=duplicate_id:SIG-001602 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-4611984E0968 | business_signal_library | 0.92 | False | duplicate_id:SIG-001604 | Rejected |
| CAND-139A0E8A5CAA | business_signal_library | 0.9 | False | duplicate_id:SIG-001600 | Rejected |
| CAND-0466F9D71E3E | business_signal_library | 0.9 | False | duplicate_id:SIG-001603 | Rejected |
| CAND-85036C18E04A | business_signal_library | 0.92 | False | duplicate_id:SIG-001601 | Rejected |
| CAND-5C77576FBBD8 | business_signal_library | 0.88 | False | duplicate_id:SIG-001602 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001604` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
