# Candidate Root Cause

**Generated:** 2026-07-13T20:38:09+00:00
**Session:** `SESSION-20260713-71E15C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000173`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260713-71E15C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000173': 1, 'duplicate_id:SIG-000174': 1, 'duplicate_id:SIG-000172': 1, 'duplicate_id:SIG-000171': 1, 'duplicate_id:SIG-000170': 1}`
- `candidate CAND-4C5A29F886D2 entity_id=SIG-000173 reason=duplicate_id:SIG-000173 conf=0.9`
- `candidate CAND-ADA1E00E2285 entity_id=SIG-000174 reason=duplicate_id:SIG-000174 conf=0.92`
- `candidate CAND-429779B7348D entity_id=SIG-000172 reason=duplicate_id:SIG-000172 conf=0.88`
- `candidate CAND-E45245F3DF48 entity_id=SIG-000171 reason=duplicate_id:SIG-000171 conf=0.92`
- `candidate CAND-57961A1BF4DB entity_id=SIG-000170 reason=duplicate_id:SIG-000170 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-4C5A29F886D2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000173 | Rejected |
| CAND-ADA1E00E2285 | business_signal_library | 0.92 | False | duplicate_id:SIG-000174 | Rejected |
| CAND-429779B7348D | business_signal_library | 0.88 | False | duplicate_id:SIG-000172 | Rejected |
| CAND-E45245F3DF48 | business_signal_library | 0.92 | False | duplicate_id:SIG-000171 | Rejected |
| CAND-57961A1BF4DB | business_signal_library | 0.9 | False | duplicate_id:SIG-000170 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000173` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
