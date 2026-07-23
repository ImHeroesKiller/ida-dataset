# Candidate Root Cause

**Generated:** 2026-07-23T20:36:54+00:00
**Session:** `SESSION-20260723-3AE336`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000748`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260723-3AE336`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000748': 1, 'duplicate_id:SIG-000747': 1, 'duplicate_id:SIG-000745': 1, 'duplicate_id:SIG-000749': 1, 'duplicate_id:SIG-000746': 1}`
- `candidate CAND-B77110AAED47 entity_id=SIG-000748 reason=duplicate_id:SIG-000748 conf=0.9`
- `candidate CAND-ED54F14E9054 entity_id=SIG-000747 reason=duplicate_id:SIG-000747 conf=0.88`
- `candidate CAND-AD21D1D9395C entity_id=SIG-000745 reason=duplicate_id:SIG-000745 conf=0.9`
- `candidate CAND-3E5703837B56 entity_id=SIG-000749 reason=duplicate_id:SIG-000749 conf=0.92`
- `candidate CAND-123A76ABC781 entity_id=SIG-000746 reason=duplicate_id:SIG-000746 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B77110AAED47 | business_signal_library | 0.9 | False | duplicate_id:SIG-000748 | Rejected |
| CAND-ED54F14E9054 | business_signal_library | 0.88 | False | duplicate_id:SIG-000747 | Rejected |
| CAND-AD21D1D9395C | business_signal_library | 0.9 | False | duplicate_id:SIG-000745 | Rejected |
| CAND-3E5703837B56 | business_signal_library | 0.92 | False | duplicate_id:SIG-000749 | Rejected |
| CAND-123A76ABC781 | business_signal_library | 0.92 | False | duplicate_id:SIG-000746 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000748` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
