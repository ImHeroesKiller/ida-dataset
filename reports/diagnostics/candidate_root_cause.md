# Candidate Root Cause

**Generated:** 2026-07-15T12:39:53+00:00
**Session:** `SESSION-20260715-C37542`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000255`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260715-C37542`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000255': 1, 'duplicate_id:SIG-000256': 1, 'duplicate_id:SIG-000258': 1, 'duplicate_id:SIG-000259': 1, 'duplicate_id:SIG-000257': 1}`
- `candidate CAND-24793DC00FB3 entity_id=SIG-000255 reason=duplicate_id:SIG-000255 conf=0.9`
- `candidate CAND-9F1346901D7A entity_id=SIG-000256 reason=duplicate_id:SIG-000256 conf=0.88`
- `candidate CAND-915B61321399 entity_id=SIG-000258 reason=duplicate_id:SIG-000258 conf=0.9`
- `candidate CAND-8080EF121D04 entity_id=SIG-000259 reason=duplicate_id:SIG-000259 conf=0.88`
- `candidate CAND-39902C1FB4D4 entity_id=SIG-000257 reason=duplicate_id:SIG-000257 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-24793DC00FB3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000255 | Rejected |
| CAND-9F1346901D7A | business_signal_library | 0.88 | False | duplicate_id:SIG-000256 | Rejected |
| CAND-915B61321399 | business_signal_library | 0.9 | False | duplicate_id:SIG-000258 | Rejected |
| CAND-8080EF121D04 | business_signal_library | 0.88 | False | duplicate_id:SIG-000259 | Rejected |
| CAND-39902C1FB4D4 | business_signal_library | 0.92 | False | duplicate_id:SIG-000257 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000255` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
