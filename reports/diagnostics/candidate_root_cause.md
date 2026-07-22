# Candidate Root Cause

**Generated:** 2026-07-22T12:45:05+00:00
**Session:** `SESSION-20260722-2FD02B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000680`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260722-2FD02B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000680': 1, 'duplicate_id:SIG-000683': 1, 'duplicate_id:SIG-000682': 1, 'duplicate_id:SIG-000681': 1, 'duplicate_id:SIG-000684': 1}`
- `candidate CAND-04774F840413 entity_id=SIG-000680 reason=duplicate_id:SIG-000680 conf=0.9`
- `candidate CAND-B79D8CEFF1CF entity_id=SIG-000683 reason=duplicate_id:SIG-000683 conf=0.9`
- `candidate CAND-9B436AB58A40 entity_id=SIG-000682 reason=duplicate_id:SIG-000682 conf=0.88`
- `candidate CAND-E29D6205F066 entity_id=SIG-000681 reason=duplicate_id:SIG-000681 conf=0.92`
- `candidate CAND-73A3A07751D4 entity_id=SIG-000684 reason=duplicate_id:SIG-000684 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-04774F840413 | business_signal_library | 0.9 | False | duplicate_id:SIG-000680 | Rejected |
| CAND-B79D8CEFF1CF | business_signal_library | 0.9 | False | duplicate_id:SIG-000683 | Rejected |
| CAND-9B436AB58A40 | business_signal_library | 0.88 | False | duplicate_id:SIG-000682 | Rejected |
| CAND-E29D6205F066 | business_signal_library | 0.92 | False | duplicate_id:SIG-000681 | Rejected |
| CAND-73A3A07751D4 | business_signal_library | 0.92 | False | duplicate_id:SIG-000684 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000680` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
