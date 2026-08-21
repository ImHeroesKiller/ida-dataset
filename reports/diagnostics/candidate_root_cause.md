# Candidate Root Cause

**Generated:** 2026-08-21T01:42:17+00:00
**Session:** `SESSION-20260821-A46354`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000850`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260821-A46354`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000850': 1, 'duplicate_id:SIG-000849': 1, 'duplicate_id:SIG-000848': 1, 'duplicate_id:SIG-000846': 1, 'duplicate_id:SIG-000847': 1}`
- `candidate CAND-5648D12987F3 entity_id=SIG-000850 reason=duplicate_id:SIG-000850 conf=0.9`
- `candidate CAND-19C3FD2CA2E7 entity_id=SIG-000849 reason=duplicate_id:SIG-000849 conf=0.9`
- `candidate CAND-907894B404F7 entity_id=SIG-000848 reason=duplicate_id:SIG-000848 conf=0.9`
- `candidate CAND-DBC52BEC24E8 entity_id=SIG-000846 reason=duplicate_id:SIG-000846 conf=0.92`
- `candidate CAND-03568C61480D entity_id=SIG-000847 reason=duplicate_id:SIG-000847 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5648D12987F3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000850 | Rejected |
| CAND-19C3FD2CA2E7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000849 | Rejected |
| CAND-907894B404F7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000848 | Rejected |
| CAND-DBC52BEC24E8 | business_signal_library | 0.92 | False | duplicate_id:SIG-000846 | Rejected |
| CAND-03568C61480D | business_signal_library | 0.9 | False | duplicate_id:SIG-000847 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000850` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
