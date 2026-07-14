# Candidate Root Cause

**Generated:** 2026-07-14T15:15:09+00:00
**Session:** `SESSION-20260714-F63B8E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000205`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260714-F63B8E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000205': 1, 'duplicate_id:SIG-000209': 1, 'duplicate_id:SIG-000207': 1, 'duplicate_id:SIG-000208': 1, 'duplicate_id:SIG-000206': 1}`
- `candidate CAND-5683E4B5DD20 entity_id=SIG-000205 reason=duplicate_id:SIG-000205 conf=0.9`
- `candidate CAND-CB658F2E3CE1 entity_id=SIG-000209 reason=duplicate_id:SIG-000209 conf=0.9`
- `candidate CAND-EDDAAF85E5FE entity_id=SIG-000207 reason=duplicate_id:SIG-000207 conf=0.9`
- `candidate CAND-BA47A0E637CD entity_id=SIG-000208 reason=duplicate_id:SIG-000208 conf=0.92`
- `candidate CAND-E0044C696D3F entity_id=SIG-000206 reason=duplicate_id:SIG-000206 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5683E4B5DD20 | business_signal_library | 0.9 | False | duplicate_id:SIG-000205 | Rejected |
| CAND-CB658F2E3CE1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000209 | Rejected |
| CAND-EDDAAF85E5FE | business_signal_library | 0.9 | False | duplicate_id:SIG-000207 | Rejected |
| CAND-BA47A0E637CD | business_signal_library | 0.92 | False | duplicate_id:SIG-000208 | Rejected |
| CAND-E0044C696D3F | business_signal_library | 0.92 | False | duplicate_id:SIG-000206 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000205` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
