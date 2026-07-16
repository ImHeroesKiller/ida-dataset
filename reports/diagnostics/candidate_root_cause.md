# Candidate Root Cause

**Generated:** 2026-07-16T23:16:07+00:00
**Session:** `SESSION-20260716-345E14`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000342`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260716-345E14`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000342': 1, 'duplicate_id:SIG-000344': 1, 'duplicate_id:SIG-000340': 1, 'duplicate_id:SIG-000343': 1, 'duplicate_id:SIG-000341': 1}`
- `candidate CAND-36847150F6EC entity_id=SIG-000342 reason=duplicate_id:SIG-000342 conf=0.92`
- `candidate CAND-2C4D87AF9207 entity_id=SIG-000344 reason=duplicate_id:SIG-000344 conf=0.88`
- `candidate CAND-42CC268A9971 entity_id=SIG-000340 reason=duplicate_id:SIG-000340 conf=0.9`
- `candidate CAND-0521021A866B entity_id=SIG-000343 reason=duplicate_id:SIG-000343 conf=0.9`
- `candidate CAND-D126AEE62318 entity_id=SIG-000341 reason=duplicate_id:SIG-000341 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-36847150F6EC | business_signal_library | 0.92 | False | duplicate_id:SIG-000342 | Rejected |
| CAND-2C4D87AF9207 | business_signal_library | 0.88 | False | duplicate_id:SIG-000344 | Rejected |
| CAND-42CC268A9971 | business_signal_library | 0.9 | False | duplicate_id:SIG-000340 | Rejected |
| CAND-0521021A866B | business_signal_library | 0.9 | False | duplicate_id:SIG-000343 | Rejected |
| CAND-D126AEE62318 | business_signal_library | 0.88 | False | duplicate_id:SIG-000341 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000342` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
