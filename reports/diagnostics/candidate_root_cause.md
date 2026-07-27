# Candidate Root Cause

**Generated:** 2026-07-27T00:22:08+00:00
**Session:** `SESSION-20260727-EEF872`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000931`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260727-EEF872`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000931': 1, 'duplicate_id:SIG-000932': 1, 'duplicate_id:SIG-000933': 1, 'duplicate_id:SIG-000930': 1, 'duplicate_id:SIG-000934': 1}`
- `candidate CAND-38F095C313C7 entity_id=SIG-000931 reason=duplicate_id:SIG-000931 conf=0.92`
- `candidate CAND-F50DA935EA41 entity_id=SIG-000932 reason=duplicate_id:SIG-000932 conf=0.88`
- `candidate CAND-8EA5657E124C entity_id=SIG-000933 reason=duplicate_id:SIG-000933 conf=0.9`
- `candidate CAND-B500438B544C entity_id=SIG-000930 reason=duplicate_id:SIG-000930 conf=0.9`
- `candidate CAND-B053BDE6A0CB entity_id=SIG-000934 reason=duplicate_id:SIG-000934 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-38F095C313C7 | business_signal_library | 0.92 | False | duplicate_id:SIG-000931 | Rejected |
| CAND-F50DA935EA41 | business_signal_library | 0.88 | False | duplicate_id:SIG-000932 | Rejected |
| CAND-8EA5657E124C | business_signal_library | 0.9 | False | duplicate_id:SIG-000933 | Rejected |
| CAND-B500438B544C | business_signal_library | 0.9 | False | duplicate_id:SIG-000930 | Rejected |
| CAND-B053BDE6A0CB | business_signal_library | 0.92 | False | duplicate_id:SIG-000934 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000931` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
