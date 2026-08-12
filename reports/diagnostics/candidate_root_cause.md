# Candidate Root Cause

**Generated:** 2026-08-12T00:00:05+00:00
**Session:** `SESSION-20260811-5557E2`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001935`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260811-5557E2`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001935': 1, 'duplicate_id:SIG-001938': 1, 'duplicate_id:SIG-001936': 1, 'duplicate_id:SIG-001937': 1, 'duplicate_id:SIG-001939': 1}`
- `candidate CAND-0CFD95D10B93 entity_id=SIG-001935 reason=duplicate_id:SIG-001935 conf=0.9`
- `candidate CAND-872D6CB636CA entity_id=SIG-001938 reason=duplicate_id:SIG-001938 conf=0.9`
- `candidate CAND-D2933E31C158 entity_id=SIG-001936 reason=duplicate_id:SIG-001936 conf=0.92`
- `candidate CAND-2DF7CD810AA2 entity_id=SIG-001937 reason=duplicate_id:SIG-001937 conf=0.88`
- `candidate CAND-4DF052ED00B7 entity_id=SIG-001939 reason=duplicate_id:SIG-001939 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-0CFD95D10B93 | business_signal_library | 0.9 | False | duplicate_id:SIG-001935 | Rejected |
| CAND-872D6CB636CA | business_signal_library | 0.9 | False | duplicate_id:SIG-001938 | Rejected |
| CAND-D2933E31C158 | business_signal_library | 0.92 | False | duplicate_id:SIG-001936 | Rejected |
| CAND-2DF7CD810AA2 | business_signal_library | 0.88 | False | duplicate_id:SIG-001937 | Rejected |
| CAND-4DF052ED00B7 | business_signal_library | 0.92 | False | duplicate_id:SIG-001939 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001935` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
