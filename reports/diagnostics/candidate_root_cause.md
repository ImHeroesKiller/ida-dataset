# Candidate Root Cause

**Generated:** 2026-08-10T08:10:16+00:00
**Session:** `SESSION-20260810-056AAA`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001796`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260810-056AAA`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001796': 1, 'duplicate_id:SIG-001799': 1, 'duplicate_id:SIG-001798': 1, 'duplicate_id:SIG-001795': 1, 'duplicate_id:SIG-001797': 1}`
- `candidate CAND-1260A3C5AECA entity_id=SIG-001796 reason=duplicate_id:SIG-001796 conf=0.92`
- `candidate CAND-91005F10776E entity_id=SIG-001799 reason=duplicate_id:SIG-001799 conf=0.92`
- `candidate CAND-DB138E51948E entity_id=SIG-001798 reason=duplicate_id:SIG-001798 conf=0.9`
- `candidate CAND-A8A824526BD3 entity_id=SIG-001795 reason=duplicate_id:SIG-001795 conf=0.9`
- `candidate CAND-DCB8E67B7950 entity_id=SIG-001797 reason=duplicate_id:SIG-001797 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-1260A3C5AECA | business_signal_library | 0.92 | False | duplicate_id:SIG-001796 | Rejected |
| CAND-91005F10776E | business_signal_library | 0.92 | False | duplicate_id:SIG-001799 | Rejected |
| CAND-DB138E51948E | business_signal_library | 0.9 | False | duplicate_id:SIG-001798 | Rejected |
| CAND-A8A824526BD3 | business_signal_library | 0.9 | False | duplicate_id:SIG-001795 | Rejected |
| CAND-DCB8E67B7950 | business_signal_library | 0.88 | False | duplicate_id:SIG-001797 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001796` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
