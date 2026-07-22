# Candidate Root Cause

**Generated:** 2026-07-22T19:42:25+00:00
**Session:** `SESSION-20260722-3FA88D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000696`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260722-3FA88D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000696': 1, 'duplicate_id:SIG-000698': 1, 'duplicate_id:SIG-000699': 1, 'duplicate_id:SIG-000697': 1, 'duplicate_id:SIG-000695': 1}`
- `candidate CAND-CB49AB834D1F entity_id=SIG-000696 reason=duplicate_id:SIG-000696 conf=0.92`
- `candidate CAND-3D1283D9D7F7 entity_id=SIG-000698 reason=duplicate_id:SIG-000698 conf=0.92`
- `candidate CAND-A67D5C7BA37C entity_id=SIG-000699 reason=duplicate_id:SIG-000699 conf=0.9`
- `candidate CAND-EF90D1E6493C entity_id=SIG-000697 reason=duplicate_id:SIG-000697 conf=0.9`
- `candidate CAND-2C87EB53EBAD entity_id=SIG-000695 reason=duplicate_id:SIG-000695 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-CB49AB834D1F | business_signal_library | 0.92 | False | duplicate_id:SIG-000696 | Rejected |
| CAND-3D1283D9D7F7 | business_signal_library | 0.92 | False | duplicate_id:SIG-000698 | Rejected |
| CAND-A67D5C7BA37C | business_signal_library | 0.9 | False | duplicate_id:SIG-000699 | Rejected |
| CAND-EF90D1E6493C | business_signal_library | 0.9 | False | duplicate_id:SIG-000697 | Rejected |
| CAND-2C87EB53EBAD | business_signal_library | 0.9 | False | duplicate_id:SIG-000695 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000696` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
