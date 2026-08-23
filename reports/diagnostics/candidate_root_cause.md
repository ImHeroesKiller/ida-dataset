# Candidate Root Cause

**Generated:** 2026-08-23T13:51:52+00:00
**Session:** `SESSION-20260823-474C92`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001130`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260823-474C92`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001130': 1, 'duplicate_id:SIG-001129': 1, 'duplicate_id:SIG-001127': 1, 'duplicate_id:SIG-001128': 1, 'duplicate_id:SIG-001126': 1}`
- `candidate CAND-693523700C2B entity_id=SIG-001130 reason=duplicate_id:SIG-001130 conf=0.9`
- `candidate CAND-D326170FA884 entity_id=SIG-001129 reason=duplicate_id:SIG-001129 conf=0.9`
- `candidate CAND-7A3E14917D24 entity_id=SIG-001127 reason=duplicate_id:SIG-001127 conf=0.9`
- `candidate CAND-48E885258442 entity_id=SIG-001128 reason=duplicate_id:SIG-001128 conf=0.9`
- `candidate CAND-1B76D8313E52 entity_id=SIG-001126 reason=duplicate_id:SIG-001126 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-693523700C2B | business_signal_library | 0.9 | False | duplicate_id:SIG-001130 | Rejected |
| CAND-D326170FA884 | business_signal_library | 0.9 | False | duplicate_id:SIG-001129 | Rejected |
| CAND-7A3E14917D24 | business_signal_library | 0.9 | False | duplicate_id:SIG-001127 | Rejected |
| CAND-48E885258442 | business_signal_library | 0.9 | False | duplicate_id:SIG-001128 | Rejected |
| CAND-1B76D8313E52 | business_signal_library | 0.92 | False | duplicate_id:SIG-001126 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001130` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
