# Candidate Root Cause

**Generated:** 2026-08-13T08:36:14+00:00
**Session:** `SESSION-20260813-E4CA79`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000019`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260813-E4CA79`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000019': 1, 'duplicate_id:SIG-000016': 1, 'duplicate_id:SIG-000020': 1, 'duplicate_id:SIG-000018': 1, 'duplicate_id:SIG-000017': 1}`
- `candidate CAND-23BF9510DC01 entity_id=SIG-000019 reason=duplicate_id:SIG-000019 conf=0.9`
- `candidate CAND-4EE08FD4225C entity_id=SIG-000016 reason=duplicate_id:SIG-000016 conf=0.92`
- `candidate CAND-5454A74C0CAF entity_id=SIG-000020 reason=duplicate_id:SIG-000020 conf=0.9`
- `candidate CAND-B8EF7ACC9F71 entity_id=SIG-000018 reason=duplicate_id:SIG-000018 conf=0.9`
- `candidate CAND-2E92562C9B64 entity_id=SIG-000017 reason=duplicate_id:SIG-000017 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-23BF9510DC01 | business_signal_library | 0.9 | False | duplicate_id:SIG-000019 | Rejected |
| CAND-4EE08FD4225C | business_signal_library | 0.92 | False | duplicate_id:SIG-000016 | Rejected |
| CAND-5454A74C0CAF | business_signal_library | 0.9 | False | duplicate_id:SIG-000020 | Rejected |
| CAND-B8EF7ACC9F71 | business_signal_library | 0.9 | False | duplicate_id:SIG-000018 | Rejected |
| CAND-2E92562C9B64 | business_signal_library | 0.9 | False | duplicate_id:SIG-000017 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000019` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
