# Candidate Root Cause

**Generated:** 2026-08-08T14:05:41+00:00
**Session:** `SESSION-20260808-2AA92B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001623`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260808-2AA92B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001623': 1, 'duplicate_id:SIG-001620': 1, 'duplicate_id:SIG-001622': 1, 'duplicate_id:SIG-001624': 1, 'duplicate_id:SIG-001621': 1}`
- `candidate CAND-FD728A46E082 entity_id=SIG-001623 reason=duplicate_id:SIG-001623 conf=0.9`
- `candidate CAND-3508F88556C2 entity_id=SIG-001620 reason=duplicate_id:SIG-001620 conf=0.9`
- `candidate CAND-9DDB5EC95294 entity_id=SIG-001622 reason=duplicate_id:SIG-001622 conf=0.88`
- `candidate CAND-2BC12BA4B61B entity_id=SIG-001624 reason=duplicate_id:SIG-001624 conf=0.92`
- `candidate CAND-1712B7B8C8B5 entity_id=SIG-001621 reason=duplicate_id:SIG-001621 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-FD728A46E082 | business_signal_library | 0.9 | False | duplicate_id:SIG-001623 | Rejected |
| CAND-3508F88556C2 | business_signal_library | 0.9 | False | duplicate_id:SIG-001620 | Rejected |
| CAND-9DDB5EC95294 | business_signal_library | 0.88 | False | duplicate_id:SIG-001622 | Rejected |
| CAND-2BC12BA4B61B | business_signal_library | 0.92 | False | duplicate_id:SIG-001624 | Rejected |
| CAND-1712B7B8C8B5 | business_signal_library | 0.92 | False | duplicate_id:SIG-001621 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001623` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
