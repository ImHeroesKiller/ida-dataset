# Candidate Root Cause

**Generated:** 2026-07-22T21:31:00+00:00
**Session:** `SESSION-20260722-12BA09`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000704`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260722-12BA09`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000704': 1, 'duplicate_id:SIG-000700': 1, 'duplicate_id:SIG-000702': 1, 'duplicate_id:SIG-000703': 1, 'duplicate_id:SIG-000701': 1}`
- `candidate CAND-6ED150D509D3 entity_id=SIG-000704 reason=duplicate_id:SIG-000704 conf=0.92`
- `candidate CAND-FCE16279571C entity_id=SIG-000700 reason=duplicate_id:SIG-000700 conf=0.9`
- `candidate CAND-43A775E687D5 entity_id=SIG-000702 reason=duplicate_id:SIG-000702 conf=0.88`
- `candidate CAND-AD7FEC1E1C89 entity_id=SIG-000703 reason=duplicate_id:SIG-000703 conf=0.9`
- `candidate CAND-F58A52D8E68D entity_id=SIG-000701 reason=duplicate_id:SIG-000701 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-6ED150D509D3 | business_signal_library | 0.92 | False | duplicate_id:SIG-000704 | Rejected |
| CAND-FCE16279571C | business_signal_library | 0.9 | False | duplicate_id:SIG-000700 | Rejected |
| CAND-43A775E687D5 | business_signal_library | 0.88 | False | duplicate_id:SIG-000702 | Rejected |
| CAND-AD7FEC1E1C89 | business_signal_library | 0.9 | False | duplicate_id:SIG-000703 | Rejected |
| CAND-F58A52D8E68D | business_signal_library | 0.92 | False | duplicate_id:SIG-000701 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000704` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
