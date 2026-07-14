# Candidate Root Cause

**Generated:** 2026-07-14T05:54:46+00:00
**Session:** `SESSION-20260714-9E440A`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000186`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260714-9E440A`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000186': 1, 'duplicate_id:SIG-000185': 1, 'duplicate_id:SIG-000188': 1, 'duplicate_id:SIG-000187': 1, 'duplicate_id:SIG-000189': 1}`
- `candidate CAND-86B273EBAE9C entity_id=SIG-000186 reason=duplicate_id:SIG-000186 conf=0.88`
- `candidate CAND-4CFAB16F2AD4 entity_id=SIG-000185 reason=duplicate_id:SIG-000185 conf=0.9`
- `candidate CAND-E6CDA3484A99 entity_id=SIG-000188 reason=duplicate_id:SIG-000188 conf=0.85`
- `candidate CAND-03366690A3AA entity_id=SIG-000187 reason=duplicate_id:SIG-000187 conf=0.92`
- `candidate CAND-78B3E8ED13A7 entity_id=SIG-000189 reason=duplicate_id:SIG-000189 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-86B273EBAE9C | business_signal_library | 0.88 | False | duplicate_id:SIG-000186 | Rejected |
| CAND-4CFAB16F2AD4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000185 | Rejected |
| CAND-E6CDA3484A99 | business_signal_library | 0.85 | False | duplicate_id:SIG-000188 | Rejected |
| CAND-03366690A3AA | business_signal_library | 0.92 | False | duplicate_id:SIG-000187 | Rejected |
| CAND-78B3E8ED13A7 | business_signal_library | 0.9 | False | duplicate_id:SIG-000189 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000186` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
