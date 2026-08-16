# Candidate Root Cause

**Generated:** 2026-08-16T13:47:09+00:00
**Session:** `SESSION-20260816-E1783E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000337`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260816-E1783E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000337': 1, 'duplicate_id:SIG-000339': 1, 'duplicate_id:SIG-000340': 1, 'duplicate_id:SIG-000338': 1, 'duplicate_id:SIG-000336': 1}`
- `candidate CAND-86E1BD39C348 entity_id=SIG-000337 reason=duplicate_id:SIG-000337 conf=0.92`
- `candidate CAND-DD8FD9363C3C entity_id=SIG-000339 reason=duplicate_id:SIG-000339 conf=0.9`
- `candidate CAND-714018194615 entity_id=SIG-000340 reason=duplicate_id:SIG-000340 conf=0.9`
- `candidate CAND-487C280C36D8 entity_id=SIG-000338 reason=duplicate_id:SIG-000338 conf=0.9`
- `candidate CAND-5D534512B943 entity_id=SIG-000336 reason=duplicate_id:SIG-000336 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-86E1BD39C348 | business_signal_library | 0.92 | False | duplicate_id:SIG-000337 | Rejected |
| CAND-DD8FD9363C3C | business_signal_library | 0.9 | False | duplicate_id:SIG-000339 | Rejected |
| CAND-714018194615 | business_signal_library | 0.9 | False | duplicate_id:SIG-000340 | Rejected |
| CAND-487C280C36D8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000338 | Rejected |
| CAND-5D534512B943 | business_signal_library | 0.9 | False | duplicate_id:SIG-000336 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000337` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
