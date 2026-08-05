# Candidate Root Cause

**Generated:** 2026-08-05T21:29:28+00:00
**Session:** `SESSION-20260805-892659`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001440`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260805-892659`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001440': 1, 'duplicate_id:SIG-001442': 1, 'duplicate_id:SIG-001443': 1, 'duplicate_id:SIG-001441': 1, 'duplicate_id:SIG-001444': 1}`
- `candidate CAND-A2257D216113 entity_id=SIG-001440 reason=duplicate_id:SIG-001440 conf=0.9`
- `candidate CAND-DEC83B651E41 entity_id=SIG-001442 reason=duplicate_id:SIG-001442 conf=0.88`
- `candidate CAND-5E18F54CF603 entity_id=SIG-001443 reason=duplicate_id:SIG-001443 conf=0.9`
- `candidate CAND-F054BD56D99E entity_id=SIG-001441 reason=duplicate_id:SIG-001441 conf=0.92`
- `candidate CAND-3F3924B9CB90 entity_id=SIG-001444 reason=duplicate_id:SIG-001444 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A2257D216113 | business_signal_library | 0.9 | False | duplicate_id:SIG-001440 | Rejected |
| CAND-DEC83B651E41 | business_signal_library | 0.88 | False | duplicate_id:SIG-001442 | Rejected |
| CAND-5E18F54CF603 | business_signal_library | 0.9 | False | duplicate_id:SIG-001443 | Rejected |
| CAND-F054BD56D99E | business_signal_library | 0.92 | False | duplicate_id:SIG-001441 | Rejected |
| CAND-3F3924B9CB90 | business_signal_library | 0.92 | False | duplicate_id:SIG-001444 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001440` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
