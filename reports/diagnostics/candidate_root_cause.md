# Candidate Root Cause

**Generated:** 2026-08-14T18:08:00+00:00
**Session:** `SESSION-20260814-587960`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000133`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260814-587960`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000133': 1, 'duplicate_id:SIG-000132': 1, 'duplicate_id:SIG-000134': 1, 'duplicate_id:SIG-000135': 1, 'duplicate_id:SIG-000131': 1}`
- `candidate CAND-1DE5D5C93E73 entity_id=SIG-000133 reason=duplicate_id:SIG-000133 conf=0.9`
- `candidate CAND-5477807A8B6F entity_id=SIG-000132 reason=duplicate_id:SIG-000132 conf=0.9`
- `candidate CAND-588C2A915668 entity_id=SIG-000134 reason=duplicate_id:SIG-000134 conf=0.9`
- `candidate CAND-2100C0B95338 entity_id=SIG-000135 reason=duplicate_id:SIG-000135 conf=0.9`
- `candidate CAND-007B8F81F6EA entity_id=SIG-000131 reason=duplicate_id:SIG-000131 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-1DE5D5C93E73 | business_signal_library | 0.9 | False | duplicate_id:SIG-000133 | Rejected |
| CAND-5477807A8B6F | business_signal_library | 0.9 | False | duplicate_id:SIG-000132 | Rejected |
| CAND-588C2A915668 | business_signal_library | 0.9 | False | duplicate_id:SIG-000134 | Rejected |
| CAND-2100C0B95338 | business_signal_library | 0.9 | False | duplicate_id:SIG-000135 | Rejected |
| CAND-007B8F81F6EA | business_signal_library | 0.92 | False | duplicate_id:SIG-000131 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000133` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
