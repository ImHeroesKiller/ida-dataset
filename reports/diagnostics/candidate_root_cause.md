# Candidate Root Cause

**Generated:** 2026-08-08T02:02:58+00:00
**Session:** `SESSION-20260808-CF5E2C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001565`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260808-CF5E2C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001565': 1, 'duplicate_id:SIG-001567': 1, 'duplicate_id:SIG-001566': 1, 'duplicate_id:SIG-001569': 1, 'duplicate_id:SIG-001568': 1}`
- `candidate CAND-C0856EA1AA38 entity_id=SIG-001565 reason=duplicate_id:SIG-001565 conf=0.9`
- `candidate CAND-20286180C2DB entity_id=SIG-001567 reason=duplicate_id:SIG-001567 conf=0.88`
- `candidate CAND-FF0771FCE5FA entity_id=SIG-001566 reason=duplicate_id:SIG-001566 conf=0.92`
- `candidate CAND-2473B4929DF7 entity_id=SIG-001569 reason=duplicate_id:SIG-001569 conf=0.92`
- `candidate CAND-5AD54FCCF401 entity_id=SIG-001568 reason=duplicate_id:SIG-001568 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-C0856EA1AA38 | business_signal_library | 0.9 | False | duplicate_id:SIG-001565 | Rejected |
| CAND-20286180C2DB | business_signal_library | 0.88 | False | duplicate_id:SIG-001567 | Rejected |
| CAND-FF0771FCE5FA | business_signal_library | 0.92 | False | duplicate_id:SIG-001566 | Rejected |
| CAND-2473B4929DF7 | business_signal_library | 0.92 | False | duplicate_id:SIG-001569 | Rejected |
| CAND-5AD54FCCF401 | business_signal_library | 0.9 | False | duplicate_id:SIG-001568 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001565` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
