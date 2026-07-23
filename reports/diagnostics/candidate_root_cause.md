# Candidate Root Cause

**Generated:** 2026-07-23T03:12:09+00:00
**Session:** `SESSION-20260723-7E072A`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000710`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260723-7E072A`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000710': 1, 'duplicate_id:SIG-000712': 1, 'duplicate_id:SIG-000714': 1, 'duplicate_id:SIG-000713': 1, 'duplicate_id:SIG-000711': 1}`
- `candidate CAND-CDC5C470F78C entity_id=SIG-000710 reason=duplicate_id:SIG-000710 conf=0.9`
- `candidate CAND-17F67C34E8C3 entity_id=SIG-000712 reason=duplicate_id:SIG-000712 conf=0.88`
- `candidate CAND-4DECFA6794E0 entity_id=SIG-000714 reason=duplicate_id:SIG-000714 conf=0.92`
- `candidate CAND-887054F43E49 entity_id=SIG-000713 reason=duplicate_id:SIG-000713 conf=0.9`
- `candidate CAND-EF49EC59F28C entity_id=SIG-000711 reason=duplicate_id:SIG-000711 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-CDC5C470F78C | business_signal_library | 0.9 | False | duplicate_id:SIG-000710 | Rejected |
| CAND-17F67C34E8C3 | business_signal_library | 0.88 | False | duplicate_id:SIG-000712 | Rejected |
| CAND-4DECFA6794E0 | business_signal_library | 0.92 | False | duplicate_id:SIG-000714 | Rejected |
| CAND-887054F43E49 | business_signal_library | 0.9 | False | duplicate_id:SIG-000713 | Rejected |
| CAND-EF49EC59F28C | business_signal_library | 0.92 | False | duplicate_id:SIG-000711 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000710` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
