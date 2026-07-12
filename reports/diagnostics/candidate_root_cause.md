# Candidate Root Cause

**Generated:** 2026-07-12T19:37:50+00:00
**Session:** `SESSION-20260712-9C1F13`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000119`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260712-9C1F13`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000119': 1, 'duplicate_id:SIG-000115': 1, 'duplicate_id:SIG-000116': 1, 'duplicate_id:SIG-000117': 1, 'duplicate_id:SIG-000118': 1}`
- `candidate CAND-2BFAA254F9FF entity_id=SIG-000119 reason=duplicate_id:SIG-000119 conf=0.92`
- `candidate CAND-75FE36D00C7C entity_id=SIG-000115 reason=duplicate_id:SIG-000115 conf=0.9`
- `candidate CAND-CB21E928D424 entity_id=SIG-000116 reason=duplicate_id:SIG-000116 conf=0.92`
- `candidate CAND-B1A8E8423E1C entity_id=SIG-000117 reason=duplicate_id:SIG-000117 conf=0.88`
- `candidate CAND-860D075C7BEB entity_id=SIG-000118 reason=duplicate_id:SIG-000118 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-2BFAA254F9FF | business_signal_library | 0.92 | False | duplicate_id:SIG-000119 | Rejected |
| CAND-75FE36D00C7C | business_signal_library | 0.9 | False | duplicate_id:SIG-000115 | Rejected |
| CAND-CB21E928D424 | business_signal_library | 0.92 | False | duplicate_id:SIG-000116 | Rejected |
| CAND-B1A8E8423E1C | business_signal_library | 0.88 | False | duplicate_id:SIG-000117 | Rejected |
| CAND-860D075C7BEB | business_signal_library | 0.9 | False | duplicate_id:SIG-000118 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000119` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
