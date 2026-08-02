# Candidate Root Cause

**Generated:** 2026-08-02T15:27:12+00:00
**Session:** `SESSION-20260802-F0F0FF`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001272`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260802-F0F0FF`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001272': 1, 'duplicate_id:SIG-001274': 1, 'duplicate_id:SIG-001273': 1, 'duplicate_id:SIG-001271': 1, 'duplicate_id:SIG-001270': 1}`
- `candidate CAND-8F3BDD2BE93D entity_id=SIG-001272 reason=duplicate_id:SIG-001272 conf=0.88`
- `candidate CAND-F12C427BF904 entity_id=SIG-001274 reason=duplicate_id:SIG-001274 conf=0.92`
- `candidate CAND-D36014074F74 entity_id=SIG-001273 reason=duplicate_id:SIG-001273 conf=0.9`
- `candidate CAND-7ECEA7908D1B entity_id=SIG-001271 reason=duplicate_id:SIG-001271 conf=0.92`
- `candidate CAND-BDE93C2C15CC entity_id=SIG-001270 reason=duplicate_id:SIG-001270 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-8F3BDD2BE93D | business_signal_library | 0.88 | False | duplicate_id:SIG-001272 | Rejected |
| CAND-F12C427BF904 | business_signal_library | 0.92 | False | duplicate_id:SIG-001274 | Rejected |
| CAND-D36014074F74 | business_signal_library | 0.9 | False | duplicate_id:SIG-001273 | Rejected |
| CAND-7ECEA7908D1B | business_signal_library | 0.92 | False | duplicate_id:SIG-001271 | Rejected |
| CAND-BDE93C2C15CC | business_signal_library | 0.9 | False | duplicate_id:SIG-001270 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001272` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
