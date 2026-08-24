# Candidate Root Cause

**Generated:** 2026-08-24T03:23:03+00:00
**Session:** `SESSION-20260824-F46ABA`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001189`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260824-F46ABA`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001189': 1, 'duplicate_id:SIG-001186': 1, 'duplicate_id:SIG-001187': 1, 'duplicate_id:SIG-001188': 1, 'duplicate_id:SIG-001190': 1}`
- `candidate CAND-9200B88FEF2F entity_id=SIG-001189 reason=duplicate_id:SIG-001189 conf=0.9`
- `candidate CAND-03DD2D829FC3 entity_id=SIG-001186 reason=duplicate_id:SIG-001186 conf=0.92`
- `candidate CAND-85DB0354642B entity_id=SIG-001187 reason=duplicate_id:SIG-001187 conf=0.9`
- `candidate CAND-32B9A7F453B0 entity_id=SIG-001188 reason=duplicate_id:SIG-001188 conf=0.9`
- `candidate CAND-DE192B40FC5E entity_id=SIG-001190 reason=duplicate_id:SIG-001190 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-9200B88FEF2F | business_signal_library | 0.9 | False | duplicate_id:SIG-001189 | Rejected |
| CAND-03DD2D829FC3 | business_signal_library | 0.92 | False | duplicate_id:SIG-001186 | Rejected |
| CAND-85DB0354642B | business_signal_library | 0.9 | False | duplicate_id:SIG-001187 | Rejected |
| CAND-32B9A7F453B0 | business_signal_library | 0.9 | False | duplicate_id:SIG-001188 | Rejected |
| CAND-DE192B40FC5E | business_signal_library | 0.9 | False | duplicate_id:SIG-001190 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001189` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
