# Candidate Root Cause

**Generated:** 2026-08-10T16:24:53+00:00
**Session:** `SESSION-20260810-018F65`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001823`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260810-018F65`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001823': 1, 'duplicate_id:SIG-001820': 1, 'duplicate_id:SIG-001821': 1, 'duplicate_id:SIG-001822': 1, 'duplicate_id:SIG-001824': 1}`
- `candidate CAND-421847671B12 entity_id=SIG-001823 reason=duplicate_id:SIG-001823 conf=0.9`
- `candidate CAND-B5852C64D250 entity_id=SIG-001820 reason=duplicate_id:SIG-001820 conf=0.9`
- `candidate CAND-406F88C2B05D entity_id=SIG-001821 reason=duplicate_id:SIG-001821 conf=0.92`
- `candidate CAND-8323A5054E46 entity_id=SIG-001822 reason=duplicate_id:SIG-001822 conf=0.88`
- `candidate CAND-4B708523A40D entity_id=SIG-001824 reason=duplicate_id:SIG-001824 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-421847671B12 | business_signal_library | 0.9 | False | duplicate_id:SIG-001823 | Rejected |
| CAND-B5852C64D250 | business_signal_library | 0.9 | False | duplicate_id:SIG-001820 | Rejected |
| CAND-406F88C2B05D | business_signal_library | 0.92 | False | duplicate_id:SIG-001821 | Rejected |
| CAND-8323A5054E46 | business_signal_library | 0.88 | False | duplicate_id:SIG-001822 | Rejected |
| CAND-4B708523A40D | business_signal_library | 0.92 | False | duplicate_id:SIG-001824 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001823` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
