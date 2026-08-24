# Candidate Root Cause

**Generated:** 2026-08-24T01:41:07+00:00
**Session:** `SESSION-20260824-4009EA`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001183`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260824-4009EA`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001183': 1, 'duplicate_id:SIG-001181': 1, 'duplicate_id:SIG-001182': 1, 'duplicate_id:SIG-001185': 1, 'duplicate_id:SIG-001184': 1}`
- `candidate CAND-B1D739FEB031 entity_id=SIG-001183 reason=duplicate_id:SIG-001183 conf=0.9`
- `candidate CAND-80F181545CBB entity_id=SIG-001181 reason=duplicate_id:SIG-001181 conf=0.92`
- `candidate CAND-D5E3CC745B71 entity_id=SIG-001182 reason=duplicate_id:SIG-001182 conf=0.9`
- `candidate CAND-B09F29A42F02 entity_id=SIG-001185 reason=duplicate_id:SIG-001185 conf=0.9`
- `candidate CAND-0F165FBDC512 entity_id=SIG-001184 reason=duplicate_id:SIG-001184 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B1D739FEB031 | business_signal_library | 0.9 | False | duplicate_id:SIG-001183 | Rejected |
| CAND-80F181545CBB | business_signal_library | 0.92 | False | duplicate_id:SIG-001181 | Rejected |
| CAND-D5E3CC745B71 | business_signal_library | 0.9 | False | duplicate_id:SIG-001182 | Rejected |
| CAND-B09F29A42F02 | business_signal_library | 0.9 | False | duplicate_id:SIG-001185 | Rejected |
| CAND-0F165FBDC512 | business_signal_library | 0.9 | False | duplicate_id:SIG-001184 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001183` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
