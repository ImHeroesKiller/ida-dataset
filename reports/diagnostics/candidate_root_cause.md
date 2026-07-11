# Candidate Root Cause

**Generated:** 2026-07-11T19:28:15+00:00
**Session:** `SESSION-20260711-FC647C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000050`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260711-FC647C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000050': 1, 'duplicate_id:SIG-000053': 1, 'duplicate_id:SIG-000054': 1, 'duplicate_id:SIG-000052': 1, 'duplicate_id:SIG-000051': 1}`
- `candidate CAND-7E4C68A8B531 entity_id=SIG-000050 reason=duplicate_id:SIG-000050 conf=0.9`
- `candidate CAND-0181BF474DB7 entity_id=SIG-000053 reason=duplicate_id:SIG-000053 conf=0.9`
- `candidate CAND-8720093C05B1 entity_id=SIG-000054 reason=duplicate_id:SIG-000054 conf=0.88`
- `candidate CAND-ECB770469DE9 entity_id=SIG-000052 reason=duplicate_id:SIG-000052 conf=0.92`
- `candidate CAND-F7AF10C9D83E entity_id=SIG-000051 reason=duplicate_id:SIG-000051 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-7E4C68A8B531 | business_signal_library | 0.9 | False | duplicate_id:SIG-000050 | Rejected |
| CAND-0181BF474DB7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000053 | Rejected |
| CAND-8720093C05B1 | business_signal_library | 0.88 | False | duplicate_id:SIG-000054 | Rejected |
| CAND-ECB770469DE9 | business_signal_library | 0.92 | False | duplicate_id:SIG-000052 | Rejected |
| CAND-F7AF10C9D83E | business_signal_library | 0.88 | False | duplicate_id:SIG-000051 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000050` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
