# Candidate Root Cause

**Generated:** 2026-07-26T11:39:36+00:00
**Session:** `SESSION-20260726-EFD17E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000897`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260726-EFD17E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000897': 1, 'duplicate_id:SIG-000898': 1, 'duplicate_id:SIG-000899': 1, 'duplicate_id:SIG-000895': 1, 'duplicate_id:SIG-000896': 1}`
- `candidate CAND-B2457272384D entity_id=SIG-000897 reason=duplicate_id:SIG-000897 conf=0.9`
- `candidate CAND-3E6A849F0ACA entity_id=SIG-000898 reason=duplicate_id:SIG-000898 conf=0.92`
- `candidate CAND-78B89CDCB008 entity_id=SIG-000899 reason=duplicate_id:SIG-000899 conf=0.9`
- `candidate CAND-6541A49644AA entity_id=SIG-000895 reason=duplicate_id:SIG-000895 conf=0.9`
- `candidate CAND-1E165D954851 entity_id=SIG-000896 reason=duplicate_id:SIG-000896 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B2457272384D | business_signal_library | 0.9 | False | duplicate_id:SIG-000897 | Rejected |
| CAND-3E6A849F0ACA | business_signal_library | 0.92 | False | duplicate_id:SIG-000898 | Rejected |
| CAND-78B89CDCB008 | business_signal_library | 0.9 | False | duplicate_id:SIG-000899 | Rejected |
| CAND-6541A49644AA | business_signal_library | 0.9 | False | duplicate_id:SIG-000895 | Rejected |
| CAND-1E165D954851 | business_signal_library | 0.92 | False | duplicate_id:SIG-000896 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000897` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
