# Candidate Root Cause

**Generated:** 2026-08-19T20:49:17+00:00
**Session:** `SESSION-20260819-15CEF4`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000712`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260819-15CEF4`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000712': 1, 'duplicate_id:SIG-000713': 1, 'duplicate_id:SIG-000711': 1, 'duplicate_id:SIG-000715': 1, 'duplicate_id:SIG-000714': 1}`
- `candidate CAND-8187BEF300B3 entity_id=SIG-000712 reason=duplicate_id:SIG-000712 conf=0.9`
- `candidate CAND-ED4669D5E804 entity_id=SIG-000713 reason=duplicate_id:SIG-000713 conf=0.9`
- `candidate CAND-2173DBA61251 entity_id=SIG-000711 reason=duplicate_id:SIG-000711 conf=0.92`
- `candidate CAND-34CA27F5A5A7 entity_id=SIG-000715 reason=duplicate_id:SIG-000715 conf=0.9`
- `candidate CAND-B73A2230ADDF entity_id=SIG-000714 reason=duplicate_id:SIG-000714 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-8187BEF300B3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000712 | Rejected |
| CAND-ED4669D5E804 | business_signal_library | 0.9 | False | duplicate_id:SIG-000713 | Rejected |
| CAND-2173DBA61251 | business_signal_library | 0.92 | False | duplicate_id:SIG-000711 | Rejected |
| CAND-34CA27F5A5A7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000715 | Rejected |
| CAND-B73A2230ADDF | business_signal_library | 0.9 | False | duplicate_id:SIG-000714 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000712` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
