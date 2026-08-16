# Candidate Root Cause

**Generated:** 2026-08-16T17:31:15+00:00
**Session:** `SESSION-20260816-CC613A`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000356`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260816-CC613A`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000356': 1, 'duplicate_id:SIG-000358': 1, 'duplicate_id:SIG-000360': 1, 'duplicate_id:SIG-000359': 1, 'duplicate_id:SIG-000357': 1}`
- `candidate CAND-1CA27A204C42 entity_id=SIG-000356 reason=duplicate_id:SIG-000356 conf=0.92`
- `candidate CAND-1309954D6F94 entity_id=SIG-000358 reason=duplicate_id:SIG-000358 conf=0.9`
- `candidate CAND-9DF6BA6B39F4 entity_id=SIG-000360 reason=duplicate_id:SIG-000360 conf=0.9`
- `candidate CAND-CD7F62EA19B9 entity_id=SIG-000359 reason=duplicate_id:SIG-000359 conf=0.9`
- `candidate CAND-D35E72A6338A entity_id=SIG-000357 reason=duplicate_id:SIG-000357 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-1CA27A204C42 | business_signal_library | 0.92 | False | duplicate_id:SIG-000356 | Rejected |
| CAND-1309954D6F94 | business_signal_library | 0.9 | False | duplicate_id:SIG-000358 | Rejected |
| CAND-9DF6BA6B39F4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000360 | Rejected |
| CAND-CD7F62EA19B9 | business_signal_library | 0.9 | False | duplicate_id:SIG-000359 | Rejected |
| CAND-D35E72A6338A | business_signal_library | 0.9 | False | duplicate_id:SIG-000357 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000356` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
