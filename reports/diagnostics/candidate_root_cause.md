# Candidate Root Cause

**Generated:** 2026-08-16T22:36:14+00:00
**Session:** `SESSION-20260816-78A971`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000384`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260816-78A971`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000384': 1, 'duplicate_id:SIG-000385': 1, 'duplicate_id:SIG-000382': 1, 'duplicate_id:SIG-000381': 1, 'duplicate_id:SIG-000383': 1}`
- `candidate CAND-86465011B29D entity_id=SIG-000384 reason=duplicate_id:SIG-000384 conf=0.9`
- `candidate CAND-88652BA65875 entity_id=SIG-000385 reason=duplicate_id:SIG-000385 conf=0.9`
- `candidate CAND-8950A674C6DF entity_id=SIG-000382 reason=duplicate_id:SIG-000382 conf=0.9`
- `candidate CAND-88A9F4771393 entity_id=SIG-000381 reason=duplicate_id:SIG-000381 conf=0.92`
- `candidate CAND-1EC736B2B5AA entity_id=SIG-000383 reason=duplicate_id:SIG-000383 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-86465011B29D | business_signal_library | 0.9 | False | duplicate_id:SIG-000384 | Rejected |
| CAND-88652BA65875 | business_signal_library | 0.9 | False | duplicate_id:SIG-000385 | Rejected |
| CAND-8950A674C6DF | business_signal_library | 0.9 | False | duplicate_id:SIG-000382 | Rejected |
| CAND-88A9F4771393 | business_signal_library | 0.92 | False | duplicate_id:SIG-000381 | Rejected |
| CAND-1EC736B2B5AA | business_signal_library | 0.9 | False | duplicate_id:SIG-000383 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000384` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
