# Candidate Root Cause

**Generated:** 2026-07-31T09:29:16+00:00
**Session:** `SESSION-20260731-455268`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001146`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260731-455268`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001146': 1, 'duplicate_id:SIG-001149': 1, 'duplicate_id:SIG-001148': 1, 'duplicate_id:SIG-001145': 1, 'duplicate_id:SIG-001147': 1}`
- `candidate CAND-F018F5075066 entity_id=SIG-001146 reason=duplicate_id:SIG-001146 conf=0.92`
- `candidate CAND-A9AD7E375327 entity_id=SIG-001149 reason=duplicate_id:SIG-001149 conf=0.92`
- `candidate CAND-80F6C2C61791 entity_id=SIG-001148 reason=duplicate_id:SIG-001148 conf=0.9`
- `candidate CAND-47A705C38662 entity_id=SIG-001145 reason=duplicate_id:SIG-001145 conf=0.9`
- `candidate CAND-0CE65281BF0F entity_id=SIG-001147 reason=duplicate_id:SIG-001147 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F018F5075066 | business_signal_library | 0.92 | False | duplicate_id:SIG-001146 | Rejected |
| CAND-A9AD7E375327 | business_signal_library | 0.92 | False | duplicate_id:SIG-001149 | Rejected |
| CAND-80F6C2C61791 | business_signal_library | 0.9 | False | duplicate_id:SIG-001148 | Rejected |
| CAND-47A705C38662 | business_signal_library | 0.9 | False | duplicate_id:SIG-001145 | Rejected |
| CAND-0CE65281BF0F | business_signal_library | 0.88 | False | duplicate_id:SIG-001147 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001146` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
