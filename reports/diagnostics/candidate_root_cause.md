# Candidate Root Cause

**Generated:** 2026-07-14T20:35:59+00:00
**Session:** `SESSION-20260714-C5C5DE`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000221`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260714-C5C5DE`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000221': 1, 'duplicate_id:SIG-000222': 1, 'duplicate_id:SIG-000224': 1, 'duplicate_id:SIG-000223': 1, 'duplicate_id:SIG-000220': 1}`
- `candidate CAND-CFDF901B9AC5 entity_id=SIG-000221 reason=duplicate_id:SIG-000221 conf=0.88`
- `candidate CAND-684994363B13 entity_id=SIG-000222 reason=duplicate_id:SIG-000222 conf=0.92`
- `candidate CAND-F61211D36EA1 entity_id=SIG-000224 reason=duplicate_id:SIG-000224 conf=0.9`
- `candidate CAND-84CB2600910C entity_id=SIG-000223 reason=duplicate_id:SIG-000223 conf=0.85`
- `candidate CAND-4C163EF764E8 entity_id=SIG-000220 reason=duplicate_id:SIG-000220 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-CFDF901B9AC5 | business_signal_library | 0.88 | False | duplicate_id:SIG-000221 | Rejected |
| CAND-684994363B13 | business_signal_library | 0.92 | False | duplicate_id:SIG-000222 | Rejected |
| CAND-F61211D36EA1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000224 | Rejected |
| CAND-84CB2600910C | business_signal_library | 0.85 | False | duplicate_id:SIG-000223 | Rejected |
| CAND-4C163EF764E8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000220 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000221` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
