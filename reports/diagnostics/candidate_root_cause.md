# Candidate Root Cause

**Generated:** 2026-08-17T04:57:10+00:00
**Session:** `SESSION-20260817-2AD8AA`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000405`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260817-2AD8AA`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000405': 1, 'duplicate_id:SIG-000403': 1, 'duplicate_id:SIG-000401': 1, 'duplicate_id:SIG-000404': 1, 'duplicate_id:SIG-000402': 1}`
- `candidate CAND-FCFF99905421 entity_id=SIG-000405 reason=duplicate_id:SIG-000405 conf=0.9`
- `candidate CAND-72280066F2EF entity_id=SIG-000403 reason=duplicate_id:SIG-000403 conf=0.9`
- `candidate CAND-86305734E6F0 entity_id=SIG-000401 reason=duplicate_id:SIG-000401 conf=0.92`
- `candidate CAND-7F3D112185BB entity_id=SIG-000404 reason=duplicate_id:SIG-000404 conf=0.9`
- `candidate CAND-D4A06DED5ECA entity_id=SIG-000402 reason=duplicate_id:SIG-000402 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-FCFF99905421 | business_signal_library | 0.9 | False | duplicate_id:SIG-000405 | Rejected |
| CAND-72280066F2EF | business_signal_library | 0.9 | False | duplicate_id:SIG-000403 | Rejected |
| CAND-86305734E6F0 | business_signal_library | 0.92 | False | duplicate_id:SIG-000401 | Rejected |
| CAND-7F3D112185BB | business_signal_library | 0.9 | False | duplicate_id:SIG-000404 | Rejected |
| CAND-D4A06DED5ECA | business_signal_library | 0.9 | False | duplicate_id:SIG-000402 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000405` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
