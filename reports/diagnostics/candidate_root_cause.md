# Candidate Root Cause

**Generated:** 2026-08-12T06:39:56+00:00
**Session:** `SESSION-20260812-946EDD`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001950`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260812-946EDD`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001950': 1, 'duplicate_id:SIG-001951': 1, 'duplicate_id:SIG-001952': 1, 'duplicate_id:SIG-001953': 1, 'duplicate_id:SIG-001954': 1}`
- `candidate CAND-A903E21938B1 entity_id=SIG-001950 reason=duplicate_id:SIG-001950 conf=0.9`
- `candidate CAND-2FA4A3906470 entity_id=SIG-001951 reason=duplicate_id:SIG-001951 conf=0.92`
- `candidate CAND-3D74F594D3D7 entity_id=SIG-001952 reason=duplicate_id:SIG-001952 conf=0.88`
- `candidate CAND-BDA57731E9C1 entity_id=SIG-001953 reason=duplicate_id:SIG-001953 conf=0.9`
- `candidate CAND-B2D0652391BC entity_id=SIG-001954 reason=duplicate_id:SIG-001954 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A903E21938B1 | business_signal_library | 0.9 | False | duplicate_id:SIG-001950 | Rejected |
| CAND-2FA4A3906470 | business_signal_library | 0.92 | False | duplicate_id:SIG-001951 | Rejected |
| CAND-3D74F594D3D7 | business_signal_library | 0.88 | False | duplicate_id:SIG-001952 | Rejected |
| CAND-BDA57731E9C1 | business_signal_library | 0.9 | False | duplicate_id:SIG-001953 | Rejected |
| CAND-B2D0652391BC | business_signal_library | 0.92 | False | duplicate_id:SIG-001954 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001950` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
