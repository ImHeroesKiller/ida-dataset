# Candidate Root Cause

**Generated:** 2026-08-21T05:52:21+00:00
**Session:** `SESSION-20260821-33A254`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000864`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260821-33A254`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000864': 1, 'duplicate_id:SIG-000865': 1, 'duplicate_id:SIG-000863': 1, 'duplicate_id:SIG-000862': 1, 'duplicate_id:SIG-000861': 1}`
- `candidate CAND-20534E02980B entity_id=SIG-000864 reason=duplicate_id:SIG-000864 conf=0.9`
- `candidate CAND-6B1C5B403403 entity_id=SIG-000865 reason=duplicate_id:SIG-000865 conf=0.9`
- `candidate CAND-5B138855275D entity_id=SIG-000863 reason=duplicate_id:SIG-000863 conf=0.9`
- `candidate CAND-1BA65F334C98 entity_id=SIG-000862 reason=duplicate_id:SIG-000862 conf=0.9`
- `candidate CAND-9D5F5D384CD0 entity_id=SIG-000861 reason=duplicate_id:SIG-000861 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-20534E02980B | business_signal_library | 0.9 | False | duplicate_id:SIG-000864 | Rejected |
| CAND-6B1C5B403403 | business_signal_library | 0.9 | False | duplicate_id:SIG-000865 | Rejected |
| CAND-5B138855275D | business_signal_library | 0.9 | False | duplicate_id:SIG-000863 | Rejected |
| CAND-1BA65F334C98 | business_signal_library | 0.9 | False | duplicate_id:SIG-000862 | Rejected |
| CAND-9D5F5D384CD0 | business_signal_library | 0.92 | False | duplicate_id:SIG-000861 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000864` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
