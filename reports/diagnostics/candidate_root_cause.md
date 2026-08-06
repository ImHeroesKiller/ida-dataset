# Candidate Root Cause

**Generated:** 2026-08-06T03:01:18+00:00
**Session:** `SESSION-20260806-3EA50A`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001452`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260806-3EA50A`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001452': 1, 'duplicate_id:SIG-001453': 1, 'duplicate_id:SIG-001454': 1, 'duplicate_id:SIG-001450': 1, 'duplicate_id:SIG-001451': 1}`
- `candidate CAND-B80C05EDDD87 entity_id=SIG-001452 reason=duplicate_id:SIG-001452 conf=0.88`
- `candidate CAND-43D2977EF7F5 entity_id=SIG-001453 reason=duplicate_id:SIG-001453 conf=0.9`
- `candidate CAND-FCC87FDEB30F entity_id=SIG-001454 reason=duplicate_id:SIG-001454 conf=0.92`
- `candidate CAND-EB26131F3B27 entity_id=SIG-001450 reason=duplicate_id:SIG-001450 conf=0.9`
- `candidate CAND-8683BF2DA0E0 entity_id=SIG-001451 reason=duplicate_id:SIG-001451 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B80C05EDDD87 | business_signal_library | 0.88 | False | duplicate_id:SIG-001452 | Rejected |
| CAND-43D2977EF7F5 | business_signal_library | 0.9 | False | duplicate_id:SIG-001453 | Rejected |
| CAND-FCC87FDEB30F | business_signal_library | 0.92 | False | duplicate_id:SIG-001454 | Rejected |
| CAND-EB26131F3B27 | business_signal_library | 0.9 | False | duplicate_id:SIG-001450 | Rejected |
| CAND-8683BF2DA0E0 | business_signal_library | 0.92 | False | duplicate_id:SIG-001451 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001452` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
