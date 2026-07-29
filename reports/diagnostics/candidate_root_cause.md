# Candidate Root Cause

**Generated:** 2026-07-29T15:28:39+00:00
**Session:** `SESSION-20260729-12D631`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001050`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260729-12D631`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001050': 1, 'duplicate_id:SIG-001051': 1, 'duplicate_id:SIG-001052': 1, 'duplicate_id:SIG-001054': 1, 'duplicate_id:SIG-001053': 1}`
- `candidate CAND-AFF5FE1A63BE entity_id=SIG-001050 reason=duplicate_id:SIG-001050 conf=0.9`
- `candidate CAND-EE315573AADC entity_id=SIG-001051 reason=duplicate_id:SIG-001051 conf=0.92`
- `candidate CAND-5F4EACD48AF9 entity_id=SIG-001052 reason=duplicate_id:SIG-001052 conf=0.88`
- `candidate CAND-6ECC9D11D9BD entity_id=SIG-001054 reason=duplicate_id:SIG-001054 conf=0.92`
- `candidate CAND-0804A7964731 entity_id=SIG-001053 reason=duplicate_id:SIG-001053 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-AFF5FE1A63BE | business_signal_library | 0.9 | False | duplicate_id:SIG-001050 | Rejected |
| CAND-EE315573AADC | business_signal_library | 0.92 | False | duplicate_id:SIG-001051 | Rejected |
| CAND-5F4EACD48AF9 | business_signal_library | 0.88 | False | duplicate_id:SIG-001052 | Rejected |
| CAND-6ECC9D11D9BD | business_signal_library | 0.92 | False | duplicate_id:SIG-001054 | Rejected |
| CAND-0804A7964731 | business_signal_library | 0.9 | False | duplicate_id:SIG-001053 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001050` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
