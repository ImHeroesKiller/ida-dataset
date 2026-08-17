# Candidate Root Cause

**Generated:** 2026-08-17T13:53:35+00:00
**Session:** `SESSION-20260817-0C56A5`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000447`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260817-0C56A5`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000447': 1, 'duplicate_id:SIG-000450': 1, 'duplicate_id:SIG-000446': 1, 'duplicate_id:SIG-000448': 1, 'duplicate_id:SIG-000449': 1}`
- `candidate CAND-D6D97FE038B1 entity_id=SIG-000447 reason=duplicate_id:SIG-000447 conf=0.9`
- `candidate CAND-649DC5295752 entity_id=SIG-000450 reason=duplicate_id:SIG-000450 conf=0.9`
- `candidate CAND-9D541A628A23 entity_id=SIG-000446 reason=duplicate_id:SIG-000446 conf=0.92`
- `candidate CAND-941280CF8705 entity_id=SIG-000448 reason=duplicate_id:SIG-000448 conf=0.9`
- `candidate CAND-9FFCF27D5DE6 entity_id=SIG-000449 reason=duplicate_id:SIG-000449 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-D6D97FE038B1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000447 | Rejected |
| CAND-649DC5295752 | business_signal_library | 0.9 | False | duplicate_id:SIG-000450 | Rejected |
| CAND-9D541A628A23 | business_signal_library | 0.92 | False | duplicate_id:SIG-000446 | Rejected |
| CAND-941280CF8705 | business_signal_library | 0.9 | False | duplicate_id:SIG-000448 | Rejected |
| CAND-9FFCF27D5DE6 | business_signal_library | 0.9 | False | duplicate_id:SIG-000449 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000447` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
