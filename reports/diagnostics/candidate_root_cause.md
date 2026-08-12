# Candidate Root Cause

**Generated:** 2026-08-12T02:23:57+00:00
**Session:** `SESSION-20260812-3330E6`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001941`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260812-3330E6`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001941': 1, 'duplicate_id:SIG-001943': 1, 'duplicate_id:SIG-001944': 1, 'duplicate_id:SIG-001940': 1, 'duplicate_id:SIG-001942': 1}`
- `candidate CAND-01980B0B19C0 entity_id=SIG-001941 reason=duplicate_id:SIG-001941 conf=0.92`
- `candidate CAND-1F784C7BEBDB entity_id=SIG-001943 reason=duplicate_id:SIG-001943 conf=0.9`
- `candidate CAND-281B29EFDED6 entity_id=SIG-001944 reason=duplicate_id:SIG-001944 conf=0.92`
- `candidate CAND-FC2D220793B1 entity_id=SIG-001940 reason=duplicate_id:SIG-001940 conf=0.9`
- `candidate CAND-BB9B571FC309 entity_id=SIG-001942 reason=duplicate_id:SIG-001942 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-01980B0B19C0 | business_signal_library | 0.92 | False | duplicate_id:SIG-001941 | Rejected |
| CAND-1F784C7BEBDB | business_signal_library | 0.9 | False | duplicate_id:SIG-001943 | Rejected |
| CAND-281B29EFDED6 | business_signal_library | 0.92 | False | duplicate_id:SIG-001944 | Rejected |
| CAND-FC2D220793B1 | business_signal_library | 0.9 | False | duplicate_id:SIG-001940 | Rejected |
| CAND-BB9B571FC309 | business_signal_library | 0.88 | False | duplicate_id:SIG-001942 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001941` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
