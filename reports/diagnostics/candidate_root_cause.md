# Candidate Root Cause

**Generated:** 2026-08-21T15:53:35+00:00
**Session:** `SESSION-20260821-D246F0`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000914`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260821-D246F0`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000914': 1, 'duplicate_id:SIG-000911': 1, 'duplicate_id:SIG-000912': 1, 'duplicate_id:SIG-000915': 1, 'duplicate_id:SIG-000913': 1}`
- `candidate CAND-2BF384131767 entity_id=SIG-000914 reason=duplicate_id:SIG-000914 conf=0.9`
- `candidate CAND-4D19923EAE3A entity_id=SIG-000911 reason=duplicate_id:SIG-000911 conf=0.92`
- `candidate CAND-15BC93996D0F entity_id=SIG-000912 reason=duplicate_id:SIG-000912 conf=0.9`
- `candidate CAND-F5759B6E1E26 entity_id=SIG-000915 reason=duplicate_id:SIG-000915 conf=0.9`
- `candidate CAND-C83D9095515C entity_id=SIG-000913 reason=duplicate_id:SIG-000913 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-2BF384131767 | business_signal_library | 0.9 | False | duplicate_id:SIG-000914 | Rejected |
| CAND-4D19923EAE3A | business_signal_library | 0.92 | False | duplicate_id:SIG-000911 | Rejected |
| CAND-15BC93996D0F | business_signal_library | 0.9 | False | duplicate_id:SIG-000912 | Rejected |
| CAND-F5759B6E1E26 | business_signal_library | 0.9 | False | duplicate_id:SIG-000915 | Rejected |
| CAND-C83D9095515C | business_signal_library | 0.9 | False | duplicate_id:SIG-000913 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000914` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
