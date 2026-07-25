# Candidate Root Cause

**Generated:** 2026-07-25T04:30:52+00:00
**Session:** `SESSION-20260725-212A67`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000818`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260725-212A67`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000818': 1, 'duplicate_id:SIG-000819': 1, 'duplicate_id:SIG-000816': 1, 'duplicate_id:SIG-000815': 1, 'duplicate_id:SIG-000817': 1}`
- `candidate CAND-66A1399D0F1A entity_id=SIG-000818 reason=duplicate_id:SIG-000818 conf=0.9`
- `candidate CAND-F2BA291379E3 entity_id=SIG-000819 reason=duplicate_id:SIG-000819 conf=0.92`
- `candidate CAND-BBBBE44C0F72 entity_id=SIG-000816 reason=duplicate_id:SIG-000816 conf=0.92`
- `candidate CAND-28DE98662920 entity_id=SIG-000815 reason=duplicate_id:SIG-000815 conf=0.9`
- `candidate CAND-C680328CAF29 entity_id=SIG-000817 reason=duplicate_id:SIG-000817 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-66A1399D0F1A | business_signal_library | 0.9 | False | duplicate_id:SIG-000818 | Rejected |
| CAND-F2BA291379E3 | business_signal_library | 0.92 | False | duplicate_id:SIG-000819 | Rejected |
| CAND-BBBBE44C0F72 | business_signal_library | 0.92 | False | duplicate_id:SIG-000816 | Rejected |
| CAND-28DE98662920 | business_signal_library | 0.9 | False | duplicate_id:SIG-000815 | Rejected |
| CAND-C680328CAF29 | business_signal_library | 0.88 | False | duplicate_id:SIG-000817 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000818` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
