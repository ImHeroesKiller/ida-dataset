# Candidate Root Cause

**Generated:** 2026-07-14T23:26:23+00:00
**Session:** `SESSION-20260714-CE883F`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000230`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260714-CE883F`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000230': 1, 'duplicate_id:SIG-000231': 1, 'duplicate_id:SIG-000233': 1, 'duplicate_id:SIG-000232': 1, 'duplicate_id:SIG-000234': 1}`
- `candidate CAND-1872110112B6 entity_id=SIG-000230 reason=duplicate_id:SIG-000230 conf=0.9`
- `candidate CAND-6013A6C1C6A0 entity_id=SIG-000231 reason=duplicate_id:SIG-000231 conf=0.88`
- `candidate CAND-8689124EF376 entity_id=SIG-000233 reason=duplicate_id:SIG-000233 conf=0.85`
- `candidate CAND-83BDFEDF80B7 entity_id=SIG-000232 reason=duplicate_id:SIG-000232 conf=0.92`
- `candidate CAND-B8B97E93685B entity_id=SIG-000234 reason=duplicate_id:SIG-000234 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-1872110112B6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000230 | Rejected |
| CAND-6013A6C1C6A0 | business_signal_library | 0.88 | False | duplicate_id:SIG-000231 | Rejected |
| CAND-8689124EF376 | business_signal_library | 0.85 | False | duplicate_id:SIG-000233 | Rejected |
| CAND-83BDFEDF80B7 | business_signal_library | 0.92 | False | duplicate_id:SIG-000232 | Rejected |
| CAND-B8B97E93685B | business_signal_library | 0.9 | False | duplicate_id:SIG-000234 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000230` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
