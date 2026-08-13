# Candidate Root Cause

**Generated:** 2026-08-13T12:02:22+00:00
**Session:** `SESSION-20260813-A4E441`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000027`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260813-A4E441`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000027': 1, 'duplicate_id:SIG-000030': 1, 'duplicate_id:SIG-000029': 1, 'duplicate_id:SIG-000028': 1, 'duplicate_id:SIG-000026': 1}`
- `candidate CAND-86F0A0EA53A2 entity_id=SIG-000027 reason=duplicate_id:SIG-000027 conf=0.9`
- `candidate CAND-8EC11A2A400A entity_id=SIG-000030 reason=duplicate_id:SIG-000030 conf=0.9`
- `candidate CAND-A10C0D644F60 entity_id=SIG-000029 reason=duplicate_id:SIG-000029 conf=0.9`
- `candidate CAND-A118C8196CDB entity_id=SIG-000028 reason=duplicate_id:SIG-000028 conf=0.9`
- `candidate CAND-C1735E6ABD70 entity_id=SIG-000026 reason=duplicate_id:SIG-000026 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-86F0A0EA53A2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000027 | Rejected |
| CAND-8EC11A2A400A | business_signal_library | 0.9 | False | duplicate_id:SIG-000030 | Rejected |
| CAND-A10C0D644F60 | business_signal_library | 0.9 | False | duplicate_id:SIG-000029 | Rejected |
| CAND-A118C8196CDB | business_signal_library | 0.9 | False | duplicate_id:SIG-000028 | Rejected |
| CAND-C1735E6ABD70 | business_signal_library | 0.92 | False | duplicate_id:SIG-000026 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000027` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
