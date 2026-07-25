# Candidate Root Cause

**Generated:** 2026-07-25T17:22:08+00:00
**Session:** `SESSION-20260725-42D712`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000852`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260725-42D712`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000852': 1, 'duplicate_id:SIG-000851': 1, 'duplicate_id:SIG-000850': 1, 'duplicate_id:SIG-000853': 1, 'duplicate_id:SIG-000854': 1}`
- `candidate CAND-E2FBCA12A4CB entity_id=SIG-000852 reason=duplicate_id:SIG-000852 conf=0.88`
- `candidate CAND-6C28C07F1969 entity_id=SIG-000851 reason=duplicate_id:SIG-000851 conf=0.92`
- `candidate CAND-7FF0CF36429B entity_id=SIG-000850 reason=duplicate_id:SIG-000850 conf=0.9`
- `candidate CAND-4DDB14EA4F0A entity_id=SIG-000853 reason=duplicate_id:SIG-000853 conf=0.9`
- `candidate CAND-299AF0CD315C entity_id=SIG-000854 reason=duplicate_id:SIG-000854 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-E2FBCA12A4CB | business_signal_library | 0.88 | False | duplicate_id:SIG-000852 | Rejected |
| CAND-6C28C07F1969 | business_signal_library | 0.92 | False | duplicate_id:SIG-000851 | Rejected |
| CAND-7FF0CF36429B | business_signal_library | 0.9 | False | duplicate_id:SIG-000850 | Rejected |
| CAND-4DDB14EA4F0A | business_signal_library | 0.9 | False | duplicate_id:SIG-000853 | Rejected |
| CAND-299AF0CD315C | business_signal_library | 0.92 | False | duplicate_id:SIG-000854 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000852` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
