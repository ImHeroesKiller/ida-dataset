# Candidate Root Cause

**Generated:** 2026-07-26T17:21:43+00:00
**Session:** `SESSION-20260726-D0A1F1`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000910`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260726-D0A1F1`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000910': 1, 'duplicate_id:SIG-000914': 1, 'duplicate_id:SIG-000911': 1, 'duplicate_id:SIG-000912': 1, 'duplicate_id:SIG-000913': 1}`
- `candidate CAND-3EBB6D5ADE3F entity_id=SIG-000910 reason=duplicate_id:SIG-000910 conf=0.9`
- `candidate CAND-19840225D121 entity_id=SIG-000914 reason=duplicate_id:SIG-000914 conf=0.88`
- `candidate CAND-FA75107855A8 entity_id=SIG-000911 reason=duplicate_id:SIG-000911 conf=0.88`
- `candidate CAND-C38ABE100C82 entity_id=SIG-000912 reason=duplicate_id:SIG-000912 conf=0.92`
- `candidate CAND-F40E67D76700 entity_id=SIG-000913 reason=duplicate_id:SIG-000913 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-3EBB6D5ADE3F | business_signal_library | 0.9 | False | duplicate_id:SIG-000910 | Rejected |
| CAND-19840225D121 | business_signal_library | 0.88 | False | duplicate_id:SIG-000914 | Rejected |
| CAND-FA75107855A8 | business_signal_library | 0.88 | False | duplicate_id:SIG-000911 | Rejected |
| CAND-C38ABE100C82 | business_signal_library | 0.92 | False | duplicate_id:SIG-000912 | Rejected |
| CAND-F40E67D76700 | business_signal_library | 0.9 | False | duplicate_id:SIG-000913 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000910` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
