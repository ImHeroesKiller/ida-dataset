# Candidate Root Cause

**Generated:** 2026-07-16T06:39:12+00:00
**Session:** `SESSION-20260716-C2751A`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000297`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260716-C2751A`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000297': 1, 'duplicate_id:SIG-000299': 1, 'duplicate_id:SIG-000296': 1, 'duplicate_id:SIG-000298': 1, 'duplicate_id:SIG-000295': 1}`
- `candidate CAND-F14F3D2E38D5 entity_id=SIG-000297 reason=duplicate_id:SIG-000297 conf=0.88`
- `candidate CAND-DD38BC5C1A47 entity_id=SIG-000299 reason=duplicate_id:SIG-000299 conf=0.92`
- `candidate CAND-105D33F3B5D9 entity_id=SIG-000296 reason=duplicate_id:SIG-000296 conf=0.92`
- `candidate CAND-66E64CF02399 entity_id=SIG-000298 reason=duplicate_id:SIG-000298 conf=0.9`
- `candidate CAND-0A5AE35D151F entity_id=SIG-000295 reason=duplicate_id:SIG-000295 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F14F3D2E38D5 | business_signal_library | 0.88 | False | duplicate_id:SIG-000297 | Rejected |
| CAND-DD38BC5C1A47 | business_signal_library | 0.92 | False | duplicate_id:SIG-000299 | Rejected |
| CAND-105D33F3B5D9 | business_signal_library | 0.92 | False | duplicate_id:SIG-000296 | Rejected |
| CAND-66E64CF02399 | business_signal_library | 0.9 | False | duplicate_id:SIG-000298 | Rejected |
| CAND-0A5AE35D151F | business_signal_library | 0.9 | False | duplicate_id:SIG-000295 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000297` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
