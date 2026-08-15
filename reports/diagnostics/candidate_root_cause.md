# Candidate Root Cause

**Generated:** 2026-08-15T15:32:02+00:00
**Session:** `SESSION-20260815-842111`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000239`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260815-842111`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000239': 1, 'duplicate_id:SIG-000236': 1, 'duplicate_id:SIG-000238': 1, 'duplicate_id:SIG-000240': 1, 'duplicate_id:SIG-000237': 1}`
- `candidate CAND-FB6EC682EA9F entity_id=SIG-000239 reason=duplicate_id:SIG-000239 conf=0.9`
- `candidate CAND-1C21F560476D entity_id=SIG-000236 reason=duplicate_id:SIG-000236 conf=0.92`
- `candidate CAND-BB068625930E entity_id=SIG-000238 reason=duplicate_id:SIG-000238 conf=0.9`
- `candidate CAND-459AD10EA8BD entity_id=SIG-000240 reason=duplicate_id:SIG-000240 conf=0.9`
- `candidate CAND-37FF9B9BE7F8 entity_id=SIG-000237 reason=duplicate_id:SIG-000237 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-FB6EC682EA9F | business_signal_library | 0.9 | False | duplicate_id:SIG-000239 | Rejected |
| CAND-1C21F560476D | business_signal_library | 0.92 | False | duplicate_id:SIG-000236 | Rejected |
| CAND-BB068625930E | business_signal_library | 0.9 | False | duplicate_id:SIG-000238 | Rejected |
| CAND-459AD10EA8BD | business_signal_library | 0.9 | False | duplicate_id:SIG-000240 | Rejected |
| CAND-37FF9B9BE7F8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000237 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000239` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
