# Candidate Root Cause

**Generated:** 2026-07-24T10:44:20+00:00
**Session:** `SESSION-20260724-A3AD9B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000776`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260724-A3AD9B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000776': 1, 'duplicate_id:SIG-000777': 1, 'duplicate_id:SIG-000779': 1, 'duplicate_id:SIG-000775': 1, 'duplicate_id:SIG-000778': 1}`
- `candidate CAND-8425185C2A12 entity_id=SIG-000776 reason=duplicate_id:SIG-000776 conf=0.92`
- `candidate CAND-01A0FE62AEA9 entity_id=SIG-000777 reason=duplicate_id:SIG-000777 conf=0.88`
- `candidate CAND-AF8D5599E5A7 entity_id=SIG-000779 reason=duplicate_id:SIG-000779 conf=0.92`
- `candidate CAND-A8EEFC1E5D93 entity_id=SIG-000775 reason=duplicate_id:SIG-000775 conf=0.9`
- `candidate CAND-FC0886765234 entity_id=SIG-000778 reason=duplicate_id:SIG-000778 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-8425185C2A12 | business_signal_library | 0.92 | False | duplicate_id:SIG-000776 | Rejected |
| CAND-01A0FE62AEA9 | business_signal_library | 0.88 | False | duplicate_id:SIG-000777 | Rejected |
| CAND-AF8D5599E5A7 | business_signal_library | 0.92 | False | duplicate_id:SIG-000779 | Rejected |
| CAND-A8EEFC1E5D93 | business_signal_library | 0.9 | False | duplicate_id:SIG-000775 | Rejected |
| CAND-FC0886765234 | business_signal_library | 0.9 | False | duplicate_id:SIG-000778 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000776` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
