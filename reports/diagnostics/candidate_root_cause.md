# Candidate Root Cause

**Generated:** 2026-08-10T22:00:50+00:00
**Session:** `SESSION-20260810-51E645`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001845`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260810-51E645`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001845': 1, 'duplicate_id:SIG-001846': 1, 'duplicate_id:SIG-001847': 1, 'duplicate_id:SIG-001848': 1, 'duplicate_id:SIG-001849': 1}`
- `candidate CAND-09CB58B58741 entity_id=SIG-001845 reason=duplicate_id:SIG-001845 conf=0.9`
- `candidate CAND-4D34DE641B60 entity_id=SIG-001846 reason=duplicate_id:SIG-001846 conf=0.92`
- `candidate CAND-FC8CDE885114 entity_id=SIG-001847 reason=duplicate_id:SIG-001847 conf=0.88`
- `candidate CAND-767358187235 entity_id=SIG-001848 reason=duplicate_id:SIG-001848 conf=0.9`
- `candidate CAND-28ADD7CCDD82 entity_id=SIG-001849 reason=duplicate_id:SIG-001849 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-09CB58B58741 | business_signal_library | 0.9 | False | duplicate_id:SIG-001845 | Rejected |
| CAND-4D34DE641B60 | business_signal_library | 0.92 | False | duplicate_id:SIG-001846 | Rejected |
| CAND-FC8CDE885114 | business_signal_library | 0.88 | False | duplicate_id:SIG-001847 | Rejected |
| CAND-767358187235 | business_signal_library | 0.9 | False | duplicate_id:SIG-001848 | Rejected |
| CAND-28ADD7CCDD82 | business_signal_library | 0.92 | False | duplicate_id:SIG-001849 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001845` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
