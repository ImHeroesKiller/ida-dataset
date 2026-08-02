# Candidate Root Cause

**Generated:** 2026-08-02T23:21:15+00:00
**Session:** `SESSION-20260802-65E0DF`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001298`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260802-65E0DF`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001298': 1, 'duplicate_id:SIG-001299': 1, 'duplicate_id:SIG-001295': 1, 'duplicate_id:SIG-001297': 1, 'duplicate_id:SIG-001296': 1}`
- `candidate CAND-8CF56A7589E4 entity_id=SIG-001298 reason=duplicate_id:SIG-001298 conf=0.9`
- `candidate CAND-E5B71F27EBAD entity_id=SIG-001299 reason=duplicate_id:SIG-001299 conf=0.92`
- `candidate CAND-38BA6F5C9251 entity_id=SIG-001295 reason=duplicate_id:SIG-001295 conf=0.9`
- `candidate CAND-4CEF5AE2E1C9 entity_id=SIG-001297 reason=duplicate_id:SIG-001297 conf=0.88`
- `candidate CAND-957970D8F994 entity_id=SIG-001296 reason=duplicate_id:SIG-001296 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-8CF56A7589E4 | business_signal_library | 0.9 | False | duplicate_id:SIG-001298 | Rejected |
| CAND-E5B71F27EBAD | business_signal_library | 0.92 | False | duplicate_id:SIG-001299 | Rejected |
| CAND-38BA6F5C9251 | business_signal_library | 0.9 | False | duplicate_id:SIG-001295 | Rejected |
| CAND-4CEF5AE2E1C9 | business_signal_library | 0.88 | False | duplicate_id:SIG-001297 | Rejected |
| CAND-957970D8F994 | business_signal_library | 0.92 | False | duplicate_id:SIG-001296 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001298` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
