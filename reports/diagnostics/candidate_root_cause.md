# Candidate Root Cause

**Generated:** 2026-08-24T09:09:16+00:00
**Session:** `SESSION-20260824-FDD28B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001206`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260824-FDD28B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001206': 1, 'duplicate_id:SIG-001207': 1, 'duplicate_id:SIG-001208': 1, 'duplicate_id:SIG-001209': 1, 'duplicate_id:SIG-001210': 1}`
- `candidate CAND-3B33411FA32A entity_id=SIG-001206 reason=duplicate_id:SIG-001206 conf=0.92`
- `candidate CAND-8888E4A314E2 entity_id=SIG-001207 reason=duplicate_id:SIG-001207 conf=0.9`
- `candidate CAND-1D87457F54B2 entity_id=SIG-001208 reason=duplicate_id:SIG-001208 conf=0.9`
- `candidate CAND-552FFA8479E2 entity_id=SIG-001209 reason=duplicate_id:SIG-001209 conf=0.9`
- `candidate CAND-DC9DF2427CC7 entity_id=SIG-001210 reason=duplicate_id:SIG-001210 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-3B33411FA32A | business_signal_library | 0.92 | False | duplicate_id:SIG-001206 | Rejected |
| CAND-8888E4A314E2 | business_signal_library | 0.9 | False | duplicate_id:SIG-001207 | Rejected |
| CAND-1D87457F54B2 | business_signal_library | 0.9 | False | duplicate_id:SIG-001208 | Rejected |
| CAND-552FFA8479E2 | business_signal_library | 0.9 | False | duplicate_id:SIG-001209 | Rejected |
| CAND-DC9DF2427CC7 | business_signal_library | 0.9 | False | duplicate_id:SIG-001210 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001206` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
