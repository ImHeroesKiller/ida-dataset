# Candidate Root Cause

**Generated:** 2026-08-15T21:36:11+00:00
**Session:** `SESSION-20260815-CDA41F`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000267`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260815-CDA41F`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000267': 1, 'duplicate_id:SIG-000268': 1, 'duplicate_id:SIG-000266': 1, 'duplicate_id:SIG-000269': 1, 'duplicate_id:SIG-000270': 1}`
- `candidate CAND-3727D4ECBA1C entity_id=SIG-000267 reason=duplicate_id:SIG-000267 conf=0.9`
- `candidate CAND-309E5112CFC6 entity_id=SIG-000268 reason=duplicate_id:SIG-000268 conf=0.9`
- `candidate CAND-442EABC28DCD entity_id=SIG-000266 reason=duplicate_id:SIG-000266 conf=0.92`
- `candidate CAND-EFE1DEAE8BCB entity_id=SIG-000269 reason=duplicate_id:SIG-000269 conf=0.9`
- `candidate CAND-B1A74EE7E6FE entity_id=SIG-000270 reason=duplicate_id:SIG-000270 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-3727D4ECBA1C | business_signal_library | 0.9 | False | duplicate_id:SIG-000267 | Rejected |
| CAND-309E5112CFC6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000268 | Rejected |
| CAND-442EABC28DCD | business_signal_library | 0.92 | False | duplicate_id:SIG-000266 | Rejected |
| CAND-EFE1DEAE8BCB | business_signal_library | 0.9 | False | duplicate_id:SIG-000269 | Rejected |
| CAND-B1A74EE7E6FE | business_signal_library | 0.9 | False | duplicate_id:SIG-000270 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000267` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
