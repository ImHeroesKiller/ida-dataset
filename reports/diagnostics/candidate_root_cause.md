# Candidate Root Cause

**Generated:** 2026-08-15T12:49:55+00:00
**Session:** `SESSION-20260815-C9B0A2`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000223`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260815-C9B0A2`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000223': 1, 'duplicate_id:SIG-000221': 1, 'duplicate_id:SIG-000225': 1, 'duplicate_id:SIG-000224': 1, 'duplicate_id:SIG-000222': 1}`
- `candidate CAND-1937A4F1CD35 entity_id=SIG-000223 reason=duplicate_id:SIG-000223 conf=0.9`
- `candidate CAND-621D9AE5EC1C entity_id=SIG-000221 reason=duplicate_id:SIG-000221 conf=0.92`
- `candidate CAND-39FE29FCECB4 entity_id=SIG-000225 reason=duplicate_id:SIG-000225 conf=0.9`
- `candidate CAND-9205D849A60B entity_id=SIG-000224 reason=duplicate_id:SIG-000224 conf=0.9`
- `candidate CAND-03DED07FA034 entity_id=SIG-000222 reason=duplicate_id:SIG-000222 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-1937A4F1CD35 | business_signal_library | 0.9 | False | duplicate_id:SIG-000223 | Rejected |
| CAND-621D9AE5EC1C | business_signal_library | 0.92 | False | duplicate_id:SIG-000221 | Rejected |
| CAND-39FE29FCECB4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000225 | Rejected |
| CAND-9205D849A60B | business_signal_library | 0.9 | False | duplicate_id:SIG-000224 | Rejected |
| CAND-03DED07FA034 | business_signal_library | 0.9 | False | duplicate_id:SIG-000222 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000223` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
