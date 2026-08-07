# Candidate Root Cause

**Generated:** 2026-08-07T19:17:29+00:00
**Session:** `SESSION-20260807-0B6E37`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001537`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260807-0B6E37`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001537': 1, 'duplicate_id:SIG-001538': 1, 'duplicate_id:SIG-001536': 1, 'duplicate_id:SIG-001535': 1, 'duplicate_id:SIG-001539': 1}`
- `candidate CAND-07C8313AF6BA entity_id=SIG-001537 reason=duplicate_id:SIG-001537 conf=0.88`
- `candidate CAND-3B98E649FED2 entity_id=SIG-001538 reason=duplicate_id:SIG-001538 conf=0.9`
- `candidate CAND-0C814FA916E3 entity_id=SIG-001536 reason=duplicate_id:SIG-001536 conf=0.92`
- `candidate CAND-9452F7F24512 entity_id=SIG-001535 reason=duplicate_id:SIG-001535 conf=0.9`
- `candidate CAND-97C9897CAC84 entity_id=SIG-001539 reason=duplicate_id:SIG-001539 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-07C8313AF6BA | business_signal_library | 0.88 | False | duplicate_id:SIG-001537 | Rejected |
| CAND-3B98E649FED2 | business_signal_library | 0.9 | False | duplicate_id:SIG-001538 | Rejected |
| CAND-0C814FA916E3 | business_signal_library | 0.92 | False | duplicate_id:SIG-001536 | Rejected |
| CAND-9452F7F24512 | business_signal_library | 0.9 | False | duplicate_id:SIG-001535 | Rejected |
| CAND-97C9897CAC84 | business_signal_library | 0.92 | False | duplicate_id:SIG-001539 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001537` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
