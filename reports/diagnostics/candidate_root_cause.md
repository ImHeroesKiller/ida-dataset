# Candidate Root Cause

**Generated:** 2026-07-25T18:23:34+00:00
**Session:** `SESSION-20260725-6510F2`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000858`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260725-6510F2`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000858': 1, 'duplicate_id:SIG-000857': 1, 'duplicate_id:SIG-000856': 1, 'duplicate_id:SIG-000855': 1, 'duplicate_id:SIG-000859': 1}`
- `candidate CAND-4A26DB47DCC7 entity_id=SIG-000858 reason=duplicate_id:SIG-000858 conf=0.9`
- `candidate CAND-24B344FA9049 entity_id=SIG-000857 reason=duplicate_id:SIG-000857 conf=0.88`
- `candidate CAND-340A1A712E76 entity_id=SIG-000856 reason=duplicate_id:SIG-000856 conf=0.92`
- `candidate CAND-D98DA0BE8222 entity_id=SIG-000855 reason=duplicate_id:SIG-000855 conf=0.9`
- `candidate CAND-C53938BA21B0 entity_id=SIG-000859 reason=duplicate_id:SIG-000859 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-4A26DB47DCC7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000858 | Rejected |
| CAND-24B344FA9049 | business_signal_library | 0.88 | False | duplicate_id:SIG-000857 | Rejected |
| CAND-340A1A712E76 | business_signal_library | 0.92 | False | duplicate_id:SIG-000856 | Rejected |
| CAND-D98DA0BE8222 | business_signal_library | 0.9 | False | duplicate_id:SIG-000855 | Rejected |
| CAND-C53938BA21B0 | business_signal_library | 0.92 | False | duplicate_id:SIG-000859 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000858` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
