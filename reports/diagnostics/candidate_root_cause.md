# Candidate Root Cause

**Generated:** 2026-07-26T13:45:43+00:00
**Session:** `SESSION-20260726-72D96E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000902`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260726-72D96E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000902': 1, 'duplicate_id:SIG-000903': 1, 'duplicate_id:SIG-000901': 1, 'duplicate_id:SIG-000904': 1, 'duplicate_id:SIG-000900': 1}`
- `candidate CAND-E67AA2435539 entity_id=SIG-000902 reason=duplicate_id:SIG-000902 conf=0.88`
- `candidate CAND-4121AD4A8A6C entity_id=SIG-000903 reason=duplicate_id:SIG-000903 conf=0.9`
- `candidate CAND-23F8F11C5691 entity_id=SIG-000901 reason=duplicate_id:SIG-000901 conf=0.92`
- `candidate CAND-44F6E1AB82A9 entity_id=SIG-000904 reason=duplicate_id:SIG-000904 conf=0.92`
- `candidate CAND-D49E017CDC5B entity_id=SIG-000900 reason=duplicate_id:SIG-000900 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-E67AA2435539 | business_signal_library | 0.88 | False | duplicate_id:SIG-000902 | Rejected |
| CAND-4121AD4A8A6C | business_signal_library | 0.9 | False | duplicate_id:SIG-000903 | Rejected |
| CAND-23F8F11C5691 | business_signal_library | 0.92 | False | duplicate_id:SIG-000901 | Rejected |
| CAND-44F6E1AB82A9 | business_signal_library | 0.92 | False | duplicate_id:SIG-000904 | Rejected |
| CAND-D49E017CDC5B | business_signal_library | 0.9 | False | duplicate_id:SIG-000900 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000902` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
