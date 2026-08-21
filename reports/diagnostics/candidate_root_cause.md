# Candidate Root Cause

**Generated:** 2026-08-21T03:23:00+00:00
**Session:** `SESSION-20260821-C75F25`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000851`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260821-C75F25`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000851': 1, 'duplicate_id:SIG-000853': 1, 'duplicate_id:SIG-000852': 1, 'duplicate_id:SIG-000855': 1, 'duplicate_id:SIG-000854': 1}`
- `candidate CAND-64774DD2A684 entity_id=SIG-000851 reason=duplicate_id:SIG-000851 conf=0.92`
- `candidate CAND-660F0AAAC765 entity_id=SIG-000853 reason=duplicate_id:SIG-000853 conf=0.9`
- `candidate CAND-A47416CD9A9A entity_id=SIG-000852 reason=duplicate_id:SIG-000852 conf=0.9`
- `candidate CAND-E060C7C03824 entity_id=SIG-000855 reason=duplicate_id:SIG-000855 conf=0.9`
- `candidate CAND-A7470D30901A entity_id=SIG-000854 reason=duplicate_id:SIG-000854 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-64774DD2A684 | business_signal_library | 0.92 | False | duplicate_id:SIG-000851 | Rejected |
| CAND-660F0AAAC765 | business_signal_library | 0.9 | False | duplicate_id:SIG-000853 | Rejected |
| CAND-A47416CD9A9A | business_signal_library | 0.9 | False | duplicate_id:SIG-000852 | Rejected |
| CAND-E060C7C03824 | business_signal_library | 0.9 | False | duplicate_id:SIG-000855 | Rejected |
| CAND-A7470D30901A | business_signal_library | 0.9 | False | duplicate_id:SIG-000854 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000851` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
