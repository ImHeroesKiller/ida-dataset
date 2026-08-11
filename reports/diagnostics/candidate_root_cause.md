# Candidate Root Cause

**Generated:** 2026-08-11T07:28:26+00:00
**Session:** `SESSION-20260811-045573`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001875`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260811-045573`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001875': 1, 'duplicate_id:SIG-001876': 1, 'duplicate_id:SIG-001877': 1, 'duplicate_id:SIG-001879': 1, 'duplicate_id:SIG-001878': 1}`
- `candidate CAND-36A3DD8F70D8 entity_id=SIG-001875 reason=duplicate_id:SIG-001875 conf=0.9`
- `candidate CAND-2BD7FF1BDE53 entity_id=SIG-001876 reason=duplicate_id:SIG-001876 conf=0.92`
- `candidate CAND-2544BB3261BE entity_id=SIG-001877 reason=duplicate_id:SIG-001877 conf=0.88`
- `candidate CAND-B413D439B66E entity_id=SIG-001879 reason=duplicate_id:SIG-001879 conf=0.92`
- `candidate CAND-044BCBB3DC08 entity_id=SIG-001878 reason=duplicate_id:SIG-001878 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-36A3DD8F70D8 | business_signal_library | 0.9 | False | duplicate_id:SIG-001875 | Rejected |
| CAND-2BD7FF1BDE53 | business_signal_library | 0.92 | False | duplicate_id:SIG-001876 | Rejected |
| CAND-2544BB3261BE | business_signal_library | 0.88 | False | duplicate_id:SIG-001877 | Rejected |
| CAND-B413D439B66E | business_signal_library | 0.92 | False | duplicate_id:SIG-001879 | Rejected |
| CAND-044BCBB3DC08 | business_signal_library | 0.9 | False | duplicate_id:SIG-001878 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001875` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
