# Candidate Root Cause

**Generated:** 2026-08-22T03:11:25+00:00
**Session:** `SESSION-20260822-34C5F6`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000963`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260822-34C5F6`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000963': 1, 'duplicate_id:SIG-000961': 1, 'duplicate_id:SIG-000965': 1, 'duplicate_id:SIG-000964': 1, 'duplicate_id:SIG-000962': 1}`
- `candidate CAND-BE63B8E64020 entity_id=SIG-000963 reason=duplicate_id:SIG-000963 conf=0.9`
- `candidate CAND-54A8A2F3160F entity_id=SIG-000961 reason=duplicate_id:SIG-000961 conf=0.92`
- `candidate CAND-115EAB36C2DC entity_id=SIG-000965 reason=duplicate_id:SIG-000965 conf=0.9`
- `candidate CAND-2CA6D2A3A34A entity_id=SIG-000964 reason=duplicate_id:SIG-000964 conf=0.9`
- `candidate CAND-B7435670F0E2 entity_id=SIG-000962 reason=duplicate_id:SIG-000962 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-BE63B8E64020 | business_signal_library | 0.9 | False | duplicate_id:SIG-000963 | Rejected |
| CAND-54A8A2F3160F | business_signal_library | 0.92 | False | duplicate_id:SIG-000961 | Rejected |
| CAND-115EAB36C2DC | business_signal_library | 0.9 | False | duplicate_id:SIG-000965 | Rejected |
| CAND-2CA6D2A3A34A | business_signal_library | 0.9 | False | duplicate_id:SIG-000964 | Rejected |
| CAND-B7435670F0E2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000962 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000963` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
