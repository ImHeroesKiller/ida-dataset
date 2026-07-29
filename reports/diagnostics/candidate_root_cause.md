# Candidate Root Cause

**Generated:** 2026-07-29T06:51:59+00:00
**Session:** `SESSION-20260729-48D382`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001032`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260729-48D382`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001032': 1, 'duplicate_id:SIG-001033': 1, 'duplicate_id:SIG-001034': 1, 'duplicate_id:SIG-001030': 1, 'duplicate_id:SIG-001031': 1}`
- `candidate CAND-04A65576A129 entity_id=SIG-001032 reason=duplicate_id:SIG-001032 conf=0.88`
- `candidate CAND-3C5C975E064E entity_id=SIG-001033 reason=duplicate_id:SIG-001033 conf=0.9`
- `candidate CAND-ADA9AE14E3AA entity_id=SIG-001034 reason=duplicate_id:SIG-001034 conf=0.92`
- `candidate CAND-58C16C9D573F entity_id=SIG-001030 reason=duplicate_id:SIG-001030 conf=0.9`
- `candidate CAND-69F62D317CF2 entity_id=SIG-001031 reason=duplicate_id:SIG-001031 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-04A65576A129 | business_signal_library | 0.88 | False | duplicate_id:SIG-001032 | Rejected |
| CAND-3C5C975E064E | business_signal_library | 0.9 | False | duplicate_id:SIG-001033 | Rejected |
| CAND-ADA9AE14E3AA | business_signal_library | 0.92 | False | duplicate_id:SIG-001034 | Rejected |
| CAND-58C16C9D573F | business_signal_library | 0.9 | False | duplicate_id:SIG-001030 | Rejected |
| CAND-69F62D317CF2 | business_signal_library | 0.92 | False | duplicate_id:SIG-001031 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001032` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
