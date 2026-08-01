# Candidate Root Cause

**Generated:** 2026-08-01T03:15:10+00:00
**Session:** `SESSION-20260801-DD665A`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001189`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260801-DD665A`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001189': 1, 'duplicate_id:SIG-001187': 1, 'duplicate_id:SIG-001186': 1, 'duplicate_id:SIG-001188': 1, 'duplicate_id:SIG-001185': 1}`
- `candidate CAND-6214C03A738E entity_id=SIG-001189 reason=duplicate_id:SIG-001189 conf=0.92`
- `candidate CAND-C0D7A55776AF entity_id=SIG-001187 reason=duplicate_id:SIG-001187 conf=0.88`
- `candidate CAND-7700314A009F entity_id=SIG-001186 reason=duplicate_id:SIG-001186 conf=0.92`
- `candidate CAND-DD3EF0ED7605 entity_id=SIG-001188 reason=duplicate_id:SIG-001188 conf=0.9`
- `candidate CAND-6F97ED1404E6 entity_id=SIG-001185 reason=duplicate_id:SIG-001185 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-6214C03A738E | business_signal_library | 0.92 | False | duplicate_id:SIG-001189 | Rejected |
| CAND-C0D7A55776AF | business_signal_library | 0.88 | False | duplicate_id:SIG-001187 | Rejected |
| CAND-7700314A009F | business_signal_library | 0.92 | False | duplicate_id:SIG-001186 | Rejected |
| CAND-DD3EF0ED7605 | business_signal_library | 0.9 | False | duplicate_id:SIG-001188 | Rejected |
| CAND-6F97ED1404E6 | business_signal_library | 0.9 | False | duplicate_id:SIG-001185 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001189` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
