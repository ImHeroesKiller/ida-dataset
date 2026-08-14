# Candidate Root Cause

**Generated:** 2026-08-14T06:28:30+00:00
**Session:** `SESSION-20260814-8920E4`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000090`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260814-8920E4`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000090': 1, 'duplicate_id:SIG-000087': 1, 'duplicate_id:SIG-000086': 1, 'duplicate_id:SIG-000089': 1, 'duplicate_id:SIG-000088': 1}`
- `candidate CAND-1F02EE26B11B entity_id=SIG-000090 reason=duplicate_id:SIG-000090 conf=0.9`
- `candidate CAND-31031D8BBA1C entity_id=SIG-000087 reason=duplicate_id:SIG-000087 conf=0.9`
- `candidate CAND-16F30B917A04 entity_id=SIG-000086 reason=duplicate_id:SIG-000086 conf=0.92`
- `candidate CAND-55DC91ECF16E entity_id=SIG-000089 reason=duplicate_id:SIG-000089 conf=0.9`
- `candidate CAND-FED3EF0B16FF entity_id=SIG-000088 reason=duplicate_id:SIG-000088 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-1F02EE26B11B | business_signal_library | 0.9 | False | duplicate_id:SIG-000090 | Rejected |
| CAND-31031D8BBA1C | business_signal_library | 0.9 | False | duplicate_id:SIG-000087 | Rejected |
| CAND-16F30B917A04 | business_signal_library | 0.92 | False | duplicate_id:SIG-000086 | Rejected |
| CAND-55DC91ECF16E | business_signal_library | 0.9 | False | duplicate_id:SIG-000089 | Rejected |
| CAND-FED3EF0B16FF | business_signal_library | 0.9 | False | duplicate_id:SIG-000088 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000090` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
