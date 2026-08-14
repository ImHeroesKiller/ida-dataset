# Candidate Root Cause

**Generated:** 2026-08-14T22:38:09+00:00
**Session:** `SESSION-20260814-959436`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000158`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260814-959436`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000158': 1, 'duplicate_id:SIG-000157': 1, 'duplicate_id:SIG-000160': 1, 'duplicate_id:SIG-000159': 1, 'duplicate_id:SIG-000156': 1}`
- `candidate CAND-12B7D27FC015 entity_id=SIG-000158 reason=duplicate_id:SIG-000158 conf=0.9`
- `candidate CAND-CB11FE4D9B77 entity_id=SIG-000157 reason=duplicate_id:SIG-000157 conf=0.9`
- `candidate CAND-C492BED24DD9 entity_id=SIG-000160 reason=duplicate_id:SIG-000160 conf=0.9`
- `candidate CAND-E41D0CC95213 entity_id=SIG-000159 reason=duplicate_id:SIG-000159 conf=0.9`
- `candidate CAND-4484FD1C8716 entity_id=SIG-000156 reason=duplicate_id:SIG-000156 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-12B7D27FC015 | business_signal_library | 0.9 | False | duplicate_id:SIG-000158 | Rejected |
| CAND-CB11FE4D9B77 | business_signal_library | 0.9 | False | duplicate_id:SIG-000157 | Rejected |
| CAND-C492BED24DD9 | business_signal_library | 0.9 | False | duplicate_id:SIG-000160 | Rejected |
| CAND-E41D0CC95213 | business_signal_library | 0.9 | False | duplicate_id:SIG-000159 | Rejected |
| CAND-4484FD1C8716 | business_signal_library | 0.92 | False | duplicate_id:SIG-000156 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000158` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
