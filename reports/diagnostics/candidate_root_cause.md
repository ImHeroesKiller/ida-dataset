# Candidate Root Cause

**Generated:** 2026-07-16T14:15:08+00:00
**Session:** `SESSION-20260716-40F733`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000318`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260716-40F733`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000318': 1, 'duplicate_id:SIG-000319': 1, 'duplicate_id:SIG-000316': 1, 'duplicate_id:SIG-000317': 1, 'duplicate_id:SIG-000315': 1}`
- `candidate CAND-5BA01F6F6A85 entity_id=SIG-000318 reason=duplicate_id:SIG-000318 conf=0.9`
- `candidate CAND-D7530D319265 entity_id=SIG-000319 reason=duplicate_id:SIG-000319 conf=0.92`
- `candidate CAND-5C1433B7991C entity_id=SIG-000316 reason=duplicate_id:SIG-000316 conf=0.92`
- `candidate CAND-C874D414FCDC entity_id=SIG-000317 reason=duplicate_id:SIG-000317 conf=0.88`
- `candidate CAND-47CD818FC5CF entity_id=SIG-000315 reason=duplicate_id:SIG-000315 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5BA01F6F6A85 | business_signal_library | 0.9 | False | duplicate_id:SIG-000318 | Rejected |
| CAND-D7530D319265 | business_signal_library | 0.92 | False | duplicate_id:SIG-000319 | Rejected |
| CAND-5C1433B7991C | business_signal_library | 0.92 | False | duplicate_id:SIG-000316 | Rejected |
| CAND-C874D414FCDC | business_signal_library | 0.88 | False | duplicate_id:SIG-000317 | Rejected |
| CAND-47CD818FC5CF | business_signal_library | 0.9 | False | duplicate_id:SIG-000315 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000318` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
