# Candidate Root Cause

**Generated:** 2026-07-12T13:42:50+00:00
**Session:** `SESSION-20260712-929EAE`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000100`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260712-929EAE`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000100': 1, 'duplicate_id:SIG-000104': 1, 'duplicate_id:SIG-000102': 1, 'duplicate_id:SIG-000103': 1, 'duplicate_id:SIG-000101': 1}`
- `candidate CAND-1420743E65AE entity_id=SIG-000100 reason=duplicate_id:SIG-000100 conf=0.9`
- `candidate CAND-930E7FC44BE5 entity_id=SIG-000104 reason=duplicate_id:SIG-000104 conf=0.92`
- `candidate CAND-1E07EEB8383C entity_id=SIG-000102 reason=duplicate_id:SIG-000102 conf=0.88`
- `candidate CAND-A542E3D7E925 entity_id=SIG-000103 reason=duplicate_id:SIG-000103 conf=0.9`
- `candidate CAND-894A2EDBE5EF entity_id=SIG-000101 reason=duplicate_id:SIG-000101 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-1420743E65AE | business_signal_library | 0.9 | False | duplicate_id:SIG-000100 | Rejected |
| CAND-930E7FC44BE5 | business_signal_library | 0.92 | False | duplicate_id:SIG-000104 | Rejected |
| CAND-1E07EEB8383C | business_signal_library | 0.88 | False | duplicate_id:SIG-000102 | Rejected |
| CAND-A542E3D7E925 | business_signal_library | 0.9 | False | duplicate_id:SIG-000103 | Rejected |
| CAND-894A2EDBE5EF | business_signal_library | 0.92 | False | duplicate_id:SIG-000101 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000100` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
