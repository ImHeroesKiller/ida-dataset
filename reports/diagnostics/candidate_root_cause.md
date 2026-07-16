# Candidate Root Cause

**Generated:** 2026-07-16T03:53:50+00:00
**Session:** `SESSION-20260716-92A106`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000294`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260716-92A106`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000294': 1, 'duplicate_id:SIG-000290': 1, 'duplicate_id:SIG-000291': 1, 'duplicate_id:SIG-000292': 1, 'duplicate_id:SIG-000293': 1}`
- `candidate CAND-8B43D8239E53 entity_id=SIG-000294 reason=duplicate_id:SIG-000294 conf=0.85`
- `candidate CAND-D3D78A09E8F6 entity_id=SIG-000290 reason=duplicate_id:SIG-000290 conf=0.85`
- `candidate CAND-58F9F2F20E69 entity_id=SIG-000291 reason=duplicate_id:SIG-000291 conf=0.9`
- `candidate CAND-DBC199765D96 entity_id=SIG-000292 reason=duplicate_id:SIG-000292 conf=0.92`
- `candidate CAND-59737FE42123 entity_id=SIG-000293 reason=duplicate_id:SIG-000293 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-8B43D8239E53 | business_signal_library | 0.85 | False | duplicate_id:SIG-000294 | Rejected |
| CAND-D3D78A09E8F6 | business_signal_library | 0.85 | False | duplicate_id:SIG-000290 | Rejected |
| CAND-58F9F2F20E69 | business_signal_library | 0.9 | False | duplicate_id:SIG-000291 | Rejected |
| CAND-DBC199765D96 | business_signal_library | 0.92 | False | duplicate_id:SIG-000292 | Rejected |
| CAND-59737FE42123 | business_signal_library | 0.88 | False | duplicate_id:SIG-000293 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000294` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
