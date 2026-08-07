# Candidate Root Cause

**Generated:** 2026-08-07T21:01:04+00:00
**Session:** `SESSION-20260807-D7A4BA`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001545`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260807-D7A4BA`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001545': 1, 'duplicate_id:SIG-001548': 1, 'duplicate_id:SIG-001546': 1, 'duplicate_id:SIG-001549': 1, 'duplicate_id:SIG-001547': 1}`
- `candidate CAND-0965B1BC78DC entity_id=SIG-001545 reason=duplicate_id:SIG-001545 conf=0.9`
- `candidate CAND-515F969C737D entity_id=SIG-001548 reason=duplicate_id:SIG-001548 conf=0.9`
- `candidate CAND-62F1B995C858 entity_id=SIG-001546 reason=duplicate_id:SIG-001546 conf=0.92`
- `candidate CAND-B92E57CDB3B3 entity_id=SIG-001549 reason=duplicate_id:SIG-001549 conf=0.92`
- `candidate CAND-0BDC5EEA2C5F entity_id=SIG-001547 reason=duplicate_id:SIG-001547 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-0965B1BC78DC | business_signal_library | 0.9 | False | duplicate_id:SIG-001545 | Rejected |
| CAND-515F969C737D | business_signal_library | 0.9 | False | duplicate_id:SIG-001548 | Rejected |
| CAND-62F1B995C858 | business_signal_library | 0.92 | False | duplicate_id:SIG-001546 | Rejected |
| CAND-B92E57CDB3B3 | business_signal_library | 0.92 | False | duplicate_id:SIG-001549 | Rejected |
| CAND-0BDC5EEA2C5F | business_signal_library | 0.88 | False | duplicate_id:SIG-001547 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001545` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
