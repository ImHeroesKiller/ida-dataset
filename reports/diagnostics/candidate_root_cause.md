# Candidate Root Cause

**Generated:** 2026-08-05T15:35:32+00:00
**Session:** `SESSION-20260805-D90EDD`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001428`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260805-D90EDD`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001428': 1, 'duplicate_id:SIG-001427': 1, 'duplicate_id:SIG-001429': 1, 'duplicate_id:SIG-001425': 1, 'duplicate_id:SIG-001426': 1}`
- `candidate CAND-E741DA3D1603 entity_id=SIG-001428 reason=duplicate_id:SIG-001428 conf=0.9`
- `candidate CAND-0B93F409FC8A entity_id=SIG-001427 reason=duplicate_id:SIG-001427 conf=0.88`
- `candidate CAND-AB1746D81743 entity_id=SIG-001429 reason=duplicate_id:SIG-001429 conf=0.92`
- `candidate CAND-B6A629091568 entity_id=SIG-001425 reason=duplicate_id:SIG-001425 conf=0.9`
- `candidate CAND-0E4DD85F612E entity_id=SIG-001426 reason=duplicate_id:SIG-001426 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-E741DA3D1603 | business_signal_library | 0.9 | False | duplicate_id:SIG-001428 | Rejected |
| CAND-0B93F409FC8A | business_signal_library | 0.88 | False | duplicate_id:SIG-001427 | Rejected |
| CAND-AB1746D81743 | business_signal_library | 0.92 | False | duplicate_id:SIG-001429 | Rejected |
| CAND-B6A629091568 | business_signal_library | 0.9 | False | duplicate_id:SIG-001425 | Rejected |
| CAND-0E4DD85F612E | business_signal_library | 0.92 | False | duplicate_id:SIG-001426 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001428` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
