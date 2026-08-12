# Candidate Root Cause

**Generated:** 2026-08-12T15:16:33+00:00
**Session:** `SESSION-20260812-94ED01`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001980`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260812-94ED01`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001980': 1, 'duplicate_id:SIG-001982': 1, 'duplicate_id:SIG-001984': 1, 'duplicate_id:SIG-001981': 1, 'duplicate_id:SIG-001983': 1}`
- `candidate CAND-942AF5908C63 entity_id=SIG-001980 reason=duplicate_id:SIG-001980 conf=0.9`
- `candidate CAND-F177B5BCC2BF entity_id=SIG-001982 reason=duplicate_id:SIG-001982 conf=0.88`
- `candidate CAND-9039943CC53D entity_id=SIG-001984 reason=duplicate_id:SIG-001984 conf=0.92`
- `candidate CAND-AC71D9E4C5C4 entity_id=SIG-001981 reason=duplicate_id:SIG-001981 conf=0.92`
- `candidate CAND-4257AF53C692 entity_id=SIG-001983 reason=duplicate_id:SIG-001983 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-942AF5908C63 | business_signal_library | 0.9 | False | duplicate_id:SIG-001980 | Rejected |
| CAND-F177B5BCC2BF | business_signal_library | 0.88 | False | duplicate_id:SIG-001982 | Rejected |
| CAND-9039943CC53D | business_signal_library | 0.92 | False | duplicate_id:SIG-001984 | Rejected |
| CAND-AC71D9E4C5C4 | business_signal_library | 0.92 | False | duplicate_id:SIG-001981 | Rejected |
| CAND-4257AF53C692 | business_signal_library | 0.9 | False | duplicate_id:SIG-001983 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001980` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
