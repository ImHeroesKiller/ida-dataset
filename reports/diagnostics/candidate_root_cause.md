# Candidate Root Cause

**Generated:** 2026-07-23T06:16:01+00:00
**Session:** `SESSION-20260723-AE0B14`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000717`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260723-AE0B14`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000717': 1, 'duplicate_id:SIG-000718': 1, 'duplicate_id:SIG-000719': 1, 'duplicate_id:SIG-000716': 1, 'duplicate_id:SIG-000715': 1}`
- `candidate CAND-F541FCB9E216 entity_id=SIG-000717 reason=duplicate_id:SIG-000717 conf=0.88`
- `candidate CAND-24C18DEDF89A entity_id=SIG-000718 reason=duplicate_id:SIG-000718 conf=0.9`
- `candidate CAND-3577E8D23C6B entity_id=SIG-000719 reason=duplicate_id:SIG-000719 conf=0.92`
- `candidate CAND-1C6D2C2ED958 entity_id=SIG-000716 reason=duplicate_id:SIG-000716 conf=0.92`
- `candidate CAND-9FDF67666FA2 entity_id=SIG-000715 reason=duplicate_id:SIG-000715 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-F541FCB9E216 | business_signal_library | 0.88 | False | duplicate_id:SIG-000717 | Rejected |
| CAND-24C18DEDF89A | business_signal_library | 0.9 | False | duplicate_id:SIG-000718 | Rejected |
| CAND-3577E8D23C6B | business_signal_library | 0.92 | False | duplicate_id:SIG-000719 | Rejected |
| CAND-1C6D2C2ED958 | business_signal_library | 0.92 | False | duplicate_id:SIG-000716 | Rejected |
| CAND-9FDF67666FA2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000715 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000717` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
