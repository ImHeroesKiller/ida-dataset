# Candidate Root Cause

**Generated:** 2026-08-15T07:46:05+00:00
**Session:** `SESSION-20260815-5B4597`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000197`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260815-5B4597`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000197': 1, 'duplicate_id:SIG-000198': 1, 'duplicate_id:SIG-000199': 1, 'duplicate_id:SIG-000200': 1, 'duplicate_id:SIG-000196': 1}`
- `candidate CAND-B3AEA1054913 entity_id=SIG-000197 reason=duplicate_id:SIG-000197 conf=0.9`
- `candidate CAND-C9F9BF174421 entity_id=SIG-000198 reason=duplicate_id:SIG-000198 conf=0.9`
- `candidate CAND-1E9D5660D39C entity_id=SIG-000199 reason=duplicate_id:SIG-000199 conf=0.9`
- `candidate CAND-A1D0297BF9C0 entity_id=SIG-000200 reason=duplicate_id:SIG-000200 conf=0.9`
- `candidate CAND-F60F0FC5477D entity_id=SIG-000196 reason=duplicate_id:SIG-000196 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B3AEA1054913 | business_signal_library | 0.9 | False | duplicate_id:SIG-000197 | Rejected |
| CAND-C9F9BF174421 | business_signal_library | 0.9 | False | duplicate_id:SIG-000198 | Rejected |
| CAND-1E9D5660D39C | business_signal_library | 0.9 | False | duplicate_id:SIG-000199 | Rejected |
| CAND-A1D0297BF9C0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000200 | Rejected |
| CAND-F60F0FC5477D | business_signal_library | 0.92 | False | duplicate_id:SIG-000196 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000197` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
