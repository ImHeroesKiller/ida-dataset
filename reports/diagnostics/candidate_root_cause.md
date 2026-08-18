# Candidate Root Cause

**Generated:** 2026-08-18T21:37:19+00:00
**Session:** `SESSION-20260818-C2B42F`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000603`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260818-C2B42F`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000603': 1, 'duplicate_id:SIG-000605': 1, 'duplicate_id:SIG-000601': 1, 'duplicate_id:SIG-000604': 1, 'duplicate_id:SIG-000602': 1}`
- `candidate CAND-037D8311BD72 entity_id=SIG-000603 reason=duplicate_id:SIG-000603 conf=0.9`
- `candidate CAND-5702BF5B1F66 entity_id=SIG-000605 reason=duplicate_id:SIG-000605 conf=0.9`
- `candidate CAND-8B94C328F325 entity_id=SIG-000601 reason=duplicate_id:SIG-000601 conf=0.92`
- `candidate CAND-BC194D4EDF3D entity_id=SIG-000604 reason=duplicate_id:SIG-000604 conf=0.9`
- `candidate CAND-47EF36AEF8EB entity_id=SIG-000602 reason=duplicate_id:SIG-000602 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-037D8311BD72 | business_signal_library | 0.9 | False | duplicate_id:SIG-000603 | Rejected |
| CAND-5702BF5B1F66 | business_signal_library | 0.9 | False | duplicate_id:SIG-000605 | Rejected |
| CAND-8B94C328F325 | business_signal_library | 0.92 | False | duplicate_id:SIG-000601 | Rejected |
| CAND-BC194D4EDF3D | business_signal_library | 0.9 | False | duplicate_id:SIG-000604 | Rejected |
| CAND-47EF36AEF8EB | business_signal_library | 0.9 | False | duplicate_id:SIG-000602 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000603` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
