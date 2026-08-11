# Candidate Root Cause

**Generated:** 2026-08-11T18:18:31+00:00
**Session:** `SESSION-20260811-90840E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001910`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260811-90840E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001910': 1, 'duplicate_id:SIG-001914': 1, 'duplicate_id:SIG-001912': 1, 'duplicate_id:SIG-001913': 1, 'duplicate_id:SIG-001911': 1}`
- `candidate CAND-3E6B54A5E96E entity_id=SIG-001910 reason=duplicate_id:SIG-001910 conf=0.9`
- `candidate CAND-02C9262ACFE9 entity_id=SIG-001914 reason=duplicate_id:SIG-001914 conf=0.92`
- `candidate CAND-39E565C75F37 entity_id=SIG-001912 reason=duplicate_id:SIG-001912 conf=0.88`
- `candidate CAND-9281BEF85D9F entity_id=SIG-001913 reason=duplicate_id:SIG-001913 conf=0.9`
- `candidate CAND-4BA0FA736164 entity_id=SIG-001911 reason=duplicate_id:SIG-001911 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-3E6B54A5E96E | business_signal_library | 0.9 | False | duplicate_id:SIG-001910 | Rejected |
| CAND-02C9262ACFE9 | business_signal_library | 0.92 | False | duplicate_id:SIG-001914 | Rejected |
| CAND-39E565C75F37 | business_signal_library | 0.88 | False | duplicate_id:SIG-001912 | Rejected |
| CAND-9281BEF85D9F | business_signal_library | 0.9 | False | duplicate_id:SIG-001913 | Rejected |
| CAND-4BA0FA736164 | business_signal_library | 0.92 | False | duplicate_id:SIG-001911 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001910` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
