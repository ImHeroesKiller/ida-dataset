# Candidate Root Cause

**Generated:** 2026-08-13T06:31:15+00:00
**Session:** `SESSION-20260813-A0EBF1`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000007`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260813-A0EBF1`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000007': 1, 'duplicate_id:SIG-000009': 1, 'duplicate_id:SIG-000006': 1, 'duplicate_id:SIG-000010': 1, 'duplicate_id:SIG-000008': 1}`
- `candidate CAND-265BCB9B46F0 entity_id=SIG-000007 reason=duplicate_id:SIG-000007 conf=0.9`
- `candidate CAND-549EB11D1F82 entity_id=SIG-000009 reason=duplicate_id:SIG-000009 conf=0.9`
- `candidate CAND-682ED5E2062F entity_id=SIG-000006 reason=duplicate_id:SIG-000006 conf=0.92`
- `candidate CAND-DC92087319C5 entity_id=SIG-000010 reason=duplicate_id:SIG-000010 conf=0.9`
- `candidate CAND-435A0D7E9D96 entity_id=SIG-000008 reason=duplicate_id:SIG-000008 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-265BCB9B46F0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000007 | Rejected |
| CAND-549EB11D1F82 | business_signal_library | 0.9 | False | duplicate_id:SIG-000009 | Rejected |
| CAND-682ED5E2062F | business_signal_library | 0.92 | False | duplicate_id:SIG-000006 | Rejected |
| CAND-DC92087319C5 | business_signal_library | 0.9 | False | duplicate_id:SIG-000010 | Rejected |
| CAND-435A0D7E9D96 | business_signal_library | 0.9 | False | duplicate_id:SIG-000008 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000007` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
