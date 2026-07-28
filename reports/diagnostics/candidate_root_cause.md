# Candidate Root Cause

**Generated:** 2026-07-28T22:24:38+00:00
**Session:** `SESSION-20260728-4DD916`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001016`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260728-4DD916`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001016': 1, 'duplicate_id:SIG-001015': 1, 'duplicate_id:SIG-001017': 1, 'duplicate_id:SIG-001018': 1, 'duplicate_id:SIG-001019': 1}`
- `candidate CAND-FF10C22AC64F entity_id=SIG-001016 reason=duplicate_id:SIG-001016 conf=0.92`
- `candidate CAND-DB2C69FBA1BE entity_id=SIG-001015 reason=duplicate_id:SIG-001015 conf=0.9`
- `candidate CAND-C65CD492EB1B entity_id=SIG-001017 reason=duplicate_id:SIG-001017 conf=0.88`
- `candidate CAND-792B7D46A0A6 entity_id=SIG-001018 reason=duplicate_id:SIG-001018 conf=0.9`
- `candidate CAND-043A2CB73D4A entity_id=SIG-001019 reason=duplicate_id:SIG-001019 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-FF10C22AC64F | business_signal_library | 0.92 | False | duplicate_id:SIG-001016 | Rejected |
| CAND-DB2C69FBA1BE | business_signal_library | 0.9 | False | duplicate_id:SIG-001015 | Rejected |
| CAND-C65CD492EB1B | business_signal_library | 0.88 | False | duplicate_id:SIG-001017 | Rejected |
| CAND-792B7D46A0A6 | business_signal_library | 0.9 | False | duplicate_id:SIG-001018 | Rejected |
| CAND-043A2CB73D4A | business_signal_library | 0.92 | False | duplicate_id:SIG-001019 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001016` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
