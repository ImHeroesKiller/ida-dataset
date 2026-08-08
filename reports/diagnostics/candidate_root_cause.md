# Candidate Root Cause

**Generated:** 2026-08-08T22:54:46+00:00
**Session:** `SESSION-20260808-0069F9`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001669`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260808-0069F9`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001669': 1, 'duplicate_id:SIG-001665': 1, 'duplicate_id:SIG-001666': 1, 'duplicate_id:SIG-001667': 1, 'duplicate_id:SIG-001668': 1}`
- `candidate CAND-D3A7B221B35F entity_id=SIG-001669 reason=duplicate_id:SIG-001669 conf=0.92`
- `candidate CAND-9210EA72952F entity_id=SIG-001665 reason=duplicate_id:SIG-001665 conf=0.9`
- `candidate CAND-61185805DAE7 entity_id=SIG-001666 reason=duplicate_id:SIG-001666 conf=0.92`
- `candidate CAND-C0BD04AFA234 entity_id=SIG-001667 reason=duplicate_id:SIG-001667 conf=0.88`
- `candidate CAND-88AC4F6EFDEC entity_id=SIG-001668 reason=duplicate_id:SIG-001668 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-D3A7B221B35F | business_signal_library | 0.92 | False | duplicate_id:SIG-001669 | Rejected |
| CAND-9210EA72952F | business_signal_library | 0.9 | False | duplicate_id:SIG-001665 | Rejected |
| CAND-61185805DAE7 | business_signal_library | 0.92 | False | duplicate_id:SIG-001666 | Rejected |
| CAND-C0BD04AFA234 | business_signal_library | 0.88 | False | duplicate_id:SIG-001667 | Rejected |
| CAND-88AC4F6EFDEC | business_signal_library | 0.9 | False | duplicate_id:SIG-001668 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001669` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
