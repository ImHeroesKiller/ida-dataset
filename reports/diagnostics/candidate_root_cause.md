# Candidate Root Cause

**Generated:** 2026-08-01T08:45:21+00:00
**Session:** `SESSION-20260801-5B5ECB`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001195`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260801-5B5ECB`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001195': 1, 'duplicate_id:SIG-001196': 1, 'duplicate_id:SIG-001199': 1, 'duplicate_id:SIG-001198': 1, 'duplicate_id:SIG-001197': 1}`
- `candidate CAND-DED0FE001A03 entity_id=SIG-001195 reason=duplicate_id:SIG-001195 conf=0.9`
- `candidate CAND-96027DD7942F entity_id=SIG-001196 reason=duplicate_id:SIG-001196 conf=0.92`
- `candidate CAND-6CEB6CB399DE entity_id=SIG-001199 reason=duplicate_id:SIG-001199 conf=0.92`
- `candidate CAND-7CF29B22DFDA entity_id=SIG-001198 reason=duplicate_id:SIG-001198 conf=0.9`
- `candidate CAND-40F3CF6C7896 entity_id=SIG-001197 reason=duplicate_id:SIG-001197 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-DED0FE001A03 | business_signal_library | 0.9 | False | duplicate_id:SIG-001195 | Rejected |
| CAND-96027DD7942F | business_signal_library | 0.92 | False | duplicate_id:SIG-001196 | Rejected |
| CAND-6CEB6CB399DE | business_signal_library | 0.92 | False | duplicate_id:SIG-001199 | Rejected |
| CAND-7CF29B22DFDA | business_signal_library | 0.9 | False | duplicate_id:SIG-001198 | Rejected |
| CAND-40F3CF6C7896 | business_signal_library | 0.88 | False | duplicate_id:SIG-001197 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001195` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
