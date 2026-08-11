# Candidate Root Cause

**Generated:** 2026-08-11T15:18:01+00:00
**Session:** `SESSION-20260811-954EB1`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001903`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260811-954EB1`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001903': 1, 'duplicate_id:SIG-001900': 1, 'duplicate_id:SIG-001904': 1, 'duplicate_id:SIG-001901': 1, 'duplicate_id:SIG-001902': 1}`
- `candidate CAND-525FBC021873 entity_id=SIG-001903 reason=duplicate_id:SIG-001903 conf=0.9`
- `candidate CAND-8504CCF5EBB7 entity_id=SIG-001900 reason=duplicate_id:SIG-001900 conf=0.9`
- `candidate CAND-DBA29C2D8332 entity_id=SIG-001904 reason=duplicate_id:SIG-001904 conf=0.92`
- `candidate CAND-E8D156AF3549 entity_id=SIG-001901 reason=duplicate_id:SIG-001901 conf=0.92`
- `candidate CAND-447F7E4B6417 entity_id=SIG-001902 reason=duplicate_id:SIG-001902 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-525FBC021873 | business_signal_library | 0.9 | False | duplicate_id:SIG-001903 | Rejected |
| CAND-8504CCF5EBB7 | business_signal_library | 0.9 | False | duplicate_id:SIG-001900 | Rejected |
| CAND-DBA29C2D8332 | business_signal_library | 0.92 | False | duplicate_id:SIG-001904 | Rejected |
| CAND-E8D156AF3549 | business_signal_library | 0.92 | False | duplicate_id:SIG-001901 | Rejected |
| CAND-447F7E4B6417 | business_signal_library | 0.88 | False | duplicate_id:SIG-001902 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001903` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
