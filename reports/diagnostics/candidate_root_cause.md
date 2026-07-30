# Candidate Root Cause

**Generated:** 2026-07-30T12:17:08+00:00
**Session:** `SESSION-20260730-212361`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001100`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260730-212361`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001100': 1, 'duplicate_id:SIG-001104': 1, 'duplicate_id:SIG-001103': 1, 'duplicate_id:SIG-001102': 1, 'duplicate_id:SIG-001101': 1}`
- `candidate CAND-EE197EE33298 entity_id=SIG-001100 reason=duplicate_id:SIG-001100 conf=0.9`
- `candidate CAND-3BE449E6CE7F entity_id=SIG-001104 reason=duplicate_id:SIG-001104 conf=0.92`
- `candidate CAND-964264F5A648 entity_id=SIG-001103 reason=duplicate_id:SIG-001103 conf=0.9`
- `candidate CAND-70AA6B25D763 entity_id=SIG-001102 reason=duplicate_id:SIG-001102 conf=0.88`
- `candidate CAND-6E825E1726AA entity_id=SIG-001101 reason=duplicate_id:SIG-001101 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-EE197EE33298 | business_signal_library | 0.9 | False | duplicate_id:SIG-001100 | Rejected |
| CAND-3BE449E6CE7F | business_signal_library | 0.92 | False | duplicate_id:SIG-001104 | Rejected |
| CAND-964264F5A648 | business_signal_library | 0.9 | False | duplicate_id:SIG-001103 | Rejected |
| CAND-70AA6B25D763 | business_signal_library | 0.88 | False | duplicate_id:SIG-001102 | Rejected |
| CAND-6E825E1726AA | business_signal_library | 0.92 | False | duplicate_id:SIG-001101 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001100` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
