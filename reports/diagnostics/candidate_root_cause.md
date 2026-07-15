# Candidate Root Cause

**Generated:** 2026-07-15T05:56:25+00:00
**Session:** `SESSION-20260715-54D37D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000241`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260715-54D37D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000241': 1, 'duplicate_id:SIG-000240': 1, 'duplicate_id:SIG-000242': 1, 'duplicate_id:SIG-000243': 1, 'duplicate_id:SIG-000244': 1}`
- `candidate CAND-ED2E6F2683D9 entity_id=SIG-000241 reason=duplicate_id:SIG-000241 conf=0.88`
- `candidate CAND-5E0BC5BBDE48 entity_id=SIG-000240 reason=duplicate_id:SIG-000240 conf=0.9`
- `candidate CAND-F0E234340EAA entity_id=SIG-000242 reason=duplicate_id:SIG-000242 conf=0.92`
- `candidate CAND-E4D897A4A916 entity_id=SIG-000243 reason=duplicate_id:SIG-000243 conf=0.85`
- `candidate CAND-821AE26795AA entity_id=SIG-000244 reason=duplicate_id:SIG-000244 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-ED2E6F2683D9 | business_signal_library | 0.88 | False | duplicate_id:SIG-000241 | Rejected |
| CAND-5E0BC5BBDE48 | business_signal_library | 0.9 | False | duplicate_id:SIG-000240 | Rejected |
| CAND-F0E234340EAA | business_signal_library | 0.92 | False | duplicate_id:SIG-000242 | Rejected |
| CAND-E4D897A4A916 | business_signal_library | 0.85 | False | duplicate_id:SIG-000243 | Rejected |
| CAND-821AE26795AA | business_signal_library | 0.9 | False | duplicate_id:SIG-000244 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000241` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
