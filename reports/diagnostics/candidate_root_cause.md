# Candidate Root Cause

**Generated:** 2026-08-10T21:16:28+00:00
**Session:** `SESSION-20260810-5B7E58`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001843`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260810-5B7E58`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001843': 1, 'duplicate_id:SIG-001840': 1, 'duplicate_id:SIG-001844': 1, 'duplicate_id:SIG-001841': 1, 'duplicate_id:SIG-001842': 1}`
- `candidate CAND-CD3F3D206FAB entity_id=SIG-001843 reason=duplicate_id:SIG-001843 conf=0.9`
- `candidate CAND-02A250DDF019 entity_id=SIG-001840 reason=duplicate_id:SIG-001840 conf=0.9`
- `candidate CAND-0CE09F601D48 entity_id=SIG-001844 reason=duplicate_id:SIG-001844 conf=0.92`
- `candidate CAND-95F0B73E454F entity_id=SIG-001841 reason=duplicate_id:SIG-001841 conf=0.92`
- `candidate CAND-9C904A280EF1 entity_id=SIG-001842 reason=duplicate_id:SIG-001842 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-CD3F3D206FAB | business_signal_library | 0.9 | False | duplicate_id:SIG-001843 | Rejected |
| CAND-02A250DDF019 | business_signal_library | 0.9 | False | duplicate_id:SIG-001840 | Rejected |
| CAND-0CE09F601D48 | business_signal_library | 0.92 | False | duplicate_id:SIG-001844 | Rejected |
| CAND-95F0B73E454F | business_signal_library | 0.92 | False | duplicate_id:SIG-001841 | Rejected |
| CAND-9C904A280EF1 | business_signal_library | 0.88 | False | duplicate_id:SIG-001842 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001843` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
