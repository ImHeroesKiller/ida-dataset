# Candidate Root Cause

**Generated:** 2026-07-31T19:51:21+00:00
**Session:** `SESSION-20260731-D0A337`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001173`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260731-D0A337`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001173': 1, 'duplicate_id:SIG-001174': 1, 'duplicate_id:SIG-001172': 1, 'duplicate_id:SIG-001171': 1, 'duplicate_id:SIG-001170': 1}`
- `candidate CAND-A540C6CC5762 entity_id=SIG-001173 reason=duplicate_id:SIG-001173 conf=0.9`
- `candidate CAND-5C3378884EF9 entity_id=SIG-001174 reason=duplicate_id:SIG-001174 conf=0.92`
- `candidate CAND-D44239221A05 entity_id=SIG-001172 reason=duplicate_id:SIG-001172 conf=0.88`
- `candidate CAND-160C910C7F83 entity_id=SIG-001171 reason=duplicate_id:SIG-001171 conf=0.92`
- `candidate CAND-379E070318F2 entity_id=SIG-001170 reason=duplicate_id:SIG-001170 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A540C6CC5762 | business_signal_library | 0.9 | False | duplicate_id:SIG-001173 | Rejected |
| CAND-5C3378884EF9 | business_signal_library | 0.92 | False | duplicate_id:SIG-001174 | Rejected |
| CAND-D44239221A05 | business_signal_library | 0.88 | False | duplicate_id:SIG-001172 | Rejected |
| CAND-160C910C7F83 | business_signal_library | 0.92 | False | duplicate_id:SIG-001171 | Rejected |
| CAND-379E070318F2 | business_signal_library | 0.9 | False | duplicate_id:SIG-001170 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001173` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
