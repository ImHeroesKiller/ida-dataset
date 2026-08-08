# Candidate Root Cause

**Generated:** 2026-08-08T16:57:59+00:00
**Session:** `SESSION-20260808-AE30CB`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001635`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260808-AE30CB`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001635': 1, 'duplicate_id:SIG-001637': 1, 'duplicate_id:SIG-001636': 1, 'duplicate_id:SIG-001639': 1, 'duplicate_id:SIG-001638': 1}`
- `candidate CAND-C3139FC6A586 entity_id=SIG-001635 reason=duplicate_id:SIG-001635 conf=0.9`
- `candidate CAND-FAFF5F22F25A entity_id=SIG-001637 reason=duplicate_id:SIG-001637 conf=0.88`
- `candidate CAND-46805EE46B79 entity_id=SIG-001636 reason=duplicate_id:SIG-001636 conf=0.92`
- `candidate CAND-93AF67A46DFA entity_id=SIG-001639 reason=duplicate_id:SIG-001639 conf=0.92`
- `candidate CAND-C6B12B5841C5 entity_id=SIG-001638 reason=duplicate_id:SIG-001638 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-C3139FC6A586 | business_signal_library | 0.9 | False | duplicate_id:SIG-001635 | Rejected |
| CAND-FAFF5F22F25A | business_signal_library | 0.88 | False | duplicate_id:SIG-001637 | Rejected |
| CAND-46805EE46B79 | business_signal_library | 0.92 | False | duplicate_id:SIG-001636 | Rejected |
| CAND-93AF67A46DFA | business_signal_library | 0.92 | False | duplicate_id:SIG-001639 | Rejected |
| CAND-C6B12B5841C5 | business_signal_library | 0.9 | False | duplicate_id:SIG-001638 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001635` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
