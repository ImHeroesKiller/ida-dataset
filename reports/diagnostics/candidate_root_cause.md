# Candidate Root Cause

**Generated:** 2026-07-24T04:33:47+00:00
**Session:** `SESSION-20260724-E28251`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000762`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260724-E28251`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000762': 1, 'duplicate_id:SIG-000763': 1, 'duplicate_id:SIG-000760': 1, 'duplicate_id:SIG-000761': 1, 'duplicate_id:SIG-000764': 1}`
- `candidate CAND-95DF584592E9 entity_id=SIG-000762 reason=duplicate_id:SIG-000762 conf=0.88`
- `candidate CAND-71726B35F166 entity_id=SIG-000763 reason=duplicate_id:SIG-000763 conf=0.9`
- `candidate CAND-A6654E22C3F8 entity_id=SIG-000760 reason=duplicate_id:SIG-000760 conf=0.9`
- `candidate CAND-C178503FF21C entity_id=SIG-000761 reason=duplicate_id:SIG-000761 conf=0.92`
- `candidate CAND-30510315D303 entity_id=SIG-000764 reason=duplicate_id:SIG-000764 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-95DF584592E9 | business_signal_library | 0.88 | False | duplicate_id:SIG-000762 | Rejected |
| CAND-71726B35F166 | business_signal_library | 0.9 | False | duplicate_id:SIG-000763 | Rejected |
| CAND-A6654E22C3F8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000760 | Rejected |
| CAND-C178503FF21C | business_signal_library | 0.92 | False | duplicate_id:SIG-000761 | Rejected |
| CAND-30510315D303 | business_signal_library | 0.92 | False | duplicate_id:SIG-000764 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000762` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
