# Candidate Root Cause

**Generated:** 2026-07-25T23:21:43+00:00
**Session:** `SESSION-20260725-DCED1B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000873`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260725-DCED1B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000873': 1, 'duplicate_id:SIG-000872': 1, 'duplicate_id:SIG-000870': 1, 'duplicate_id:SIG-000874': 1, 'duplicate_id:SIG-000871': 1}`
- `candidate CAND-63BD73946C6A entity_id=SIG-000873 reason=duplicate_id:SIG-000873 conf=0.9`
- `candidate CAND-630CE51BFB40 entity_id=SIG-000872 reason=duplicate_id:SIG-000872 conf=0.88`
- `candidate CAND-AB92AD76BF68 entity_id=SIG-000870 reason=duplicate_id:SIG-000870 conf=0.9`
- `candidate CAND-622A8D66B757 entity_id=SIG-000874 reason=duplicate_id:SIG-000874 conf=0.92`
- `candidate CAND-171622300BD8 entity_id=SIG-000871 reason=duplicate_id:SIG-000871 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-63BD73946C6A | business_signal_library | 0.9 | False | duplicate_id:SIG-000873 | Rejected |
| CAND-630CE51BFB40 | business_signal_library | 0.88 | False | duplicate_id:SIG-000872 | Rejected |
| CAND-AB92AD76BF68 | business_signal_library | 0.9 | False | duplicate_id:SIG-000870 | Rejected |
| CAND-622A8D66B757 | business_signal_library | 0.92 | False | duplicate_id:SIG-000874 | Rejected |
| CAND-171622300BD8 | business_signal_library | 0.92 | False | duplicate_id:SIG-000871 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000873` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
