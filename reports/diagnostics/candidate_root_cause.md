# Candidate Root Cause

**Generated:** 2026-07-14T16:43:39+00:00
**Session:** `SESSION-20260714-E01796`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000211`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260714-E01796`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000211': 1, 'duplicate_id:SIG-000214': 1, 'duplicate_id:SIG-000212': 1, 'duplicate_id:SIG-000213': 1, 'duplicate_id:SIG-000210': 1}`
- `candidate CAND-8D11029D5BE1 entity_id=SIG-000211 reason=duplicate_id:SIG-000211 conf=0.88`
- `candidate CAND-AAC0D0884237 entity_id=SIG-000214 reason=duplicate_id:SIG-000214 conf=0.9`
- `candidate CAND-58D14B9F4237 entity_id=SIG-000212 reason=duplicate_id:SIG-000212 conf=0.92`
- `candidate CAND-9642D6153AC2 entity_id=SIG-000213 reason=duplicate_id:SIG-000213 conf=0.85`
- `candidate CAND-DB719B453546 entity_id=SIG-000210 reason=duplicate_id:SIG-000210 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-8D11029D5BE1 | business_signal_library | 0.88 | False | duplicate_id:SIG-000211 | Rejected |
| CAND-AAC0D0884237 | business_signal_library | 0.9 | False | duplicate_id:SIG-000214 | Rejected |
| CAND-58D14B9F4237 | business_signal_library | 0.92 | False | duplicate_id:SIG-000212 | Rejected |
| CAND-9642D6153AC2 | business_signal_library | 0.85 | False | duplicate_id:SIG-000213 | Rejected |
| CAND-DB719B453546 | business_signal_library | 0.9 | False | duplicate_id:SIG-000210 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000211` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
