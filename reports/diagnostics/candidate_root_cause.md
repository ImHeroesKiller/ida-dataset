# Candidate Root Cause

**Generated:** 2026-07-14T02:59:17+00:00
**Session:** `SESSION-20260714-E49A61`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000181`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260714-E49A61`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000181': 1, 'duplicate_id:SIG-000180': 1, 'duplicate_id:SIG-000184': 1, 'duplicate_id:SIG-000182': 1, 'duplicate_id:SIG-000183': 1}`
- `candidate CAND-356BE86EC100 entity_id=SIG-000181 reason=duplicate_id:SIG-000181 conf=0.92`
- `candidate CAND-5795E3C572CE entity_id=SIG-000180 reason=duplicate_id:SIG-000180 conf=0.9`
- `candidate CAND-ED3867329576 entity_id=SIG-000184 reason=duplicate_id:SIG-000184 conf=0.92`
- `candidate CAND-261044072835 entity_id=SIG-000182 reason=duplicate_id:SIG-000182 conf=0.88`
- `candidate CAND-3F8ED64B6EBC entity_id=SIG-000183 reason=duplicate_id:SIG-000183 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-356BE86EC100 | business_signal_library | 0.92 | False | duplicate_id:SIG-000181 | Rejected |
| CAND-5795E3C572CE | business_signal_library | 0.9 | False | duplicate_id:SIG-000180 | Rejected |
| CAND-ED3867329576 | business_signal_library | 0.92 | False | duplicate_id:SIG-000184 | Rejected |
| CAND-261044072835 | business_signal_library | 0.88 | False | duplicate_id:SIG-000182 | Rejected |
| CAND-3F8ED64B6EBC | business_signal_library | 0.9 | False | duplicate_id:SIG-000183 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000181` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
