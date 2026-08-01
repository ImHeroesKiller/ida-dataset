# Candidate Root Cause

**Generated:** 2026-08-01T12:23:24+00:00
**Session:** `SESSION-20260801-7A77C1`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001206`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260801-7A77C1`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001206': 1, 'duplicate_id:SIG-001208': 1, 'duplicate_id:SIG-001205': 1, 'duplicate_id:SIG-001209': 1, 'duplicate_id:SIG-001207': 1}`
- `candidate CAND-78EEEC4CEDC2 entity_id=SIG-001206 reason=duplicate_id:SIG-001206 conf=0.92`
- `candidate CAND-63AB1F2E39C3 entity_id=SIG-001208 reason=duplicate_id:SIG-001208 conf=0.9`
- `candidate CAND-0912BE028A2D entity_id=SIG-001205 reason=duplicate_id:SIG-001205 conf=0.9`
- `candidate CAND-3A79545D91E6 entity_id=SIG-001209 reason=duplicate_id:SIG-001209 conf=0.92`
- `candidate CAND-63885CC80000 entity_id=SIG-001207 reason=duplicate_id:SIG-001207 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-78EEEC4CEDC2 | business_signal_library | 0.92 | False | duplicate_id:SIG-001206 | Rejected |
| CAND-63AB1F2E39C3 | business_signal_library | 0.9 | False | duplicate_id:SIG-001208 | Rejected |
| CAND-0912BE028A2D | business_signal_library | 0.9 | False | duplicate_id:SIG-001205 | Rejected |
| CAND-3A79545D91E6 | business_signal_library | 0.92 | False | duplicate_id:SIG-001209 | Rejected |
| CAND-63885CC80000 | business_signal_library | 0.88 | False | duplicate_id:SIG-001207 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001206` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
