# Candidate Root Cause

**Generated:** 2026-07-22T23:24:19+00:00
**Session:** `SESSION-20260722-794013`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000709`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260722-794013`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000709': 1, 'duplicate_id:SIG-000706': 1, 'duplicate_id:SIG-000705': 1, 'duplicate_id:SIG-000707': 1, 'duplicate_id:SIG-000708': 1}`
- `candidate CAND-1A47A915A5C5 entity_id=SIG-000709 reason=duplicate_id:SIG-000709 conf=0.92`
- `candidate CAND-F3B12583158E entity_id=SIG-000706 reason=duplicate_id:SIG-000706 conf=0.92`
- `candidate CAND-2CFAB84C6598 entity_id=SIG-000705 reason=duplicate_id:SIG-000705 conf=0.9`
- `candidate CAND-9427D9BA3F8A entity_id=SIG-000707 reason=duplicate_id:SIG-000707 conf=0.88`
- `candidate CAND-2861C2E62087 entity_id=SIG-000708 reason=duplicate_id:SIG-000708 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-1A47A915A5C5 | business_signal_library | 0.92 | False | duplicate_id:SIG-000709 | Rejected |
| CAND-F3B12583158E | business_signal_library | 0.92 | False | duplicate_id:SIG-000706 | Rejected |
| CAND-2CFAB84C6598 | business_signal_library | 0.9 | False | duplicate_id:SIG-000705 | Rejected |
| CAND-9427D9BA3F8A | business_signal_library | 0.88 | False | duplicate_id:SIG-000707 | Rejected |
| CAND-2861C2E62087 | business_signal_library | 0.9 | False | duplicate_id:SIG-000708 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000709` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
