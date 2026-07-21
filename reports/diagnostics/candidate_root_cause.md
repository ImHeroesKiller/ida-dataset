# Candidate Root Cause

**Generated:** 2026-07-21T09:46:49+00:00
**Session:** `SESSION-20260721-585A91`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000617`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260721-585A91`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000617': 1, 'duplicate_id:SIG-000619': 1, 'duplicate_id:SIG-000618': 1, 'duplicate_id:SIG-000615': 1, 'duplicate_id:SIG-000616': 1}`
- `candidate CAND-FCAB21EAB39B entity_id=SIG-000617 reason=duplicate_id:SIG-000617 conf=0.88`
- `candidate CAND-C043FCD55052 entity_id=SIG-000619 reason=duplicate_id:SIG-000619 conf=0.92`
- `candidate CAND-F7A0FAF0B43C entity_id=SIG-000618 reason=duplicate_id:SIG-000618 conf=0.9`
- `candidate CAND-B12181371BB8 entity_id=SIG-000615 reason=duplicate_id:SIG-000615 conf=0.9`
- `candidate CAND-BE080401434E entity_id=SIG-000616 reason=duplicate_id:SIG-000616 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-FCAB21EAB39B | business_signal_library | 0.88 | False | duplicate_id:SIG-000617 | Rejected |
| CAND-C043FCD55052 | business_signal_library | 0.92 | False | duplicate_id:SIG-000619 | Rejected |
| CAND-F7A0FAF0B43C | business_signal_library | 0.9 | False | duplicate_id:SIG-000618 | Rejected |
| CAND-B12181371BB8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000615 | Rejected |
| CAND-BE080401434E | business_signal_library | 0.92 | False | duplicate_id:SIG-000616 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000617` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
