# Candidate Root Cause

**Generated:** 2026-08-19T21:46:05+00:00
**Session:** `SESSION-20260819-E11352`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000718`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260819-E11352`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000718': 1, 'duplicate_id:SIG-000719': 1, 'duplicate_id:SIG-000716': 1, 'duplicate_id:SIG-000720': 1, 'duplicate_id:SIG-000717': 1}`
- `candidate CAND-394CDF8C500B entity_id=SIG-000718 reason=duplicate_id:SIG-000718 conf=0.9`
- `candidate CAND-CE2C693434AD entity_id=SIG-000719 reason=duplicate_id:SIG-000719 conf=0.9`
- `candidate CAND-FD4CB910C709 entity_id=SIG-000716 reason=duplicate_id:SIG-000716 conf=0.92`
- `candidate CAND-08A3707BCC12 entity_id=SIG-000720 reason=duplicate_id:SIG-000720 conf=0.9`
- `candidate CAND-1A21BA6EEF49 entity_id=SIG-000717 reason=duplicate_id:SIG-000717 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-394CDF8C500B | business_signal_library | 0.9 | False | duplicate_id:SIG-000718 | Rejected |
| CAND-CE2C693434AD | business_signal_library | 0.9 | False | duplicate_id:SIG-000719 | Rejected |
| CAND-FD4CB910C709 | business_signal_library | 0.92 | False | duplicate_id:SIG-000716 | Rejected |
| CAND-08A3707BCC12 | business_signal_library | 0.9 | False | duplicate_id:SIG-000720 | Rejected |
| CAND-1A21BA6EEF49 | business_signal_library | 0.9 | False | duplicate_id:SIG-000717 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000718` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
