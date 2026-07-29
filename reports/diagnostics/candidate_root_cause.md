# Candidate Root Cause

**Generated:** 2026-07-29T17:36:52+00:00
**Session:** `SESSION-20260729-F8EDBC`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001058`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260729-F8EDBC`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001058': 1, 'duplicate_id:SIG-001057': 1, 'duplicate_id:SIG-001056': 1, 'duplicate_id:SIG-001059': 1, 'duplicate_id:SIG-001055': 1}`
- `candidate CAND-68A0CE1C3679 entity_id=SIG-001058 reason=duplicate_id:SIG-001058 conf=0.9`
- `candidate CAND-2D19BDB5865A entity_id=SIG-001057 reason=duplicate_id:SIG-001057 conf=0.88`
- `candidate CAND-5310A82B5B37 entity_id=SIG-001056 reason=duplicate_id:SIG-001056 conf=0.92`
- `candidate CAND-CE894317FA03 entity_id=SIG-001059 reason=duplicate_id:SIG-001059 conf=0.92`
- `candidate CAND-19D4BF893B29 entity_id=SIG-001055 reason=duplicate_id:SIG-001055 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-68A0CE1C3679 | business_signal_library | 0.9 | False | duplicate_id:SIG-001058 | Rejected |
| CAND-2D19BDB5865A | business_signal_library | 0.88 | False | duplicate_id:SIG-001057 | Rejected |
| CAND-5310A82B5B37 | business_signal_library | 0.92 | False | duplicate_id:SIG-001056 | Rejected |
| CAND-CE894317FA03 | business_signal_library | 0.92 | False | duplicate_id:SIG-001059 | Rejected |
| CAND-19D4BF893B29 | business_signal_library | 0.9 | False | duplicate_id:SIG-001055 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001058` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
