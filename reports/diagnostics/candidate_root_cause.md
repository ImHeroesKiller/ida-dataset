# Candidate Root Cause

**Generated:** 2026-08-17T05:50:37+00:00
**Session:** `SESSION-20260817-735FA0`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000409`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260817-735FA0`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000409': 1, 'duplicate_id:SIG-000408': 1, 'duplicate_id:SIG-000410': 1, 'duplicate_id:SIG-000407': 1, 'duplicate_id:SIG-000406': 1}`
- `candidate CAND-F1398F040ED9 entity_id=SIG-000409 reason=duplicate_id:SIG-000409 conf=0.9`
- `candidate CAND-8E353BD08CBA entity_id=SIG-000408 reason=duplicate_id:SIG-000408 conf=0.9`
- `candidate CAND-09BAE78C2B32 entity_id=SIG-000410 reason=duplicate_id:SIG-000410 conf=0.9`
- `candidate CAND-68CE24663D79 entity_id=SIG-000407 reason=duplicate_id:SIG-000407 conf=0.9`
- `candidate CAND-A5797FB7240C entity_id=SIG-000406 reason=duplicate_id:SIG-000406 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F1398F040ED9 | business_signal_library | 0.9 | False | duplicate_id:SIG-000409 | Rejected |
| CAND-8E353BD08CBA | business_signal_library | 0.9 | False | duplicate_id:SIG-000408 | Rejected |
| CAND-09BAE78C2B32 | business_signal_library | 0.9 | False | duplicate_id:SIG-000410 | Rejected |
| CAND-68CE24663D79 | business_signal_library | 0.9 | False | duplicate_id:SIG-000407 | Rejected |
| CAND-A5797FB7240C | business_signal_library | 0.92 | False | duplicate_id:SIG-000406 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000409` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
