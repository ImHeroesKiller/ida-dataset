# Candidate Root Cause

**Generated:** 2026-08-17T07:12:01+00:00
**Session:** `SESSION-20260817-BE07F8`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000415`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260817-BE07F8`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000415': 1, 'duplicate_id:SIG-000411': 1, 'duplicate_id:SIG-000413': 1, 'duplicate_id:SIG-000412': 1, 'duplicate_id:SIG-000414': 1}`
- `candidate CAND-12DBF1076032 entity_id=SIG-000415 reason=duplicate_id:SIG-000415 conf=0.9`
- `candidate CAND-83351C7A4D95 entity_id=SIG-000411 reason=duplicate_id:SIG-000411 conf=0.92`
- `candidate CAND-7A5FCD8E447D entity_id=SIG-000413 reason=duplicate_id:SIG-000413 conf=0.9`
- `candidate CAND-0480E26BAFBE entity_id=SIG-000412 reason=duplicate_id:SIG-000412 conf=0.9`
- `candidate CAND-B85683BBB53F entity_id=SIG-000414 reason=duplicate_id:SIG-000414 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-12DBF1076032 | business_signal_library | 0.9 | False | duplicate_id:SIG-000415 | Rejected |
| CAND-83351C7A4D95 | business_signal_library | 0.92 | False | duplicate_id:SIG-000411 | Rejected |
| CAND-7A5FCD8E447D | business_signal_library | 0.9 | False | duplicate_id:SIG-000413 | Rejected |
| CAND-0480E26BAFBE | business_signal_library | 0.9 | False | duplicate_id:SIG-000412 | Rejected |
| CAND-B85683BBB53F | business_signal_library | 0.9 | False | duplicate_id:SIG-000414 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000415` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
