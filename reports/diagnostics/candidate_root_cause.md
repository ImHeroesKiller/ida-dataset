# Candidate Root Cause

**Generated:** 2026-08-08T07:16:10+00:00
**Session:** `SESSION-20260808-A13386`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001588`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260808-A13386`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001588': 1, 'duplicate_id:SIG-001589': 1, 'duplicate_id:SIG-001586': 1, 'duplicate_id:SIG-001585': 1, 'duplicate_id:SIG-001587': 1}`
- `candidate CAND-38DFA43DA3D2 entity_id=SIG-001588 reason=duplicate_id:SIG-001588 conf=0.9`
- `candidate CAND-C5036684EBBE entity_id=SIG-001589 reason=duplicate_id:SIG-001589 conf=0.92`
- `candidate CAND-1FA0E2A84F6F entity_id=SIG-001586 reason=duplicate_id:SIG-001586 conf=0.92`
- `candidate CAND-1C86A58C2E4B entity_id=SIG-001585 reason=duplicate_id:SIG-001585 conf=0.9`
- `candidate CAND-9608A06A24F7 entity_id=SIG-001587 reason=duplicate_id:SIG-001587 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-38DFA43DA3D2 | business_signal_library | 0.9 | False | duplicate_id:SIG-001588 | Rejected |
| CAND-C5036684EBBE | business_signal_library | 0.92 | False | duplicate_id:SIG-001589 | Rejected |
| CAND-1FA0E2A84F6F | business_signal_library | 0.92 | False | duplicate_id:SIG-001586 | Rejected |
| CAND-1C86A58C2E4B | business_signal_library | 0.9 | False | duplicate_id:SIG-001585 | Rejected |
| CAND-9608A06A24F7 | business_signal_library | 0.88 | False | duplicate_id:SIG-001587 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001588` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
