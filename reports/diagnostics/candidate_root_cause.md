# Candidate Root Cause

**Generated:** 2026-08-10T15:23:41+00:00
**Session:** `SESSION-20260810-2815A3`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001815`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260810-2815A3`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001815': 1, 'duplicate_id:SIG-001818': 1, 'duplicate_id:SIG-001817': 1, 'duplicate_id:SIG-001816': 1, 'duplicate_id:SIG-001819': 1}`
- `candidate CAND-7F02BB489258 entity_id=SIG-001815 reason=duplicate_id:SIG-001815 conf=0.9`
- `candidate CAND-F7B420C643B5 entity_id=SIG-001818 reason=duplicate_id:SIG-001818 conf=0.9`
- `candidate CAND-7A3A0770DDC0 entity_id=SIG-001817 reason=duplicate_id:SIG-001817 conf=0.88`
- `candidate CAND-E178CF59C7FA entity_id=SIG-001816 reason=duplicate_id:SIG-001816 conf=0.92`
- `candidate CAND-120B106D216C entity_id=SIG-001819 reason=duplicate_id:SIG-001819 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-7F02BB489258 | business_signal_library | 0.9 | False | duplicate_id:SIG-001815 | Rejected |
| CAND-F7B420C643B5 | business_signal_library | 0.9 | False | duplicate_id:SIG-001818 | Rejected |
| CAND-7A3A0770DDC0 | business_signal_library | 0.88 | False | duplicate_id:SIG-001817 | Rejected |
| CAND-E178CF59C7FA | business_signal_library | 0.92 | False | duplicate_id:SIG-001816 | Rejected |
| CAND-120B106D216C | business_signal_library | 0.92 | False | duplicate_id:SIG-001819 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001815` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
