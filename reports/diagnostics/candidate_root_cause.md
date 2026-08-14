# Candidate Root Cause

**Generated:** 2026-08-14T02:18:14+00:00
**Session:** `SESSION-20260814-00E7A7`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000076`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260814-00E7A7`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000076': 1, 'duplicate_id:SIG-000078': 1, 'duplicate_id:SIG-000080': 1, 'duplicate_id:SIG-000079': 1, 'duplicate_id:SIG-000077': 1}`
- `candidate CAND-6098831DA016 entity_id=SIG-000076 reason=duplicate_id:SIG-000076 conf=0.92`
- `candidate CAND-F0E411C9BD27 entity_id=SIG-000078 reason=duplicate_id:SIG-000078 conf=0.9`
- `candidate CAND-2B87EFB07273 entity_id=SIG-000080 reason=duplicate_id:SIG-000080 conf=0.9`
- `candidate CAND-46A8DDBB1C6D entity_id=SIG-000079 reason=duplicate_id:SIG-000079 conf=0.9`
- `candidate CAND-501F4B01BE97 entity_id=SIG-000077 reason=duplicate_id:SIG-000077 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-6098831DA016 | business_signal_library | 0.92 | False | duplicate_id:SIG-000076 | Rejected |
| CAND-F0E411C9BD27 | business_signal_library | 0.9 | False | duplicate_id:SIG-000078 | Rejected |
| CAND-2B87EFB07273 | business_signal_library | 0.9 | False | duplicate_id:SIG-000080 | Rejected |
| CAND-46A8DDBB1C6D | business_signal_library | 0.9 | False | duplicate_id:SIG-000079 | Rejected |
| CAND-501F4B01BE97 | business_signal_library | 0.9 | False | duplicate_id:SIG-000077 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000076` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
