# Candidate Root Cause

**Generated:** 2026-08-19T19:46:15+00:00
**Session:** `SESSION-20260819-A4941C`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000706`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260819-A4941C`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000706': 1, 'duplicate_id:SIG-000708': 1, 'duplicate_id:SIG-000709': 1, 'duplicate_id:SIG-000707': 1, 'duplicate_id:SIG-000710': 1}`
- `candidate CAND-7B3913658076 entity_id=SIG-000706 reason=duplicate_id:SIG-000706 conf=0.92`
- `candidate CAND-B85787D30495 entity_id=SIG-000708 reason=duplicate_id:SIG-000708 conf=0.9`
- `candidate CAND-5AF978B3AC61 entity_id=SIG-000709 reason=duplicate_id:SIG-000709 conf=0.9`
- `candidate CAND-1BDE6C8AEEFB entity_id=SIG-000707 reason=duplicate_id:SIG-000707 conf=0.9`
- `candidate CAND-03F983158044 entity_id=SIG-000710 reason=duplicate_id:SIG-000710 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-7B3913658076 | business_signal_library | 0.92 | False | duplicate_id:SIG-000706 | Rejected |
| CAND-B85787D30495 | business_signal_library | 0.9 | False | duplicate_id:SIG-000708 | Rejected |
| CAND-5AF978B3AC61 | business_signal_library | 0.9 | False | duplicate_id:SIG-000709 | Rejected |
| CAND-1BDE6C8AEEFB | business_signal_library | 0.9 | False | duplicate_id:SIG-000707 | Rejected |
| CAND-03F983158044 | business_signal_library | 0.9 | False | duplicate_id:SIG-000710 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000706` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
