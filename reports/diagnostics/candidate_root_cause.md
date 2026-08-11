# Candidate Root Cause

**Generated:** 2026-08-11T12:03:16+00:00
**Session:** `SESSION-20260811-D581F9`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001892`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260811-D581F9`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001892': 1, 'duplicate_id:SIG-001891': 1, 'duplicate_id:SIG-001893': 1, 'duplicate_id:SIG-001890': 1, 'duplicate_id:SIG-001894': 1}`
- `candidate CAND-DBCBB4308D9F entity_id=SIG-001892 reason=duplicate_id:SIG-001892 conf=0.88`
- `candidate CAND-6944F416ECF5 entity_id=SIG-001891 reason=duplicate_id:SIG-001891 conf=0.92`
- `candidate CAND-7BA6898FB3F8 entity_id=SIG-001893 reason=duplicate_id:SIG-001893 conf=0.9`
- `candidate CAND-541B78C9AA6B entity_id=SIG-001890 reason=duplicate_id:SIG-001890 conf=0.9`
- `candidate CAND-292075F9F3FD entity_id=SIG-001894 reason=duplicate_id:SIG-001894 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-DBCBB4308D9F | business_signal_library | 0.88 | False | duplicate_id:SIG-001892 | Rejected |
| CAND-6944F416ECF5 | business_signal_library | 0.92 | False | duplicate_id:SIG-001891 | Rejected |
| CAND-7BA6898FB3F8 | business_signal_library | 0.9 | False | duplicate_id:SIG-001893 | Rejected |
| CAND-541B78C9AA6B | business_signal_library | 0.9 | False | duplicate_id:SIG-001890 | Rejected |
| CAND-292075F9F3FD | business_signal_library | 0.92 | False | duplicate_id:SIG-001894 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001892` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
