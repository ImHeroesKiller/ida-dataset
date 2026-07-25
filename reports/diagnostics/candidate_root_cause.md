# Candidate Root Cause

**Generated:** 2026-07-25T22:22:27+00:00
**Session:** `SESSION-20260725-288E3B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000867`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260725-288E3B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000867': 1, 'duplicate_id:SIG-000868': 1, 'duplicate_id:SIG-000865': 1, 'duplicate_id:SIG-000866': 1, 'duplicate_id:SIG-000869': 1}`
- `candidate CAND-A2412F3819FF entity_id=SIG-000867 reason=duplicate_id:SIG-000867 conf=0.88`
- `candidate CAND-3C9C4E1065B7 entity_id=SIG-000868 reason=duplicate_id:SIG-000868 conf=0.9`
- `candidate CAND-3B61574EA4B2 entity_id=SIG-000865 reason=duplicate_id:SIG-000865 conf=0.9`
- `candidate CAND-A420880A8B10 entity_id=SIG-000866 reason=duplicate_id:SIG-000866 conf=0.92`
- `candidate CAND-0B62FBAE1CCF entity_id=SIG-000869 reason=duplicate_id:SIG-000869 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A2412F3819FF | business_signal_library | 0.88 | False | duplicate_id:SIG-000867 | Rejected |
| CAND-3C9C4E1065B7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000868 | Rejected |
| CAND-3B61574EA4B2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000865 | Rejected |
| CAND-A420880A8B10 | business_signal_library | 0.92 | False | duplicate_id:SIG-000866 | Rejected |
| CAND-0B62FBAE1CCF | business_signal_library | 0.92 | False | duplicate_id:SIG-000869 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000867` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
