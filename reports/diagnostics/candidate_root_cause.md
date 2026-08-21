# Candidate Root Cause

**Generated:** 2026-08-21T21:44:03+00:00
**Session:** `SESSION-20260821-DE19C8`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000942`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260821-DE19C8`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000942': 1, 'duplicate_id:SIG-000941': 1, 'duplicate_id:SIG-000945': 1, 'duplicate_id:SIG-000943': 1, 'duplicate_id:SIG-000944': 1}`
- `candidate CAND-F40ED70585BC entity_id=SIG-000942 reason=duplicate_id:SIG-000942 conf=0.9`
- `candidate CAND-D05D8BFD8E9C entity_id=SIG-000941 reason=duplicate_id:SIG-000941 conf=0.92`
- `candidate CAND-068E89992D0B entity_id=SIG-000945 reason=duplicate_id:SIG-000945 conf=0.9`
- `candidate CAND-14B811C82B77 entity_id=SIG-000943 reason=duplicate_id:SIG-000943 conf=0.9`
- `candidate CAND-4C542EFD33CC entity_id=SIG-000944 reason=duplicate_id:SIG-000944 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F40ED70585BC | business_signal_library | 0.9 | False | duplicate_id:SIG-000942 | Rejected |
| CAND-D05D8BFD8E9C | business_signal_library | 0.92 | False | duplicate_id:SIG-000941 | Rejected |
| CAND-068E89992D0B | business_signal_library | 0.9 | False | duplicate_id:SIG-000945 | Rejected |
| CAND-14B811C82B77 | business_signal_library | 0.9 | False | duplicate_id:SIG-000943 | Rejected |
| CAND-4C542EFD33CC | business_signal_library | 0.9 | False | duplicate_id:SIG-000944 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000942` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
