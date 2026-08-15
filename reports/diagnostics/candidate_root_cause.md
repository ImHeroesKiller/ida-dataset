# Candidate Root Cause

**Generated:** 2026-08-15T04:46:15+00:00
**Session:** `SESSION-20260815-42C2D4`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000185`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260815-42C2D4`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000185': 1, 'duplicate_id:SIG-000181': 1, 'duplicate_id:SIG-000182': 1, 'duplicate_id:SIG-000183': 1, 'duplicate_id:SIG-000184': 1}`
- `candidate CAND-4DA9813C75D8 entity_id=SIG-000185 reason=duplicate_id:SIG-000185 conf=0.9`
- `candidate CAND-94DC3388F896 entity_id=SIG-000181 reason=duplicate_id:SIG-000181 conf=0.92`
- `candidate CAND-BC123BBB87A0 entity_id=SIG-000182 reason=duplicate_id:SIG-000182 conf=0.9`
- `candidate CAND-BD5632845F94 entity_id=SIG-000183 reason=duplicate_id:SIG-000183 conf=0.9`
- `candidate CAND-E0D49E185C19 entity_id=SIG-000184 reason=duplicate_id:SIG-000184 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-4DA9813C75D8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000185 | Rejected |
| CAND-94DC3388F896 | business_signal_library | 0.92 | False | duplicate_id:SIG-000181 | Rejected |
| CAND-BC123BBB87A0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000182 | Rejected |
| CAND-BD5632845F94 | business_signal_library | 0.9 | False | duplicate_id:SIG-000183 | Rejected |
| CAND-E0D49E185C19 | business_signal_library | 0.9 | False | duplicate_id:SIG-000184 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000185` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
