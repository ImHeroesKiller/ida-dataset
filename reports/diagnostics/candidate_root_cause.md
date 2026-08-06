# Candidate Root Cause

**Generated:** 2026-08-06T14:34:33+00:00
**Session:** `SESSION-20260806-4C324B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001470`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260806-4C324B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001470': 1, 'duplicate_id:SIG-001473': 1, 'duplicate_id:SIG-001472': 1, 'duplicate_id:SIG-001471': 1, 'duplicate_id:SIG-001474': 1}`
- `candidate CAND-28BDC862B752 entity_id=SIG-001470 reason=duplicate_id:SIG-001470 conf=0.9`
- `candidate CAND-A5698800C1C2 entity_id=SIG-001473 reason=duplicate_id:SIG-001473 conf=0.9`
- `candidate CAND-859F81929DBF entity_id=SIG-001472 reason=duplicate_id:SIG-001472 conf=0.88`
- `candidate CAND-97FD626B2091 entity_id=SIG-001471 reason=duplicate_id:SIG-001471 conf=0.92`
- `candidate CAND-11E37F7287A0 entity_id=SIG-001474 reason=duplicate_id:SIG-001474 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-28BDC862B752 | business_signal_library | 0.9 | False | duplicate_id:SIG-001470 | Rejected |
| CAND-A5698800C1C2 | business_signal_library | 0.9 | False | duplicate_id:SIG-001473 | Rejected |
| CAND-859F81929DBF | business_signal_library | 0.88 | False | duplicate_id:SIG-001472 | Rejected |
| CAND-97FD626B2091 | business_signal_library | 0.92 | False | duplicate_id:SIG-001471 | Rejected |
| CAND-11E37F7287A0 | business_signal_library | 0.92 | False | duplicate_id:SIG-001474 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001470` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
