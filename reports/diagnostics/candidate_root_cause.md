# Candidate Root Cause

**Generated:** 2026-07-28T11:37:27+00:00
**Session:** `SESSION-20260728-4474C8`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000993`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260728-4474C8`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000993': 1, 'duplicate_id:SIG-000994': 1, 'duplicate_id:SIG-000990': 1, 'duplicate_id:SIG-000991': 1, 'duplicate_id:SIG-000992': 1}`
- `candidate CAND-FCC38BA16DE1 entity_id=SIG-000993 reason=duplicate_id:SIG-000993 conf=0.9`
- `candidate CAND-BDEB7C09384A entity_id=SIG-000994 reason=duplicate_id:SIG-000994 conf=0.92`
- `candidate CAND-BB814C2D5C63 entity_id=SIG-000990 reason=duplicate_id:SIG-000990 conf=0.9`
- `candidate CAND-C342BDC7F30A entity_id=SIG-000991 reason=duplicate_id:SIG-000991 conf=0.92`
- `candidate CAND-82DD8E520197 entity_id=SIG-000992 reason=duplicate_id:SIG-000992 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-FCC38BA16DE1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000993 | Rejected |
| CAND-BDEB7C09384A | business_signal_library | 0.92 | False | duplicate_id:SIG-000994 | Rejected |
| CAND-BB814C2D5C63 | business_signal_library | 0.9 | False | duplicate_id:SIG-000990 | Rejected |
| CAND-C342BDC7F30A | business_signal_library | 0.92 | False | duplicate_id:SIG-000991 | Rejected |
| CAND-82DD8E520197 | business_signal_library | 0.88 | False | duplicate_id:SIG-000992 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000993` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
