# Candidate Root Cause

**Generated:** 2026-07-29T22:24:25+00:00
**Session:** `SESSION-20260729-8B9494`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001072`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260729-8B9494`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001072': 1, 'duplicate_id:SIG-001070': 1, 'duplicate_id:SIG-001073': 1, 'duplicate_id:SIG-001074': 1, 'duplicate_id:SIG-001071': 1}`
- `candidate CAND-83F5ABFF91FA entity_id=SIG-001072 reason=duplicate_id:SIG-001072 conf=0.88`
- `candidate CAND-9F1ADC90BBB9 entity_id=SIG-001070 reason=duplicate_id:SIG-001070 conf=0.9`
- `candidate CAND-7D934C4C297B entity_id=SIG-001073 reason=duplicate_id:SIG-001073 conf=0.9`
- `candidate CAND-9343B107AE51 entity_id=SIG-001074 reason=duplicate_id:SIG-001074 conf=0.92`
- `candidate CAND-8DC21786DE0B entity_id=SIG-001071 reason=duplicate_id:SIG-001071 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-83F5ABFF91FA | business_signal_library | 0.88 | False | duplicate_id:SIG-001072 | Rejected |
| CAND-9F1ADC90BBB9 | business_signal_library | 0.9 | False | duplicate_id:SIG-001070 | Rejected |
| CAND-7D934C4C297B | business_signal_library | 0.9 | False | duplicate_id:SIG-001073 | Rejected |
| CAND-9343B107AE51 | business_signal_library | 0.92 | False | duplicate_id:SIG-001074 | Rejected |
| CAND-8DC21786DE0B | business_signal_library | 0.92 | False | duplicate_id:SIG-001071 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001072` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
