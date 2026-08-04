# Candidate Root Cause

**Generated:** 2026-08-04T16:32:02+00:00
**Session:** `SESSION-20260804-EB7CC5`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001376`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260804-EB7CC5`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001376': 1, 'duplicate_id:SIG-001378': 1, 'duplicate_id:SIG-001377': 1, 'duplicate_id:SIG-001379': 1, 'duplicate_id:SIG-001375': 1}`
- `candidate CAND-ACF1EBC24A56 entity_id=SIG-001376 reason=duplicate_id:SIG-001376 conf=0.92`
- `candidate CAND-A0CA7591273B entity_id=SIG-001378 reason=duplicate_id:SIG-001378 conf=0.9`
- `candidate CAND-781BE6D1A2F7 entity_id=SIG-001377 reason=duplicate_id:SIG-001377 conf=0.88`
- `candidate CAND-4266184BBD4C entity_id=SIG-001379 reason=duplicate_id:SIG-001379 conf=0.92`
- `candidate CAND-7B1162808D7C entity_id=SIG-001375 reason=duplicate_id:SIG-001375 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-ACF1EBC24A56 | business_signal_library | 0.92 | False | duplicate_id:SIG-001376 | Rejected |
| CAND-A0CA7591273B | business_signal_library | 0.9 | False | duplicate_id:SIG-001378 | Rejected |
| CAND-781BE6D1A2F7 | business_signal_library | 0.88 | False | duplicate_id:SIG-001377 | Rejected |
| CAND-4266184BBD4C | business_signal_library | 0.92 | False | duplicate_id:SIG-001379 | Rejected |
| CAND-7B1162808D7C | business_signal_library | 0.9 | False | duplicate_id:SIG-001375 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001376` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
