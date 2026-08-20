# Candidate Root Cause

**Generated:** 2026-08-20T10:46:55+00:00
**Session:** `SESSION-20260820-08A8BD`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000778`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260820-08A8BD`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000778': 1, 'duplicate_id:SIG-000779': 1, 'duplicate_id:SIG-000776': 1, 'duplicate_id:SIG-000777': 1, 'duplicate_id:SIG-000780': 1}`
- `candidate CAND-5CE8A3A9B00F entity_id=SIG-000778 reason=duplicate_id:SIG-000778 conf=0.9`
- `candidate CAND-FCDD30C2201E entity_id=SIG-000779 reason=duplicate_id:SIG-000779 conf=0.9`
- `candidate CAND-D15DD9EDDBAD entity_id=SIG-000776 reason=duplicate_id:SIG-000776 conf=0.92`
- `candidate CAND-C9DFBF2336E4 entity_id=SIG-000777 reason=duplicate_id:SIG-000777 conf=0.9`
- `candidate CAND-CAAFCF36935F entity_id=SIG-000780 reason=duplicate_id:SIG-000780 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5CE8A3A9B00F | business_signal_library | 0.9 | False | duplicate_id:SIG-000778 | Rejected |
| CAND-FCDD30C2201E | business_signal_library | 0.9 | False | duplicate_id:SIG-000779 | Rejected |
| CAND-D15DD9EDDBAD | business_signal_library | 0.92 | False | duplicate_id:SIG-000776 | Rejected |
| CAND-C9DFBF2336E4 | business_signal_library | 0.9 | False | duplicate_id:SIG-000777 | Rejected |
| CAND-CAAFCF36935F | business_signal_library | 0.9 | False | duplicate_id:SIG-000780 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000778` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
