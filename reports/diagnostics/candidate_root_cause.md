# Candidate Root Cause

**Generated:** 2026-08-12T10:26:39+00:00
**Session:** `SESSION-20260812-AEB60B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001968`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260812-AEB60B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001968': 1, 'duplicate_id:SIG-001965': 1, 'duplicate_id:SIG-001969': 1, 'duplicate_id:SIG-001966': 1, 'duplicate_id:SIG-001967': 1}`
- `candidate CAND-14ADACDBEF4E entity_id=SIG-001968 reason=duplicate_id:SIG-001968 conf=0.9`
- `candidate CAND-8E0E1260496F entity_id=SIG-001965 reason=duplicate_id:SIG-001965 conf=0.9`
- `candidate CAND-3FBFC8A1436A entity_id=SIG-001969 reason=duplicate_id:SIG-001969 conf=0.92`
- `candidate CAND-0A041731FC7F entity_id=SIG-001966 reason=duplicate_id:SIG-001966 conf=0.92`
- `candidate CAND-65BDA6FDD09B entity_id=SIG-001967 reason=duplicate_id:SIG-001967 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-14ADACDBEF4E | business_signal_library | 0.9 | False | duplicate_id:SIG-001968 | Rejected |
| CAND-8E0E1260496F | business_signal_library | 0.9 | False | duplicate_id:SIG-001965 | Rejected |
| CAND-3FBFC8A1436A | business_signal_library | 0.92 | False | duplicate_id:SIG-001969 | Rejected |
| CAND-0A041731FC7F | business_signal_library | 0.92 | False | duplicate_id:SIG-001966 | Rejected |
| CAND-65BDA6FDD09B | business_signal_library | 0.88 | False | duplicate_id:SIG-001967 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001968` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
