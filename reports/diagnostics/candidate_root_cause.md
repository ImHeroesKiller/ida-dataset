# Candidate Root Cause

**Generated:** 2026-07-17T00:27:59+00:00
**Session:** `SESSION-20260717-84032C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000346`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260717-84032C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000346': 1, 'duplicate_id:SIG-000347': 1, 'duplicate_id:SIG-000345': 1, 'duplicate_id:SIG-000348': 1, 'duplicate_id:SIG-000349': 1}`
- `candidate CAND-47412DE29FD3 entity_id=SIG-000346 reason=duplicate_id:SIG-000346 conf=0.88`
- `candidate CAND-BCAF37C2A947 entity_id=SIG-000347 reason=duplicate_id:SIG-000347 conf=0.92`
- `candidate CAND-88C287BA2ED0 entity_id=SIG-000345 reason=duplicate_id:SIG-000345 conf=0.9`
- `candidate CAND-EB3B100437CC entity_id=SIG-000348 reason=duplicate_id:SIG-000348 conf=0.9`
- `candidate CAND-B5358284CBE7 entity_id=SIG-000349 reason=duplicate_id:SIG-000349 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-47412DE29FD3 | business_signal_library | 0.88 | False | duplicate_id:SIG-000346 | Rejected |
| CAND-BCAF37C2A947 | business_signal_library | 0.92 | False | duplicate_id:SIG-000347 | Rejected |
| CAND-88C287BA2ED0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000345 | Rejected |
| CAND-EB3B100437CC | business_signal_library | 0.9 | False | duplicate_id:SIG-000348 | Rejected |
| CAND-B5358284CBE7 | business_signal_library | 0.88 | False | duplicate_id:SIG-000349 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000346` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
