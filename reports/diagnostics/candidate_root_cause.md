# Candidate Root Cause

**Generated:** 2026-07-13T19:06:35+00:00
**Session:** `SESSION-20260713-0D8DDD`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000168`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260713-0D8DDD`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000168': 1, 'duplicate_id:SIG-000165': 1, 'duplicate_id:SIG-000166': 1, 'duplicate_id:SIG-000167': 1, 'duplicate_id:SIG-000169': 1}`
- `candidate CAND-B4BEF09F0359 entity_id=SIG-000168 reason=duplicate_id:SIG-000168 conf=0.85`
- `candidate CAND-A6284C9FE7DD entity_id=SIG-000165 reason=duplicate_id:SIG-000165 conf=0.9`
- `candidate CAND-422D3FE54EE2 entity_id=SIG-000166 reason=duplicate_id:SIG-000166 conf=0.92`
- `candidate CAND-31E135690274 entity_id=SIG-000167 reason=duplicate_id:SIG-000167 conf=0.88`
- `candidate CAND-57F278088148 entity_id=SIG-000169 reason=duplicate_id:SIG-000169 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B4BEF09F0359 | business_signal_library | 0.85 | False | duplicate_id:SIG-000168 | Rejected |
| CAND-A6284C9FE7DD | business_signal_library | 0.9 | False | duplicate_id:SIG-000165 | Rejected |
| CAND-422D3FE54EE2 | business_signal_library | 0.92 | False | duplicate_id:SIG-000166 | Rejected |
| CAND-31E135690274 | business_signal_library | 0.88 | False | duplicate_id:SIG-000167 | Rejected |
| CAND-57F278088148 | business_signal_library | 0.9 | False | duplicate_id:SIG-000169 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000168` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
