# Candidate Root Cause

**Generated:** 2026-08-03T06:45:34+00:00
**Session:** `SESSION-20260803-8679D0`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001309`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260803-8679D0`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001309': 1, 'duplicate_id:SIG-001307': 1, 'duplicate_id:SIG-001305': 1, 'duplicate_id:SIG-001306': 1, 'duplicate_id:SIG-001308': 1}`
- `candidate CAND-C42D8057D855 entity_id=SIG-001309 reason=duplicate_id:SIG-001309 conf=0.92`
- `candidate CAND-752239D17974 entity_id=SIG-001307 reason=duplicate_id:SIG-001307 conf=0.88`
- `candidate CAND-DC6EF6D68062 entity_id=SIG-001305 reason=duplicate_id:SIG-001305 conf=0.9`
- `candidate CAND-EA7A51628294 entity_id=SIG-001306 reason=duplicate_id:SIG-001306 conf=0.92`
- `candidate CAND-1EEC5BA4013D entity_id=SIG-001308 reason=duplicate_id:SIG-001308 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-C42D8057D855 | business_signal_library | 0.92 | False | duplicate_id:SIG-001309 | Rejected |
| CAND-752239D17974 | business_signal_library | 0.88 | False | duplicate_id:SIG-001307 | Rejected |
| CAND-DC6EF6D68062 | business_signal_library | 0.9 | False | duplicate_id:SIG-001305 | Rejected |
| CAND-EA7A51628294 | business_signal_library | 0.92 | False | duplicate_id:SIG-001306 | Rejected |
| CAND-1EEC5BA4013D | business_signal_library | 0.9 | False | duplicate_id:SIG-001308 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001309` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
