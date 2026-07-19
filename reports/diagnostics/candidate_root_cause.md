# Candidate Root Cause

**Generated:** 2026-07-19T15:16:39+00:00
**Session:** `SESSION-20260719-576916`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000513`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260719-576916`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000513': 1, 'duplicate_id:SIG-000511': 1, 'duplicate_id:SIG-000514': 1, 'duplicate_id:SIG-000510': 1, 'duplicate_id:SIG-000512': 1}`
- `candidate CAND-9956C8913B78 entity_id=SIG-000513 reason=duplicate_id:SIG-000513 conf=0.9`
- `candidate CAND-C24CB460C076 entity_id=SIG-000511 reason=duplicate_id:SIG-000511 conf=0.92`
- `candidate CAND-9C27C5F4CD59 entity_id=SIG-000514 reason=duplicate_id:SIG-000514 conf=0.92`
- `candidate CAND-2F76B6F88FED entity_id=SIG-000510 reason=duplicate_id:SIG-000510 conf=0.9`
- `candidate CAND-D7475D5FB2E8 entity_id=SIG-000512 reason=duplicate_id:SIG-000512 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-9956C8913B78 | business_signal_library | 0.9 | False | duplicate_id:SIG-000513 | Rejected |
| CAND-C24CB460C076 | business_signal_library | 0.92 | False | duplicate_id:SIG-000511 | Rejected |
| CAND-9C27C5F4CD59 | business_signal_library | 0.92 | False | duplicate_id:SIG-000514 | Rejected |
| CAND-2F76B6F88FED | business_signal_library | 0.9 | False | duplicate_id:SIG-000510 | Rejected |
| CAND-D7475D5FB2E8 | business_signal_library | 0.88 | False | duplicate_id:SIG-000512 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000513` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
