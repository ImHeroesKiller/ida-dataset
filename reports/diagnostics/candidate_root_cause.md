# Candidate Root Cause

**Generated:** 2026-08-13T18:11:25+00:00
**Session:** `SESSION-20260813-65F6F8`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000046`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260813-65F6F8`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000046': 1, 'duplicate_id:SIG-000048': 1, 'duplicate_id:SIG-000047': 1, 'duplicate_id:SIG-000050': 1, 'duplicate_id:SIG-000049': 1}`
- `candidate CAND-AF02AD0AA513 entity_id=SIG-000046 reason=duplicate_id:SIG-000046 conf=0.92`
- `candidate CAND-CFD47DCE2AC3 entity_id=SIG-000048 reason=duplicate_id:SIG-000048 conf=0.9`
- `candidate CAND-F69D2CADBA0C entity_id=SIG-000047 reason=duplicate_id:SIG-000047 conf=0.9`
- `candidate CAND-3ECFB698A50D entity_id=SIG-000050 reason=duplicate_id:SIG-000050 conf=0.9`
- `candidate CAND-F9C5239223FF entity_id=SIG-000049 reason=duplicate_id:SIG-000049 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-AF02AD0AA513 | business_signal_library | 0.92 | False | duplicate_id:SIG-000046 | Rejected |
| CAND-CFD47DCE2AC3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000048 | Rejected |
| CAND-F69D2CADBA0C | business_signal_library | 0.9 | False | duplicate_id:SIG-000047 | Rejected |
| CAND-3ECFB698A50D | business_signal_library | 0.9 | False | duplicate_id:SIG-000050 | Rejected |
| CAND-F9C5239223FF | business_signal_library | 0.9 | False | duplicate_id:SIG-000049 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000046` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
