# Candidate Root Cause

**Generated:** 2026-08-15T14:34:04+00:00
**Session:** `SESSION-20260815-797194`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000231`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260815-797194`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000231': 1, 'duplicate_id:SIG-000233': 1, 'duplicate_id:SIG-000232': 1, 'duplicate_id:SIG-000234': 1, 'duplicate_id:SIG-000235': 1}`
- `candidate CAND-9F48A06A9A9A entity_id=SIG-000231 reason=duplicate_id:SIG-000231 conf=0.92`
- `candidate CAND-36C043D9BA27 entity_id=SIG-000233 reason=duplicate_id:SIG-000233 conf=0.9`
- `candidate CAND-BC6B96355CA2 entity_id=SIG-000232 reason=duplicate_id:SIG-000232 conf=0.9`
- `candidate CAND-C7A327C61215 entity_id=SIG-000234 reason=duplicate_id:SIG-000234 conf=0.9`
- `candidate CAND-49AC909FD045 entity_id=SIG-000235 reason=duplicate_id:SIG-000235 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-9F48A06A9A9A | business_signal_library | 0.92 | False | duplicate_id:SIG-000231 | Rejected |
| CAND-36C043D9BA27 | business_signal_library | 0.9 | False | duplicate_id:SIG-000233 | Rejected |
| CAND-BC6B96355CA2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000232 | Rejected |
| CAND-C7A327C61215 | business_signal_library | 0.9 | False | duplicate_id:SIG-000234 | Rejected |
| CAND-49AC909FD045 | business_signal_library | 0.9 | False | duplicate_id:SIG-000235 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000231` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
