# Candidate Root Cause

**Generated:** 2026-08-11T05:29:04+00:00
**Session:** `SESSION-20260811-BE5468`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001870`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260811-BE5468`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001870': 1, 'duplicate_id:SIG-001873': 1, 'duplicate_id:SIG-001871': 1, 'duplicate_id:SIG-001874': 1, 'duplicate_id:SIG-001872': 1}`
- `candidate CAND-62C71300BE88 entity_id=SIG-001870 reason=duplicate_id:SIG-001870 conf=0.9`
- `candidate CAND-BA243BC289F1 entity_id=SIG-001873 reason=duplicate_id:SIG-001873 conf=0.9`
- `candidate CAND-C08EC5CFE357 entity_id=SIG-001871 reason=duplicate_id:SIG-001871 conf=0.92`
- `candidate CAND-778593C606D2 entity_id=SIG-001874 reason=duplicate_id:SIG-001874 conf=0.92`
- `candidate CAND-D531B90C059E entity_id=SIG-001872 reason=duplicate_id:SIG-001872 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-62C71300BE88 | business_signal_library | 0.9 | False | duplicate_id:SIG-001870 | Rejected |
| CAND-BA243BC289F1 | business_signal_library | 0.9 | False | duplicate_id:SIG-001873 | Rejected |
| CAND-C08EC5CFE357 | business_signal_library | 0.92 | False | duplicate_id:SIG-001871 | Rejected |
| CAND-778593C606D2 | business_signal_library | 0.92 | False | duplicate_id:SIG-001874 | Rejected |
| CAND-D531B90C059E | business_signal_library | 0.88 | False | duplicate_id:SIG-001872 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001870` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
