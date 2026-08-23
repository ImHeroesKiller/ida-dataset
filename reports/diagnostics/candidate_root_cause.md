# Candidate Root Cause

**Generated:** 2026-08-23T11:40:10+00:00
**Session:** `SESSION-20260823-147772`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001116`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260823-147772`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001116': 1, 'duplicate_id:SIG-001117': 1, 'duplicate_id:SIG-001119': 1, 'duplicate_id:SIG-001120': 1, 'duplicate_id:SIG-001118': 1}`
- `candidate CAND-9B248CD55043 entity_id=SIG-001116 reason=duplicate_id:SIG-001116 conf=0.92`
- `candidate CAND-B8503A0A8BF1 entity_id=SIG-001117 reason=duplicate_id:SIG-001117 conf=0.9`
- `candidate CAND-8E3D98DA9F81 entity_id=SIG-001119 reason=duplicate_id:SIG-001119 conf=0.9`
- `candidate CAND-15F8B850A35F entity_id=SIG-001120 reason=duplicate_id:SIG-001120 conf=0.9`
- `candidate CAND-3D4E08D5BE9F entity_id=SIG-001118 reason=duplicate_id:SIG-001118 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-9B248CD55043 | business_signal_library | 0.92 | False | duplicate_id:SIG-001116 | Rejected |
| CAND-B8503A0A8BF1 | business_signal_library | 0.9 | False | duplicate_id:SIG-001117 | Rejected |
| CAND-8E3D98DA9F81 | business_signal_library | 0.9 | False | duplicate_id:SIG-001119 | Rejected |
| CAND-15F8B850A35F | business_signal_library | 0.9 | False | duplicate_id:SIG-001120 | Rejected |
| CAND-3D4E08D5BE9F | business_signal_library | 0.9 | False | duplicate_id:SIG-001118 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001116` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
