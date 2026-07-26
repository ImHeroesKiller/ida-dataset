# Candidate Root Cause

**Generated:** 2026-07-26T15:29:00+00:00
**Session:** `SESSION-20260726-D9965F`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000905`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260726-D9965F`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000905': 1, 'duplicate_id:SIG-000908': 1, 'duplicate_id:SIG-000907': 1, 'duplicate_id:SIG-000906': 1, 'duplicate_id:SIG-000909': 1}`
- `candidate CAND-331DB45CB392 entity_id=SIG-000905 reason=duplicate_id:SIG-000905 conf=0.9`
- `candidate CAND-8569D23A7B0E entity_id=SIG-000908 reason=duplicate_id:SIG-000908 conf=0.9`
- `candidate CAND-123002292EC8 entity_id=SIG-000907 reason=duplicate_id:SIG-000907 conf=0.88`
- `candidate CAND-E9B6500188C3 entity_id=SIG-000906 reason=duplicate_id:SIG-000906 conf=0.92`
- `candidate CAND-34369A9A57A8 entity_id=SIG-000909 reason=duplicate_id:SIG-000909 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-331DB45CB392 | business_signal_library | 0.9 | False | duplicate_id:SIG-000905 | Rejected |
| CAND-8569D23A7B0E | business_signal_library | 0.9 | False | duplicate_id:SIG-000908 | Rejected |
| CAND-123002292EC8 | business_signal_library | 0.88 | False | duplicate_id:SIG-000907 | Rejected |
| CAND-E9B6500188C3 | business_signal_library | 0.92 | False | duplicate_id:SIG-000906 | Rejected |
| CAND-34369A9A57A8 | business_signal_library | 0.92 | False | duplicate_id:SIG-000909 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000905` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
