# Candidate Root Cause

**Generated:** 2026-07-11T11:49:33+00:00
**Session:** `SESSION-20260711-FB328B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000043`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260711-FB328B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000043': 1, 'duplicate_id:SIG-000042': 1, 'duplicate_id:SIG-000040': 1, 'duplicate_id:SIG-000044': 1, 'duplicate_id:SIG-000041': 1}`
- `candidate CAND-6311DFB6B180 entity_id=SIG-000043 reason=duplicate_id:SIG-000043 conf=0.9`
- `candidate CAND-B8DEAB4C7490 entity_id=SIG-000042 reason=duplicate_id:SIG-000042 conf=0.88`
- `candidate CAND-BADF000AB75B entity_id=SIG-000040 reason=duplicate_id:SIG-000040 conf=0.9`
- `candidate CAND-5B59CD29ABBA entity_id=SIG-000044 reason=duplicate_id:SIG-000044 conf=0.92`
- `candidate CAND-B76D41661BD0 entity_id=SIG-000041 reason=duplicate_id:SIG-000041 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-6311DFB6B180 | business_signal_library | 0.9 | False | duplicate_id:SIG-000043 | Rejected |
| CAND-B8DEAB4C7490 | business_signal_library | 0.88 | False | duplicate_id:SIG-000042 | Rejected |
| CAND-BADF000AB75B | business_signal_library | 0.9 | False | duplicate_id:SIG-000040 | Rejected |
| CAND-5B59CD29ABBA | business_signal_library | 0.92 | False | duplicate_id:SIG-000044 | Rejected |
| CAND-B76D41661BD0 | business_signal_library | 0.92 | False | duplicate_id:SIG-000041 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000043` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
