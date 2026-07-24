# Candidate Root Cause

**Generated:** 2026-07-24T15:15:23+00:00
**Session:** `SESSION-20260724-43A649`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000785`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260724-43A649`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000785': 1, 'duplicate_id:SIG-000788': 1, 'duplicate_id:SIG-000786': 1, 'duplicate_id:SIG-000787': 1, 'duplicate_id:SIG-000789': 1}`
- `candidate CAND-BEED05AE271D entity_id=SIG-000785 reason=duplicate_id:SIG-000785 conf=0.9`
- `candidate CAND-66EEE04B8710 entity_id=SIG-000788 reason=duplicate_id:SIG-000788 conf=0.9`
- `candidate CAND-6F238F01EBD2 entity_id=SIG-000786 reason=duplicate_id:SIG-000786 conf=0.92`
- `candidate CAND-DBF4E7752C4E entity_id=SIG-000787 reason=duplicate_id:SIG-000787 conf=0.88`
- `candidate CAND-2942B7F544C9 entity_id=SIG-000789 reason=duplicate_id:SIG-000789 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-BEED05AE271D | business_signal_library | 0.9 | False | duplicate_id:SIG-000785 | Rejected |
| CAND-66EEE04B8710 | business_signal_library | 0.9 | False | duplicate_id:SIG-000788 | Rejected |
| CAND-6F238F01EBD2 | business_signal_library | 0.92 | False | duplicate_id:SIG-000786 | Rejected |
| CAND-DBF4E7752C4E | business_signal_library | 0.88 | False | duplicate_id:SIG-000787 | Rejected |
| CAND-2942B7F544C9 | business_signal_library | 0.92 | False | duplicate_id:SIG-000789 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000785` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
