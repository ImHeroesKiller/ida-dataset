# Candidate Root Cause

**Generated:** 2026-08-10T09:41:12+00:00
**Session:** `SESSION-20260810-0E6F20`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001804`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260810-0E6F20`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001804': 1, 'duplicate_id:SIG-001800': 1, 'duplicate_id:SIG-001802': 1, 'duplicate_id:SIG-001803': 1, 'duplicate_id:SIG-001801': 1}`
- `candidate CAND-51A4B5BD7D49 entity_id=SIG-001804 reason=duplicate_id:SIG-001804 conf=0.9`
- `candidate CAND-28370DA4E7D9 entity_id=SIG-001800 reason=duplicate_id:SIG-001800 conf=0.9`
- `candidate CAND-30D1529C5A60 entity_id=SIG-001802 reason=duplicate_id:SIG-001802 conf=0.9`
- `candidate CAND-4B3AD44A5CD2 entity_id=SIG-001803 reason=duplicate_id:SIG-001803 conf=0.92`
- `candidate CAND-EC6CCFE41188 entity_id=SIG-001801 reason=duplicate_id:SIG-001801 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-51A4B5BD7D49 | business_signal_library | 0.9 | False | duplicate_id:SIG-001804 | Rejected |
| CAND-28370DA4E7D9 | business_signal_library | 0.9 | False | duplicate_id:SIG-001800 | Rejected |
| CAND-30D1529C5A60 | business_signal_library | 0.9 | False | duplicate_id:SIG-001802 | Rejected |
| CAND-4B3AD44A5CD2 | business_signal_library | 0.92 | False | duplicate_id:SIG-001803 | Rejected |
| CAND-EC6CCFE41188 | business_signal_library | 0.92 | False | duplicate_id:SIG-001801 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001804` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
