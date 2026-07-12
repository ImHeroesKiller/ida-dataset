# Candidate Root Cause

**Generated:** 2026-07-12T11:31:27+00:00
**Session:** `SESSION-20260712-A064BA`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000096`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260712-A064BA`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000096': 1, 'duplicate_id:SIG-000098': 1, 'duplicate_id:SIG-000097': 1, 'duplicate_id:SIG-000099': 1, 'duplicate_id:SIG-000095': 1}`
- `candidate CAND-F88023CF0DFE entity_id=SIG-000096 reason=duplicate_id:SIG-000096 conf=0.92`
- `candidate CAND-EB74A7F042D0 entity_id=SIG-000098 reason=duplicate_id:SIG-000098 conf=0.9`
- `candidate CAND-6D09CFF0C911 entity_id=SIG-000097 reason=duplicate_id:SIG-000097 conf=0.88`
- `candidate CAND-0353C4B3311E entity_id=SIG-000099 reason=duplicate_id:SIG-000099 conf=0.92`
- `candidate CAND-6E760DFEF276 entity_id=SIG-000095 reason=duplicate_id:SIG-000095 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F88023CF0DFE | business_signal_library | 0.92 | False | duplicate_id:SIG-000096 | Rejected |
| CAND-EB74A7F042D0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000098 | Rejected |
| CAND-6D09CFF0C911 | business_signal_library | 0.88 | False | duplicate_id:SIG-000097 | Rejected |
| CAND-0353C4B3311E | business_signal_library | 0.92 | False | duplicate_id:SIG-000099 | Rejected |
| CAND-6E760DFEF276 | business_signal_library | 0.9 | False | duplicate_id:SIG-000095 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000096` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
