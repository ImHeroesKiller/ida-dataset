# Candidate Root Cause

**Generated:** 2026-08-13T22:00:51+00:00
**Session:** `SESSION-20260813-A94B2E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000062`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260813-A94B2E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000062': 1, 'duplicate_id:SIG-000061': 1, 'duplicate_id:SIG-000065': 1, 'duplicate_id:SIG-000063': 1, 'duplicate_id:SIG-000064': 1}`
- `candidate CAND-04E1F35159FA entity_id=SIG-000062 reason=duplicate_id:SIG-000062 conf=0.9`
- `candidate CAND-AE9AD9FFE8D9 entity_id=SIG-000061 reason=duplicate_id:SIG-000061 conf=0.92`
- `candidate CAND-5427B6E34134 entity_id=SIG-000065 reason=duplicate_id:SIG-000065 conf=0.9`
- `candidate CAND-C887AAEAD014 entity_id=SIG-000063 reason=duplicate_id:SIG-000063 conf=0.9`
- `candidate CAND-1F3F8BE0A9A0 entity_id=SIG-000064 reason=duplicate_id:SIG-000064 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-04E1F35159FA | business_signal_library | 0.9 | False | duplicate_id:SIG-000062 | Rejected |
| CAND-AE9AD9FFE8D9 | business_signal_library | 0.92 | False | duplicate_id:SIG-000061 | Rejected |
| CAND-5427B6E34134 | business_signal_library | 0.9 | False | duplicate_id:SIG-000065 | Rejected |
| CAND-C887AAEAD014 | business_signal_library | 0.9 | False | duplicate_id:SIG-000063 | Rejected |
| CAND-1F3F8BE0A9A0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000064 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000062` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
