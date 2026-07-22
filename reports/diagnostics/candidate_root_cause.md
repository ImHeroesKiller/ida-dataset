# Candidate Root Cause

**Generated:** 2026-07-22T08:56:24+00:00
**Session:** `SESSION-20260722-E517A7`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000671`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260722-E517A7`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000671': 1, 'duplicate_id:SIG-000672': 1, 'duplicate_id:SIG-000673': 1, 'duplicate_id:SIG-000670': 1, 'duplicate_id:SIG-000674': 1}`
- `candidate CAND-68CEC2B5B171 entity_id=SIG-000671 reason=duplicate_id:SIG-000671 conf=0.92`
- `candidate CAND-50836D1CF523 entity_id=SIG-000672 reason=duplicate_id:SIG-000672 conf=0.88`
- `candidate CAND-79FD77C7E9C2 entity_id=SIG-000673 reason=duplicate_id:SIG-000673 conf=0.9`
- `candidate CAND-01A693A9D5BF entity_id=SIG-000670 reason=duplicate_id:SIG-000670 conf=0.9`
- `candidate CAND-35BBF11CBBBD entity_id=SIG-000674 reason=duplicate_id:SIG-000674 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-68CEC2B5B171 | business_signal_library | 0.92 | False | duplicate_id:SIG-000671 | Rejected |
| CAND-50836D1CF523 | business_signal_library | 0.88 | False | duplicate_id:SIG-000672 | Rejected |
| CAND-79FD77C7E9C2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000673 | Rejected |
| CAND-01A693A9D5BF | business_signal_library | 0.9 | False | duplicate_id:SIG-000670 | Rejected |
| CAND-35BBF11CBBBD | business_signal_library | 0.92 | False | duplicate_id:SIG-000674 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000671` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
