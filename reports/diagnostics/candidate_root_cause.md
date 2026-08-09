# Candidate Root Cause

**Generated:** 2026-08-09T23:57:37+00:00
**Session:** `SESSION-20260809-0820F7`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001777`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260809-0820F7`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001777': 1, 'duplicate_id:SIG-001775': 1, 'duplicate_id:SIG-001776': 1, 'duplicate_id:SIG-001779': 1, 'duplicate_id:SIG-001778': 1}`
- `candidate CAND-0785D81B29C6 entity_id=SIG-001777 reason=duplicate_id:SIG-001777 conf=0.88`
- `candidate CAND-502B11A9E985 entity_id=SIG-001775 reason=duplicate_id:SIG-001775 conf=0.9`
- `candidate CAND-277FAC02722C entity_id=SIG-001776 reason=duplicate_id:SIG-001776 conf=0.92`
- `candidate CAND-E1A52A7DA3B6 entity_id=SIG-001779 reason=duplicate_id:SIG-001779 conf=0.92`
- `candidate CAND-15040BB44B21 entity_id=SIG-001778 reason=duplicate_id:SIG-001778 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-0785D81B29C6 | business_signal_library | 0.88 | False | duplicate_id:SIG-001777 | Rejected |
| CAND-502B11A9E985 | business_signal_library | 0.9 | False | duplicate_id:SIG-001775 | Rejected |
| CAND-277FAC02722C | business_signal_library | 0.92 | False | duplicate_id:SIG-001776 | Rejected |
| CAND-E1A52A7DA3B6 | business_signal_library | 0.92 | False | duplicate_id:SIG-001779 | Rejected |
| CAND-15040BB44B21 | business_signal_library | 0.9 | False | duplicate_id:SIG-001778 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001777` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
