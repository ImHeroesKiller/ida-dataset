# Candidate Root Cause

**Generated:** 2026-08-18T14:46:32+00:00
**Session:** `SESSION-20260818-16397F`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000566`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260818-16397F`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000566': 1, 'duplicate_id:SIG-000569': 1, 'duplicate_id:SIG-000570': 1, 'duplicate_id:SIG-000567': 1, 'duplicate_id:SIG-000568': 1}`
- `candidate CAND-03D80D0E8A57 entity_id=SIG-000566 reason=duplicate_id:SIG-000566 conf=0.92`
- `candidate CAND-59FB54702D7C entity_id=SIG-000569 reason=duplicate_id:SIG-000569 conf=0.9`
- `candidate CAND-08CAFF865115 entity_id=SIG-000570 reason=duplicate_id:SIG-000570 conf=0.9`
- `candidate CAND-932F4070C262 entity_id=SIG-000567 reason=duplicate_id:SIG-000567 conf=0.9`
- `candidate CAND-101C3123F01D entity_id=SIG-000568 reason=duplicate_id:SIG-000568 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-03D80D0E8A57 | business_signal_library | 0.92 | False | duplicate_id:SIG-000566 | Rejected |
| CAND-59FB54702D7C | business_signal_library | 0.9 | False | duplicate_id:SIG-000569 | Rejected |
| CAND-08CAFF865115 | business_signal_library | 0.9 | False | duplicate_id:SIG-000570 | Rejected |
| CAND-932F4070C262 | business_signal_library | 0.9 | False | duplicate_id:SIG-000567 | Rejected |
| CAND-101C3123F01D | business_signal_library | 0.9 | False | duplicate_id:SIG-000568 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000566` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
