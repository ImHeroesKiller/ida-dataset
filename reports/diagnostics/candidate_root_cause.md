# Candidate Root Cause

**Generated:** 2026-08-07T18:13:18+00:00
**Session:** `SESSION-20260807-D38828`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001534`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260807-D38828`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001534': 1, 'duplicate_id:SIG-001531': 1, 'duplicate_id:SIG-001533': 1, 'duplicate_id:SIG-001530': 1, 'duplicate_id:SIG-001532': 1}`
- `candidate CAND-E6BA4DA62432 entity_id=SIG-001534 reason=duplicate_id:SIG-001534 conf=0.92`
- `candidate CAND-C36EFAB8501D entity_id=SIG-001531 reason=duplicate_id:SIG-001531 conf=0.92`
- `candidate CAND-351FD6502BD6 entity_id=SIG-001533 reason=duplicate_id:SIG-001533 conf=0.9`
- `candidate CAND-C95D71887F38 entity_id=SIG-001530 reason=duplicate_id:SIG-001530 conf=0.9`
- `candidate CAND-888DB2638967 entity_id=SIG-001532 reason=duplicate_id:SIG-001532 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-E6BA4DA62432 | business_signal_library | 0.92 | False | duplicate_id:SIG-001534 | Rejected |
| CAND-C36EFAB8501D | business_signal_library | 0.92 | False | duplicate_id:SIG-001531 | Rejected |
| CAND-351FD6502BD6 | business_signal_library | 0.9 | False | duplicate_id:SIG-001533 | Rejected |
| CAND-C95D71887F38 | business_signal_library | 0.9 | False | duplicate_id:SIG-001530 | Rejected |
| CAND-888DB2638967 | business_signal_library | 0.88 | False | duplicate_id:SIG-001532 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001534` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
