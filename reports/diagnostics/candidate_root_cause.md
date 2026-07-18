# Candidate Root Cause

**Generated:** 2026-07-18T09:45:56+00:00
**Session:** `SESSION-20260718-360CF4`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000425`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260718-360CF4`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000425': 1, 'duplicate_id:SIG-000427': 1, 'duplicate_id:SIG-000428': 1, 'duplicate_id:SIG-000426': 1, 'duplicate_id:SIG-000429': 1}`
- `candidate CAND-05B01C784938 entity_id=SIG-000425 reason=duplicate_id:SIG-000425 conf=0.9`
- `candidate CAND-7F8CC145289F entity_id=SIG-000427 reason=duplicate_id:SIG-000427 conf=0.88`
- `candidate CAND-8A6C4EC0F26F entity_id=SIG-000428 reason=duplicate_id:SIG-000428 conf=0.9`
- `candidate CAND-F5BB9625724B entity_id=SIG-000426 reason=duplicate_id:SIG-000426 conf=0.92`
- `candidate CAND-9EB754886DF5 entity_id=SIG-000429 reason=duplicate_id:SIG-000429 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-05B01C784938 | business_signal_library | 0.9 | False | duplicate_id:SIG-000425 | Rejected |
| CAND-7F8CC145289F | business_signal_library | 0.88 | False | duplicate_id:SIG-000427 | Rejected |
| CAND-8A6C4EC0F26F | business_signal_library | 0.9 | False | duplicate_id:SIG-000428 | Rejected |
| CAND-F5BB9625724B | business_signal_library | 0.92 | False | duplicate_id:SIG-000426 | Rejected |
| CAND-9EB754886DF5 | business_signal_library | 0.92 | False | duplicate_id:SIG-000429 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000425` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
