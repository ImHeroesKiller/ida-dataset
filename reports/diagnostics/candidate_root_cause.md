# Candidate Root Cause

**Generated:** 2026-07-12T00:16:22+00:00
**Session:** `SESSION-20260711-5A4AE1`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000072`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260711-5A4AE1`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000072': 1, 'duplicate_id:SIG-000074': 1, 'duplicate_id:SIG-000070': 1, 'duplicate_id:SIG-000071': 1, 'duplicate_id:SIG-000073': 1}`
- `candidate CAND-401A73410DF1 entity_id=SIG-000072 reason=duplicate_id:SIG-000072 conf=0.88`
- `candidate CAND-FCD94172818A entity_id=SIG-000074 reason=duplicate_id:SIG-000074 conf=0.92`
- `candidate CAND-81129CD87137 entity_id=SIG-000070 reason=duplicate_id:SIG-000070 conf=0.9`
- `candidate CAND-80DE126FD04E entity_id=SIG-000071 reason=duplicate_id:SIG-000071 conf=0.92`
- `candidate CAND-416BDE6E21C1 entity_id=SIG-000073 reason=duplicate_id:SIG-000073 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-401A73410DF1 | business_signal_library | 0.88 | False | duplicate_id:SIG-000072 | Rejected |
| CAND-FCD94172818A | business_signal_library | 0.92 | False | duplicate_id:SIG-000074 | Rejected |
| CAND-81129CD87137 | business_signal_library | 0.9 | False | duplicate_id:SIG-000070 | Rejected |
| CAND-80DE126FD04E | business_signal_library | 0.92 | False | duplicate_id:SIG-000071 | Rejected |
| CAND-416BDE6E21C1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000073 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000072` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
