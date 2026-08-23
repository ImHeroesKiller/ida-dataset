# Candidate Root Cause

**Generated:** 2026-08-23T04:57:08+00:00
**Session:** `SESSION-20260823-511578`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001081`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260823-511578`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001081': 1, 'duplicate_id:SIG-001082': 1, 'duplicate_id:SIG-001084': 1, 'duplicate_id:SIG-001085': 1, 'duplicate_id:SIG-001083': 1}`
- `candidate CAND-24E800931F68 entity_id=SIG-001081 reason=duplicate_id:SIG-001081 conf=0.92`
- `candidate CAND-B7E7AC536580 entity_id=SIG-001082 reason=duplicate_id:SIG-001082 conf=0.9`
- `candidate CAND-66B89D78A6CC entity_id=SIG-001084 reason=duplicate_id:SIG-001084 conf=0.9`
- `candidate CAND-DB8DC72C8186 entity_id=SIG-001085 reason=duplicate_id:SIG-001085 conf=0.9`
- `candidate CAND-9D9232DAD541 entity_id=SIG-001083 reason=duplicate_id:SIG-001083 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-24E800931F68 | business_signal_library | 0.92 | False | duplicate_id:SIG-001081 | Rejected |
| CAND-B7E7AC536580 | business_signal_library | 0.9 | False | duplicate_id:SIG-001082 | Rejected |
| CAND-66B89D78A6CC | business_signal_library | 0.9 | False | duplicate_id:SIG-001084 | Rejected |
| CAND-DB8DC72C8186 | business_signal_library | 0.9 | False | duplicate_id:SIG-001085 | Rejected |
| CAND-9D9232DAD541 | business_signal_library | 0.9 | False | duplicate_id:SIG-001083 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001081` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
