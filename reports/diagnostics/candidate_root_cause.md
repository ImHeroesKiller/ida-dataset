# Candidate Root Cause

**Generated:** 2026-08-13T23:55:39+00:00
**Session:** `SESSION-20260813-DD8346`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000071`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260813-DD8346`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000071': 1, 'duplicate_id:SIG-000074': 1, 'duplicate_id:SIG-000072': 1, 'duplicate_id:SIG-000075': 1, 'duplicate_id:SIG-000073': 1}`
- `candidate CAND-63B4BCFE7C41 entity_id=SIG-000071 reason=duplicate_id:SIG-000071 conf=0.92`
- `candidate CAND-6AD197EF8905 entity_id=SIG-000074 reason=duplicate_id:SIG-000074 conf=0.9`
- `candidate CAND-7E60E0B381E2 entity_id=SIG-000072 reason=duplicate_id:SIG-000072 conf=0.9`
- `candidate CAND-ECB6D93A9BDE entity_id=SIG-000075 reason=duplicate_id:SIG-000075 conf=0.9`
- `candidate CAND-B00092369106 entity_id=SIG-000073 reason=duplicate_id:SIG-000073 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-63B4BCFE7C41 | business_signal_library | 0.92 | False | duplicate_id:SIG-000071 | Rejected |
| CAND-6AD197EF8905 | business_signal_library | 0.9 | False | duplicate_id:SIG-000074 | Rejected |
| CAND-7E60E0B381E2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000072 | Rejected |
| CAND-ECB6D93A9BDE | business_signal_library | 0.9 | False | duplicate_id:SIG-000075 | Rejected |
| CAND-B00092369106 | business_signal_library | 0.9 | False | duplicate_id:SIG-000073 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000071` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
