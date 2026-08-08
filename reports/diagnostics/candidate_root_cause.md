# Candidate Root Cause

**Generated:** 2026-08-08T17:51:53+00:00
**Session:** `SESSION-20260808-DBFB89`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001640`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260808-DBFB89`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001640': 1, 'duplicate_id:SIG-001642': 1, 'duplicate_id:SIG-001643': 1, 'duplicate_id:SIG-001641': 1, 'duplicate_id:SIG-001644': 1}`
- `candidate CAND-5612AC7149E7 entity_id=SIG-001640 reason=duplicate_id:SIG-001640 conf=0.9`
- `candidate CAND-BC6D8BB3F4CF entity_id=SIG-001642 reason=duplicate_id:SIG-001642 conf=0.88`
- `candidate CAND-CFDC56B70A7A entity_id=SIG-001643 reason=duplicate_id:SIG-001643 conf=0.9`
- `candidate CAND-A751D3F2AD33 entity_id=SIG-001641 reason=duplicate_id:SIG-001641 conf=0.92`
- `candidate CAND-A4F50BFF6519 entity_id=SIG-001644 reason=duplicate_id:SIG-001644 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5612AC7149E7 | business_signal_library | 0.9 | False | duplicate_id:SIG-001640 | Rejected |
| CAND-BC6D8BB3F4CF | business_signal_library | 0.88 | False | duplicate_id:SIG-001642 | Rejected |
| CAND-CFDC56B70A7A | business_signal_library | 0.9 | False | duplicate_id:SIG-001643 | Rejected |
| CAND-A751D3F2AD33 | business_signal_library | 0.92 | False | duplicate_id:SIG-001641 | Rejected |
| CAND-A4F50BFF6519 | business_signal_library | 0.92 | False | duplicate_id:SIG-001644 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001640` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
