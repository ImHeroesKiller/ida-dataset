# Candidate Root Cause

**Generated:** 2026-08-14T08:30:22+00:00
**Session:** `SESSION-20260814-E02F6C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000097`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260814-E02F6C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000097': 1, 'duplicate_id:SIG-000099': 1, 'duplicate_id:SIG-000098': 1, 'duplicate_id:SIG-000100': 1, 'duplicate_id:SIG-000096': 1}`
- `candidate CAND-F949B58C5D38 entity_id=SIG-000097 reason=duplicate_id:SIG-000097 conf=0.9`
- `candidate CAND-59BB819AA772 entity_id=SIG-000099 reason=duplicate_id:SIG-000099 conf=0.9`
- `candidate CAND-10B508123E33 entity_id=SIG-000098 reason=duplicate_id:SIG-000098 conf=0.9`
- `candidate CAND-B84D780067E3 entity_id=SIG-000100 reason=duplicate_id:SIG-000100 conf=0.9`
- `candidate CAND-96ED62A4D01D entity_id=SIG-000096 reason=duplicate_id:SIG-000096 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F949B58C5D38 | business_signal_library | 0.9 | False | duplicate_id:SIG-000097 | Rejected |
| CAND-59BB819AA772 | business_signal_library | 0.9 | False | duplicate_id:SIG-000099 | Rejected |
| CAND-10B508123E33 | business_signal_library | 0.9 | False | duplicate_id:SIG-000098 | Rejected |
| CAND-B84D780067E3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000100 | Rejected |
| CAND-96ED62A4D01D | business_signal_library | 0.92 | False | duplicate_id:SIG-000096 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000097` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
